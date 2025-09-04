# first line

# banned.py

from typing import Optional, List
from datetime import date, datetime
from server.objects.users.root import Root, UserLevel

class Banned(Root):
    """
    Utente bannato: non può fare nulla.
    Serve principalmente per bloccare registrazioni/accessi con stessa mail o username.
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
        lvl: UserLevel = UserLevel.BANNED
    ):
        super().__init__(id, mail, username, password_hash, birthday, bio, profile_pic, lvl)

    # =====================
    # OVERRIDE PERMESSI
    # =====================
    def get_permissions(self) -> List[str]:
        return []

    def can_post_content(self) -> bool:
        return False

    def access_all_content(self, *args, **kwargs):
        raise PermissionError("Utente bannato non può accedere ai contenuti.")

    # =====================
    # BLOCCO TUTTI GLI ALTRI METODI
    # =====================
    def upload_media(self, *args, **kwargs):
        raise PermissionError("Utente bannato non può caricare contenuti.")

    def add_concert_video(self, *args, **kwargs):
        raise PermissionError("Utente bannato non può aggiungere video di concerti.")

    def comment_content(self, *args, **kwargs):
        raise PermissionError("Utente bannato non può commentare contenuti.")

    def add_segment_note(self, *args, **kwargs):
        raise PermissionError("Utente bannato non può aggiungere note sui contenuti.")

    def manage_content(self, *args, **kwargs):
        raise PermissionError("Utente bannato non può gestire contenuti.")

    def moderate_content(self, *args, **kwargs):
        raise PermissionError("Utente bannato non può moderare contenuti.")

    def moderate_comment(self, *args, **kwargs):
        raise PermissionError("Utente bannato non può moderare commenti.")

    def approve_user(self, *args, **kwargs):
        raise PermissionError("Utente bannato non può approvare utenti.")

    def deny_user(self, *args, **kwargs):
        raise PermissionError("Utente bannato non può negare registrazioni.")

    def delete_user(self, *args, **kwargs):
        raise PermissionError("Utente bannato non può eliminare utenti.")

    def advanced_video_search(self, *args, **kwargs):
        raise PermissionError("Utente bannato non può fare ricerche per video")

    def advanced_document_search(self, *args, **kwargs):
        raise PermissionError("Utente bannato non può fare ricerche per documenti")

    def advanced_song_search(self, *args, **kwargs):
        raise PermissionError("Utente bannato non può fare ricerche per song")

    # =====================
    # FACTORY METHOD
    # =====================
    @classmethod
    def from_dict(cls, data: dict) -> Optional["Banned"]:
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
            lvl=UserLevel(data.get("lvl", UserLevel.BANNED.value))
        )

# last line