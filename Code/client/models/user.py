# first line

from enum import Enum
from typing import Dict, Any, List, Optional

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
        id: Optional[int],
        username: Optional[str],
        followers_count: int = 0,
        following_count: int = 0,
        bio: str = "",
        lvl: Optional[UserLevel] = UserLevel.REGULAR,
        profile_pic: Optional[str] = None,
        publications_count: int = 0,
    ):
        # stable attributes matching server object
        self.id = id
        self.username = username
        self.followers_count = followers_count
        self.following_count = following_count
        self.bio = bio or ""
        self.lvl = lvl if isinstance(lvl, UserLevel) else (UserLevel(lvl) if lvl is not None else UserLevel.REGULAR)
        self.profile_pic = profile_pic
        self.publications_count = publications_count

    @staticmethod
    def _unwrap_envelope(data: Any) -> Dict[str, Any]:
        # unwrap nested envelopes commonly returned by server
        inner = data if isinstance(data, dict) else {}
        seen = set()
        while isinstance(inner, dict):
            if id(inner) in seen:
                break
            seen.add(id(inner))
            for k in ("response", "result", "user", "user_obj"):
                if k in inner and isinstance(inner[k], (dict, list)):
                    inner = inner[k]
                    break
            else:
                break
        return inner if isinstance(inner, dict) else {}

    @staticmethod
    def from_server(data: Dict[str, Any]) -> "User":
        """
        Robustly create a User from server data. Accepts many shapes:
        - direct user dict
        - envelope: {"status":"OK","response":{...}}
        - alternative key names
        """
        raw = User._unwrap_envelope(data)
        if not isinstance(raw, dict):
            raw = {}

        # normalization with fallbacks
        uid = raw.get("id") or raw.get("user_id") or raw.get("_id")
        username = raw.get("username") or raw.get("user") or raw.get("name")
        # counts: try multiple alternatives
        followers_count = int(raw.get("followers_count")
                              or raw.get("followers")
                              or raw.get("followers_count_total", 0) or 0)
        following_count = int(raw.get("following_count")
                              or raw.get("followed")
                              or raw.get("following")
                              or 0)
        publications_count = int(raw.get("publications_count") or raw.get("count") or raw.get("media_count") or 0)
        profile_pic = raw.get("profile_pic") or raw.get("profile_picture_url") or raw.get("avatar")
        bio = raw.get("full_bio") or raw.get("bio") or raw.get("description") or ""

        # lvl may be int or string; try safe conversions
        lvl_raw = raw.get("lvl") if "lvl" in raw else raw.get("level") if "level" in raw else raw.get("lvl_value", None)
        lvl = UserLevel.REGULAR
        try:
            if lvl_raw is not None:
                # accept numeric strings too
                if isinstance(lvl_raw, str) and lvl_raw.isdigit():
                    lvl = UserLevel(int(lvl_raw))
                elif isinstance(lvl_raw, (int, float)):
                    lvl = UserLevel(int(lvl_raw))
                else:
                    # try mapping by name
                    lvl = UserLevel[lvl_raw.upper()] if isinstance(lvl_raw, str) and lvl_raw.upper() in UserLevel.__members__ else UserLevel.REGULAR
        except Exception:
            lvl = UserLevel.REGULAR

        return User(
            id=uid,
            username=username,
            followers_count=followers_count,
            following_count=following_count,
            bio=bio,
            lvl=lvl,
            profile_pic=profile_pic,
            publications_count=publications_count
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize the model in the shape client code (templates / services) expects.
        Keep both 'profile_pic' (id) and 'profile_picture_url' keys for compatibility.
        """
        return {
            "id": self.id,
            "username": self.username,
            "profile_pic": self.profile_pic,
            "profile_picture_url": f"/profile/picture/{self.profile_pic}" if self.profile_pic else None,
            "publications_count": int(self.publications_count or 0),
            "following_count": int(self.following_count or 0),
            "followers_count": int(self.followers_count or 0),
            "full_bio": self.bio,
            "bio": self.bio,
            # expose lvl as integer to simplify checks in existing code
            "lvl": int(self.lvl.value) if isinstance(self.lvl, UserLevel) else self.lvl
        }

    # ===== STATIC INFORMATION ABOUT PERMISSIONS =====
    @classmethod
    def possible_action_list(cls) -> Dict[int, str]:
        return cls.PERMISSIONS

    def get_permission(self) -> List[int]:
        """
        Basic permission list generator. This is a simplified implementation
        kept for backward compatibility with existing client checks.
        """
        lvl = self.lvl
        allowed = []

        # banned: very restricted
        if lvl == UserLevel.BANNED:
            # allow minimal actions optionally
            if 1 in self.PERMISSIONS:
                allowed.append(1)
            return allowed

        # root can do everything
        if lvl == UserLevel.ROOT:
            return list(self.PERMISSIONS.keys())

        # otherwise return most actions (this can be tuned)
        for action_id in self.PERMISSIONS.keys():
            allowed.append(action_id)
        return allowed

# last line