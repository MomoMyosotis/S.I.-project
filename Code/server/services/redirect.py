# first line

import json
from typing import Optional, Any, Tuple
from services import user_services, media_services, interventions_services

# =====================
# ENCODER JSON
# =====================
def default_encoder(obj):
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

# =====================
# DISPATCH COMMANDS
# =====================
COMMAND_MAP = {
    # USER
    "login_user": user_services.login_user,
    "register_user": user_services.register_user,
    "recover": user_services.recover,
    "assistance": user_services.assistance,
    "get_profile": user_services.get_profile,
    "edit_profile": user_services.edit_profile,
    "follow_user": user_services.follow_user,
    "unfollow_user": user_services.unfollow_user,
    "get_followers": user_services.get_followers,
    "get_followed": user_services.get_followed,
    # MEDIA
    "create_song": media_services.create_song_services,
    "get_song": media_services.get_song_services,
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
    # INTERVENTIONS
    "create_comment" : interventions_services.create_comment,
    "fetch_comment" : interventions_services.get_comments,
    "update_comment" : interventions_services.update_comment,
    "delete_comment" : interventions_services.delete_comment,
    "create_note" : interventions_services.create_note,
    "fetch_note" : interventions_services.get_note,
    "update_note" : interventions_services.update_note,
    "delete_note" : interventions_services.delete_note,
    # SEARCH/DIZIONARI
    "search_song": interventions_services.search_song,
    "search_document": interventions_services.search_document,
    "search_video": interventions_services.search_video,
    "add_entry": interventions_services.add_entry,
    "remove_entry": interventions_services.remove_entry,
    "get_entries": interventions_services.get_entries,
}

def dispatch_command(command: str, args: list, user_obj: Optional[Any]) -> Tuple[str, Optional[Any], Optional[str], str]:

    print(f"[DEBUG][dispatch_command] START - command={command}, args={args}, user_obj={user_obj}")

    # Verifica se l'utente è loggato, tranne per i comandi speciali (login, register, recover, assistance)
    if user_obj is None and command not in ["login_user", "register_user", "recover", "assistance"]:
        print(f"[DEBUG][dispatch_command] ERROR - User is not logged in, access denied for command {command}")
        return json.dumps({"error_msg": "User is not logged in. Please log in to proceed."}), None, None, "ERROR"

    func = COMMAND_MAP.get(command)
    if not func:
        print(f"[DEBUG][dispatch_command] ERROR - Unknown command {command}")
        return json.dumps({"error_msg": f"Unknown command {command}"}), None, None, "ERROR"

    try:
        # LOGIN/REGISTER rimangono speciali
        if command in ["login_user", "register_user"]:
            result = func(args)
        else:
            result = func(user_obj, *args)

        new_token = None
        if command in ["login_user", "register_user"] and isinstance(result, dict):
            if "token" in result:
                new_token = result["token"]
                user_obj = result.get("user_obj")

        serialized = json.dumps(result, default=default_encoder)
        return serialized, user_obj, new_token, "OK"

    except Exception as e:
        import traceback
        traceback.print_exc()
        return json.dumps({"error_msg": str(e)}), None, None, "ERROR"

# last line