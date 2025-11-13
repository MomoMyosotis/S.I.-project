# first line

import random
from typing import Type, Optional, Dict, Any, List
from server.objects.media.song import Song
from server.objects.media.document import Document
from server.objects.media.video import Video
from server.objects.media.media import Media
from server.utils.media_utils import fetch_dict_entry, create_dict_entry

# =========================
# GENERIC CREATION (optional, CLI/debug)
# =========================
FIELDS_MAP = {
    "SONG": ["title", "year", "duration", "location", "additional_info", "authors", "performers", "genres", "references", "is_author", "is_performer"],
    "DOC": ["title", "stored_at", "pages", "format", "references", "authors"],
    "VIDEO": ["title", "year", "duration", "location", "additional_info", "director", "authors", "performers", "genres", "references", "is_author", "is_performer"]
}

# =========================
# GENERIC OBJECT HELPERS
# =========================
def build_object(cls: Type[Media], data: Optional[Dict[str, Any]]):
    print(f"[DEBUG][build_object] cls={cls.__name__}, data={data}")
    if not data:
        print("[DEBUG][build_object] data is None/empty -> returning None")
        return None
    obj = cls.from_dict(data)
    print(f"[DEBUG][build_object] Built object={obj}")
    return obj

def get_object(cls: Type[Media], object_id: int):
    print(f"[DEBUG][get_object] cls={cls.__name__}, object_id={object_id}")
    if cls is Song:
        obj = Song.fetch_full_song(object_id)
    elif cls is Video:
        obj = Video.fetch_full_video(object_id)
    elif cls is Document:
        obj = Document.fetch_full_document(object_id)
    else:
        obj = cls.fetch(object_id)
    print(f"[DEBUG][get_object] Retrieved object={obj}")
    return obj

def create_object(cls: Type[Media], user_obj: Dict[str, Any], data: Dict[str, Any]):
    print(f"[DEBUG][create_object] cls={cls.__name__}, user_obj={user_obj}, data={data}")
    obj = cls.from_dict(data)
    print(f"[DEBUG][create_object] Object built from dict: {obj}")
    if not obj:
        print("[DEBUG][create_object] Object is None -> returning None")
        return None

    # Associa il media all’utente che lo ha creato
    if user_obj and "id" in user_obj:
        obj.user_id = user_obj["id"]
        print(f"[DEBUG][create_object] Set obj.user_id={obj.user_id}")

    print(f"[DEBUG][create_object] Saving object {obj}")
    obj.save()  # Salva media + relazioni M:N
    print(f"[DEBUG][create_object] Object saved: {obj}")
    return obj

def update_object(obj: Media, updates: Dict[str, Any]):
    print(f"[DEBUG][update_object] obj={obj}, updates={updates}")
    for k, v in updates.items():
        print(f"[DEBUG][update_object] Setting {k}={v}")
        setattr(obj, k, v)
    print(f"[DEBUG][update_object] Saving updated object {obj}")
    obj.save()
    print(f"[DEBUG][update_object] Object after save {obj}")
    return obj

def delete_object(obj: Media):
    print(f"[DEBUG][delete_object] Deleting object {obj}")
    obj.delete()
    print(f"[DEBUG][delete_object] Deleted object {obj}")
    return {"success": True}

# =========================
# SONG SERVICES
# =========================
def get_song_services(user_obj, song_id: int):
    print(f"[DEBUG][get_song_services] song_id={song_id}")
    return get_object(Song, song_id)

def create_song_services(user_obj: dict, data: dict):
    print(f"[DEBUG][create_song_services] user_obj={user_obj}, data={data}")

    data["type"] = "song"
    if user_obj:
        data["user_id"] = user_obj.get("id")
    if data.get("stored_at") is None:
        data["stored_at"] = "server/storage/songs"
    if "performers" in data:
        data["performers"] = prepare_performers(data["performers"])

    # Costruisci oggetto (non salva ancora relazioni M:N)
    song = Song.from_dict(data)

    # Associa l'utente creatore
    if user_obj and "id" in user_obj:
        song.user_id = user_obj["id"]

    # Salva nel DB
    song.save()
    return song

def update_song_services(user_obj, song_id: int, updates: dict):
    print(f"[DEBUG][update_song_services] song_id={song_id}, updates={updates}")
    song = get_object(Song, song_id)
    if not song:
        print("[DEBUG][update_song_services] Song not found")
        return {"error": "Song not found"}
    return update_object(song, updates)

def delete_song_services(user_obj, song_id: int):
    print(f"[DEBUG][delete_song_services] song_id={song_id}")
    song = get_object(Song, song_id)
    if not song:
        print("[DEBUG][delete_song_services] Song not found")
        return {"error": "Song not found"}
    return delete_object(song)

# =========================
# DOCUMENT SERVICES
# =========================
def create_document_services(user_obj, data: dict):
    data["type"] = "document"
    if data.get("stored_at") is None:
        data["stored_at"] = "server/storage/documents"

    return create_object(Document, user_obj, data)

def get_document_services(user_obj, doc_id: int):
    return get_object(Document, doc_id)

def update_document_services(user_obj, doc_id: int, updates: dict):
    doc_obj = get_object(Document, doc_id)
    if not doc_obj:
        return {"error": "Document not found"}
    return update_object(doc_obj, updates)

def delete_document_services(user_obj, doc_id: int):
    doc_obj = get_object(Document, doc_id)
    if not doc_obj:
        return {"error": "Document not found"}
    return delete_object(doc_obj)

# =========================
# VIDEO SERVICES
# =========================
def create_video_services(user_obj, data: dict):
    data["type"] = "video"
    if data.get("stored_at") is None:
        data["stored_at"] = "server/storage/videos"
    return create_object(Video, user_obj, data)

def get_video_services(user_obj, video_id: int):
    return get_object(Video, video_id)

def update_video_services(user_obj, video_id: int, updates: dict):
    video = get_object(Video, video_id)
    if not video:
        return {"error": "Video not found"}
    return update_object(video, updates)

def delete_video_services(user_obj, video_id: int):
    video = get_object(Video, video_id)
    if not video:
        return {"error": "Video not found"}
    return delete_object(video)

# ========================
# SUPPORT
# =========================

def prepare_performers(performers: list) -> list:
    """
    Controlla e crea performer esterni e assicura che gli utenti siano performer.
    Restituisce la lista di performer pronta da associare al media.
    """
    result = []
    for p in performers:
        if p["type"] == "user":
            # L'utente esiste già, mantieni solo id
            result.append({"type": "user", "id": p["id"]})
        elif p["type"] == "external":
            # Controlla se esiste nel dict performers
            existing = fetch_dict_entry("performers", p["name"])
            if existing:
                pid = existing["id"]
            else:
                pid = create_dict_entry("performers", p["name"])
            result.append({"type": "external", "id": pid, "name": p["name"]})
        else:
            raise ValueError(f"Tipo performer non valido: {p['type']}")
    return result

def get_feed_services(user_obj, search: str = "", filter_by: str = "all", offset: int = 0, limit: int = 10):
    print(f"[DEBUG] feed request received offset={offset}, limit={limit}, search='{search}', filter_by='{filter_by}'")

    # Funzione helper per fetchare e filtrare direttamente nel DB
    def fetch_media(cls):
        return cls.fetch_all(search=search, filter_by=filter_by, offset=offset, limit=limit)

    # Prendi media separatamente dal DB
    songs = fetch_media(Song)
    videos = fetch_media(Video)
    documents = fetch_media(Document)

    # Combina risultati
    all_media = songs + videos + documents

    from server.db.db_crud import get_user_username_by_id as duck

    results = []
    for m in all_media:
        d = m.to_dict()
        user_id = d.get("user_id")
        username = duck(user_id)
        results.append({
            "id": d.get("id"),
            "title": d.get("title"),
            "username": username or "Unknown",
            "thumbnail": d.get("thumbnail", "https://via.placeholder.com/100"),
            "tags": d.get("genres") or d.get("keywords") or [],
            "type": d.get("type"),
        })

    return {"status": "OK", "results": results, "count": len(results)}

# last line