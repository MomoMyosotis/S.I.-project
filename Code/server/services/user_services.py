# first line

from typing import List, Optional, Dict, Any
from datetime import datetime
import secrets
from server.objects.users.root import Root, UserLevel
from server.db.db_crud import verify_password
from server.utils import user_utils as utils

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
def is_logged(user_obj: Optional[Any]) -> bool:
    if not user_obj:
        return False
    # se user_obj è dict o oggetto Root, verifica id esistente
    user_id = user_obj["id"] if isinstance(user_obj, dict) else getattr(user_obj, "id", None)
    return user_id is not None

def login_user(login_field: str, password: str, config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    try:
        # recupera l'utente
        if "@" in login_field:
            user_data = Root.get_user(mail=login_field)
        else:
            user_data = Root.get_user(username=login_field)

        if not user_data:
            print(f"[DEBUG][login_user] Login fallito: utente '{login_field}' non trovato")
            return {"status": "error", "user_obj": None, "error_msg": "User not found"}

        user_obj = _build_user_obj(user_data)
        user_dict = user_obj.to_dict_public()

        # verifica password
        if not verify_password(password, user_obj.password_hash):
            print(f"[DEBUG][login_user] Password errata per utente '{login_field}'")
            return {"status": "wrong_password", "user_obj": None, "error_msg": "WRONG_PASSWORD"}

        # controllo blacklist
        if config and user_obj.mail in config.get("BLACKLIST", []):
            print(f"[DEBUG][login_user] Utente '{login_field}' in blacklist")
            return {"status": "blacklisted", "user_obj": None, "error_msg": "BLACKLISTED"}

        # login OK
        token = secrets.token_hex(16)
        return {
            "status": "accepted",
            "user_obj": user_dict,
            "token": token,
            "error_msg": None
        }

    except Exception as e:
        print(f"[DEBUG][login_user] Errore generico: {e}")
        return {"status": "error", "user_obj": None, "error_msg": str(e)}

def register_user(mail: str, username: str, password: str, birthday_str: str) -> Dict[str, Any]:
    try:
        if not mail or not username or not password or not birthday_str:
            return {"status": "ERROR", "error_msg": "Missing required fields"}

        # parsing della data
        try:
            birthday = datetime.fromisoformat(birthday_str).date()
        except ValueError:
            return {"status": "ERROR", "error_msg": "Invalid birthday format, expected YYYY-MM-DD"}

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
    if not is_logged(user_obj):
        return {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": None}

    # safe extraction while you migrate to full Root everywhere
    username = user_obj["username"] if isinstance(user_obj, dict) else getattr(user_obj, "username", None)
    target_name = target_name or username

    target_data = Root.get_user_by_username(target_name)
    if not target_data:
        return None
    target_obj = _build_user_obj(target_data)
    return target_obj.to_dict_public() if target_obj else None


def edit_profile(user_obj: Root, username: str, bio: str, profile_pic: str) -> str:
    if not is_logged(user_obj):
        return {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": None}
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
    if not is_logged(user_obj):
        return {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": None}
    follower_id = user_obj["id"] if isinstance(user_obj, dict) else user_obj.id
    target = Root.get_user_by_username(target_name)
    if not target:
        return "ERROR: User not found"
    result = Root.follow_user(follower_id, target["id"], user_obj if isinstance(user_obj, dict) else None)
    return result["response"] if result["status"] == "OK" else f"ERROR: {result['error_msg']}"

def unfollow_user(user_obj: Any, target_name: str) -> str:
    if not is_logged(user_obj):
        return {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": None}
    follower_id = user_obj["id"] if isinstance(user_obj, dict) else user_obj.id
    target = Root.get_user_by_username(target_name)
    if not target:
        return "ERROR: User not found"
    result = Root.unfollow_user(follower_id, target["id"], user_obj if isinstance(user_obj, dict) else None)
    return result["response"] if result["status"] == "OK" else f"ERROR: {result['error_msg']}"

def get_followers(user_obj: dict) -> list[dict]:
    if not is_logged(user_obj):
        return {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": None}
    return utils.get_followers(user_obj["id"])

def get_followed(user_obj: dict) -> list[dict]:
    if not is_logged(user_obj):
        return {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": None}
    return utils.get_followed(user_obj["id"])

# =====================
# RECUPERO / ASSISTENZA
# =====================
def recover(email: str) -> Dict[str, Any]:
    # placeholder
    return {"status": "ok", "error_msg": None}

def assistance(username: str, message: str) -> Dict[str, Any]:
    # esempio placeholder
    print(f"[DEBUG] Assistance request from {username}: {message}")
    return {"status": "ok", "error_msg": None}


# last line