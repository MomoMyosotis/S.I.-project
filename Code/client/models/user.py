# first line

from enum import Enum
from typing import Dict, Any, List

class UserLevel(Enum):
    ROOT = 0
    ADMIN = 1
    MOD = 2
    PUBLISHER = 3
    REGULAR = 4
    RESTRICTED = 5
    BANNED = 6

class User:
    # ===== PERMISSIONS MAP (clean & grouped) =====
    PERMISSIONS: Dict[int, str] = {
        1:  "create own account",
        2:  "update profile data or password/email",
        3:  "ban a user",
        4:  "access any user's data",
        13: "follow users",
        14: "unfollow users",
        15: "see any profile",
        5:  "create media",
        6:  "access any media",
        7:  "update any media",
        8:  "delete any media",
        16: "advanced media search",
        9:  "create interventions",
        10: "access any interventions",
        11: "update any intervention",
        12: "delete any intervention",
        17: "see media commented by itself",
        18: "create own library",
    }

    def __init__(
        self,
        id: int,
        username: str,
        followers: int,
        followed: int,
        bio: str = "",
        lvl: UserLevel = UserLevel.REGULAR,
        profile_pic: str = "",
        publications_count: int = 0,
        following_count: int = 0,
        followers_count: int = 0
    ):
        print(f"[DEBUG][User.__init__] id={id}, username={username}, followers={followers}, followed={followed}, bio='{bio}', lvl={lvl}")
        self.id = id
        self.username = username
        self.followers = followers
        self.followed = followed
        self.bio = bio
        self.lvl = lvl
        self.profile_pic = profile_pic
        self.publications_count = publications_count
        self.following_count = following_count
        self.followers_count = followers_count

    @staticmethod
    def from_server(data: Dict[str, Any]) -> "User":
        print(f"[DEBUG][User.from_server] raw server data: {data}")
        # normalize keys that server might return with slightly different names
        normalized = dict(data)
        normalized["user_id"] = normalized.get("user_id", normalized.get("id"))
        normalized["followers_count"] = normalized.get("followers_count", normalized.get("followers", 0))
        normalized["following_count"] = normalized.get("following_count", normalized.get("followed_count", normalized.get("following", 0)))
        normalized["profile_pic"] = normalized.get("profile_pic", normalized.get("profile_picture_url", ""))
        normalized["bio"] = normalized.get("bio", normalized.get("full_bio", ""))

        user = User(
            id=normalized.get("user_id"),
            username=normalized.get("username"),
            followers=normalized.get("followers_count", 0),
            followed=normalized.get("following_count", 0),
            bio=normalized.get("bio", ""),
            lvl=UserLevel(normalized.get("lvl")) if normalized.get("lvl") is not None else UserLevel.REGULAR,
            profile_pic=normalized.get("profile_pic", ""),
            publications_count=normalized.get("publications_count", 0),
            following_count=normalized.get("following_count", 0),
            followers_count=normalized.get("followers_count", 0)
        )
        print(f"[DEBUG][User.from_server] created User instance: {user.__dict__}")
        return user

    def to_dict(self) -> Dict[str, Any]:
        # shape data expected by the client profile page
        return {
            "id": self.id,
            "username": self.username,
            "profile_picture_url": self.profile_pic or None,
            "profile_pic": self.profile_pic,
            "publications_count": self.publications_count,
            "following_count": self.following_count,
            "followed_count": self.following_count,
            "followers_count": self.followers_count,
            "full_bio": self.bio,
            "bio": self.bio,
            "lvl": self.lvl.value if isinstance(self.lvl, UserLevel) else self.lvl
        }

    # ===== STATIC INFORMATION ABOUT PERMISSIONS =====
    @classmethod
    def possible_action_list(cls) -> Dict[int, str]:
        print("[DEBUG][User.possible_action_list] returning PERMISSIONS map")
        return cls.PERMISSIONS

    # ===== PERMISSION CHECKER (draft) =====
    def get_permission(self) -> List[int]:
        print(f"[DEBUG][User.get_permission] Checking permissions for lvl={self.lvl}")
        lvl = self.lvl
        allowed = []

        for action_id, description in self.PERMISSIONS.items():
            if lvl == UserLevel.BANNED:
                if action_id in [1, 15]:
                    allowed.append(action_id)
                    print(f"[DEBUG][User.get_permission] BANNED allowed action {action_id}: {description}")
                continue

            if lvl == UserLevel.RESTRICTED:
                if action_id in [11, 12, 9]:
                    print(f"[DEBUG][User.get_permission] RESTRICTED denied action {action_id}: {description}")
                    continue

            if lvl == UserLevel.ROOT:
                allowed.append(action_id)
                print(f"[DEBUG][User.get_permission] ROOT allowed action {action_id}: {description}")
                continue

            allowed.append(action_id)
            print(f"[DEBUG][User.get_permission] allowed action {action_id}: {description}")

        print(f"[DEBUG][User.get_permission] final allowed list: {allowed}")
        return allowed

# last line