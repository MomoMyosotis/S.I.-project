# first  line

# restricted.py

from typing import Optional, List, Dict, Any
from datetime import date, datetime
from server.objects.users.root import Root, UserLevel

class Restricted(Root):
    """
    Utente con accesso limitato: può solo visualizzare contenuti.
    """
    def __init__(
        self,
        id: int,
        mail: str,
        username: str,
        password_hash: str,
        birthday: date,
        bio: Optional[str] = "",
        profile_pic: Optional[str] = None,
        lvl: UserLevel = UserLevel.RESTRICTED
    ):
        super().__init__(id, mail, username, password_hash, birthday, bio, profile_pic, lvl)

    # =====================
    # OVERRIDE PERMESSI
    # =====================
    def get_permissions(self) -> List[str]:
        return ["view_content"]

    def can_post_content(self) -> bool:
        return False

    # =====================
    # METODI SPECIFICI
    # =====================
    def view_content(self, content_id: int) -> Dict[str, Any]:
        return {"status": "OK", "action": "VIEW_CONTENT", "content_id": content_id}

    # =====================
    # BLOCCO METODI NON PERMESSI
    # =====================
    def upload_media(self, *args, **kwargs):
        raise PermissionError("Restricted non può caricare contenuti.")

    def add_concert_video(self, *args, **kwargs):
        raise PermissionError("Restricted non può aggiungere video di concerti.")

    def comment_content(self, *args, **kwargs):
        raise PermissionError("Restricted non può commentare contenuti.")

    def add_segment_note(self, *args, **kwargs):
        raise PermissionError("Restricted non può aggiungere note sui contenuti.")

    def manage_content(self, *args, **kwargs):
        raise PermissionError("Restricted non può gestire contenuti.")

    def moderate_content(self, *args, **kwargs):
        raise PermissionError("Restricted non può moderare contenuti.")

    def moderate_comment(self, *args, **kwargs):
        raise PermissionError("Restricted non può moderare commenti.")

    def approve_user(self, *args, **kwargs):
        raise PermissionError("Restricted non può approvare utenti.")

    def deny_user(self, *args, **kwargs):
        raise PermissionError("Restricted non può negare registrazioni.")

    def delete_user(self, *args, **kwargs):
        raise PermissionError("Restricted non può eliminare utenti.")

    # =====================
    # FACTORY METHOD
    # =====================
    @classmethod
    def from_dict(cls, data: dict) -> Optional["Restricted"]:
        if not data:
            return None
        birthday = data.get("birthday")
        if isinstance(birthday, str):
            birthday = datetime.fromisoformat(birthday).date()
        return cls(
            id=data.get("id"),
            mail=data.get("mail"),
            username=data.get("username"),
            password_hash=data.get("password_hash"),
            birthday=birthday,
            bio=data.get("bio", ""),
            profile_pic=data.get("profile_pic"),
            lvl=UserLevel(data.get("lvl", UserLevel.RESTRICTED.value))
        )

# last line