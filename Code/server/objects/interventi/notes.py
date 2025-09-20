# first line

from typing import Optional, Dict, Any, List
from server.objects.users.root import Root
from server.db.db_crud import (
    create_note_db,
    fetch_note_db,
    update_note_db,
    delete_note_db,
    create_relation
)

class Note:
    def __init__(self,
                id: Optional[int] = None,
                author: Optional[int] = None,
                media_id: Optional[int] = None,
                x_coord: Optional[float] = None,
                y_coord: Optional[float] = None,
                start_time: Optional[float] = None,
                end_time: Optional[float] = None,
                solos: Optional[str] = None,
                rhythm: Optional[str] = None,
                note_type: Optional[str] = "regular",
                content: Optional[str] = None):
        self.id = id
        self.author = author
        self.media_id = media_id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.start_time = start_time
        self.end_time = end_time
        self.solos = solos
        self.rhythm = rhythm
        self.note_type = note_type
        self.content = content

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "author": self.author,
            "media_id": self.media_id,
            "x_coord": self.x_coord,
            "y_coord": self.y_coord,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "solos": self.solos,
            "rhythm": self.rhythm,
            "note_type": self.note_type,
            "content": self.content
        }

    # =====================
    # CRUD
    # =====================
    @classmethod
    def create_note(cls, author: int, media_id: int, note_type: str = "regular",
                    start_time: float = None, end_time: float = None,
                    x_coord: float = None, y_coord: float = None,
                    solos: str = None, rhythm: str = None, content: str = None) -> Optional[int]:
        return create_note_db(
            author, media_id, note_type,
            start_time=start_time, end_time=end_time,
            x_coord=x_coord, y_coord=y_coord,
            solos=solos, rhythm=rhythm, content=content
        )

    @classmethod
    def add_detailed_note(cls, author: int, media_id: int,
                            note_type: str = "regular",
                            start_time: float = None, end_time: float = None,
                            x_coord: float = None, y_coord: float = None,
                            solos: str = None, rhythm: str = None, content: str = None,
                            performers: List[int] = None, instruments: List[int] = None) -> Optional[int]:
        note_id = cls.create_note(
            author, media_id, note_type,
            start_time, end_time, x_coord, y_coord, solos, rhythm, content
        )

        if performers or instruments:
            # Inserisce tutte le combinazioni performer-instrument
            if performers and instruments:
                for performer in performers:
                    for instrument in instruments:
                        create_relation(
                            "note_performers_instruments",
                            ("note_id", "performer_id", "instrument_id"),
                            (note_id, performer, instrument)
                        )
            elif performers:
                for performer in performers:
                    create_relation(
                        "note_performers_instruments",
                        ("note_id", "performer_id", "instrument_id"),
                        (note_id, performer, None)
                    )
            elif instruments:
                for instrument in instruments:
                    create_relation(
                        "note_performers_instruments",
                        ("note_id", "performer_id", "instrument_id"),
                        (note_id, None, instrument)
                    )

        return note_id

    @classmethod
    def fetch_notes(cls, media_id: int) -> List["Note"]:
        rows = fetch_note_db("media_id", media_id)
        return [cls.from_dict(r) for r in rows]

    @classmethod
    def fetch_by_id(cls, note_id: int) -> Optional["Note"]:
        rows = fetch_note_db("id", note_id)
        if not rows:
            return None
        return cls.from_dict(rows[0])

    @classmethod
    def update_note(cls, user_id: int, note_id: int, new_content: str) -> bool:
        note = fetch_note_db("id", note_id)
        if not note:
            return False
        owner_id = note[0]["author"]
        if not Root.can_manage_content(user_id, owner_id):
            raise PermissionError("Non hai i permessi per modificare questa nota")
        return update_note_db(note_id, "content", new_content)

    @classmethod
    def delete_note(cls, user_id: int, note_id: int) -> bool:
        note = fetch_note_db("id", note_id)
        if not note:
            return False
        owner_id = note[0]["author"]
        if not Root.can_manage_content(user_id, owner_id):
            raise PermissionError("Non hai i permessi per cancellare questa nota")
        return delete_note_db(note_id)

    # =====================
    # CONVERSIONE DICTIONARY
    # =====================
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Note":
        return cls(
            id=data.get("id"),
            author=data.get("author"),
            media_id=data.get("media_id"),
            x_coord=data.get("x_coord"),
            y_coord=data.get("y_coord"),
            start_time=data.get("start_time"),
            end_time=data.get("end_time"),
            solos=data.get("solos"),
            rhythm=data.get("rhythm"),
            note_type=data.get("note_type"),
            content=data.get("content")
        )

# last line