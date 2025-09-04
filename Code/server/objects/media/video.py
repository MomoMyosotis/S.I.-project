# first line

from typing import Optional, Dict, Any, List
from .media import Media
from db.db_crud import advanced_video_search_db, fetch_interventions_db

class Video(Media):
    def __init__(
        self,
        id: Optional[int] = None,
        title: Optional[str] = None,
        user_id: Optional[str] = None,
        year: Optional[int] = None,
        description: Optional[str] = None,
        link: Optional[str] = None,
        duration: Optional[int] = None,
        location: Optional[str] = None,
        additional_info: Optional[str] = None,
        director: Optional[str] = None,
        **kwargs
    ):
        super().__init__(id, title, user_id, year, description, link, **kwargs)
        self.duration = duration
        self.location = location
        self.additional_info = additional_info
        self.director = director

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
    # CLASS METHODS SPECIFICHE VIDEO
    # =====================
    @classmethod
    def fetch_full_video(cls, video_id: int) -> Optional[Dict[str, Any]]:
        media = Media.fetch_media(video_id)
        if not media:
            return None
        # eventuali relazioni future tipo authors, performers possono essere aggiunte qui
        media["comments"] = fetch_interventions_db("comments", "media_id", video_id)
        media["notes"] = fetch_interventions_db("notes", "media_id", video_id)
        return media

    @classmethod
    def advanced_video_search(cls, filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        return advanced_video_search_db(filters)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Optional["Video"]:
        if not data:
            return None
        return cls(
            id=data.get("id"),
            title=data.get("title"),
            user_id=data.get("user_id"),
            year=data.get("year"),
            description=data.get("description"),
            link=data.get("link"),
            duration=data.get("duration"),
            location=data.get("location"),
            additional_info=data.get("additional_info"),
            director=data.get("director")
        )

# last line