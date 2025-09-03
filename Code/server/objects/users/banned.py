# first line

from typing import Optional, List
from datetime import date, datetime
from server.objects.users.root import Root, UserLevel

class Banned(Root):
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
        lvl: UserLevel = UserLevel.BANNED
    ):
        super().__init__(id, mail, username, password_hash, birthday, bio, profile_pic, followers, followed, lvl)

    def get_permissions(self) -> List[str]:
        # Utente bannato non ha permessi
        return []

    def can_post_content(self) -> bool:
        return False

    def access_all_content(self):
        print(f"{self.username} is banned and cannot access any content.")
        # Qui potresti anche sollevare eccezione o bloccare logica reale
        # raise PermissionError("Utente bannato non può accedere ai contenuti.")

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
            followers=data.get("followers", []),
            followed=data.get("followed", []),
            lvl=UserLevel(data.get("lvl", UserLevel.BANNED.value))
        )

# last line