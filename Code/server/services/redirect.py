# first line

from typing import Optional, Any, Tuple
from services import user_services, media_services, interventions_services

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
    "create_song": media_services.create_song,
    "get_song": media_services.get_song,
    "update_song": media_services.update_song,
    "delete_song": media_services.delete_song,
    "create_document": media_services.create_document,
    "get_document": media_services.get_document,
    "update_document": media_services.update_document,
    "delete_document": media_services.delete_document,
    "create_video": media_services.create_video,
    "get_video": media_services.get_video,
    "update_video": media_services.update_video,
    "delete_video": media_services.delete_video,
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

def dispatch_command(command: str, args: list, user_obj: Optional[Any]) -> Tuple[Any, Optional[Any], Optional[str]]:

    func = COMMAND_MAP.get(command)
    if not func:
        return {"error_msg": f"Unknown command {command}"}, None, None

    try:
        # LOGIN/REGISTER non richiedono user_obj già esistente
        if command in ["login_user", "register_user"]:
            result = func(args)  # login/register ricevono args come lista
        else:
            result = func(user_obj, *args)  # tutte le altre richiedono user_obj

        new_token = None
        # Gestione token per login/register
        if command in ["login_user", "register_user"] and isinstance(result, dict):
            if "token" in result:
                new_token = result["token"]
                user_obj = result.get("user_obj")
        return result, user_obj, new_token
    except Exception as e:
        return {"error_msg": str(e)}, None, None

# last line