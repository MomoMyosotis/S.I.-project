# first line

from typing import Optional, Dict, Any, List
from .media import Media
from db.db_crud import fetch_relations, advanced_song_search_db, create_relation, delete_relation

class Song(Media):

    def __init__(
        self,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.type = "song"  # forza tipo song

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
    # RELAZIONI M:N
    # =====================
    def _sync_relations(self):
        # Nessuna azione, perché create_media_db() ha già gestito tutto
        pass

    # =====================
    # CLASS METHODS
    # =====================
    @classmethod
    def fetch_full_song(cls, song_id: int) -> Optional["Song"]:
        media_data = cls.fetch(media_id=song_id)  # usa fetch generico di Media
        if not media_data:
            return None

        media_data.genres = [r["genre_id"] for r in fetch_relations("media_genres", "media_id", song_id)]
        media_data.authors = [r["author_id"] for r in fetch_relations("media_authors", "media_id", song_id)]
        media_data.performers = [r["performer_id"] for r in fetch_relations("media_performances", "media_id", song_id)]
#        media_data.comments = fetch_interventions_db("comments", "media_id", song_id)
#        media_data.notes = fetch_interventions_db("notes", "media_id", song_id)

        return media_data

    @classmethod
    def advanced_song_search(cls, filters: Dict[str, Any]) -> List["Song"]:
        results = advanced_song_search_db(filters)
        return [cls.from_dict(r) for r in results]

# last line