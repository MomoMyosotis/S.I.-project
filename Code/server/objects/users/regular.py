# first line

from typing import Optional, Dict, Any, List
from datetime import date, datetime
from server.objects.users.root import Root, UserLevel

class Regular(Root):
    """
    Utente di default del sistema: può pubblicare contenuti e commentare,
    inserire video/link YouTube di concerti, aggiungere meta-informazioni
    sui brani, e commentare spartiti/testi/accordi.
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
        followers: Optional[List[int]] = None,
        followed: Optional[List[int]] = None,
        lvl: UserLevel = UserLevel.REGULAR
    ):
        super().__init__(id, mail, username, password_hash, birthday, bio, profile_pic, followers, followed, lvl)

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
    # METODI SPECIFICI DEL REGULAR USER
    # =====================
    def upload_media(self, media_type: str, media_data: Dict[str, Any]):
        print(f"{self.username} ha caricato {media_type} con i dati: {media_data}")
        # Qui puoi integrare logica reale di upload usando classmethod CRUD di Root

    def add_concert_video(self, video_link: str, meta_info: Dict[str, Any]):
        print(f"{self.username} ha aggiunto un video di concerto: {video_link} con meta-info: {meta_info}")
        # Possibile integrazione con DB o Root.create_content()

    def comment_content(self, content_id: int, comment: str):
        print(f"{self.username} ha commentato il contenuto {content_id}: {comment}")
        # Possibile integrazione con Root.update_content()

    def add_segment_note(self, content_id: int, start: float, end: float, note: str):
        print(f"{self.username} ha aggiunto una nota sul contenuto {content_id} da {start} a {end}: {note}")
        # Possibile integrazione con Root.update_content()

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
            followers=data.get("followers", []),
            followed=data.get("followed", []),
            lvl=UserLevel(data.get("lvl", UserLevel.REGULAR.value))
        )

# last line