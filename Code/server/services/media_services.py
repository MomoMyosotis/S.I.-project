# first line

from typing import Type, Optional, Dict, Any, List
from objects.media.song import Song
from objects.media.document import Document
from objects.media.video import Video
from objects.media.media import Media
#from db import db_crud as db_low

# =========================
# BUILD OBJECT GENERIC
# =========================
def build_object(cls: Type, data: Optional[Dict[str, Any]]):
    """Crea un oggetto della classe cls a partire da un dizionario."""
    return cls.from_dict(data) if data else None

def get_object(cls: Type, media_type: str, object_id: int):
    """Recupera un media generico dal DB e lo converte in oggetto."""
    data = Media.fetch_media(media_type.lower(), object_id)
    return build_object(cls, data)

def create_object(cls: Type, media_type: str, data: Dict[str, Any]):
    """Crea un nuovo media, lo recupera e restituisce l'oggetto corrispondente."""
    media_id = Media.create_media(data, media_type.lower())
    if not media_id:
        return None
    fetched_data = Media.fetch_media(media_type.lower(), media_id)
    return cls.from_dict(fetched_data) if fetched_data else None

def update_object(media_type: str, object_id: int, updates: Dict[str, Any]) -> bool:
    """Aggiorna un media generico."""
    return Media.update_media(media_type.lower(), object_id, updates)

def delete_object(media_type: str, object_id: int) -> bool:
    """Elimina un media generico."""
    return Media.delete_media(media_type.lower(), object_id)

# =========================
# SONG
# =========================
get_song = lambda song_id: get_object(Song, "song", song_id)
create_song = lambda data: create_object(Song, "song", data)
update_song = lambda song_id, updates: update_object("song", song_id, updates)
delete_song = lambda song_id: delete_object("song", song_id)

# =========================
# DOCUMENT
# =========================
get_document = lambda doc_id: get_object(Document, "document", doc_id)
create_document = lambda data: create_object(Document, "document", data)
update_document = lambda doc_id, updates: update_object("document", doc_id, updates)
delete_document = lambda doc_id: delete_object("document", doc_id)

# =========================
# VIDEO
# =========================
get_video = lambda video_id: get_object(Video, "video", video_id)
create_video = lambda data: create_object(Video, "video", data)
update_video = lambda video_id, updates: update_object("video", video_id, updates)
delete_video = lambda video_id: delete_object("video", video_id)

# =========================
# GENERIC CREATION (optional, CLI/debug)
# =========================
FIELDS_MAP = {
    "SONG": ["title","year","duration","location","additional_info"],
    "DOC": ["title","author","year","format","pages","caption","song_id"],
    "VIDEO": ["title","year","duration","location","additional_info","director"]
}

def create_media_generic(cmd: str, args: List[Any]):
    """Crea un media generico a partire da un comando tipo SONG_CREATE"""
    media_type = cmd.split("_")[0].upper()
    func_map = {
        "SONG": create_song,
        "DOC": create_document,
        "VIDEO": create_video
    }
    func = func_map.get(media_type)
    if not func:
        print(f"[DEBUG] create_media_generic: unknown media type {media_type}")
        return None
    keys = FIELDS_MAP.get(media_type, [])
    data = {k: args[i] if i < len(args) else None for i, k in enumerate(keys)}
    data["type"] = media_type.lower()
    return func(data)

# last line