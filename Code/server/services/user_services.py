# first line

from typing import List, Optional, Dict, Any
from datetime import datetime
import secrets
from server.objects.users.root import Root, UserLevel
from server.db.db_crud import verify_password, db_get_followers, db_get_following
from server.utils import user_utils as utils

# =====================
# COSTRUTTORE DI OGGETTI ROOT
# =====================
def _build_user_obj(user_data: Dict[str, Any]) -> Optional[Root]:
    if not user_data:
        return None

    def _extract_level(data: Dict[str, Any]) -> UserLevel:
        # Accept many possible DB keys to avoid silently defaulting to REGULAR (4)
        for k in ("lvl", "lvl_id", "level", "lvl_value", "level_id"):
            if k in data and data[k] is not None:
                val = data[k]
                if isinstance(val, UserLevel):
                    return val
                try:
                    return UserLevel(int(val))
                except Exception:
                    print(f"[DEBUG][_extract_level] couldn't parse level from key {k}: {val!r}")
                    break
        # final fallback
        return UserLevel.REGULAR

    bday_value = user_data.get("birthday")
    birthday = (
        datetime.strptime(bday_value, "%Y-%m-%d").date()
        if isinstance(bday_value, str) else bday_value
    )
    level = _extract_level(user_data)
    user = Root(
        id=user_data.get("id"),
        mail=user_data.get("mail"),
        username=user_data.get("username"),
        password_hash=user_data.get("password_hash"),
        birthday=birthday,
        bio=user_data.get("bio"),
        profile_pic=user_data.get("profile_pic"),
        lvl=level
    )
    # populate follower/following lists so to_dict_public returns correct counts
    try:
        if user.id is not None:
            followers = db_get_followers(user.id) or []
            following = db_get_following(user.id) or []
            # store as lists of ids (keeps memory small) — other code only needs counts or id checks
            user.followers = [r.get("id") for r in followers if r.get("id") is not None]
            user.followed = [r.get("id") for r in following if r.get("id") is not None]
    except Exception as e:
        print(f"[DEBUG][_build_user_obj] could not load follow lists: {e}")
    return user

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
    if not target_obj:
        return None
    public = target_obj.to_dict_public()
    # if viewer is logged, add is_followed flag
    try:
        viewer_id = user_obj["id"] if isinstance(user_obj, dict) else getattr(user_obj, "id", None)
        if viewer_id:
            following = db_get_following(viewer_id) or []
            public["is_followed"] = any(f.get("id") == target_obj.id for f in following)
    except Exception:
        public["is_followed"] = False
    return public

def edit_profile(user_obj: Root, username=None, bio=None, profile_pic=None) -> str:
    if not is_logged(user_obj):
        return {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": None}

    # If caller passed a payload dict as the second arg, extract fields
    if isinstance(username, dict):
        payload = username
        # prefer 'bio' then 'full_bio'
        bio = payload.get("bio") if payload.get("bio") is not None else payload.get("full_bio", bio)
        profile_pic = payload.get("profile_pic", profile_pic)
        username = payload.get("username", None)

    # Default username to current user if missing
    if username is None:
        username = user_obj["username"] if isinstance(user_obj, dict) else getattr(user_obj, "username", None)

    # Build updates only with provided (non-None) fields
    updates = {}
    if username is not None:
        updates["username"] = username
    if bio is not None:
        updates["bio"] = bio
    if profile_pic is not None:
        updates["profile_pic"] = profile_pic

    if not updates:
        return "ERROR: No updates provided"

    # Resolve user id
    uid = user_obj["id"] if isinstance(user_obj, dict) else getattr(user_obj, "id", None)
    success = Root.update_user(uid, updates)
    if success:
        # Update in-memory object (if Root instance)
        if not isinstance(user_obj, dict):
            if "username" in updates:
                user_obj.username = updates["username"]
            if "bio" in updates:
                user_obj.bio = updates["bio"]
            if "profile_pic" in updates:
                user_obj.profile_pic = updates["profile_pic"]
        else:
            # if it's a dict, update keys for callers relying on it
            user_obj.update(updates)
        return "PROFILE_UPDATED"
    return "ERROR: Failed to update profile"

def change_lvl(user_obj: Root, *args) -> dict:
    """
    Change a target user's level.

    Accepts either:
        - (user_obj, new_level)           -> change caller's own level (rare)
        - (user_obj, target_username, new_level) -> change another user's level

    Returns a dict { "status": "OK", "response": "..."} on success or
    { "status": "ERROR", "error_msg": "..." } on failure.
    """
    if not is_logged(user_obj):
        return {"status": "ERROR", "error_msg": "NOT_LOGGED_IN"}

    # resolve viewer id & level
    viewer_id = user_obj["id"] if isinstance(user_obj, dict) else getattr(user_obj, "id", None)
    viewer_lvl_raw = user_obj.get("lvl") if isinstance(user_obj, dict) else getattr(user_obj, "lvl", None)
    try:
        viewer_lvl = int(viewer_lvl_raw) if isinstance(viewer_lvl_raw, (int, float, str)) and str(viewer_lvl_raw).isdigit() else (viewer_lvl_raw.value if hasattr(viewer_lvl_raw, "value") else None)
    except Exception:
        viewer_lvl = None

    # parse args
    if len(args) == 1:
        # only new_level -> target is self
        target_identifier = viewer_id
        try:
            new_level = int(args[0])
        except Exception:
            return {"status": "ERROR", "error_msg": "Invalid new_level"}
    elif len(args) >= 2:
        target_identifier = args[0]
        try:
            new_level = int(args[1])
        except Exception:
            return {"status": "ERROR", "error_msg": "Invalid new_level"}
    else:
        return {"status": "ERROR", "error_msg": "Missing parameters"}

    # fetch target user row
    if isinstance(target_identifier, int):
        target_row = Root.get_user(user_id=target_identifier)
    else:
        target_row = Root.get_user_by_username(str(target_identifier))

    if not target_row:
        return {"status": "ERROR", "error_msg": "Target user not found"}

    target_id = target_row.get("id")
    target_lvl = None
    try:
        t_lvl = target_row.get("lvl") if "lvl" in target_row else target_row.get("level")
        target_lvl = int(t_lvl) if isinstance(t_lvl, (int, float, str)) and str(t_lvl).isdigit() else (UserLevel(t_lvl).value if isinstance(t_lvl, UserLevel) else None)
    except Exception:
        target_lvl = None

    # Permission checks:
    # - root (0) can change anyone
    # - admin (1) can change anyone except roots (target_lvl == 0)
    # - others cannot change levels of others; only root/admin allowed to change any level
    if viewer_id == target_id:
        # changing own level allowed only for admins/roots (avoid regular users escalating themselves)
        if viewer_lvl not in (UserLevel.ROOT.value, UserLevel.ADMIN.value):
            return {"status": "ERROR", "error_msg": "Permission denied to change own level"}
    else:
        if viewer_lvl == UserLevel.ROOT.value:
            pass  # allowed
        elif viewer_lvl == UserLevel.ADMIN.value:
            if target_lvl == UserLevel.ROOT.value:
                return {"status": "ERROR", "error_msg": "Cannot manage root account"}
        else:
            return {"status": "ERROR", "error_msg": "Permission denied"}

    # apply level change
    try:
        ok = Root.change_user_level(target_id, new_level)
        if ok:
            # if server uses object instances, try to update in-memory user_obj too
            if not isinstance(user_obj, dict):
                try:
                    if getattr(user_obj, "id", None) == target_id:
                        user_obj.lvl = UserLevel(new_level)
                except Exception:
                    pass
            return {"status": "OK", "response": "LEVEL_CHANGED"}
        return {"status": "ERROR", "error_msg": "Failed to change level"}
    except Exception as e:
        return {"status": "ERROR", "error_msg": str(e)}

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
# RECUPERO / ASSISTENZA (placeholders 4 now)
# =====================
def recover(email: str) -> Dict[str, Any]:
    # placeholder
    return {"status": "ok", "error_msg": None}

def assistance(username: str, message: str) -> Dict[str, Any]:
    # placeholder
    print(f"[DEBUG] Assistance request from {username}: {message}")
    return {"status": "ok", "error_msg": None}

# has to pass maybe from server.utils.user_utils that then calls server.db.db_crud
def search_users(user_obj: Any, term: str = "", offset: int = 0, limit: int = 20):
    try:
        from server.db.db_crud import fetch_all
        if term is None:
            term = ""
        q = """
            SELECT id, username, mail, bio, profile_pic
            FROM users
            WHERE username ILIKE %s OR mail ILIKE %s
            ORDER BY username ASC
            OFFSET %s LIMIT %s
        """
        pattern = f"%{term}%"
        rows = fetch_all(q, (pattern, pattern, offset, limit)) or []
        results = []
        for r in rows:
            results.append({
                "id": r.get("id"),
                "username": r.get("username"),
                "bio": r.get("bio"),
                "profile_pic": r.get("profile_pic"),
                "type": "user",
                "thumbnail": f"/profile/picture/{r.get('profile_pic')}" if r.get("profile_pic") else "/static/images/no pp.jpg"
            })
        return {"status": "OK", "response": results, "count": len(results)}
    except Exception as e:
        print(f"[ERROR][search_users] {e}")
        return {"status": "ERROR", "error_msg": str(e)}

# last line