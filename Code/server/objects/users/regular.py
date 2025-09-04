# first line

from typing import Optional, Dict, Any, List
from datetime import date, datetime
from server.objects.users.root import Root, UserLevel

class Regular(Root):
    """
    Utente standard: può pubblicare contenuti, commentare, aggiungere video/meta-info, 
    e commentare contenuti propri e altrui.
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
        lvl: UserLevel = UserLevel.REGULAR
    ):
        super().__init__(id, mail, username, password_hash, birthday, bio, profile_pic, lvl)

    # =====================
    # OVERRIDE PERMESSI
    # =====================
    def get_permissions(self) -> List[str]:
        return [
            "can_post_content",
            "can_comment",
            "can_add_video_meta",
            "can_comment_own_and_other_content",
            "can_access_advanced_search"
        ]

    def can_post_content(self) -> bool:
        return True

    # =====================
    # METODI SPECIFICI
    # =====================
    def upload_media(self, media_type: str, media_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "OK", "action": "MEDIA_UPLOADED", "type": media_type, "data": media_data}

    def add_concert_video(self, video_link: str, meta_info: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "OK", "action": "VIDEO_ADDED", "link": video_link, "meta": meta_info}

    def comment_content(self, content_id: int, comment: str) -> Dict[str, Any]:
        return {"status": "OK", "action": "COMMENT_ADDED", "content_id": content_id, "comment": comment}

    def add_segment_note(self, content_id: int, start: float, end: float, note: str) -> Dict[str, Any]:
        return {"status": "OK", "action": "NOTE_ADDED", "content_id": content_id, "start": start, "end": end, "note": note}

    def access_all_content(self) -> Dict[str, Any]:
        return {"status": "OK", "action": "ACCESS_GRANTED", "scope": "ALL_CONTENT"}

    # =====================
    # BLOCCO METODI NON PERMESSI
    # =====================
    def manage_content(self, *args, **kwargs):
        raise PermissionError("Regular non può gestire contenuti altrui.")

    def moderate_content(self, *args, **kwargs):
        raise PermissionError("Regular non può moderare contenuti.")

    def moderate_comment(self, *args, **kwargs):
        raise PermissionError("Regular non può moderare commenti.")

    def approve_user(self, *args, **kwargs):
        raise PermissionError("Regular non può approvare utenti.")

    def deny_user(self, *args, **kwargs):
        raise PermissionError("Regular non può negare registrazioni.")

    def delete_user(self, *args, **kwargs):
        raise PermissionError("Regular non può eliminare utenti.")

    # =====================
    # FACTORY METHOD
    # =====================
    @classmethod
    def from_dict(cls, data: dict) -> Optional["Regular"]:
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
            lvl=UserLevel(data.get("lvl", UserLevel.REGULAR.value))
        )

# last line