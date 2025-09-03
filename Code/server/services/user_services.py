# first line

from typing import List, Optional, Dict, Any
from datetime import datetime
import secrets
from objects.users.root import UserLevel
from objects.users.root import Root
from db.db_crud import verify_password
from utils import user_utils as utils

# =====================
# COSTRUTTORE DI OGGETTI ROOT
# =====================
def _build_user_obj(user_data: Dict[str, Any]) -> Optional[Root]:
    if not user_data:
        return None
    bday_value = user_data.get("birthday")
    birthday = (
        datetime.strptime(bday_value, "%Y-%m-%d").date()
        if isinstance(bday_value, str) else bday_value
    )
    return Root(
        id=user_data.get("id"),
        mail=user_data.get("mail"),
        username=user_data.get("username"),
        password_hash=user_data.get("password_hash"),
        birthday=birthday,
        bio=user_data.get("bio"),
        profile_pic=user_data.get("profile_pic"),
        lvl=UserLevel(user_data.get("lvl", UserLevel.REGULAR.value))
    )

# =====================
# LOGIN / REGISTRAZIONE
# =====================
def login_user(args: List[str], config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    try:
        login_field, password = args[0], args[1]
        if "@" in login_field:
            user_data = Root.get_user(mail=login_field)
        else:
            user_data = Root.get_user(username=login_field)
        if not user_data:
            return {"status": "error", "user_obj": None, "error_msg": "404"}

        user_obj = _build_user_obj(user_data)
        user_dict = user_obj.to_dict_public()  # converti in dict per JSON

        # verifica password
        if not verify_password(password, user_obj.password_hash):
            return {"status": "wrong_password", "user_obj": None, "error_msg": "WRONG_PASSWORD"}

        if config and user_obj.mail in config.get("BLACKLIST", []):
            return {"status": "blacklisted", "user_obj": None, "error_msg": "BLACKLISTED"}

        token = secrets.token_hex(16)
        return {
            "status": "accepted",
            "user_obj": user_dict,   # restituisci il dict, non l'oggetto
            "token": token,
            "error_msg": None
        }
    except Exception as e:
        return {"status": "error", "user_obj": None, "error_msg": str(e)}

def register_user(args: List[Any]) -> Dict[str, Any]:
    try:
        mail, username, password, birthday = args[0], args[1], args[2], args[3]
        if not mail or not username or not password or not birthday:
            return {"status": "ERROR", "error_msg": "Missing required fields"}

        # controllo unicità
        if Root.get_user(username=username):
            return {"status": "ERROR", "error_msg": "Username already in use"}
        if Root.get_user(mail=mail):
            return {"status": "ERROR", "error_msg": "Email already in use"}

        user_id = Root.create_user(mail, username, password, birthday)
        if not user_id:
            return {"status": "ERROR", "error_msg": "Failed to create user"}

        user_data_list = Root.get_user(user_id=user_id)
        if not user_data_list:
            return {"status": "ERROR", "error_msg": "Failed to fetch user after creation"}
        user_data = Root.get_user(user_id=user_id)
        user_obj = _build_user_obj(user_data)

        # genera token
        token = secrets.token_hex(16)

        return {
            "status": "OK",
            "user_id": user_id,
            "user_obj": user_obj.to_dict_public(),
            "token": token
        }
    except Exception as e:
        return {"status": "ERROR", "error_msg": str(e)}

# =====================
# PROFILO / SOCIAL
# =====================
def get_profile(user_obj: Root, target_name: Optional[str] = None) -> Optional[Dict[str, Any]]:
    target_name = target_name or user_obj.username
    target_data = Root.get_user_by_username(target_name)
    if not target_data:
        return None
    target_obj = _build_user_obj(target_data)
    return target_obj.to_dict_public() if target_obj else None

def edit_profile(user_obj: Root, username: str, bio: str, profile_pic: str) -> str:
    updates = {"username": username, "bio": bio, "profile_pic": profile_pic}
    success = Root.update_user(user_obj.id, updates)
    if success:
        # Aggiorno l'oggetto in memoria
        user_obj.username = username
        user_obj.bio = bio
        user_obj.profile_pic = profile_pic
        return "PROFILE_UPDATED"
    return "ERROR: Failed to update profile"

def follow_user(user_obj: Any, target_name: str) -> str:
    # Se user_obj è dict, prendi id
    follower_id = user_obj["id"] if isinstance(user_obj, dict) else user_obj.id

    target = Root.get_user_by_username(target_name)
    if not target:
        return "ERROR: User not found"

    result = Root.follow_user(follower_id, target["id"])
    return result["response"] if result["status"] == "OK" else f"ERROR: {result['error_msg']}"

def unfollow_user(user_obj: Any, target_name: str) -> str:
    follower_id = user_obj["id"] if isinstance(user_obj, dict) else user_obj.id

    target = Root.get_user_by_username(target_name)
    if not target:
        return "ERROR: User not found"

    result = Root.unfollow_user(follower_id, target["id"])
    return result["response"] if result["status"] == "OK" else f"ERROR: {result['error_msg']}"

def get_followers(user_obj: dict) -> list[dict]:
    followers = utils.get_followers(user_obj["id"])
    return followers


def get_followed(user_obj: dict) -> list[dict]:
    followed = utils.get_followed(user_obj["id"])
    return followed

# =====================
# RECUPERO / ASSISTENZA
# =====================
def recover(email: str) -> Dict[str, Any]:
    # placeholder
    return {"status": "ok", "error_msg": None}

def assistance(args: List[str]) -> Dict[str, Any]:
    # placeholder
    return {"status": "ok", "error_msg": None}

# last line