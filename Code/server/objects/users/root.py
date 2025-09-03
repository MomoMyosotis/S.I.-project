# first line

from enum import Enum
from datetime import date, datetime
from typing import Optional, Dict, Any, List
from logs.logger import log_event
from db.db_crud import (
    hash_pswd,
    create_user_db,
    fetch_user_db,
    update_user_db,
    delete_user_db,
    fetch_user_roles_db,
    follow_user as db_add_follow,
    unfollow_user as db_remove_follow
)

# Enum per i livelli degli utenti
class UserLevel(Enum):
    ROOT = 0
    ADMIN = 1
    MOD = 2
    PUBLISHER = 3
    REGULAR = 4
    RESTRICTED = 5
    BANNED = 6

class Root():
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

    def get_permissions(self):
        return []

    def can_post_content(self) -> bool:
        return True

    # =====================
    # METODI DI ISTANZA
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

    @classmethod
    def get_by_id(cls, user_id: int) -> Optional["Root"]:
        data = cls.get_user(user_id=user_id)
        print(f"[DEBUG] get_by_id({user_id}) -> {data} (type={type(data)})")
        if not data:
            return None
        return cls(
            id=data["id"],
            mail=data["mail"],
            username=data["username"],
            password_hash=data["password_hash"],
            birthday=data["birthday"] if isinstance(data["birthday"], date) else datetime.strptime(data["birthday"], "%Y-%m-%d").date(),
            bio=data.get("bio", ""),
            profile_pic=data.get("profile_pic"),
            lvl=UserLevel(data.get("lvl", UserLevel.REGULAR.value))
        )

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
    # METODI DI CLASSE / CRUD UTENTE
    # =====================
    @classmethod
    def create_user(cls, mail: str, username: str, password: str, birthday: str,
                    bio: str = "", profile_pic: str = "") -> Optional[int]:
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
            return result[0] if result else None  # prendi il primo elemento
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

    # =====================
    # METODI DI GESTIONE / AMMINISTRAZIONE
    # =====================
    @classmethod
    def is_admin(cls, user_id: int) -> bool:
        user = cls.get_user(user_id)
        return user and user.get("lvl", UserLevel.REGULAR.value) <= UserLevel.ADMIN.value

    @classmethod
    def can_manage_content(cls, user_id: int, owner_id: int) -> bool:
        return user_id == owner_id or cls.is_admin(user_id)

    @classmethod
    def request_registration(cls, mail: str, username: str, password: str, birthday: str, bio: str = "") -> Optional[int]:
        uid = cls.create_user(mail, username, password, birthday, bio=bio)
        if uid:
            cls.update_user(uid, {"status": "pending"})
        return uid

    @classmethod
    def approve_user(cls, admin_id: int, user_id: int, role: str = "publisher") -> bool:
        if not cls.is_admin(admin_id):
            raise PermissionError("Solo admin")
        user = cls.get_user(user_id)
        mail = user["mail"] if user else "unknown"
        log_event("unknown", mail, "APPROVED", f"Ruolo impostato a {role}")
        return cls.update_user(user_id, {"status": "active", "role": role})

    @classmethod
    def deny_user(cls, admin_id: int, user_id: int, reason: str = "") -> bool:
        if not cls.is_admin(admin_id):
            raise PermissionError("Solo admin")
        user = cls.get_user(user_id)
        mail = user["mail"] if user else "unknown"
        log_event("unknown", mail, "DENIED", reason)
        return cls.update_user(user_id, {"status": "denied"})

    # =====================
    # METODI DI LOGIN
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