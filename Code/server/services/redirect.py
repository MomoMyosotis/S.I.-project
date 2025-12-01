# first line

import json, base64, inspect
from typing import Optional, Any, Tuple
from server.services import user_services, media_services, interventions_services
from server.utils.storage_manager import (save_file,
                                    update_file,
                                    fetch_file,
                                    download_file,
                                    delete_file
                                    )
from server.objects.users.root import Root
# =====================
# ENCODER JSON
# =====================
def default_encoder(obj):
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

# =====================
# FILE MANAGER WRAPPERS
# =====================
def dispatch_save_file(user_obj, file_type, file_name, content: bytes):
    import base64, traceback
    try:
        if isinstance(content, str):
            try:
                content_bytes = base64.b64decode(content)
            except Exception:
                content_bytes = content.encode('utf-8')
        else:
            content_bytes = content

        save_file(file_type, file_name, content_bytes)
        return {"status": "OK", "response": f"{file_name} saved successfully"}
    except Exception as e:
        traceback.print_exc()
        return {"status": "ERROR", "error_msg": str(e)}

def dispatch_fetch_file(user_obj, file_type, file_name):
    import base64, traceback
    try:
        content = fetch_file(file_type, file_name)
        if content is None:
            return {"status": "ERROR", "error_msg": "File not found"}
        return {"status": "OK", "response": base64.b64encode(content).decode('utf-8')}
    except Exception as e:
        traceback.print_exc()
        return {"status": "ERROR", "error_msg": str(e)}

def dispatch_update_file(user_obj, file_type, file_name, content: bytes):
    import base64, traceback
    try:
        if isinstance(content, str):
            try:
                content_bytes = base64.b64decode(content)
            except Exception:
                content_bytes = content.encode('utf-8')
        else:
            content_bytes = content
        update_file(file_type, file_name, content_bytes)
        return {"status": "OK", "response": f"{file_name} updated successfully"}
    except Exception as e:
        traceback.print_exc()
        return {"status": "ERROR", "error_msg": str(e)}

def dispatch_download_file(user_obj, file_type, file_name, target_path: str):
    download_file(file_type, file_name, target_path)
    return f"{file_name} downloaded to {target_path}"

def dispatch_delete_file(user_obj, file_type, file_name):
    import traceback
    try:
        msg = delete_file(file_type, file_name)
        if "does not exist" in msg:
            return {"status": "ERROR", "error_msg": msg}
        return {"status": "OK", "response": msg}
    except Exception as e:
        traceback.print_exc()
        return {"status": "ERROR", "error_msg": str(e)}
# =====================
# DISPATCH COMMANDS
# =====================
COMMAND_MAP = {
    # USER
    "login": user_services.login_user,
    "register": user_services.register_user,
    "recover": user_services.recover,
    "assistance": user_services.assistance,
    "get_profile": user_services.get_profile,
    "edit_profile": user_services.edit_profile,
    "follow_user": user_services.follow_user,
    "unfollow_user": user_services.unfollow_user,
    "get_followers": user_services.get_followers,
    "get_followed": user_services.get_followed,
    "search_users": user_services.search_users,
    # =====================
    # MEDIA
    "create_song": media_services.create_song_services,
    "get_song": media_services.get_song_services,
    "get_media": media_services.get_media_services,            # <-- ADDED generic getter
    "update_song": media_services.update_song_services,
    "delete_song": media_services.delete_song_services,
    "create_document": media_services.create_document_services,
    "get_document": media_services.get_document_services,
    "update_document": media_services.update_document_services,
    "delete_document": media_services.delete_document_services,
    "create_video": media_services.create_video_services,
    "get_video": media_services.get_video_services,
    "update_video": media_services.update_video_services,
    "delete_video": media_services.delete_video_services,
    "get_feed": media_services.get_feed_services,
    "get_user_publications": media_services.get_user_publications_services,
    # INTERVENTIONS
    "create_comment" : interventions_services.create_comment,
    "fetch_comment" : interventions_services.get_comments,
    "update_comment" : interventions_services.update_comment,
    "delete_comment" : interventions_services.delete_comment,
    "create_note" : interventions_services.create_note,
    "fetch_note" : interventions_services.get_notes,
    "update_note" : interventions_services.update_note,
    "delete_note" : interventions_services.delete_note,
    # SEARCH/DIZIONARI
    "search_song": interventions_services.search_song,
    "search_document": interventions_services.search_document,
    "search_video": interventions_services.search_video,
    "add_entry": interventions_services.add_entry,
    "remove_entry": interventions_services.remove_entry,
    "get_entries": interventions_services.get_entries,
    # FILE MANAGER
    "save_file" : dispatch_save_file,
    "fetch_file" : dispatch_fetch_file,
    "update_file" : dispatch_update_file,
    "download_file" : dispatch_download_file,
    "delete_file" : dispatch_delete_file,
}

def dispatch_command(command: str, args: list, user_obj: Optional[Any]) -> Tuple[str, Optional[Any], Optional[str], str]:
    print(f"[DEBUG][dispatch_command] START - command={command}, args={args}, user_obj={user_obj}")
    command = command.lower()

    if isinstance(user_obj, dict):
        uid = user_obj.get("id")
        uname = user_obj.get("username")
        full = None
        if uid:
            full = Root.get_user(user_id=uid)
        elif uname:
            full = Root.get_user(username=uname)
        if full:
            user_obj = user_services._build_user_obj(full)

    if user_obj is None and command not in ["login", "register", "recover", "assistance"]:
        return json.dumps({"error_msg": "User is not logged in. Please log in to proceed.", "status": "error"}), None, None, "ERROR"

    func = COMMAND_MAP.get(command)
    if not func:
        return json.dumps({"error_msg": f"Unknown command {command}", "status": "error"}), None, None, "ERROR"

    try:
        # support functions that expect named params by accepting a single dict arg
        if command in ["login", "register", "recover", "assistance"]:
            result = func(*args)
        else:
            # if client passed a single dict, try to unpack it as kwargs
            if len(args) == 1 and isinstance(args[0], dict):
                try:
                    result = func(user_obj, **args[0])
                except TypeError:
                    # fallback to positional if kwargs don't match signature
                    result = func(user_obj, *args)
            else:
                result = func(user_obj, *args)

        new_token = None
        if command in ["login", "register"] and isinstance(result, dict):
            if "token" in result:
                new_token = result["token"]
                # result['user_obj'] is the public dict returned to client; 
                # rebuild the server-side Root from DB full row so we don't lose internal fields (lvl, etc.)
                public = result.get("user_obj")
                if isinstance(public, dict):
                    uid = public.get("id")
                    uname = public.get("username")
                    full = None
                    if uid:
                        full = Root.get_user(user_id=uid)
                    elif uname:
                        full = Root.get_user(username=uname)
                    user_obj = user_services._build_user_obj(full) if full else public

        serialized = json.dumps(result, default=default_encoder)

        status = result.get("status", "OK") if isinstance(result, dict) else "OK"

        return serialized, user_obj, new_token, status

    except Exception as e:
        import traceback
        traceback.print_exc()
        return json.dumps({"error_msg": str(e), "status": "error"}), None, None, "ERROR"


# last line