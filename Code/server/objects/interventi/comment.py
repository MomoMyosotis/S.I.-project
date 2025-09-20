# first line

from typing import Optional, Dict, Any, List
from server.objects.users.root import Root
from server.logs.logger import log_event
from server.db.db_crud import (
    create_comment_db,
    fetch_comments_by_media_db,
    fetch_comment_replies_db,
    fetch_comments_by_note_db,
    fetch_comment_db,
    update_comment_db,
    fetch_media_db,
    delete_comment_db
)
# ========================
# Comment class con debug
# ========================
class Comment:
    def __init__(self,
                id: Optional[int] = None,
                user_id: Optional[int] = None,
                media_id: Optional[int] = None,
                note_id: Optional[int] = None,
                parent_comment_id: Optional[int] = None,
                text: str = ""
                ):
        self.id = id
        self.user_id = user_id
        self.media_id = media_id
        self.note_id = note_id
        self.parent_comment_id = parent_comment_id
        self.text = text
        print(f"[DEBUG __init__] Created Comment object: {self.to_dict()}")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "media_id": self.media_id,
            "note_id": self.note_id,
            "parent_comment_id": self.parent_comment_id,
            "text": self.text
        }

    # -----------------------
    # CRUD
    # -----------------------
    @classmethod
    def add_comment(cls, user_id: int, text: str,
                    media_id: Optional[int] = None,
                    note_id: Optional[int] = None,
                    parent_comment_id: Optional[int] = None) -> Optional["Comment"]:
        print(f"[DEBUG add_comment] START - user_id={user_id}, text={text}, media_id={media_id}, note_id={note_id}, parent_comment_id={parent_comment_id}")
        new_id = create_comment_db(
            user_id=user_id,
            text=text,
            media_id=media_id,
            note_id=note_id,
            parent_comment_id=parent_comment_id
        )
        print(f"[DEBUG add_comment] new_id returned from DB: {new_id}")

        if not new_id:
            print(f"[DEBUG add_comment] Comment creation failed")
            return None

        # ricarica i dati dal DB
        row = fetch_comment_db("id", new_id)
        print(f"[DEBUG add_comment] fetch_comment_db returned: {row}")

        if row:
            data = row[0]
            comment_obj = cls(
                id=data["id"],
                user_id=data["user_id"],
                media_id=data.get("media_id"),
                note_id=data.get("note_id"),
                parent_comment_id=data.get("parent_comment_id"),
                text=data["text"]
            )
            print(f"[DEBUG add_comment] Created Comment object from DB: {comment_obj.to_dict()}")
            return comment_obj

        print(f"[DEBUG add_comment] No data found after insert")
        return None

    @classmethod
    def fetch_by_media(cls, media_id: int) -> List[Dict[str, Any]]:
        print(f"[DEBUG fetch_by_media] media_id={media_id}")
        result = fetch_comments_by_media_db(media_id)
        print(f"[DEBUG fetch_by_media] returned {len(result)} comments")
        return result

    @classmethod
    def fetch_by_note(cls, note_id: int) -> List[Dict[str, Any]]:
        print(f"[DEBUG fetch_by_note] note_id={note_id}")
        result = fetch_comments_by_note_db(note_id)
        print(f"[DEBUG fetch_by_note] returned {len(result)} comments")
        return result

    @classmethod
    def fetch_replies(cls, parent_comment_id: int) -> List[Dict[str, Any]]:
        print(f"[DEBUG fetch_replies] parent_comment_id={parent_comment_id}")
        result = fetch_comment_replies_db(parent_comment_id)
        print(f"[DEBUG fetch_replies] returned {len(result)} replies")
        return result

    @classmethod
    def fetch_by_id(cls, comment_id: int) -> Optional["Comment"]:
        print(f"[DEBUG fetch_by_id] comment_id={comment_id}")
        result = fetch_comment_db("id", comment_id)
        print(f"[DEBUG fetch_by_id] fetch_comment_db returned: {result}")
        if not result:
            return None
        return cls.from_dict(result[0])

    @classmethod
    def update_comment(cls, user_id: int, comment_id: int, new_text: str) -> bool:
        print(f"[DEBUG update_comment] user_id={user_id}, comment_id={comment_id}, new_text={new_text}")
        comment = fetch_comment_db("id", comment_id)
        print(f"[DEBUG update_comment] fetched comment: {comment}")
        if not comment:
            return False
        owner_id = comment[0]["user_id"]
        if not Root.can_manage_content(user_id, owner_id):
            raise PermissionError("Non hai i permessi per modificare questo commento")
        result = update_comment_db(comment_id, "text", new_text)
        print(f"[DEBUG update_comment] update_comment_db result: {result}")
        return result

    @classmethod
    def delete_comment(cls, user_id: int, comment_id: int) -> bool:
        print(f"[DEBUG delete_comment] user_id={user_id}, comment_id={comment_id}")
        comment = fetch_comment_db("id", comment_id)
        print(f"[DEBUG delete_comment] fetched comment: {comment}")
        if not comment:
            return False
        owner_id = comment[0]["user_id"]

        media = None
        if comment[0].get("media_id"):
            media = fetch_media_db(comment[0]["media_id"])
            print(f"[DEBUG delete_comment] fetched media: {media}")
        media_owner_id = media["user_id"] if media else None

        if not Root.can_manage_content(user_id, owner_id) and user_id != media_owner_id:
            raise PermissionError("Non hai i permessi per cancellare questo commento")
        result = delete_comment_db(comment_id)
        print(f"[DEBUG delete_comment] delete_comment_db result: {result}")
        return result

    # -----------------------
    # COSTRUTTORE DA DIZIONARIO
    # -----------------------
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Comment":
        print(f"[DEBUG from_dict] data={data}")
        return cls(
            id=data.get("id"),
            user_id=data.get("user_id"),
            media_id=data.get("media_id"),
            note_id=data.get("note_id"),
            parent_comment_id=data.get("parent_comment_id"),
            text=data.get("text")
        )

# last line