# first line

from typing import List, Optional, Dict, Any
from datetime import datetime, date
import secrets
from server.objects.user import User, UserLevel
from server.db.db_crud import verify_password, db_get_followers, db_get_following, db_count_followers, db_count_following, db_count_user_publications
from server.utils import user_utils as utils

# =====================
# HELPER: Convert internal dict to public (remove sensitive fields for client)
# =====================
def _to_public_dict(internal_dict: Dict[str, Any]) -> Dict[str, Any]:
    """Remove internal fields (followed, followers lists) before sending to client."""
    if not isinstance(internal_dict, dict):
        return internal_dict
    public = internal_dict.copy()
    # Remove internal fields that client shouldn't see
    public.pop("followed", None)
    public.pop("followers", None)
    return public

# =====================
# COSTRUTTORE DI OGGETTI ROOT
# =====================
def _build_user_obj(user_data: Dict[str, Any]) -> Optional[User]:
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
                    #print(f"[DEBUG][_extract_level] couldn't parse level from key {k}: {val!r}")
                    break
        # final fallback
        return UserLevel.REGULAR

    bday_value = user_data.get("birthday")
    birthday = (
        datetime.strptime(bday_value, "%Y-%m-%d").date()
        if isinstance(bday_value, str) else bday_value
    )
    level = _extract_level(user_data)
    user = User(
        id=user_data.get("id"),
        mail=user_data.get("mail"),
        username=user_data.get("username"),
        password_hash=user_data.get("password_hash"),
        birthday=birthday,
        bio=user_data.get("bio"),
        profile_pic=user_data.get("profile_pic"),
        lvl=level
    )
    # Don't load follower/following lists - counts will be recalculated on demand
    # Initialize empty lists to avoid None checks
    user.followers = []
    user.followed = []
    return user

# =====================
# LOGIN / REGISTRAZIONE
# =====================
def is_logged(user_obj: Optional[Any]) -> bool:
    if not user_obj:
        return False
    # se user_obj è dict o oggetto User, verifica id esistente
    user_id = user_obj["id"] if isinstance(user_obj, dict) else getattr(user_obj, "id", None)
    return user_id is not None

def login_user(login_field: str, password: str, config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Authenticate user and return session token.
    Also checks if password is the default temporary password.
    """
    try:
        # recupera l'utente
        if "@" in login_field:
            user_data = User.get_user(mail=login_field)
        else:
            user_data = User.get_user(username=login_field)

        if not user_data:
            #print(f"[DEBUG][login_user] Login fallito: utente '{login_field}' non trovato")
            return {"status": "error", "user_obj": None, "error_msg": "User not found"}

        user_obj = _build_user_obj(user_data)
        user_dict = user_obj.to_dict_public()

        # verifica password
        if not verify_password(password, user_obj.password_hash):
            #print(f"[DEBUG][login_user] Password errata per utente '{login_field}'")
            return {"status": "wrong_password", "user_obj": None, "error_msg": "WRONG_PASSWORD"}

        # verifica livello: bannati (lvl 6) non possono accedere
        if user_obj.lvl == UserLevel.BANNED:
            #print(f"[DEBUG][login_user] Utente '{login_field}' bannato (lvl=6)")
            return {"status": "banned", "user_obj": None, "error_msg": "Your account has been banned"}

        # controllo blacklist
        if config and user_obj.mail in config.get("BLACKLIST", []):
            #print(f"[DEBUG][login_user] Utente '{login_field}' in blacklist")
            return {"status": "blacklisted", "user_obj": None, "error_msg": "BLACKLISTED"}

        # login OK
        token = secrets.token_hex(16)
        
        # Check if password is the temporary password
        from server.services.email_service import DEFAULT_RESET_PASSWORD
        must_change_password = password == DEFAULT_RESET_PASSWORD
        
        return {
            "status": "accepted",
            "user_obj": user_dict,
            "token": token,
            "error_msg": None,
            "must_change_password": must_change_password
        }

    except Exception as e:
        #print(f"[DEBUG][login_user] Errore generico: {e}")
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
        if User.get_user(username=username):
            return {"status": "ERROR", "error_msg": "Username already in use"}
        if User.get_user(mail=mail):
            return {"status": "ERROR", "error_msg": "Email already in use"}

        user_id = User.create_user(mail, username, password, birthday)
        if not user_id:
            return {"status": "ERROR", "error_msg": "Failed to create user"}

        user_data_list = User.get_user(user_id=user_id)
        if not user_data_list:
            return {"status": "ERROR", "error_msg": "Failed to fetch user after creation"}
        user_data = User.get_user(user_id=user_id)
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
def get_profile(user_obj: User, target_name: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """
    Get profile of a target user (or self if target_name is None).
    Returns unified profile_payload with all counts fresh from database.
    Response structure: {"user": profile_payload} or {"self": profile_payload + is_self flag}
    """
    if not is_logged(user_obj):
        return {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": None}

    # Safe extraction while migrating to full User everywhere
    viewer_id = user_obj["id"] if isinstance(user_obj, dict) else getattr(user_obj, "id", None)
    viewer_username = user_obj["username"] if isinstance(user_obj, dict) else getattr(user_obj, "username", None)
    
    # If no target specified, default to viewer's own profile using viewer_id
    if target_name:
        target_data = User.get_user_by_username(target_name)
    else:
        # Use viewer_id if no target_name provided
        target_data = User.get_user(user_id=viewer_id)
    
    if not target_data:
        return None
    
    target_obj = _build_user_obj(target_data)
    if not target_obj:
        return None
    
    # Build unified profile_payload with all counts fresh from database
    profile_payload = {
        "id": target_obj.id,
        "username": target_obj.username,
        "profile_pic": target_obj.profile_pic,
        "followers_count": db_count_followers(target_obj.id),
        "following_count": db_count_following(target_obj.id),
        "publications_count": db_count_user_publications(target_obj.id),
        "bio": target_obj.bio,
        "lvl": target_obj.lvl.value
    }
    
    # Determine if the viewer is following the target user
    # Only check if viewing someone else's profile (not self)
    is_self = viewer_id == target_obj.id
    is_followed = False
    
    if not is_self and viewer_id:
        try:
            # Get the viewer's following list and check if target is in it
            following_list = db_get_following(viewer_id)
            # following_list contains dicts with user info; check if target_obj.id matches any
            for followed_user in following_list:
                followed_id = followed_user.get("id") or followed_user.get("user_id") or followed_user.get("_id")
                if followed_id == target_obj.id:
                    is_followed = True
                    break
        except Exception as e:
            # On error, default to not following (safe fallback)
            #print(f"[DEBUG][get_profile] Error checking follow status: {e}")
            is_followed = False
    
    # Add follow flag to profile payload so frontend can display correct button
    profile_payload["is_followed"] = is_followed
    profile_payload["is_following"] = is_followed  # Both keys for compatibility
    
    # Return unified structure: always use "user" key, is_self goes in separate "self" metadata
    return {
        "status": "OK",
        "user": profile_payload,
        "self": {"is_self": is_self}
    }

def get_viewer_profile(user_obj: User) -> Optional[Dict[str, Any]]:
    """
    Alias for get_profile() with no target - returns the logged-in viewer's own profile.
    For backward compatibility with client code.
    """
    return get_profile(user_obj, target_name=None)

def edit_profile(user_obj: User, username=None, bio=None, profile_pic=None) -> str:
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

    # Resolve target user id: if username is provided, fetch the target user; otherwise use logged-in user
    from server.db.db_crud import get_user_id_by_username
    
    if username:
        # Editing a target user's profile (admin/root editing another user)
        target_id = get_user_id_by_username(username)
        if not target_id:
            return "ERROR: Target user not found"
        uid = target_id
    else:
        # Editing own profile
        uid = user_obj["id"] if isinstance(user_obj, dict) else getattr(user_obj, "id", None)
    
    success = User.update_user(uid, updates)
    if success:
        # Update in-memory object only if editing self (not when editing another user)
        if uid == (user_obj["id"] if isinstance(user_obj, dict) else getattr(user_obj, "id", None)):
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

def change_lvl(user_obj: User, *args) -> dict:
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
        target_row = User.get_user(user_id=target_identifier)
    else:
        target_row = User.get_user_by_username(str(target_identifier))

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
        ok = User.change_user_level(target_id, new_level)
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

def follow_user(user_obj: Any, target_name: str) -> dict:
    # updates both the followed and the follower's data
    if not is_logged(user_obj):
        return {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": None}
    
    # user_obj should already be a dict from redirect.py
    follower_id = user_obj["id"] if isinstance(user_obj, dict) else getattr(user_obj, "id", None)
    
    target = User.get_user_by_username(target_name)
    if not target:
        return {"status": "ERROR", "error_msg": "User not found"}

    result = User.follow_user(follower_id, target["id"], user_obj)
    
    if result["status"] == "OK":
        # Return full updated user data including new follow counts
        # Filter internal fields before sending to client
        public_user = _to_public_dict(user_obj)
        return {
            "status": "OK",
            "response": result["response"],
            "follower_followed_count": result.get("follower_followed_count"),
            "followee_followers_count": result.get("followee_followers_count"),
            "user_obj": public_user
        }
    else:
        return {"status": "ERROR", "error_msg": result.get("error_msg", "Follow failed")}

def unfollow_user(user_obj: Any, target_name: str) -> dict:
    if not is_logged(user_obj):
        return {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": None}
    
    # user_obj should already be a dict from redirect.py
    follower_id = user_obj["id"] if isinstance(user_obj, dict) else getattr(user_obj, "id", None)
    
    target = User.get_user_by_username(target_name)
    if not target:
        return {"status": "ERROR", "error_msg": "User not found"}
    result = User.unfollow_user(follower_id, target["id"], user_obj)
    
    if result["status"] == "OK":
        # Return full updated user data including new follow counts
        # Filter internal fields before sending to client
        public_user = _to_public_dict(user_obj)
        return {
            "status": "OK",
            "response": result["response"],
            "follower_followed_count": result.get("follower_followed_count"),
            "followee_followers_count": result.get("followee_followers_count"),
            "user_obj": public_user
        }
    else:
        return {"status": "ERROR", "error_msg": result.get("error_msg", "Unfollow failed")}

def get_followers(user_obj: Any, target_name: str) -> dict:
    """Get followers of a target user (or self if target_name is empty)."""
    if not is_logged(user_obj):
        return {"status": "ERROR", "error_msg": "NOT_LOGGED_IN"}
    
    # If no target specified, use the current user
    if not target_name:
        target_name = user_obj["username"] if isinstance(user_obj, dict) else getattr(user_obj, "username", None)
    
    # Fetch target user to get their id
    target_data = User.get_user_by_username(target_name)
    if not target_data:
        return {"status": "ERROR", "error_msg": "User not found"}
    
    target_id = target_data.get("id")
    followers = db_get_followers(target_id)
    
    # Extract usernames from follower objects
    follower_usernames = []
    for f in followers:
        if isinstance(f, dict) and "username" in f:
            follower_usernames.append(f["username"])
    
    return {"status": "OK", "response": follower_usernames}

def get_following(user_obj: Any, target_name: str) -> dict:
    """Get users that a target user is following (or self if target_name is empty)."""
    if not is_logged(user_obj):
        return {"status": "ERROR", "error_msg": "NOT_LOGGED_IN"}
    
    # If no target specified, use the current user
    if not target_name:
        target_name = user_obj["username"] if isinstance(user_obj, dict) else getattr(user_obj, "username", None)
    
    # Fetch target user to get their id
    target_data = User.get_user_by_username(target_name)
    if not target_data:
        return {"status": "ERROR", "error_msg": "User not found"}
    
    target_id = target_data.get("id")
    following = db_get_following(target_id)
    
    # Extract usernames from following objects
    following_usernames = []
    for f in following:
        if isinstance(f, dict) and "username" in f:
            following_usernames.append(f["username"])
    
    return {"status": "OK", "response": following_usernames}

def get_followers_old(user_obj: dict) -> list[dict]:
    if not is_logged(user_obj):
        return {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": None}
    return utils.get_followers(user_obj["id"])

def get_followed(user_obj: dict) -> list[dict]:
    if not is_logged(user_obj):
        return {"status": "error", "error_msg": "NOT_LOGGED_IN", "user_obj": None}
    return utils.get_followed(user_obj["id"])

# =====================
# RECUPERO / ASSISTENZA (Email Functionality)
# =====================
def recover(identifier: str) -> Dict[str, Any]:
    """
    Handle password recovery request.
    Sends a recovery email to the provided email address if user exists.
    Accepts either username or email as identifier.
    """
    try:
        from server.services.email_service import send_recovery_email
        
        # Determine if identifier is email or username
        if "@" in identifier:
            user_data = User.get_user(mail=identifier)
            email = identifier
        else:
            user_data = User.get_user(username=identifier)
            email = user_data.get("mail") if user_data else None
        
        if not user_data:
            # Don't leak whether user exists, return success anyway for security
            #print(f"[DEBUG][recover] User not found for identifier: {identifier}")
            return {
                "status": "OK",
                "error_msg": None,
                "message": "If an account exists with this identifier, a recovery link has been sent"
            }
        
        username = user_data.get("username", "User")
        
        # Send recovery email
        result = send_recovery_email(email, username)
        
        if result.get("status") == "OK":
            return {
                "status": "OK",
                "error_msg": None,
                "message": f"Recovery email sent to {email}"
            }
        else:
            #print(f"[ERROR][recover] Failed to send recovery email: {result.get('error_msg')}")
            return {
                "status": "ERROR",
                "error_msg": result.get("error_msg", "Failed to send recovery email")
            }
    
    except Exception as e:
        #print(f"[ERROR][recover] Exception: {str(e)}")
        return {
            "status": "ERROR",
            "error_msg": f"Recovery process failed: {str(e)}"
        }

def assistance(identifier: str, message: str) -> Dict[str, Any]:
    """
    Handle user assistance/support request.
    Sends a confirmation email to the user and notifies admin.
    Accepts either username or email as identifier.
    """
    try:
        from server.services.email_service import send_assistance_email
        from server.logic.config_loader import load_config
        
        # Determine if identifier is email or username
        if "@" in identifier:
            user_data = User.get_user(mail=identifier)
        else:
            user_data = User.get_user_by_username(identifier)
        
        if not user_data:
            #print(f"[DEBUG][assistance] User not found: {identifier}")
            return {
                "status": "ERROR",
                "error_msg": f"User '{identifier}' not found"
            }
        
        user_email = user_data.get("mail")
        username = user_data.get("username", "User")
        if not user_email:
            #print(f"[DEBUG][assistance] No email for user: {identifier}")
            return {
                "status": "ERROR",
                "error_msg": "User email not found"
            }
        
        # Load config to get admin email
        try:
            config = load_config()
            admin_email = config.get("ADMIN_EMAIL")
        except Exception as e:
            #print(f"[WARNING][assistance] Failed to load config for admin email: {str(e)}")
            admin_email = None
        
        # Send assistance emails
        result = send_assistance_email(user_email, username, message, admin_email)
        
        if result.get("status") == "OK":
            #print(f"[DEBUG][assistance] Assistance email sent to {user_email}")
            return {
                "status": "OK",
                "error_msg": None,
                "message": f"Assistance request received. Confirmation sent to {user_email}"
            }
        else:
            #print(f"[ERROR][assistance] Failed to send assistance email: {result.get('error_msg')}")
            return {
                "status": "ERROR",
                "error_msg": result.get("error_msg", "Failed to send assistance email")
            }
    
    except Exception as e:
        #print(f"[ERROR][assistance] Exception: {str(e)}")
        return {
            "status": "ERROR",
            "error_msg": f"Assistance process failed: {str(e)}"
        }

def reset_password(reset_token: str) -> Dict[str, Any]:
    """
    Handle password reset using a reset token.
    Validates the token and resets the password to a default password.
    """
    try:
        from server.services.email_service import consume_reset_token, DEFAULT_RESET_PASSWORD
        
        # Validate and consume the token
        email = consume_reset_token(reset_token)
        if not email:
            return {
                "status": "ERROR",
                "error_msg": "Invalid or expired reset token"
            }
        
        # Fetch user by email
        user_data = User.get_user(mail=email)
        if not user_data:
            #print(f"[DEBUG][reset_password] User not found for email: {email}")
            return {
                "status": "ERROR",
                "error_msg": "User not found"
            }
        
        user_id = user_data.get("id")
        
        # Update password to default
        from server.db.db_crud import hash_pswd, update_user_db
        new_password_hash = hash_pswd(DEFAULT_RESET_PASSWORD)
        
        success = update_user_db(user_id, {"password_hash": new_password_hash})
        
        if success:
            #print(f"[DEBUG][reset_password] Password reset successfully for {email}")
            return {
                "status": "OK",
                "error_msg": None,
                "message": f"Password reset successful. Your new password is: {DEFAULT_RESET_PASSWORD}",
                "new_password": DEFAULT_RESET_PASSWORD
            }
        else:
            #print(f"[ERROR][reset_password] Failed to update password for {email}")
            return {
                "status": "ERROR",
                "error_msg": "Failed to reset password"
            }
    
    except Exception as e:
        #print(f"[ERROR][reset_password] Exception: {str(e)}")
        return {
            "status": "ERROR",
            "error_msg": f"Password reset failed: {str(e)}"
        }

def change_password(user_obj: Any, new_password: str) -> Dict[str, Any]:
    """
    Change the password for an authenticated user.
    Used when user needs to change from temporary password.
    Bypasses permission checks as this is a required action.
    """
    try:
        # Extract user_id from either User object or dict
        user_id = None
        username = None
        
        if isinstance(user_obj, User):
            user_id = user_obj.id
            username = user_obj.username
        elif isinstance(user_obj, dict):
            user_id = user_obj.get("id")
            username = user_obj.get("username")
        
        if not user_id:
            return {
                "status": "ERROR",
                "error_msg": "User not authenticated"
            }
        
        # Validate password length
        if not new_password or len(new_password) < 6:
            return {
                "status": "ERROR",
                "error_msg": "Password must be at least 6 characters long"
            }
        
        # Hash the new password
        from server.db.db_crud import hash_pswd, update_user_db
        new_password_hash = hash_pswd(new_password)
        
        # Update password in database - directly update without permission checks
        success = update_user_db(user_id, {"password_hash": new_password_hash})
        
        if success:
            #print(f"[DEBUG][change_password] Password changed successfully for user {username} (id={user_id})")
            return {
                "status": "OK",
                "message": "Password changed successfully"
            }
        else:
            #print(f"[ERROR][change_password] Failed to update password for user {username} (id={user_id})")
            return {
                "status": "ERROR",
                "error_msg": "Failed to update password"
            }
    
    except Exception as e:
        #print(f"[ERROR][change_password] Exception: {str(e)}")
        import traceback
        traceback.print_exc()
        return {
            "status": "ERROR",
            "error_msg": f"Password change failed: {str(e)}"
        }

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
        #print(f"[ERROR][search_users] {e}")
        return {"status": "ERROR", "error_msg": str(e)}

# last line