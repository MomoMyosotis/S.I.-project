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
                        fetch_media_db,
                        update_media_db,
                        delete_media_db,
                        fetch_interventions_db
)

class Media(ABC):
    def __init__(
        self,
        id: Optional[int] = None,
        title: Optional[str] = None,
        year: Optional[int] = None,
        description: Optional[str] = None,
        link: Optional[str] = None
    ):
        self.id = id
        self.title = title
        self.year = year
        self.description = description
        self.link = link

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
        if "type" not in media_data or media_data["type"] not in ALLOWED_TYPES:
            return "Tipo media non valido"
        if "title" not in media_data or not media_data["title"].strip():
            return "Titolo mancante"
        if "year" in media_data and not isinstance(media_data["year"], int):
            return "Anno non valido"
        return True

    @classmethod
    def create_media(cls, media_data: Dict[str, Any], child_table: str = None, child_fields: tuple = ()) -> Optional[int]:
        valid = cls.validate_media_data(media_data)
        if valid is not True:
            raise ValueError(valid)

        fields = (
            media_data.get("type"),
            media_data.get("title"),
            media_data.get("year"),
            media_data.get("description",""),
            media_data.get("link",""),
            media_data.get("file_path",""),
            media_data.get("created_at", datetime.now()),
            media_data.get("user_id"),
        )
        # qui si chiama la funzione CRUD corretta, non se stessa
        from db.db_crud import create_media_db
        return create_media_db(fields, child_table, child_fields)

    @classmethod
    def fetch_media(cls, media_id: int, child_table: str = None, child_fields: List[str] = None) -> Optional[Dict[str, Any]]:
        return fetch_media_db(media_id, child_table, child_fields)

    @classmethod
    def update_media(cls, media_id: int, updates: Dict[str, Any], table: str = "media") -> bool:
        return update_media_db(media_id, updates, table)

    @classmethod
    def delete_media(cls, media_id: int):
        return delete_media_db(media_id)

    @classmethod
    def fetch_interventions(cls, table: str, field: str, value: Any) -> List[Dict[str, Any]]:
        """Recupera interventi (comments, notes) filtrando per un campo specifico."""
        return fetch_interventions_db(table, field, value)

    # =====================
    # ISTANZA
    # =====================
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "description": self.description,
            "link": self.link,
            "media_type": self.media_type()
        }

    def __repr__(self) -> str:
        return f"<{self.media_type().capitalize()} id={self.id}, title={self.title}>"

# last line