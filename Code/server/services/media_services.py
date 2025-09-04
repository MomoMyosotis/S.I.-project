# first line

from typing import Type, Optional, Dict, Any, List
from objects.media.song import Song
from objects.media.document import Document
from objects.media.video import Video
from objects.media.media import Media

# =========================
# GENERIC CREATION (optional, CLI/debug)
# =========================
FIELDS_MAP = {
    "SONG": ["title", "year", "duration", "location", "additional_info"],
    "DOC": ["title", "author", "year", "format", "pages", "caption", "song_id"],
    "VIDEO": ["title", "year", "duration", "location", "additional_info", "director"]
}

# =========================
# BUILD OBJECT GENERIC
# =========================
def build_object(cls: Type[Media], data: Optional[Dict[str, Any]]):
    print(f"[DEBUG] build_object | cls={cls.__name__} data={data}")
    return cls.build_object(data) if data else None  # usa il build_object della classe Media

def get_object(cls: Type[Media], child_table: str, object_id: int, child_fields: List[str] = None):
    data = cls.fetch_media(object_id, child_table, child_fields)
    if not data:
        return None
    return cls.build_object(data)

def create_object(cls: Type, media_type: str, data: Dict[str, Any]):
    print(f"[DEBUG] create_object | cls={cls.__name__} media_type={media_type} data={data}")
    media_id = Media.create_media(data, media_type.lower())
    print(f"[DEBUG] create_object created media_id={media_id}")
    if not media_id:
        return None
    fetched_data = Media.fetch_media(media_id, media_type.lower())
    print(f"[DEBUG] create_object fetched_data={fetched_data}")
    return cls.from_dict(fetched_data) if fetched_data else None

def update_object(media_type: str, object_id: int, updates: Dict[str, Any]) -> Dict[str, Any]:
    print(f"[DEBUG] update_object | media_type={media_type} object_id={object_id} updates={updates}")
    success = Media.update_media( object_id, updates, media_type.lower())
    return {"success": True} if success else {"error": "update failed"}

def delete_object(media_type: str, object_id: int) -> Dict[str, Any]:
    print(f"[DEBUG] delete_object | media_type={media_type} object_id={object_id}")
    deleted = Media.delete_media(object_id)
    return {"success": True} if deleted else {"error": "delete failed"}

# =========================
# SONG
# =========================
def get_song_services(user_id: int, song_id: int):
    child_fields = ["duration", "location", "additional_info"]
    song = get_object(Song, "songs", song_id, child_fields=child_fields)
    return song.to_dict() if song else None

def create_song_services(user_obj: dict, data: dict) -> Optional[int]:
    print(f"[DEBUG] create_song_services | user_id={user_obj['id']} data={data}")

    child_table = "songs"
    child_columns = ("duration", "location", "additional_info")
    child_values = (
        data.get("duration"),
        data.get("location"),
        data.get("additional_info"),
    )

    song_id = Song.create_media(
        media_data=data,
        child_table=child_table,
        child_columns=child_columns,
        child_values=child_values
    )
    print(f"[DEBUG] create_song_services created song_id={song_id}")
    return song_id

def update_song_services(user_id: int, song_id: int, updates: dict):
    # Se l'update riguarda title, year, description → tabella media
    media_updates = {k: v for k, v in updates.items() if k in ["title", "year", "description", "link"]}
    child_updates = {k: v for k, v in updates.items() if k not in media_updates}

    result = {}
    if media_updates:
        result.update(update_object("media", song_id, media_updates))
    if child_updates:
        result.update(update_object("songs", song_id, child_updates))
    return result

def delete_song_services(user_id: int, song_id: int):
    print(f"[DEBUG] delete_song_services | user_id={user_id} song_id={song_id}")
    try:
        return delete_object("songs", song_id)
    except Exception as e:
        print(f"[DEBUG] delete_song_services exception: {e}")
        return {"error": f"delete_song_services failed: {e}"}

# =========================
# DOCUMENT
# =========================
def get_document_services(user_id: int, doc_id: int):
    print(f"[DEBUG] get_document_services | user_id={user_id} doc_id={doc_id}")
    try:
        doc_obj = get_object(Document, "documents", doc_id)
        return doc_obj.to_dict() if doc_obj else None
    except Exception as e:
        print(f"[DEBUG] get_document_services exception: {e}")
        return {"error": f"get_document_services failed: {e}"}

def create_document_services(user_obj: dict, data: dict) -> Optional[int]:
    print(f"[DEBUG] create_document_services | data={data}")
    child_table = "documents"
    child_columns = ("format", "pages", "caption", "song_id")
    child_values = (
        data.get("format"),
        data.get("pages"),
        data.get("caption"),
        data.get("song_id"),
    )
    doc_id = Document.create_media(
        media_data=data,
        child_table=child_table,
        child_columns=child_columns,
        child_values=child_values
    )
    print(f"[DEBUG] create_document_services created doc_id={doc_id}")
    return doc_id

def update_document_services(user_id: int, doc_id: int, updates: dict):
    print(f"[DEBUG] update_document_services | user_id={user_id} doc_id={doc_id} updates={updates}")
    try:
        return update_object("documents", doc_id, updates)
    except Exception as e:
        print(f"[DEBUG] update_document_services exception: {e}")
        return {"error": f"update_document_services failed: {e}"}

def delete_document_services(user_id: int, doc_id: int):
    print(f"[DEBUG] delete_document_services | user_id={user_id} doc_id={doc_id}")
    try:
        return delete_object("documents", doc_id)
    except Exception as e:
        print(f"[DEBUG] delete_document_services exception: {e}")
        return {"error": f"delete_document_services failed: {e}"}

# =========================
# VIDEO
# =========================
def get_video_services(user_id: int, video_id: int):
    child_fields = ["duration", "location", "additional_info", "director"]
    video = get_object(Video, "videos", video_id, child_fields=child_fields)
    return video.to_dict() if video else None

def create_video_services(user_obj: dict, data: dict) -> Optional[int]:
    print(f"[DEBUG] create_video_services | user_id={user_obj['id']} data={data}")

    child_table = "videos"
    child_columns = ("duration", "location", "additional_info", "director")
    child_values = (
        data.get("duration"),
        data.get("location"),
        data.get("additional_info"),
        data.get("director"),
    )

    video_id = Video.create_media(
        media_data=data,
        child_table=child_table,
        child_columns=child_columns,
        child_values=child_values
    )
    print(f"[DEBUG] create_video_services created video_id={video_id}")
    return video_id

def update_video_services(user_id: int, video_id: int, updates: dict):
    # Se l'update riguarda title, year, description, link → tabella media
    media_updates = {k: v for k, v in updates.items() if k in ["title", "year", "description", "link"]}
    child_updates = {k: v for k, v in updates.items() if k not in media_updates}

    result = {}
    if media_updates:
        result.update(update_object("media", video_id, media_updates))
    if child_updates:
        result.update(update_object("videos", video_id, child_updates))
    return result

def delete_video_services(user_id: int, video_id: int):
    print(f"[DEBUG] delete_video_services | user_id={user_id} video_id={video_id}")
    try:
        return delete_object("videos", video_id)
    except Exception as e:
        print(f"[DEBUG] delete_video_services exception: {e}")
        return {"error": f"delete_video_services failed: {e}"}

# =========================
# GENERIC CREATION (optional, CLI/debug)
# =========================
def create_media_generic(cmd: str, args: List[Any]):
    """Crea un media generico a partire da un comando tipo SONG_CREATE"""
    media_type = cmd.split("_")[0].upper()
    print(f"[DEBUG] create_media_generic | cmd={cmd} args={args} media_type={media_type}")
    func_map = {
        "SONG": create_song_services,
        "DOC": create_document_services,
        "VIDEO": create_video_services
    }
    func = func_map.get(media_type)
    if not func:
        print(f"[DEBUG] create_media_generic: unknown media type {media_type}")
        return None
    keys = FIELDS_MAP.get(media_type, [])
    data = {k: args[i] if i < len(args) else None for i, k in enumerate(keys)}
    data["type"] = media_type.lower()
    print(f"[DEBUG] create_media_generic prepared data: {data}")
    return func(data)

# last line