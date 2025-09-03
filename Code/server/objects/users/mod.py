# first line
from typing import Optional, List
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
        followers: Optional[List[int]] = None,
        followed: Optional[List[int]] = None,
        lvl: UserLevel = UserLevel.MOD
    ):
        super().__init__(id, mail, username, password_hash, birthday, bio, profile_pic, followers, followed, lvl)

    def get_permissions(self) -> List[str]:
        return ["moderate_content", "moderate_comments", "access_advanced_search"]

    def can_post_content(self) -> bool:
        return False

    # =====================
    # METODI SPECIFICI DEL MOD
    # =====================
    def moderate_content(self, content_id: int):
        print(f"{self.username} can moderate content with ID {content_id}.")
        # Qui potresti inserire logica reale di moderazione

    def moderate_comment(self, comment_id: int):
        print(f"{self.username} can moderate comment with ID {comment_id}.")
        # Logica reale di moderazione dei commenti

    def access_all_content(self):
        """Accesso ai contenuti moderabili, ma non ai propri contenuti da pubblicatore"""
        print(f"{self.username} can access all moderatable content.")
        # Qui potresti filtrare i contenuti dal DB

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
            followers=data.get("followers", []),
            followed=data.get("followed", []),
            lvl=UserLevel(data.get("lvl", UserLevel.MOD.value))
        )

# last line