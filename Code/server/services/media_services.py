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
    # If an object is passed already, return it
    if isinstance(data, Media):
        print(f"[DEBUG][build_object] data is already a Media instance -> returning it")
        return data
    obj = cls.from_dict(data)
    print(f"[DEBUG][build_object] Built object={obj}")
    return obj

def get_object(cls: Type[Media], object_id: int):
    print(f"[DEBUG][get_object] cls={cls.__name__}, object_id={object_id}")
    # Prefer a class-level "fetch_full_<type>" hook if present
    hook_name = f"fetch_full_{cls.__name__.lower()}"
    hook = getattr(cls, hook_name, None)
    if callable(hook):
        obj = hook(object_id)
    else:
        # fallback to generic fetch
        obj = cls.fetch(object_id)
    print(f"[DEBUG][get_object] Retrieved object={obj}")
    return obj

def create_object(cls: Type[Media], user_obj: Optional[Any], data: Dict[str, Any]):
    print(f"[DEBUG][create_object] cls={cls.__name__}, user_obj={user_obj}, data={data}")
    # build object instance from dict (or accept object)
    obj = build_object(cls, data) if not isinstance(data, Media) else data
    if not obj:
        print("[DEBUG][create_object] Object is None -> returning None")
        return None
    # Accept user_obj as either dict or Root object; extract id safely
    uid = None
    if user_obj:
        if isinstance(user_obj, dict):
            uid = user_obj.get("id")
        else:
            uid = getattr(user_obj, "id", None)
    if uid:
        obj.user_id = uid
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

def create_song_services(user_obj, data: dict):
    print(f"[DEBUG][create_song_services] user_obj={user_obj}, data={data}")

    data["type"] = "song"
    if user_obj:
        uid = user_obj.get("id") if isinstance(user_obj, dict) else getattr(user_obj, "id", None)
        if uid:
            data["user_id"] = uid
    if data.get("stored_at") is None:
        data["stored_at"] = "server/storage/songs"
    if "performers" in data:
        # normalize performers to list of ids (db expects ids)
        data["performers"] = prepare_performers(data["performers"])

    # Costruisci oggetto (non salva ancora relazioni M:N)
    song = Song.from_dict(data)

    # Associa l'utente creatore (redundant if set above but safe)
    if user_obj:
        uid = user_obj.get("id") if isinstance(user_obj, dict) else getattr(user_obj, "id", None)
        if uid:
            song.user_id = uid

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
    Restituisce la lista di performer IDs pronta da associare al media.
    """
    result_ids = []
    for p in performers:
        if p["type"] == "user":
            # user performer is expected to provide an id
            result_ids.append(int(p["id"]))
        elif p["type"] == "external":
            # Controlla se esiste nel dict performers (returns dict row or None)
            existing = fetch_dict_entry("performers", p["name"])
            if existing:
                pid = existing["id"]
            else:
                pid = create_dict_entry("performers", p["name"])
            if pid is None:
                raise ValueError(f"Unable to create/fetch external performer '{p['name']}'")
            result_ids.append(pid)
        else:
            raise ValueError(f"Tipo performer non valido: {p['type']}")
    return result_ids

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

# =========================
# USER PUBLICATIONS SERVICES
# =========================
from server.db.db_crud import get_user_username_by_id as duck, fetch_all, fetch_one, get_user_id_by_username

def get_user_publications_services(user_obj, username: str, offset: int = 0, limit: int = 10):
    """
    Returns the list of media published by the specified username.
    Response shape: {"status":"OK", "results":[{...media...}], "count": total_count}
    """
    try:
        # Resolve username -> user_id
        uid = get_user_id_by_username(username)
        if uid is None:
            return {"status": "OK", "results": [], "count": 0}

        # fetch rows from media table for that user (ordered by created_at desc)
        query = "SELECT * FROM media WHERE user_id = %s ORDER BY created_at DESC OFFSET %s LIMIT %s;"
        rows = fetch_all(query, (uid, offset, limit))

        # total count (without pagination)
        cnt_row = fetch_one("SELECT COUNT(*) as cnt FROM media WHERE user_id = %s", (uid,))
        total_count = int(cnt_row["cnt"]) if cnt_row and "cnt" in cnt_row else len(rows)

        # Normalize rows into dicts with serializable fields using Media.from_dict -> to_dict
        results = []
        for r in rows:
            try:
                media_obj = Media.from_dict(dict(r))
                results.append(media_obj.to_dict())
            except Exception:
                # fallback: include raw row but ensure created_at is isoformat if present
                raw = dict(r)
                ca = raw.get("created_at")
                if hasattr(ca, "isoformat"):
                    raw["created_at"] = ca.isoformat()
                results.append(raw)

        return {"status": "OK", "results": results, "count": total_count}

    except Exception as e:
        print(f"[ERROR][get_user_publications_services] {e}")
        return {"status": "error", "error_msg": str(e)}

def get_media_services(user_obj, media_id: int):
    """
    Generic media fetch: returns a normalized dict for any media type (song/video/document).
    Used by the client show page (command 'get_media').
    Enhanced: include publisher username, author names, tags, duration_display and date (year).
    """
    try:
        # allow string ids too
        mid = int(media_id)
        media_obj = Media.fetch(mid)
        if not media_obj:
            return {"status": "error", "error_msg": "Media not found"}

        m = media_obj.to_dict()

        # publisher username
        try:
            username = duck(m.get("user_id"))
            if username:
                m["username"] = username
        except Exception:
            m["username"] = m.get("username")  # keep existing if present

        # resolve authors -> names
        try:
            author_ids = m.get("authors") or []
            if author_ids:
                rows = fetch_all("SELECT id, name FROM authors WHERE id = ANY(%s);", (author_ids,))
                author_names = [r["name"] for r in rows]
            else:
                author_names = []
            m["author_names"] = author_names
            # provide a single 'author' string for legacy clients
            if not m.get("author"):
                if author_names:
                    m["author"] = ", ".join(author_names)
                else:
                    m["author"] = m.get("username") or None
        except Exception:
            m["author_names"] = m.get("author_names", [])
            m["author"] = m.get("author") or m.get("username")

        # resolve genre tags -> names
        try:
            genre_ids = m.get("genres") or []
            if genre_ids:
                rows = fetch_all("SELECT id, name FROM genres WHERE id = ANY(%s);", (genre_ids,))
                tags = [r["name"] for r in rows]
            else:
                tags = []
            m["tags"] = tags
        except Exception:
            m["tags"] = m.get("tags", [])

        # duration formatting (seconds -> M:SS)
        try:
            dur = m.get("duration")
            if dur is not None:
                secs = int(dur)
                m["duration_display"] = f"{secs//60}:{secs%60:02d}"
                m["duration_seconds"] = secs
            else:
                m["duration_display"] = None
                m["duration_seconds"] = None
        except Exception:
            m["duration_display"] = None
            m["duration_seconds"] = None

        # published date: expose year as 'date' (client expects date)
        if m.get("year") is not None and not m.get("date"):
            m["date"] = str(m.get("year"))

        return {"status": "OK", "response": m}
    except Exception as e:
        print(f"[ERROR][get_media_services] {e}")
        return {"status": "error", "error_msg": str(e)}