# first line

from typing import Optional, Dict, Any, List
from datetime import datetime
from objects.users.root import Root
from db.db_crud import (create_intervention_db,
                        create_relation,
                        fetch_interventions_db,
                        update_intervention_db,
                        delete_intervention_db
                        )

class Note:
    def __init__(self,
                id: Optional[int] = None,
                song_id: Optional[int] = None,
                x_coord: Optional[float] = None,
                y_coord: Optional[float] = None,
                start_time: Optional[float] = None,
                end_time: Optional[float] = None,
                solos: Optional[str] = None,
                rhythm: Optional[str] = None,
                link: Optional[str] = None,
                comment: Optional[str] = None):
        """
        Inizializza un oggetto Note con i campi provenienti dalla tabella SQL.
        """
        self.id = id
        self.song_id = song_id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.start_time = start_time
        self.end_time = end_time
        self.solos = solos
        self.rhythm = rhythm
        self.link = link
        self.comment = comment

    def to_dict(self) -> Dict[str, Any]:
        """
        Serializza l'oggetto Note in un dizionario (utile per API/JSON).
        """
        return {
            "id": self.id,
            "song_id": self.song_id,
            "x_coord": self.x_coord,
            "y_coord": self.y_coord,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "solos": self.solos,
            "rhythm": self.rhythm,
            "link": self.link,
            "comment": self.comment
        }

    @classmethod
    def create_note(user_id: int, media_id: int, start_time: float, end_time: float, content: str) -> Optional[int]:
        now = datetime.now()
        fields = ('user_id', 'media_id', 'start_time', 'end_time', 'content', 'created_at')
        values = (user_id, media_id, start_time, end_time, content, now)
        return create_intervention_db("notes", fields, values)

    @classmethod
    def add_detailed_note(user_id: int, media_id: int, start_time: float, end_time: float,
                        content: str, performers: List[int] = None, instruments: List[int] = None) -> Optional[int]:
        note_id = Note.create(user_id, media_id, start_time, end_time, content)
        if performers:
            for performer in performers:
                create_relation("note_performers", ("note_id", "performer_id"), (note_id, performer))
        if instruments:
            for instrument in instruments:
                create_relation("note_instruments", ("note_id", "instrument_id"), (note_id, instrument))
        return note_id

    @classmethod
    def fetch_note(media_id: int) -> List["Note"]:
        rows = fetch_interventions_db("notes", "media_id", media_id, order_by="start_time ASC")
        return [Note.from_dict(r) for r in rows]

    @classmethod
    def update_note(user_id: int, note_id: int, new_content: str) -> bool:
        note = fetch_interventions_db("notes", "id", note_id)
        if not note:
            return False
        owner_id = note[0]["user_id"]
        if not Root.can_manage_content(user_id, owner_id):
            raise PermissionError("Non hai i permessi per modificare questa nota")
        return update_intervention_db("notes", note_id, "content", new_content)

    @classmethod
    def delete_note(user_id: int, note_id: int) -> bool:
        note = fetch_interventions_db("notes", "id", note_id)
        if not note:
            return False
        owner_id = note[0]["user_id"]
        if not Root.can_manage_content(user_id, owner_id):
            raise PermissionError("Non hai i permessi per cancellare questa nota")
        return delete_intervention_db("notes", note_id)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Note":
        """
        Crea un'istanza di Note da un dizionario.
        """
        return cls(
            id=data.get("id"),
            song_id=data.get("song_id"),
            x_coord=data.get("x_coord"),
            y_coord=data.get("y_coord"),
            start_time=data.get("start_time"),
            end_time=data.get("end_time"),
            solos=data.get("solos"),
            rhythm=data.get("rhythm"),
            link=data.get("link"),
            comment=data.get("comment")
        )

# last line