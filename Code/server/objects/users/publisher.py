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
        followers: Optional[List[int]] = None,
        followed: Optional[List[int]] = None,
        lvl: UserLevel = UserLevel.PUBLISHER
    ):
        super().__init__(id, mail, username, password_hash, birthday, bio, profile_pic, followers, followed, lvl)

    def get_permissions(self) -> List[str]:
        return ["post_content", "comment", "access_advanced_search"]

    def can_post_content(self) -> bool:
        return True

    # =====================
    # METODI SPECIFICI DEL PUBLISHER
    # =====================
    def upload_media(self, media_type: str, media_data: Dict[str, Any]):
        print(f"{self.username} uploaded {media_type} with data: {media_data}.")
        # Qui puoi integrare logica reale di upload tramite Root o DB

    def manage_own_content(self, action: str, content_id: int):
        print(f"{self.username} {action} their own content with ID {content_id}.")
        # Potresti chiamare self.update_content(content_id, {...}) se implementato nel Root

    def access_own_content(self):
        print(f"{self.username} can access their own published content.")
        # Qui potresti recuperare i contenuti dal DB filtrando per self.id

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
            followers=data.get("followers", []),
            followed=data.get("followed", []),
            lvl=UserLevel(data.get("lvl", UserLevel.PUBLISHER.value))
        )

# last line