# first line

from typing import Optional, Dict, Any
from .media import Media
from server.db.db_crud import fetch_relations

class Video(Media):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = "video"
        self.director = kwargs.get("director")

    def media_type(self) -> str:
        return "video"

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "duration": self.duration,
            "location": self.location,
            "additional_info": self.additional_info,
            "director": self.director
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
    def fetch_full_video(cls, video_id: int) -> Optional["Video"]:
        media_data = cls.fetch(media_id=video_id)
        if not media_data:
            return None

        media_data.genres = [r["genre_id"] for r in fetch_relations("media_genres", "media_id", video_id)]
        media_data.authors = [r["author_id"] for r in fetch_relations("media_authors", "media_id", video_id)]
        media_data.performers = [r["performer_id"] for r in fetch_relations("media_performances", "media_id", video_id)]
        #media_data.comments = fetch_interventions_db("comments", "media_id", video_id)
        #media_data.notes = fetch_interventions_db("notes", "media_id", video_id)

        return media_data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Optional["Video"]:
        if not data:
            return None
        return cls(**data)

# last line