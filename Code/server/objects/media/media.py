# first line

# ============================================================
# MEDIA BASE CLASS
# ============================================================
# Qui definiamo la classe base "Media" che rappresenta un generico contenuto
# multimediale (es. canzone, documento, video). Non è pensata per essere
# usata direttamente ma come "contratto" da cui ereditano le sottoclassi.
# ============================================================

# ABC = Abstract Base Class → libreria di Python per creare classi astratte
# (cioè classi che non possono essere istanziate direttamente).
# Le classi figlie DEVONO implementare i metodi definiti come @abstractmethod.
# ============================================================
# MEDIA BASE CLASS
# ============================================================
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, List
from datetime import datetime
import json
from db.db_crud import create_media_db, fetch_media_db, update_media_db, delete_media_db

class Media(ABC):
    def __init__(
        self,
        media_id: Optional[int] = None,
        type: str = None,
        user_id: Optional[int] = None,
        title: Optional[str] = None,
        year: Optional[int] = None,
        description: Optional[str] = None,
        link: Optional[str] = None,
        duration: Optional[int] = None,
        location: Optional[str] = None,
        additional_info: Optional[str] = None,
        stored_at: Optional[str] = None,
        created_at: Optional[datetime] = None,
        genres: Optional[List[str]] = None,
        authors: Optional[List[int]] = None,
        performers: Optional[List[int]] = None,
        references: Optional[List[int]] = None,
        is_author: Optional[bool] = None,
        is_performer: Optional[bool] = None,
        **kwargs
    ):
        print(f"[DEBUG][Media.__init__] Called with title={title}, type={type}, year={year}, user_id={user_id}, kwargs={kwargs}")

        # Alias tra id e media_id
        self.id = media_id or kwargs.get("id")
        self.media_id = self.id

        self.type = type
        self.title = title
        self.user_id = user_id
        self.year = year
        self.description = description
        self.link = link
        self.duration = duration
        self.location = location
        self.additional_info = additional_info
        self.stored_at = stored_at
        self.created_at = created_at or datetime.now()
        self.genres = genres or []
        self.authors = authors or []
        self.performers = performers or []
        self.references = references or []
        self.is_author = bool(is_author)
        self.is_performer = bool(is_performer)
        self._deleted = False

        # Gestione extra attr
        for k, v in kwargs.items():
            print(f"[DEBUG][Media.__init__] Extra attr: {k}={v}")
            setattr(self, k, v)

        # Gestione tracklist
        tracklist = kwargs.get("tracklist")
        if tracklist is not None:
            self.additional_info = json.dumps(tracklist)

        print(f"[DEBUG][Media.__init__] Finished -> {self}")

    @abstractmethod
    def media_type(self) -> str:
        pass

    # =====================
    # CRUD BASE
    # =====================
    def save(self):
        print(f"[DEBUG][Media.save] Called on {self}")
        if self._deleted:
            raise Exception("Cannot save a deleted object")

        payload = self.to_dict()
        print(f"[DEBUG][Media.save] Payload to create_media_db={payload}")

        if not self.media_id:
            print("[DEBUG][Media.save] No media_id -> creating new record")
            result = create_media_db(payload)
            print(f"[DEBUG][Media.save] Result from create_media_db={result}")
            self.media_id = result["id"] if result else None
            print(f"[DEBUG][Media.save] Assigned new media_id={self.media_id}")
        else:
            print(f"[DEBUG][Media.save] Updating existing media_id={self.media_id}")
            updates = {
                "title": self.title,
                "description": self.description,
                "link": self.link,
                "year": self.year,
                "duration": self.duration,
                "location": self.location,
                "additional_info": self.additional_info,
                "is_author": self.is_author,
                "is_performer": self.is_performer
            }
            print(f"[DEBUG][Media.save] Updates dict={updates}")
            update_media_db(self.media_id, updates)

        print(f"[DEBUG][Media.save] Syncing relations for {self}")
        self._sync_relations()
        print(f"[DEBUG][Media.save] END for {self}")

    def delete(self):
        print(f"[DEBUG][Media.delete] Called on {self}")
        if self._deleted:
            print(f"[DEBUG][Media.delete] Object already deleted")
            return False

        if self.media_id:
            delete_media_db(self.media_id)
            print(f"[DEBUG][Media.delete] Deleted media_id={self.media_id}")
            self.media_id = None

        self._deleted = True
        return True

    @classmethod
    def fetch(cls, media_id: int):
        print(f"[DEBUG][Media.fetch] Called cls={cls.__name__}, media_id={media_id}")
        data = fetch_media_db(media_id)
        print(f"[DEBUG][Media.fetch] Data from DB={data}")
        if not data:
            print("[DEBUG][Media.fetch] No data found -> returning None")
            return None
        obj = cls.from_dict(data)
        print(f"[DEBUG][Media.fetch] Built object={obj}")
        return obj

    # =====================
    # RELAZIONI M:N
    # =====================
    def _sync_relations(self):
        print(f"[DEBUG][Media._sync_relations] Called for {self}")
        # Override nelle sottoclassi per gestire relazioni come authors, performers, genres.

    def to_dict(self) -> Dict[str, Any]:
        d = {
            "media_id": self.media_id,
            "type": self.type,
            "title": self.title,
            "user_id": self.user_id,
            "year": self.year,
            "description": self.description,
            "link": self.link,
            "duration": self.duration,
            "location": self.location,
            "additional_info": self.additional_info,
            "stored_at": self.stored_at,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "genres": self.genres,
            "authors": self.authors,
            "performers": self.performers,
            "references": self.references,
            "is_author": self.is_author,
            "is_performer": self.is_performer
        }

        # Deserializza tracklist se presente
        if self.additional_info:
            try:
                d["tracklist"] = json.loads(self.additional_info)
            except Exception:
                d["tracklist"] = None

        print(f"[DEBUG][Media.to_dict] {self} -> {d}")
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        if 'id' in data:
            data['media_id'] = data.pop('id')
        print(f"[DEBUG][Media.from_dict] cls={cls.__name__}, data={data}")
        obj = cls(**data)
        print(f"[DEBUG][Media.from_dict] Built object={obj}")
        return obj

    def __repr__(self) -> str:
        return f"<{self.media_type().capitalize()} id={self.media_id}, title={self.title}>"

# last line