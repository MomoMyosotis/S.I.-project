# first line

from typing import Optional, Dict, Any, List
from datetime import date, datetime
from server.objects.users.root import Root, UserLevel

class Publisher(Root):
    def __init__(
        self,
        id: int,
        mail: str,
        username: str,
        password_hash: str,
        birthday: date,
        bio: Optional[str] = "",
        profile_pic: Optional[str] = None,
        lvl: UserLevel = UserLevel.PUBLISHER
    ):
        super().__init__(id, mail, username, password_hash, birthday, bio, profile_pic, lvl)

    # =====================
    # OVERRIDE PERMESSI
    # =====================
    def get_permissions(self) -> List[str]:
        """Permessi specifici del publisher"""
        return ["post_content", "moderate_own_comments", "access_advanced_search"]

    def can_post_content(self) -> bool:
        return True

    # =====================
    # METODI SPECIFICI DEL PUBLISHER
    # =====================
    def upload_media(self, media_type: str, media_data: Dict[str, Any]) -> Dict[str, Any]:
        # Logica reale per pubblicare contenuti
        return {"status": "OK", "action": "MEDIA_UPLOADED", "type": media_type, "data": media_data}

    def manage_own_content(self, action: str, content_id: int) -> Dict[str, Any]:
        # Logica reale di gestione contenuti propri
        return {"status": "OK", "action": f"CONTENT_{action.upper()}", "content_id": content_id}

    def access_own_content(self) -> Dict[str, Any]:
        return {"status": "OK", "action": "ACCESS_GRANTED", "scope": "OWN_CONTENT"}

    def moderate_comment(self, comment_id: int) -> Dict[str, Any]:
        # Moderazione di commenti/interventi sui propri contenuti
        return {"status": "OK", "action": "COMMENT_MODERATED", "comment_id": comment_id}

    def access_all_content(self) -> Dict[str, Any]:
        # Può vedere tutti i contenuti
        return {"status": "OK", "action": "ACCESS_GRANTED", "scope": "ALL_CONTENT"}

    # =====================
    # BLOCCO METODI NON PERMESSI
    # =====================
    def manage_content(self, *args, **kwargs):
        raise PermissionError("Publisher non può gestire contenuti altrui.")

    def approve_user(self, *args, **kwargs):
        raise PermissionError("Publisher non può approvare utenti.")

    def deny_user(self, *args, **kwargs):
        raise PermissionError("Publisher non può negare registrazioni.")

    def delete_user(self, *args, **kwargs):
        raise PermissionError("Publisher non può eliminare utenti.")

    # =====================
    # FACTORY METHOD
    # =====================
    @classmethod
    def from_dict(cls, data: dict) -> Optional["Publisher"]:
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
            lvl=UserLevel(data.get("lvl", UserLevel.PUBLISHER.value))
        )

# last line