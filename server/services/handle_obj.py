# first line
from typing import Optional, Dict, Any, List
import datetime
from objects.media.song import Song
from objects.media.document import Document
from objects.media.video import Video
from services.logger import log_event
from services import obj_crud

# =========================
# VALIDAZIONE INPUT
# =========================

def validate_media_input(data: Dict[str, Any]) -> Optional[str]:
    if not data.get("title"):
        log_event("SYSTEM", "SYSTEM", "VALIDATION", "ERROR: missing title")
        return "ERROR: missing title"

    year = data.get("year")
    if year is not None:
        try:
            data["year"] = int(year)
        except ValueError:
            log_event("SYSTEM", "SYSTEM", "VALIDATION", f"ERROR: invalid year '{year}'")
            return f"ERROR: invalid year '{year}'"

    duration = data.get("duration")
    if duration is not None:
        try:
            data["duration"] = int(duration)
        except ValueError:
            log_event("SYSTEM", "SYSTEM", "VALIDATION", f"ERROR: invalid duration '{duration}'")
            return f"ERROR: invalid duration '{duration}'"

    birthday = data.get("birthday")
    if birthday is not None:
        try:
            data["birthday"] = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
        except ValueError:
            log_event("SYSTEM", "SYSTEM", "VALIDATION", f"ERROR: invalid date '{birthday}'")
            return f"ERROR: invalid date '{birthday}'"
    return None

# =========================
# LOG EVENTI
# =========================

def log_action(ip: str, user: str, action: str, message: str):
    log_event(ip, user, action, message)

# =========================
# LIST MEDIA
# =========================

def list_media(media_type: str) -> List[Any]:
    media_type = media_type.lower()
    if media_type == "song":
        songs = obj_crud.get_all_songs()
        print(f"[DEBUG] list_media: {len(songs)} songs found")
        return songs
    elif media_type == "document":
        docs = obj_crud.get_all_documents()
        print(f"[DEBUG] list_media: {len(docs)} documents found")
        return docs
    elif media_type == "video":
        vids = obj_crud.get_all_videos()
        print(f"[DEBUG] list_media: {len(vids)} videos found")
        return vids
    else:
        print(f"[DEBUG] list_media: unknown media type {media_type}")
        raise ValueError(f"Tipo di media sconosciuto: {media_type}")

# =========================
# CREAZIONE MEDIA
# =========================

def create_media_from_input(media_type: str, data: Dict[str, Any]):
    err = validate_media_input(data)
    if err:
        print(f"[DEBUG] create_media_from_input validation failed: {err}")
        return None

    media_type = media_type.lower()
    if media_type == "song":
        obj = obj_crud.create_song(data)
    elif media_type == "document":
        obj = obj_crud.create_document(data)
    elif media_type == "video":
        obj = obj_crud.create_video(data)
    else:
        print(f"[DEBUG] create_media_from_input: unknown media type {media_type}")
        return None

    print(f"[DEBUG] create_media_from_input: created {obj}")
    return obj

# last line