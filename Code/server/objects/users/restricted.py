# first  line

from typing import Optional, List
from datetime import date, datetime
from server.objects.users.root import Root, UserLevel

class Restricted(Root):
    def __init__(
        self,
        id: int,
        mail: str,
        username: str,
        password_hash: str,
        birthday: date,
        bio: Optional[str] = "",
        profile_pic: Optional[str] = None,
        followers: Optional[List[int]] = None,
        followed: Optional[List[int]] = None,
        lvl: UserLevel = UserLevel.RESTRICTED
    ):
        super().__init__(id, mail, username, password_hash, birthday, bio, profile_pic, followers, followed, lvl)

    def get_permissions(self) -> List[str]:
        # Utente restricted può solo visualizzare contenuti
        return ["view_content"]

    def can_post_content(self) -> bool:
        return False

    # =====================
    # METODI SPECIFICI DEL RESTRICTED USER
    # =====================
    def view_content(self, content_id: int):
        print(f"{self.username} is viewing content with ID {content_id}.")
        # Qui puoi integrare logica reale per recuperare contenuto dal DB

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
            followers=data.get("followers", []),
            followed=data.get("followed", []),
            lvl=UserLevel(data.get("lvl", UserLevel.RESTRICTED.value))
        )

# last line