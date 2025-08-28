# first line

from typing import List, Any, Dict, Optional
from db.handle_obj_low import (
    fetch_user_by_key, add_follow, remove_follow, get_followers, get_followed, redirect, update_user_profile
)
from objects.users.user import User, UserLevel
from datetime import datetime
import uuid
from services import obj_crud as media_handler

# =========================
# UTILITY PER USER OBJECT
# =========================
def _build_user(user_data: Dict[str, Any]) -> Optional[User]:
    if not user_data:
        return None
    bday_value = user_data.get("birthday")
    birthday = datetime.strptime(bday_value, "%Y-%m-%d").date() if isinstance(bday_value, str) else bday_value
    return User(
        id=user_data.get("id"),
        mail=user_data.get("mail"),
        username=user_data.get("username"),
        password_hash=user_data.get("password"),
        birthday=birthday,
        bio=user_data.get("bio"),
        profile_pic=user_data.get("foto_profilo"),
        lvl=UserLevel(user_data.get("lvl"))
    )

def _safe_get_username(user_id: int) -> Optional[str]:
    udata = fetch_user_by_key("id", user_id)
    return udata.get("username") if udata else None

# =========================
# MEDIA UTILS GENERICI
# =========================
MEDIA_FUNCTIONS = {
    "SONG": {
        "create": media_handler.create_song,
        "get": media_handler.get_song,
        "update": media_handler.update_song,
        "delete": media_handler.delete_song
    },
    "DOC": {
        "create": media_handler.create_document,
        "get": media_handler.get_document,
        "update": media_handler.update_document,
        "delete": media_handler.delete_document
    },
    "VIDEO": {
        "create": media_handler.create_video,
        "get": media_handler.get_video,
        "update": media_handler.update_video,
        "delete": media_handler.delete_video
    },
}

FIELDS_MAP = {
    "SONG": ["title","performer","year","duration","location","additional_info"],
    "DOC": ["title","author","year","format","pages","caption","song_id"],
    "VIDEO": ["title","director","year","duration","location","additional_info"]
}

def _update_media(user_obj: User, args: list, media_type: str):
    if len(args) < 2 or len(args) % 2 != 1:
        return "ERROR: Invalid args"

    media_id = args[0]
    updates = {args[i]: args[i+1] for i in range(1, len(args), 2)}

    # chiama la funzione di update vera
    func = MEDIA_FUNCTIONS.get(media_type, {}).get("update")
    if not func:
        return f"ERROR: Unknown media type {media_type}"

    result = func(media_id, updates)
    return "OK" if result else "ERROR: Failed to update"


def _delete_media(user_obj: User, args: list, media_type: str):
    func = MEDIA_FUNCTIONS.get(media_type, {}).get("delete")
    if not func:
        return f"ERROR: Unknown media type {media_type}"
    media_id = args[0]
    result = func(media_id)
    return "OK" if result else "ERROR: Failed to delete"

def create_media_generic(cmd: str, args: List[str]):
    # riusa handle_obj
    return media_handler.create_media_generic(cmd, args)

# =========================
# COMANDI
# =========================
UNAUTH_COMMANDS = {"LOGIN", "REGISTER", "RECOVER", "ASSISTANCE"}

USER_COMMANDS = {
    "USER_GET_PROFILE": "_get_profile",
    "USER_EDIT_PROFILE": "_edit_profile",
    "USER_FOLLOW": "_follow_user",
    "USER_UNFOLLOW": "_unfollow_user",
    "USER_GET_FOLLOWERS": "_get_followers",
    "USER_GET_FOLLOWED": "_get_followed",
}

# =========================
# DISPATCHER PRINCIPALE
# =========================
def dispatch_command(command: str, args: List[str], user_obj: Optional[User] = None,
                    conn=None, ip=None, config=None, sessions=None, mode_ref=None, approval_queue=None):
    cmd = command.upper()
    new_user_obj = None
    new_token = None

    # --- NON AUTENTICATI ---
    if cmd in UNAUTH_COMMANDS:
        if cmd == "LOGIN":
            blacklist = config.get("BLACKLIST =^^=", []) if config else []
            status = redirect([args[0], args[1]], blacklist, 1)
            if status["status"] == "accepted":
                new_token = str(uuid.uuid4())
                new_user_obj = _build_user(status["user"])
                return f"OK|{new_token}\n", new_user_obj, new_token
            elif status["status"] == "wrong_password":
                return "WRONG_PASSWORD\n", None, None
            elif status["status"] == "blacklisted":
                return "BLACKLISTED\n", None, None
            else:
                return "404\n", None, None

        elif cmd == "REGISTER":
            birthday = args[3] if args[3] else "2000-01-01"
            user_data = [
                args[1], args[2], args[0], "", args[3] or birthday, "About me:", "4"
            ]
            result = redirect(user_data, None, 2)
            resp = "ACCEPTED\n" if result is True else f"ERROR: invalid data {result}\n"
            return resp, None, None

        elif cmd == "RECOVER":
            return f"RECOVER_SENT|{args[0]}\n", None, None

        elif cmd == "ASSISTANCE":
            return "ASSISTANCE_REQUESTED\n", None, None

    # --- UTENTE LOGGATO ---
    if cmd in USER_COMMANDS or cmd.split("_")[0] in {"SONG","DOC","VIDEO"}:
        if not user_obj:
            return "ERROR: NOT_LOGGED_IN\n", None, None

        # --- USER HANDLERS ---
        if cmd == "USER_GET_PROFILE":
            target_name = args[0] if args else user_obj.username
            target_data = fetch_user_by_key("username", target_name)
            if not target_data:
                return "ERROR: User not found\n", None, None
            return _build_user(target_data).to_dict_public(), None, None

        elif cmd == "USER_EDIT_PROFILE":
            username, bio, profile_pic = args
            user_obj.edit_profile(username=username, bio=bio, profile_pic=profile_pic)
            ok = update_user_profile(user_obj.id, username=username, bio=bio, profile_pic=profile_pic)
            return ("PROFILE_UPDATED\n" if ok else "ERROR: Failed to update profile\n"), None, None

        elif cmd == "USER_FOLLOW":
            target_user = _build_user(fetch_user_by_key("username", args[0]))
            if not target_user:
                return "ERROR: User not found\n", None, None
            user_obj.follow(target_user)
            ok = add_follow(user_obj.id, target_user.id)
            return ("FOLLOWED\n" if ok else "ERROR: Failed to follow\n"), None, None

        elif cmd == "USER_UNFOLLOW":
            target_user = _build_user(fetch_user_by_key("username", args[0]))
            if not target_user:
                return "ERROR: User not found\n", None, None
            user_obj.unfollow(target_user)
            ok = remove_follow(user_obj.id, target_user.id)
            return ("UNFOLLOWED\n" if ok else "ERROR: Failed to unfollow\n"), None, None

        elif cmd == "USER_GET_FOLLOWERS":
            ids = get_followers(user_obj.id)
            names = [_safe_get_username(i) for i in ids if i]
            return f"{'|'.join(names)}\n", None, None

        elif cmd == "USER_GET_FOLLOWED":
            ids = get_followed(user_obj.id)
            names = [_safe_get_username(i) for i in ids if i]
            return f"{'|'.join(names)}\n", None, None

        # --- MEDIA CRUD HANDLERS ---
        try:
            if cmd.endswith("_CREATE"):
                result = create_media_generic(cmd, args)
                return (f"OK|{getattr(result,'id', result)}\n" if result else "ERROR: Failed to create\n"), None, None

            elif cmd.endswith("_UPDATE"):
                media_type = cmd.split("_")[0]
                result = _update_media(user_obj, args, media_type)
                return f"{result}\n", None, None

            elif cmd.endswith("_DELETE"):
                media_type = cmd.split("_")[0]
                result = _delete_media(user_obj, args, media_type)
                return f"{result}\n", None, None

            elif cmd.endswith("_GET"):
                media_type = cmd.split("_")[0]
                func = MEDIA_FUNCTIONS.get(media_type, {}).get("get")
                if not func:
                    return f"ERROR: Unknown media type {media_type}\n", None, None
                result = func(args[0])
                return (f"OK|{result}\n" if result else "ERROR: Not found\n"), None, None

            else:
                func = USER_COMMANDS.get(cmd)
                result = func(*args) if func else None
                return (f"OK|{result}\n" if result else "ERROR\n"), None, None

        except Exception as e:
            return f"ERROR: {str(e)}\n", None, None

    return "ERROR: Unknown command\n", None, None

# last line