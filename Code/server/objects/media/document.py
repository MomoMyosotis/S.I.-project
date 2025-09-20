# first line

from typing import Optional, Dict, Any
from .media import Media
from server.db.db_crud import fetch_relations

class Document(Media):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = "document"
        self.pages = kwargs.get("pages")
        self.format = kwargs.get("format")

    def media_type(self) -> str:
        return "document"

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "stored_at": self.stored_at,
            "pages": self.pages,
            "format": self.format,
            "references": getattr(self, "references", [])
            # in futuro puoi aggiungere "comments": self.comments, "notes": self.notes
        })
        return data

    # =====================
    # RELAZIONI M:N
    # =====================
    def _sync_relations(self):
        # Nessuna azione, perché create_media_db() ha già gestito tutto
        pass

    # =====================
    # CLASS METHODS
    # =====================
    @classmethod
    def fetch_full_document(cls, doc_id: int) -> Optional["Document"]:
        media_data = cls.fetch(media_id=doc_id)
        if not media_data:
            return None


        media_data.authors = [r["author_id"] for r in fetch_relations("media_authors", "media_id", doc_id)]
        #media_data.comments = fetch_interventions_db("comments", "media_id", doc_id)
        #media_data.notes = fetch_interventions_db("notes", "media_id", doc_id)
        media_data.references = [r["passive_id"] for r in fetch_relations("media_references", "active_id", doc_id)]

        return media_data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Optional["Document"]:
        if not data:
            return None
        return cls(**data)

# last line