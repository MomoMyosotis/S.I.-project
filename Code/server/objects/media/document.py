# first line

from typing import Optional, Dict, Any, List
from .media import Media
from db.db_crud import advanced_document_search_db

class Document(Media):
    def __init__(
        self,
        id: Optional[int] = None,
        title: Optional[str] = None,
        year: Optional[int] = None,
        description: Optional[str] = None,
        link: Optional[str] = None,
        format: Optional[str] = None,
        pages: Optional[int] = None,
        caption: Optional[str] = None,
        song_id: Optional[int] = None
    ):
        super().__init__(id, title, year, description, link)
        self.format = format
        self.pages = pages
        self.caption = caption
        self.song_id = song_id

    def media_type(self) -> str:
        return "document"

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "format": self.format,
            "pages": self.pages,
            "caption": self.caption,
            "song_id": self.song_id
        })
        return data

    # =====================
    # METODI DI CLASSE
    # =====================
    @classmethod
    def advanced_document_search(cls, filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        return advanced_document_search_db(filters)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Optional["Document"]:
        if not data:
            return None
        return cls(
            id=data.get("id"),
            title=data.get("title"),
            year=data.get("year"),
            description=data.get("description"),
            link=data.get("link"),
            format=data.get("format"),
            pages=data.get("pages"),
            caption=data.get("caption"),
            song_id=data.get("song_id")
        )

# last line