# first line

from enum import Enum
from datetime import date, datetime
from typing import Optional, Dict, Any, List
from db.db_crud import (
    hash_pswd,
    create_user_db,
    fetch_user_db,
    update_user_db,
    delete_user_db,
    fetch_user_roles_db,
    follow_user as db_add_follow,
    unfollow_user as db_remove_follow,
    create_media_db,
    fetch_media_db,
    update_media_db,
    delete_media_db,
    advanced_document_search_db,
    advanced_video_search_db,
    advanced_song_search_db
)

class UserLevel(Enum):
    ROOT = 0
    ADMIN = 1
    MOD = 2
    PUBLISHER = 3
    REGULAR = 4
    RESTRICTED = 5
    BANNED = 6

class Root:
    def __init__(self, id: int, mail: str, username: str, password_hash: str, birthday: date,
                bio: str = "", profile_pic: Optional[str] = None, lvl: UserLevel = UserLevel.REGULAR):
        self.id = id
        self.mail = mail
        self.username = username
        self.password_hash = password_hash
        self.birthday = birthday
        self.bio = bio
        self.profile_pic = profile_pic
        self.followers: List[int] = []
        self.followed: List[int] = []
        self.lvl = lvl

    # =====================
    # PERMESSI
    # =====================
    def get_permissions(self):
        return []

    def can_post_content(self) -> bool:
        return True

    def access_all_content(self) -> bool:
        return True

    # =====================
    # GESTIONE CONTENUTI
    # =====================
    def manage_content(self, action: str, media_id: Optional[int] = None, fields: Optional[Dict[str, Any]] = None):
        if action not in ["create", "update", "delete"]:
            raise ValueError("Azione non valida")
        if action in ["update", "delete"] and not media_id:
            raise ValueError("media_id richiesto per update/delete")

        owner_id = None
        if media_id:
            media = fetch_media_db(media_id)
            if not media:
                raise ValueError("Contenuto non trovato")
            owner_id = media.get("user_id")

        if media_id and not self.can_manage_content(self.id, owner_id):
            raise PermissionError("Non puoi gestire questo contenuto")

        if action == "create":
            media_type = fields.pop("type", "song")
            title = fields.pop("title", "Untitled")
            year = fields.pop("year", None)
            description = fields.pop("description", "")
            link = fields.pop("link", "")
            created_at = fields.pop("created_at", datetime.now())
            return create_media_db((media_type, title, year, description, link, created_at))
        elif action == "update":
            return update_media_db(media_id, fields)
        elif action == "delete":
            return delete_media_db(media_id)

    # =====================
    # MODERAZIONE CONTENUTI
    # =====================
    def moderate_content(self, media_id: int, action: str, target_user_id: Optional[int] = None, updates: Optional[Dict[str, Any]] = None):
        if action not in ["edit", "delete", "ban_user", "restrict_user"]:
            raise ValueError("Azione di moderazione non valida")

        media = fetch_media_db(media_id)
        if not media:
            raise ValueError("Contenuto non trovato")

        owner_id = media.get("user_id")
        if not self.is_admin(self.id) and self.id != owner_id and self.lvl != UserLevel.MOD:
            raise PermissionError("Non puoi moderare questo contenuto")

        if action == "edit":
            if not updates:
                raise ValueError("Dati aggiornamento richiesti")
            return update_media_db(media_id, updates)
        elif action == "delete":
            return delete_media_db(media_id)
        elif action in ["ban_user", "restrict_user"]:
            if not target_user_id:
                target_user_id = owner_id
            new_lvl = UserLevel.BANNED.value if action == "ban_user" else UserLevel.RESTRICTED.value
            return update_user_db(target_user_id, {"lvl": new_lvl})

    @staticmethod
    def advanced_song_search(filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        return advanced_song_search_db(filters)

    @staticmethod
    def advanced_document_search(filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        return advanced_document_search_db(filters)

    @staticmethod
    def advanced_video_search(filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        return advanced_video_search_db(filters)

    # =====================
    # ISTANZA / UTILI
    # =====================
    def to_dict_public(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "username": self.username,
            "birthday": self.birthday.isoformat() if isinstance(self.birthday, date) else self.birthday,
            "bio": self.bio,
            "profile_pic": self.profile_pic,
            "followers_count": len(self.followers),
            "followed_count": len(self.followed),
            "lvl": self.lvl.value
        }

    def check_password(self, password: str, hasher) -> bool:
        return hasher(password, self.password_hash)

    # =====================
    # CRUD UTENTE / FOLLOW
    # =====================
    @classmethod
    def create_user(cls, mail: str, username: str, password: str, birthday: str, bio: str = "", profile_pic: str = "") -> Optional[int]:
        password_hash = hash_pswd(password)
        if isinstance(birthday, str):
            birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
        fields = (mail, username, password_hash, birthday, bio, profile_pic)
        return create_user_db(fields)

    @classmethod
    def get_user(cls, user_id: int = None, username: str = None, mail: str = None) -> Optional[Dict[str, Any]]:
        filters = {}
        if user_id is not None:
            filters["id"] = user_id
        if username is not None:
            filters["username"] = username
        if mail is not None:
            filters["mail"] = mail
        result = fetch_user_db(filters=filters if filters else None)
        if isinstance(result, list):
            return result[0] if result else None
        return result

    @classmethod
    def get_user_by_username(cls, username: str) -> Optional[Dict[str, Any]]:
        return cls.get_user(username=username)

    @classmethod
    def get_user_roles(cls, user_id: int) -> List[str]:
        return fetch_user_roles_db(user_id)

    @classmethod
    def update_user(cls, user_id: int, updates: Dict[str, Any]) -> bool:
        return update_user_db(user_id, updates)

    @classmethod
    def delete_user(cls, user_id: int) -> bool:
        return delete_user_db(user_id)

    @classmethod
    def follow_user(cls, follower_id: int, followee_id: int):
        if not cls.get_user(user_id=follower_id) or not cls.get_user(user_id=followee_id):
            return {"status": "ERROR", "error_msg": "Utente non trovato"}
        db_add_follow(follower_id, followee_id)
        return {"status": "OK", "response": "FOLLOWED"}

    @classmethod
    def unfollow_user(cls, follower_id: int, followee_id: int):
        if not cls.get_user(user_id=follower_id) or not cls.get_user(user_id=followee_id):
            return {"status": "ERROR", "error_msg": "Utente non trovato"}
        db_remove_follow(follower_id, followee_id)
        return {"status": "OK", "response": "UNFOLLOWED"}

    # =====================
    # PERMESSI / UTILI
    # =====================
    @classmethod
    def can_manage_content(cls, user_id: int, owner_id: int) -> bool:
        return user_id == owner_id or cls.is_admin(user_id)

    @classmethod
    def is_admin(cls, user_id: int) -> bool:
        user = cls.get_user(user_id)
        return user and user.get("lvl", UserLevel.REGULAR.value) <= UserLevel.ADMIN.value

    # =====================
    # LOGIN
    # =====================
    @classmethod
    def get_user_by_login(cls, mail: str, password: str) -> Optional[Dict[str, Any]]:
        user = cls.get_user(mail=mail)
        if user and "password_hash" in user:
            from db.db_crud import verify_password
            if verify_password(password, user["password_hash"]):
                return user
        return None

    @classmethod
    def get_username(cls, user_id: int) -> Optional[str]:
        user = cls.get_user(user_id=user_id)
        return user["username"] if user else None

# last lined