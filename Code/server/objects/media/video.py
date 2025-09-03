# first line

from typing import Optional, Dict, Any, List
from .media import Media
from db.db_crud import advanced_video_search_db

class Video(Media):
    def __init__(
        self,
        id: Optional[int] = None,
        title: Optional[str] = None,
        year: Optional[int] = None,
        description: Optional[str] = None,
        link: Optional[str] = None,
        duration: Optional[int] = None,
        location: Optional[str] = None,
        additional_info: Optional[str] = None,
        director: Optional[str] = None
    ):
        super().__init__(id, title, year, description, link)
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
    # CLASS METHODS
    # =====================
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
            year=data.get("year"),
            description=data.get("description"),
            link=data.get("link"),
            duration=data.get("duration"),
            location=data.get("location"),
            additional_info=data.get("additional_info"),
            director=data.get("director")
        )

# last line