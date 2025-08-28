# first line
from typing import Type, Optional, Dict, Any
from objects.media.song import Song
from objects.media.document import Document
from objects.media.video import Video
from db import handle_obj_low as db_low

# =========================
# MAPPE DI SUPPORTO
# =========================
FIELDS_MAP = {
    "SONG": ["title","performer","year","duration","location","additional_info"],
    "DOC": ["title","author","year","format","pages","caption","song_id"],
    "VIDEO": ["title","director","year","duration","location","additional_info"]
}

# =========================
# BUILD OBJECT
# =========================
def build_object(cls: Type, data: Optional[Dict[str, Any]]):
    if not data:
        print(f"[DEBUG] build_object: no data for {cls.__name__}")
        return None
    return cls.from_dict(data)

# =========================
# GET OBJECT GENERIC
# =========================
def get_object(cls: Type, media_type: str, object_id: int):
    data = db_low.fetch_media(media_type, object_id)
    obj = build_object(cls, data)
    print(f"[DEBUG] get_object({cls.__name__}, id={object_id}) -> {obj}")
    return obj

# =========================
# UPDATE / DELETE GENERIC
# =========================
def update_object(media_type: str, object_id: int, updates: Dict[str, Any]) -> bool:
    result = db_low.update_media(media_type, object_id, updates)
    print(f"[DEBUG] update_object({media_type}, id={object_id}) -> {result}")
    return result

def delete_object(media_type: str, object_id: int) -> bool:
    result = db_low.delete_media(media_type, object_id)
    print(f"[DEBUG] delete_object({media_type}, id={object_id}) -> {result}")
    return result

# =========================
# CREATE SPECIFICI
# =========================
def create_song(data: Dict[str, Any]) -> Optional[Song]:
    media_id = db_low.create_media(data, "song")
    if not media_id:
        print("[DEBUG] create_song failed")
        return None
    print(f"[DEBUG] create_song success: media_id={media_id}")
    fetched_data = db_low.fetch_media("song", media_id)
    return Song.from_dict(fetched_data) if fetched_data else None

def create_document(data: Dict[str, Any]) -> Optional[Document]:
    media_id = db_low.create_media(data, "document")
    if not media_id:
        print("[DEBUG] create_document failed")
        return None
    print(f"[DEBUG] create_document success: media_id={media_id}")
    fetched_data = db_low.fetch_media("document", media_id)
    return Document.from_dict(fetched_data) if fetched_data else None

def create_video(data: Dict[str, Any]) -> Optional[Video]:
    media_id = db_low.create_media(data, "video")
    if not media_id:
        print("[DEBUG] create_video failed")
        return None
    print(f"[DEBUG] create_video success: media_id={media_id}")
    fetched_data = db_low.fetch_media("video", media_id)
    return Video.from_dict(fetched_data) if fetched_data else None

# =========================
# GET SPECIFICI
# =========================
def get_song(song_id: int) -> Optional[Song]:
    return get_object(Song, "song", song_id)

def get_document(doc_id: int) -> Optional[Document]:
    return get_object(Document, "document", doc_id)

def get_video(video_id: int) -> Optional[Video]:
    return get_object(Video, "video", video_id)

# =========================
# UPDATE SPECIFICI
# =========================
def update_song(song_id: int, updates: Dict[str, Any]) -> bool:
    return update_object("song", song_id, updates)

def update_document(doc_id: int, updates: Dict[str, Any]) -> bool:
    return update_object("document", doc_id, updates)

def update_video(video_id: int, updates: Dict[str, Any]) -> bool:
    return update_object("video", video_id, updates)

# =========================
# DELETE SPECIFICI
# =========================
def delete_song(song_id: int) -> bool:
    return delete_object("song", song_id)

def delete_document(doc_id: int) -> bool:
    return delete_object("document", doc_id)

def delete_video(video_id: int) -> bool:
    return delete_object("video", video_id)

# =========================
# CREAZIONE GENERICA da rimuover o al massimo da usare per note e commenti idk
# =========================
def create_media_generic(cmd: str, args: list[str]):
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
    obj = func(data)
    print(f"[DEBUG] create_media_generic({media_type}) -> {obj}")
    return obj

# last line
