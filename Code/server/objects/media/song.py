# first line

from typing import Optional, Dict, Any, List
from .media import Media
from db.db_crud import (
                        fetch_media_db,
                        fetch_relations,
                        fetch_interventions_db,
                        advanced_song_search
)

class Song(Media):
    def __init__(
        self,
        id: Optional[int] = None,
        title: Optional[str] = None,
        year: Optional[int] = None,
        description: Optional[str] = None,
        link: Optional[str] = None,
        duration: Optional[int] = None,
        location: Optional[str] = None,
        additional_info: Optional[str] = None
    ):
        super().__init__(id, title, year, description, link)
        self.duration = duration
        self.location = location
        self.additional_info = additional_info

    def media_type(self) -> str:
        return "song"

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "duration": self.duration,
            "location": self.location,
            "additional_info": self.additional_info
        })
        return data

    # =====================
    # CLASS METHODS
    # =====================
    @classmethod
    def fetch_full_song(cls, song_id: int) -> Optional[Dict[str, Any]]:
        media = fetch_media_db(song_id)
        if not media:
            return None
        media["genres"] = fetch_relations("song_genres", "song_id", song_id)
        media["authors"] = fetch_relations("song_authors", "song_id", song_id)
        media["performers"] = fetch_relations("song_performances", "song_id", song_id)
        media["comments"] = fetch_interventions_db("comments", "media_id", song_id)
        media["notes"] = fetch_interventions_db("notes", "media_id", song_id)
        return media

    @classmethod
    def advanced_song_search(cls, filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        return advanced_song_search(filters)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Optional["Song"]:
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
            additional_info=data.get("additional_info")
        )

# last line