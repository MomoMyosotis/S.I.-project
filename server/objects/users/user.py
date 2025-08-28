from enum import Enum
from datetime import date


class UserLevel(Enum):
    BANNED = 0
    REGULAR = 1
    PUBLISHER = 2
    MODERATOR = 3
    ADMIN = 4
    ROOT = 5


class User:
    def __init__(self, id, mail, username, password_hash, birthday, bio="", profile_pic=None, 
                followers=None, followed=None, lvl=UserLevel.REGULAR):
        self.id = id
        self.mail = mail
        self.username = username
        self.password_hash = password_hash
        self.birthday = birthday
        self.bio = bio
        self.profile_pic = profile_pic
        self.followers = followers if followers is not None else []
        self.followed = followed if followed is not None else []
        self.lvl = lvl

    def __str__(self):
        return f"User({self.username}, lvl={self.lvl.name})"

    # Serializzazione interna (server)
    def to_dict_internal(self):
        return {
            "id": self.id,
            "mail": self.mail,
            "username": self.username,
            "password_hash": self.password_hash,
            "birthday": self.birthday.isoformat() if isinstance(self.birthday, date) else self.birthday,
            "bio": self.bio,
            "profile_pic": self.profile_pic,
            "followers": self.followers,
            "followed": self.followed,
            "lvl": self.lvl.value
        }

    # Serializzazione pubblica (per client)
    def to_dict_public(self):
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

    # --- Metodi ---
    def check_password(self, password, hasher):
        """Verifica la password. `hasher` è una funzione esterna tipo bcrypt.checkpw"""
        return hasher(password, self.password_hash)

    def edit_profile(self, username=None, bio=None, profile_pic=None):
        if username:
            self.username = username
        if bio:
            self.bio = bio
        if profile_pic:
            self.profile_pic = profile_pic

    def has_role(self, role: UserLevel) -> bool:
        return self.lvl.value >= role.value

    def follow(self, other_user):
        if other_user.id not in self.followed:
            self.followed.append(other_user.id)
            other_user.followers.append(self.id)

    def unfollow(self, other_user):
        if other_user.id in self.followed:
            self.followed.remove(other_user.id)
            if self.id in other_user.followers:
                other_user.followers.remove(self.id)

    def get_followers(self):
        return self.followers

    def get_followed(self):
        return self.followed

    def to_dict_summary(self):
        """Versione compatta per feed, commenti o liste utenti"""
        return {
            "id": self.id,
            "username": self.username,
            "profile_pic": self.profile_pic,
            "lvl": self.lvl.value
        }