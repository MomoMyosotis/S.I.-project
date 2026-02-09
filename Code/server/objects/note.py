# first line
import datetime
from server.db.db_crud import (create_note_db,
                               fetch_note_db,
                               update_note_db,
                               delete_note_db)


# structure of the note in the db
"""
-- ========================================
-- NOTE
-- ========================================
CREATE TABLE notes (
    id PRIMARY KEY SERIAL,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    media_id INT REFERENCES media(id) ON DELETE CASCADE,
    start NUMERIC (8 , 2)
    end NUMERIC (8 , 2),
    type BOOLEAN NOT NULL DEFAULT 1, -- TRUE = text, FALSE = graphic
    text TEXT,
    stored_at VARCHAR(255),
    private BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    page INT,
    A_point VARCHAR(255),
    B_point VARCHAR(255)
)
"""

class Note:
    def __init__ (self, user_id, media_id, start, end, type, text=None, stored_at=None, private=False, page=None, A_point=None, B_point=None):
        self.user_id = user_id
        self.media_id = media_id
        self.start = start
        self.end = end
        self.type = type
        self.text = text
        self.stored_at = stored_at
        self.private = private
        self.created_at = datetime.datetime.now()
        self.page = page
        self.A_point = A_point
        self.B_point = B_point

    @staticmethod
    def create_note(user_id, media_id, start=None, end=None,type=True, text=None, stored_at=None, private=False, page=None, A_point=None, B_point=None):
        """Create a note in the DB and return a Note instance with id set, or None on failure."""
        new_id = create_note_db(user_id, media_id, start, end, type, text, stored_at, private)
        if not new_id:
            return None
        note = Note(user_id=user_id, media_id=media_id, start=start, end=end, type=type, text=text, stored_at=stored_at, private=private)
        try:
            note.id = int(new_id)
        except Exception:
            note.id = new_id
        return note

    @staticmethod
    def fetch_note(user_id, media_id):
        return fetch_note_db(user_id, media_id)

    @staticmethod
    def update_note(note_id, **kwargs):
        return update_note_db(note_id, **kwargs)

    @staticmethod
    def delete_note(note_id):
        return delete_note_db(note_id)

    @classmethod
    def fetch_by_media(cls, media_id):
        """Return list of notes (dicts) for a given media id."""
        try:
            from server.db.db_crud import fetch_all
            rows = fetch_all(
                "SELECT id, user_id, media_id, note_start, note_end, type, text, stored_at, private, created_at FROM notes WHERE media_id = %s ORDER BY note_start ASC",
                (media_id,)
            )
            return rows or []
        except Exception:
            return []

    @classmethod
    def fetch_by_id(cls, note_id):
        """Return a single note dict by id or None."""
        try:
            from server.db.db_crud import fetch_one
            row = fetch_one("SELECT id, user_id, media_id, note_start, note_end, type, text, stored_at, private, created_at FROM notes WHERE id = %s", (note_id,))
            return row
        except Exception:
            return None

    def from_dict(self, data):
        self.user_id = data.get("user_id")
        self.media_id = data.get("media_id")
        self.start = data.get("note_start")
        self.end = data.get("note_end")
        self.type = data.get("type")
        self.text = data.get("text")
        self.stored_at = data.get("stored_at")
        self.private = data.get("private", False)
        self.created_at = data.get("created_at", datetime.datetime.now())
        self.page = data.get("page")
        self.A_point = data.get("A_point")
        self.B_point = data.get("B_point")

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "media_id": self.media_id,
            "start": self.start,
            "end": self.end,
            "type": self.type,
            "text": self.text,
            "stored_at": self.stored_at,
            "private": self.private,
            "created_at": self.created_at,
            "page": self.page,
            "A_point": self.A_point,
            "B_point": self.B_point
        }

# last line