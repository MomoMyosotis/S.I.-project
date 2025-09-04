# first line

from typing import Optional, List, Dict, Any
from datetime import date, datetime
from server.objects.users.root import Root, UserLevel

class Mod(Root):
    def __init__(
        self,
        id: int,
        mail: str,
        username: str,
        password_hash: str,
        birthday: date,
        bio: Optional[str] = "",
        profile_pic: Optional[str] = None,
        lvl: UserLevel = UserLevel.MOD
    ):
        super().__init__(id, mail, username, password_hash, birthday, bio, profile_pic, lvl)

    # =====================
    # OVERRIDE PERMESSI
    # =====================
    def get_permissions(self) -> List[str]:
        """Permessi specifici del moderatore"""
        return ["manage_content", "moderate_content", "moderate_comments", "access_advanced_search"]

    def can_post_content(self) -> bool:
        """Il moderatore non pubblica come un publisher"""
        return False

    # =====================
    # METODI SPECIFICI DEL MOD
    # =====================
    def manage_content(self, content_id: Optional[int] = None) -> Dict[str, Any]:
        # Qui va la logica reale di gestione contenuti (upload/edit/delete)
        return {"status": "OK", "action": "CONTENT_MANAGED", "content_id": content_id}

    def moderate_content(self, content_id: int) -> Dict[str, Any]:
        return {"status": "OK", "action": "CONTENT_MODERATED", "content_id": content_id}

    def moderate_comment(self, comment_id: int) -> Dict[str, Any]:
        return {"status": "OK", "action": "COMMENT_MODERATED", "comment_id": comment_id}

    def access_all_content(self) -> Dict[str, Any]:
        return {"status": "OK", "action": "ACCESS_GRANTED", "scope": "ALL_CONTENT"}

    # =====================
    # BLOCCO METODI NON PERMESSI
    # =====================
    def approve_user(self, *args, **kwargs):
        raise PermissionError("Moderatore non può approvare utenti.")

    def deny_user(self, *args, **kwargs):
        raise PermissionError("Moderatore non può negare registrazioni.")

    def delete_user(self, *args, **kwargs):
        raise PermissionError("Moderatore non può eliminare utenti.")

    # =====================
    # FACTORY METHOD
    # =====================
    @classmethod
    def from_dict(cls, data: dict) -> Optional["Mod"]:
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
            lvl=UserLevel(data.get("lvl", UserLevel.MOD.value))
        )

# last line