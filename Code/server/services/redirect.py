# first line

from server.services import user_services, media_services, interventions_services
from server.utils.storage_manager import (save_file,
                                    update_file,
                                    fetch_file,
                                    download_file,
                                    delete_file)
from server.objects.user import User
from server.services.interventions_services import get_commented_medias
from typing import Optional, Any, Tuple
import json

# =====================
# ENCODER JSON
# =====================
def default_encoder(obj):
    from datetime import datetime, date
    from decimal import Decimal
    
    # Handle datetime objects
    if isinstance(obj, datetime):
        return obj.isoformat()
    # Handle date objects
    if isinstance(obj, date):
        return obj.isoformat()
    # Handle Decimal objects
    if isinstance(obj, Decimal):
        return float(obj)
    # Handle objects with to_dict method
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

# =====================
# METADATA FETCHERS
# =====================
def get_metadata_for_client():
    """
    Fetch all metadata from database: instruments, genres, media titles, authors.
    Returns a dict suitable for client-side autocomplete/suggestions.
    """
    from server.db.db_crud import fetch_all_dict_entries, fetch_all
    
    metadata = {}
    
    # Fetch instruments
    try:
        instruments = fetch_all_dict_entries("instruments")
        metadata["instruments"] = [inst.get("name") for inst in (instruments or []) if inst.get("name")]
    except Exception as e:
        #print(f"[ERROR] Failed to fetch instruments: {e}")
        metadata["instruments"] = []
    
    # Fetch genres/tags
    try:
        genres = fetch_all_dict_entries("genres")
        metadata["genres"] = [g.get("name") for g in (genres or []) if g.get("name")]
        # full objects for id->name resolution on clients that need it
        metadata["genre_objects"] = genres or []
    except Exception as e:
        #print(f"[ERROR] Failed to fetch genres: {e}")
        metadata["genres"] = []
        metadata["genre_objects"] = []
    
    # Fetch authors
    try:
        authors = fetch_all_dict_entries("authors")
        metadata["authors"] = [a.get("name") for a in (authors or []) if a.get("name")]
    except Exception as e:
        #print(f"[ERROR] Failed to fetch authors: {e}")
        metadata["authors"] = []
    
    # Fetch performers
    try:
        performers = fetch_all_dict_entries("performers")
        metadata["performers"] = [p.get("name") for p in (performers or []) if p.get("name")]
    except Exception as e:
        #print(f"[ERROR] Failed to fetch performers: {e}")
        metadata["performers"] = []
    
    # Fetch media titles (recent/popular)
    try:
        # Use GROUP BY + MAX(created_at) so PostgreSQL can ORDER correctly when selecting distinct titles
        media_titles = fetch_all("SELECT title, MAX(created_at) as latest FROM media WHERE title IS NOT NULL GROUP BY title ORDER BY latest DESC LIMIT 100")
        metadata["media_titles"] = [m.get("title") for m in (media_titles or []) if m.get("title")]
    except Exception as e:
        #print(f"[ERROR] Failed to fetch media titles: {e}")
        metadata["media_titles"] = []
    
    return metadata

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
    "reset_password": user_services.reset_password,
    "assistance": user_services.assistance,
    "change_password": user_services.change_password,
    "get_profile": user_services.get_profile,
    "get_viewer_profile": user_services.get_viewer_profile,
    "edit_profile": user_services.edit_profile,
    "follow_user": user_services.follow_user,
    "unfollow_user": user_services.unfollow_user,
    "get_followers": user_services.get_followers,
    "get_following": user_services.get_following,
    "get_followed": user_services.get_followed,
    "search_users": user_services.search_users,
    "change_lvl": user_services.change_lvl,
    # =====================
    # MEDIA
    # =====================
    "create_song": media_services.create_song_services,
    "get_song": media_services.get_song_services,
    "get_media": media_services.get_media_services,
    "update_media": media_services.update_media_services,
    "update_song": media_services.update_song_services,
    "delete_song": media_services.delete_song_services,
    "create_document": media_services.create_document_services,
    "get_document": media_services.get_document_services,
    "fix_document_metadata": media_services.fix_document_metadata_services,
    "update_document": media_services.update_document_services,
    "delete_document": media_services.delete_document_services,
    "create_video": media_services.create_video_services,
    "get_video": media_services.get_video_services,
    "update_video": media_services.update_video_services,
    "delete_video": media_services.delete_video_services,
    "get_feed": media_services.get_feed_services,
    "composed_query": media_services.composed_query_services,
    "get_user_publications": media_services.get_user_publications_services,
    "create_concert": media_services.create_concert_services,
    "get_concert": media_services.get_concert_services,
    "add_concert_segment": media_services.add_concert_segment_services,
    "get_concert_segments": media_services.get_concert_segments_services,
    "update_concert_segment": media_services.update_concert_segment_services,
    "delete_concert_segment": media_services.delete_concert_segment_services,
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
    "get_commented_medias": interventions_services.get_commented_medias,
    "get_commented_media": interventions_services.get_commented_media_paginated,
    "get_followed_media": interventions_services.get_followed_media_paginated,
    # METADATA (for client-side autocomplete/suggestions)
    "get_metadata": lambda user_obj, *args: get_metadata_for_client(),
    # FILE MANAGER
    "save_file" : dispatch_save_file,
    "fetch_file" : dispatch_fetch_file,
    "update_file" : dispatch_update_file,
    "download_file" : dispatch_download_file,
    "delete_file" : dispatch_delete_file,
}

def dispatch_command(command: str, args: list, user_obj: Optional[Any]) -> Tuple[str, Optional[Any], Optional[str], str]:
    #print(f"[DEBUG][dispatch_command] START - command={command}, args={args}, user_obj={user_obj}")
    command = command.lower()

    # If user_obj is missing, attempt to resolve it from the incoming HTTP request.
    # Token precedence: Authorization Bearer header -> session cookie -> JSON body token.
    # This lets server handlers determine the request actor even when client sent
    # the token in a header/cookie rather than in the JSON payload.
    if user_obj is None:
        try:
            from flask import request
            token_candidate = None

            # Authorization header (Bearer)
            auth = request.headers.get("Authorization") or request.headers.get("authorization")
            if auth:
                parts = auth.split()
                if len(parts) == 2 and parts[0].lower() == "bearer":
                    token_candidate = parts[1].strip()
                else:
                    token_candidate = auth.strip()

            # Cookie fallback
            if not token_candidate:
                token_candidate = request.cookies.get("session_token") or request.cookies.get("token")

            # JSON body fallback (safe/silent)
            if not token_candidate:
                try:
                    body = request.get_json(silent=True) or {}
                    token_candidate = body.get("token") or token_candidate
                except Exception:
                    pass

            if token_candidate:
                try:
                    # import sessions lazily to avoid circular imports at module import time
                    from server.logic.api_server import sessions
                    cand = sessions.get(token_candidate)
                    if cand:
                        user_obj = cand
                        print(f"[DEBUG][dispatch_command] Resolved user_obj from request token")
                except Exception:
                    pass
        except Exception:
            pass

    # =====================
    # EXTRACT USER_ID FROM ARGS IF user_obj IS None
    # =====================
    # If user_obj is None but first arg is a user_id (int), extract it and build user_obj
    if user_obj is None and args and len(args) > 0:
        first_arg = args[0]
        if isinstance(first_arg, int):
            # Try to fetch user and build user_obj
            try:
                full = User.get_user(user_id=first_arg)
                if full:
                    user_obj_instance = user_services._build_user_obj(full)
                    user_obj = user_obj_instance.to_dict_internal() if user_obj_instance else None
                    # Remove the user_id from args since it's now in user_obj
                    args = args[1:]
                    #print(f"[DEBUG][dispatch_command] Built user_obj from user_id={first_arg}, remaining args={args}")
            except Exception as e:
                print(f"[DEBUG][dispatch_command] Failed to build user_obj from user_id: {e}")

    print(f"[DEBUG][dispatch_command] After user_id extraction - user_obj={'(set)' if user_obj else 'None'}, args={args}")

    if isinstance(user_obj, dict):
        uid = user_obj.get("id")
        uname = user_obj.get("username")
        full = None
        if uid:
            full = User.get_user(user_id=uid)
        elif uname:
            full = User.get_user(username=uname)
        if full:
            # Build User object to load follow lists from DB, use internal dict with follow lists for server-side tracking
            user_obj_instance = user_services._build_user_obj(full)
            user_obj = user_obj_instance.to_dict_internal() if user_obj_instance else user_obj

    # allow some public commands without authentication (feed browsing, user search, media viewing, etc.)
    if user_obj is None and command not in ["login", "register", "recover", "reset_password", "assistance", "change_password", "get_feed", "search_users", "get_metadata", "get_media", "get_document", "fix_document_metadata", "composed_query"]:
        return json.dumps({"error_msg": "User is not logged in. Please log in to proceed.", "status": "error"}), None, None, "ERROR"

    func = COMMAND_MAP.get(command)
    if not func:
        return json.dumps({"error_msg": f"Unknown command {command}", "status": "error"}), None, None, "ERROR"

    try:
        # support functions that expect named params by accepting a single dict arg
        if command in ["login", "register", "recover", "reset_password", "assistance"]:
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
                        full = User.get_user(user_id=uid)
                    elif uname:
                        full = User.get_user(username=uname)
                    user_obj_instance = user_services._build_user_obj(full) if full else None
                    user_obj = user_obj_instance.to_dict_internal() if user_obj_instance else public

        serialized = json.dumps(result, default=default_encoder)

        status = result.get("status", "OK") if isinstance(result, dict) else "OK"

        return serialized, user_obj, new_token, status

    except Exception as e:
        import traceback
        traceback.print_exc()
        return json.dumps({"error_msg": str(e), "status": "error"}), None, None, "ERROR"

# last line