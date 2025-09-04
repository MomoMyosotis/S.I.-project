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
from abc import ABC, abstractmethod

# Per i tipi (Optional = può essere None, Dict/Any = per serializzazione JSON)
from typing import Optional, Dict, Any, List, Union
from datetime import datetime
from db.db_crud import (
                        create_media_db,
                        fetch_media_db,
                        update_media_db,
                        delete_media_db,
                        fetch_interventions_db
)

class Media(ABC):
    def __init__(self,
                id=None,
                title=None,
                user_id=None,
                year=None,
                description=None,
                link=None,
                created_at=None,
                **kwargs
                ):
        self.id = id
        self.title = title
        self.user_id = user_id
        self.year = year
        self.description = description
        self.link = link
        self.created_at = created_at
        for k, v in kwargs.items():
            setattr(self, k, v)

    @abstractmethod
    def media_type(self) -> str:
        pass

    # =====================
    # STATIC / CLASS METHODS
    # =====================
    @staticmethod
    def validate_media_data(media_data: Dict[str, Any]) -> Union[bool, str]:
        ALLOWED_TYPES = {
            "song","video","document","score","lyrics","chords",
            "mp3","mp4","midi","youtube","podcast","concert"
        }
        print(f"[DEBUG] validate_media_data | media_data={media_data}")
        if "type" not in media_data or media_data["type"] not in ALLOWED_TYPES:
            return "Tipo media non valido"
        if "title" not in media_data or not media_data["title"].strip():
            return "Titolo mancante"
        if "year" in media_data and not isinstance(media_data["year"], int):
            return "Anno non valido"
        return True

    @classmethod
    def create_media(
        cls,
        media_data: Dict[str, Any],
        child_table: str = None,
        child_columns: tuple = (),
        child_values: tuple = ()
    ) -> Optional[int]:
        print(f"[DEBUG] create_media | media_data={media_data} child_table={child_table} child_columns={child_columns} child_values={child_values}")

        # Validazione dei dati
        valid = cls.validate_media_data(media_data)
        if valid is not True:
            raise ValueError(valid)

        # Campi principali della tabella media
        fields = (
            media_data.get("type"),
            media_data.get("title"),
            media_data.get("user_id"),
            media_data.get("year"),
            media_data.get("description", ""),
            media_data.get("link", ""),
            media_data.get("created_at", datetime.now()),
        )
        print(f"[DEBUG] create_media prepared fields: {fields}")

        # Creazione effettiva nel DB
        media_id = create_media_db(fields, child_table, child_columns, child_values)
        print(f"[DEBUG] create_media_db returned media_id={media_id}")
        return media_id


    @classmethod
    def fetch_media(cls, media_id: int, child_table: str = None, child_fields: List[str] = None) -> Optional[Dict[str, Any]]:
        print(f"[DEBUG] fetch_media | media_id={media_id}, child_table={child_table}, child_fields={child_fields}")
        data = fetch_media_db(media_id, child_table, child_fields)
        print(f"[DEBUG] fetch_media_db returned: {data}")
        return data

    @classmethod
    def update_media(cls, media_id: int, updates: Dict[str, Any], table: str = "media") -> bool:
        print(f"[DEBUG] update_media | media_id={media_id}, updates={updates}, table={table}")
        result = update_media_db(media_id, updates, table)
        print(f"[DEBUG] update_media_db returned: {result}")
        return result

    @classmethod
    def delete_media(cls, media_id: int):
        print(f"[DEBUG] delete_media | media_id={media_id}")
        result = delete_media_db(media_id)
        print(f"[DEBUG] delete_media_db returned: {result}")
        return result

    @classmethod
    def fetch_interventions(cls, table: str, field: str, value: Any) -> List[Dict[str, Any]]:
        print(f"[DEBUG] fetch_interventions | table={table}, field={field}, value={value}")
        interventions = fetch_interventions_db(table, field, value)
        print(f"[DEBUG] fetch_interventions_db returned {len(interventions)} items")
        return interventions

    # =====================
    # ISTANZA
    # =====================
    @classmethod
    def build_object(cls, data: dict):
        """
        Metodo generico per costruire un oggetto Media o sottoclasse (Song, Document, ecc.)
        passando dinamicamente tutti i campi ricevuti.
        """
        return cls(**data)

    def to_dict(self) -> Dict[str, Any]:
        base = {
            "id": self.id,
            "title": self.title,
            "user_id": self.user_id,
            "year": self.year,
            "description": self.description,
            "link": self.link,
            "media_type": self.media_type(),
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
        extras = {k: v for k, v in self.__dict__.items() if k not in base}
        return {**base, **extras}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)



    def __repr__(self) -> str:
        return f"<{self.media_type().capitalize()} id={self.id}, title={self.title}>"

# last line