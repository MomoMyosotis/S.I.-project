# first line

from typing import Type, Optional, Dict, Any
from server.objects.media.song import Song
from server.objects.media.document import Document
from server.objects.media.video import Video
from server.objects.media.media import Media
from server.utils.media_utils import fetch_dict_entry, create_dict_entry
from server.objects.media.concert import Concert
import json
from server.db.db_crud import get_user_id_by_username

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
    hook_name = f"fetch_full_{cls.__name__.lower()}"
    hook = getattr(cls, hook_name, None)
    if callable(hook):
        obj = hook(object_id)
    else:
        obj = cls.fetch(object_id)
    print(f"[DEBUG][get_object] Retrieved object={obj}")
    return obj

def create_object(cls: Type[Media], user_obj: Optional[Any], data: Dict[str, Any]):
    print(f"[DEBUG][create_object] cls={cls.__name__}, user_obj={user_obj}, data={data}")
    obj = build_object(cls, data) if not isinstance(data, Media) else data
    if not obj:
        print("[DEBUG][create_object] Object is None -> returning None")
        return None
    target_user_id = getattr(obj, "user_id", None)
    actor_user_id = None
    if user_obj:
        if isinstance(user_obj, dict):
            actor_user_id = user_obj.get("id")
        else:
            actor_user_id = getattr(user_obj, "id", None)
    if target_user_id:
        print(f"[DEBUG][create_object] Using payload user_id={target_user_id}")
    elif actor_user_id:
        obj.user_id = actor_user_id
        print(f"[DEBUG][create_object] Fallback obj.user_id={actor_user_id}")

    print(f"[DEBUG][create_object] Saving object {obj}")
    obj.save()
    print(f"[DEBUG][create_object] Object saved: {obj}")

    return obj

def update_object(obj: Media, updates: Dict[str, Any]):
    print(f"[DEBUG][update_object] obj={obj}, updates={updates}")
    # filter out problematic fields that may cause SQL errors or should not be updated directly
    DISALLOWED_FIELDS = {"references", "raw", "created_at", "id", "media_id"}
    # split keys between media table and document child table
    MEDIA_ONLY_KEYS = set()  # leave empty to default to media updates
    DOC_KEYS = {"pages", "format", "caption"}

    # build sanitized updates (remove disallowed)
    sanitized = {}
    for k, v in updates.items():
        if k in DISALLOWED_FIELDS:
            print(f"[DEBUG][update_object] Skipping disallowed update field: {k}")
            continue
        sanitized[k] = v

    if not sanitized:
        print("[DEBUG][update_object] No sanitized fields to update -> returning object")
        return obj

    # apply attributes in-memory
    for k, v in sanitized.items():
        print(f"[DEBUG][update_object] Setting {k}={v}")
        try:
            setattr(obj, k, v)
        except Exception as e:
            print(f"[DEBUG][update_object] failed to set attribute {k} on object: {e}")

    # split into media vs document updates where relevant
    media_updates = {}
    doc_updates = {}
    for k, v in sanitized.items():
        if k in DOC_KEYS:
            doc_updates[k] = v
        else:
            media_updates[k] = v

    # --- NEW: handle relational fields (authors, genres, performers) ---
    # convert names -> ids (create dictionary entries when needed) and update relation tables
    relation_map = {
        "authors": ("authors", "media_authors", "author_id"),
        "genres": ("genres", "media_genres", "genre_id"),
        "performers": ("performers", "media_performances", "performer_id")
    }

    try:
        from server.db.db_crud import create_dict_entry as db_create_dict_entry, create_relation as db_create_relation, delete_relation as db_delete_relation
        for key, params in relation_map.items():
            if key in sanitized:
                table_name, rel_table, rel_col = params
                val = sanitized[key]
                if val is None:
                    # clear relations
                    try:
                        if getattr(obj, "id", None):
                            db_delete_relation(rel_table, {"media_id": getattr(obj, "id")})
                        setattr(obj, key, [])
                    except Exception as e:
                        print(f"[DEBUG][update_object] failed to clear relations for {key}: {e}")
                    # ensure we don't try to update media table with this field
                    media_updates.pop(key, None)
                    continue

                # normalize to list
                items = []
                if isinstance(val, str):
                    # comma separated string -> split
                    items = [s.strip() for s in val.split(",") if s.strip()]
                elif isinstance(val, (list, tuple)):
                    items = list(val)
                else:
                    items = [val]

                ids = []
                for it in items:
                    try:
                        if isinstance(it, int):
                            ids.append(int(it))
                            continue
                        # dict form like {type:'user', id: ...}
                        if isinstance(it, dict):
                            if "id" in it and it["id"]:
                                ids.append(int(it["id"]))
                                continue
                            name = it.get("name") or it.get("username") or it.get("performer")
                        else:
                            name = str(it).strip()
                        if not name:
                            continue
                        # create/fetch dict entry
                        nid = db_create_dict_entry(table_name, name)
                        if nid:
                            ids.append(nid)
                    except Exception as e:
                        print(f"[DEBUG][update_object] failed to normalize relation item {it} for {key}: {e}")

                # replace relations in DB: delete existing then insert new ones
                try:
                    mid = getattr(obj, "id", None)
                    if mid is not None:
                        db_delete_relation(rel_table, {"media_id": mid})
                        for iid in ids:
                            db_create_relation(rel_table, ("media_id", rel_col), (mid, iid))
                        # update in-memory object
                        setattr(obj, key, ids)
                except Exception as e:
                    print(f"[DEBUG][update_object] failed to update relation table {rel_table}: {e}")

                # make sure these are not attempted on media table
                media_updates.pop(key, None)
    except Exception as e:
        print(f"[DEBUG][update_object] relation handling failed: {e}")

    # perform DB updates directly to avoid Media.save() full-payload update
    try:
        from server.db.db_crud import update_media_db
        if media_updates:
            print(f"[DEBUG][update_object] Updating media table id={getattr(obj,'id',None)} with {media_updates}")
            update_media_db(getattr(obj, "id", None), media_updates)

            # If updating a concert link, ensure the concerts row and media.linked_media are kept in sync
            try:
                if 'link' in media_updates:
                    mid = getattr(obj, 'id', None)
                    if mid is not None and getattr(obj, 'type', None) == 'concert':
                        from server.db.db_crud import create_concert_db, fetch_one, update_media_db as _update_media_db
                        # upsert concerts table so the latest link/title/description are stored
                        try:
                            create_concert_db(mid, media_updates.get('link'), media_updates.get('title') or getattr(obj, 'title', None), media_updates.get('description') or getattr(obj,'description',None))
                        except Exception as e:
                            print(f"[DEBUG][update_object] failed to upsert concerts table: {e}")

                        # merge/update linked_media JSON in media table
                        try:
                            cur_row = fetch_one("SELECT linked_media FROM media WHERE id=%s", (mid,))
                            existing = cur_row.get('linked_media') if cur_row else None
                            try:
                                lm = json.loads(existing) if existing else []
                            except Exception:
                                lm = []
                            if not isinstance(lm, list):
                                lm = [lm]
                            link = media_updates.get('link')
                            entry = {"type": "link", "source": ("youtube" if "youtube" in (link or "").lower() else "external"), "url": link, "title": media_updates.get('title') or getattr(obj, 'title', None)}
                            # avoid duplicate by url
                            if not any(isinstance(i, dict) and i.get('url') == link for i in lm):
                                lm.append(entry)
                                _update_media_db(mid, {'linked_media': json.dumps(lm)})
                        except Exception as e:
                            print(f"[DEBUG][update_object] failed to sync linked_media: {e}")
            except Exception as e:
                print(f"[DEBUG][update_object] concert link sync failed: {e}")
    except Exception as e:
        print(f"[ERROR][update_object] failed to update media table: {e}")

    if doc_updates:
        try:
            from server.db.db_crud import update_document_db
            print(f"[DEBUG][update_object] Updating documents table id={getattr(obj,'id',None)} with {doc_updates}")
            update_document_db(getattr(obj, "id", None), doc_updates)
        except Exception as e:
            print(f"[ERROR][update_object] failed to update documents table: {e}")

    print(f"[DEBUG][update_object] Object after DB update {obj}")
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

def create_song_services(user_obj, data: dict = None, **kwargs):
    # Accept either a single data dict or keyword args (dispatcher may unpack)
    if data is None:
        data = {}
    if isinstance(data, dict) and kwargs:
        data = {**data, **kwargs}
    elif not isinstance(data, dict) and kwargs:
        # unexpected shapes: treat kwargs as the payload
        data = dict(kwargs)

    print(f"[DEBUG][create_song_services] user_obj={user_obj}, data={data}")

    # normalize alternate keys and aliases
    if 'i_am_author' in data and 'is_author' not in data:
        data['is_author'] = bool(data.pop('i_am_author'))
    if 'i_am_performer' in data and 'is_performer' not in data:
        data['is_performer'] = bool(data.pop('i_am_performer'))
    if 'is_composer' in data and 'is_author' not in data:
        data['is_author'] = bool(data.get('is_composer'))

    # year aliases
    if 'publication_year' in data and 'year' not in data:
        try:
            data['year'] = int(data.get('publication_year')) if data.get('publication_year') else None
        except Exception:
            data['year'] = None
    if 'composition_year' in data and 'year' not in data:
        try:
            data['year'] = int(data.get('composition_year')) if data.get('composition_year') else None
        except Exception:
            pass

    # single-string genre -> list
    if 'genre' in data and 'genres' not in data:
        g = data.get('genre')
        if isinstance(g, str):
            data['genres'] = [s.strip() for s in g.split(',') if s.strip()]
        elif isinstance(g, (list, tuple)):
            data['genres'] = list(g)

    # support publish-on-behalf: map on_behalf_of -> user_id if present
    if 'on_behalf_of' in data:
        try:
            ob = str(data.get('on_behalf_of')).strip()
            if ob:
                uid = get_user_id_by_username(ob)
                if uid:
                    data['user_id'] = uid
                else:
                    print(f"[create_song_services] on_behalf_of username '{ob}' not found")
        except Exception as e:
            print(f"[create_song_services] error resolving on_behalf_of: {e}")

    data["type"] = "song"
    # only set creator from actor if not explicitly publishing on behalf of someone
    if data.get("user_id") is None and user_obj:
        uid = user_obj.get("id") if isinstance(user_obj, dict) else getattr(user_obj, "id", None)
        if uid:
            data["user_id"] = uid
    if data.get("stored_at") is None:
        data["stored_at"] = "server/storage/songs"

    # handle automatic metadata (duration/format)
    def _parse_duration(d):
        import re
        if d is None:
            return None
        if isinstance(d, (int, float)):
            return int(round(float(d)))
        s = str(d).strip()
        if ':' in s:
            try:
                parts = [int(p) for p in s.split(':')]
            except Exception:
                parts = []
            if len(parts) == 2:
                return parts[0] * 60 + parts[1]
            if len(parts) == 3:
                return parts[0] * 3600 + parts[1] * 60 + parts[2]
        import re
        m = re.search(r"([0-9]+(?:\.[0-9]+)?)", s)
        if m:
            try:
                return int(round(float(m.group(1))))
            except Exception:
                return None
        return None

    auto = data.get("automatic")
    if isinstance(auto, dict):
        if data.get("duration") is None and auto.get("duration") is not None:
            dur = _parse_duration(auto.get("duration"))
            if dur is not None:
                data["duration"] = dur
        if auto.get("format") is not None:
            data["file_format"] = auto.get("format")
            try:
                import json as _json
                info = {"detected_format": auto.get("format")}
                if data.get("additional_info"):
                    try:
                        existing = _json.loads(data.get("additional_info"))
                        if isinstance(existing, dict):
                            existing.update(info)
                            data["additional_info"] = _json.dumps(existing)
                        else:
                            data["additional_info"] = _json.dumps(info)
                    except Exception:
                        data["additional_info"] = _json.dumps(info)
                else:
                    data["additional_info"] = _json.dumps(info)
            except Exception:
                data["additional_info"] = f"format:{auto.get('format')}"

    if "performers" in data:
        # normalize performers to list of ids (db expects ids)
        try:
            perf_ids = prepare_performers(data["performers"])
        except Exception as e:
            return {"status": "ERROR", "error_msg": f"performers normalization failed: {e}"}
        # validate/repair performer ids: ensure we have performer rows for each
        from server.db.db_crud import fetch_one, get_or_create_performer_for_user
        final_pids = []
        seen = set()
        for pid in perf_ids:
            row = fetch_one("SELECT id FROM performers WHERE id=%s", (pid,))
            if row:
                nid = int(row['id'])
            else:
                # pid may be a user id: try to create a performer for that user
                urow = fetch_one("SELECT id, username FROM users WHERE id=%s", (pid,))
                if urow and urow.get('id'):
                    creator_uid = urow['id']
                    pname = urow.get('username') or str(creator_uid)
                    nid = get_or_create_performer_for_user(creator_uid, pname)
                    if nid is None:
                        return {"status": "ERROR", "error_msg": f"Unable to create performer entry for user id {creator_uid}"}
                else:
                    return {"status": "ERROR", "error_msg": f"Performer id {pid} does not exist"}
            if nid not in seen:
                seen.add(nid)
                final_pids.append(nid)
        data["performers"] = final_pids

    # Costruisci oggetto (non salva ancora relazioni M:N)
    song = Song.from_dict(data)

    # Ensure the song's owner matches the requested owner (on_behalf or actor)
    if data.get('user_id') is not None:
        song.user_id = data.get('user_id')

    # Salva nel DB
    created_id = song.save()
    if not created_id:
        return {"status": "ERROR", "error_msg": "Failed to persist song"}
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
def create_document_services(user_obj, data: dict = None, **kwargs):
    if data is None:
        data = {}
    if isinstance(data, dict) and kwargs:
        data = {**data, **kwargs}
    elif not isinstance(data, dict) and kwargs:
        data = dict(kwargs)

    # map automatic into document fields
    auto = data.get("automatic")
    if isinstance(auto, dict):
        if auto.get("format") and not data.get("format"):
            data["format"] = auto.get("format")
        if auto.get("pages") and not data.get("pages"):
            try:
                data["pages"] = int(auto.get("pages"))
            except Exception:
                pass

    # if linked_to is present, inherit owner from the linked media
    if data.get('linked_to'):
        try:
            from server.db.db_crud import fetch_one
            lm = fetch_one("SELECT user_id FROM media WHERE id=%s", (data.get('linked_to'),))
            if lm and lm.get('user_id'):
                data['user_id'] = lm['user_id']
        except Exception as e:
            print(f"[create_document_services] unable to inherit owner from linked media: {e}")

    # normalize single-string genre alias
    if 'genre' in data and 'genres' not in data:
        g = data.get('genre')
        if isinstance(g, str):
            data['genres'] = [s.strip() for s in g.split(',') if s.strip()]
        elif isinstance(g, (list, tuple)):
            data['genres'] = list(g)

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
def create_video_services(user_obj, data: dict = None, **kwargs):
    if data is None:
        data = {}
    if isinstance(data, dict) and kwargs:
        data = {**data, **kwargs}
    elif not isinstance(data, dict) and kwargs:
        data = dict(kwargs)

    # handle automatic metadata
    auto = data.get("automatic")
    if isinstance(auto, dict):
        if data.get("duration") is None and auto.get("duration") is not None:
            try:
                data["duration"] = int(round(float(auto.get("duration"))))
            except Exception:
                pass

    data["type"] = "video"
    if data.get("stored_at") is None:
        data["stored_at"] = "server/storage/videos"
    return create_object(Video, user_obj, data)


# =========================
# CONCERT SERVICES
# =========================
from server.objects.media.concert import Concert
from server.db.db_crud import create_concert_db, fetch_concert_by_video_id, create_concert_segment_db, fetch_concert_segments_db, update_concert_segment_db, delete_concert_segment_db


def _extract_user_lvl(user_obj):
    viewer_lvl_raw = user_obj.get("lvl") if isinstance(user_obj, dict) else getattr(user_obj, "lvl", None)
    viewer_lvl = int(viewer_lvl_raw) if isinstance(viewer_lvl_raw, (int, float, str)) and str(viewer_lvl_raw).isdigit() else None
    return viewer_lvl


def create_concert_services(user_obj, data: dict = None, **kwargs):
    if data is None:
        data = {}
    if isinstance(data, dict) and kwargs:
        data = {**data, **kwargs}
    elif not isinstance(data, dict) and kwargs:
        data = dict(kwargs)

    data["type"] = "concert"
    if data.get("stored_at") is None:
        data["stored_at"] = "server/storage/videos"
    print(f"[DEBUG][create_concert_services] user={user_obj}, data={data}")

    # disallow banned users (lvl 6) from creating concerts
    lvl = _extract_user_lvl(user_obj) if user_obj else None
    if lvl == 6:
        return {"error": "Insufficient permissions to create concert"}

    # create concert media and concerts row will be created inside create_media_db
    concert = create_object(Concert, user_obj, data)
    return concert


def get_concert_services(user_obj, video_id: int):
    print(f"[DEBUG][get_concert_services] user={user_obj}, video_id={video_id}")
    return Concert.fetch_full_concert(video_id)


def add_concert_segment_services(user_obj, video_id: int, segment_data: dict):
    print(f"[DEBUG][add_concert_segment_services] user={user_obj}, video_id={video_id}, segment_data={segment_data}")
    # user must not be RESTRICTED or BANNED (lvl 5 or 6)
    lvl = _extract_user_lvl(user_obj) if user_obj else None
    if lvl in (5, 6):
        print(f"[DEBUG][add_concert_segment_services] permission denied for user lvl={lvl}")
        return {"error": "Insufficient permissions to add concert metadata"}

    concert = fetch_concert_by_video_id(video_id)
    print(f"[DEBUG][add_concert_segment_services] fetched concert: {concert!r}")
    if not concert:
        print(f"[DEBUG][add_concert_segment_services] concert not found for video_id={video_id}")
        return {"error": "Concert not found"}
    concert_id = concert.get("video_id")
    print(f"[DEBUG][add_concert_segment_services] concert_id={concert_id}")

    # normalize performers -> ids
    performers_in = segment_data.get("performers")
    performers_ids = None
    if performers_in:
        try:
            performers_ids = prepare_performers(performers_in)
        except Exception:
            performers_ids = None

    # normalize instruments -> ids (create if needed)
    instruments_in = segment_data.get("instruments")
    instruments_ids = None
    if instruments_in:
        instruments_ids = []
        for itm in (instruments_in if isinstance(instruments_in, (list, tuple)) else [instruments_in]):
            try:
                if isinstance(itm, int):
                    instruments_ids.append(itm)
                elif isinstance(itm, dict) and itm.get("id"):
                    instruments_ids.append(int(itm.get("id")))
                else:
                    name = str(itm).strip()
                    if not name:
                        continue
                    # attempt to find existing
                    row = fetch_dict_entry("instruments", name)
                    if row and row.get("id"):
                        instruments_ids.append(row.get("id"))
                    else:
                        nid = create_dict_entry("instruments", name)
                        if nid:
                            instruments_ids.append(nid)
            except Exception:
                continue

    print(f"[DEBUG][add_concert_segment_services] performers_ids={performers_ids}, instruments_ids={instruments_ids}")
    seg_id = create_concert_segment_db(
        concert_id=concert_id,
        media_id=segment_data.get("media_id"),
        song_title=segment_data.get("song_title"),
        start_time=segment_data.get("start_time"),
        end_time=segment_data.get("end_time"),
        comment=segment_data.get("comment"),
        performers=performers_ids,
        instruments=instruments_ids,
    )
    if not seg_id:
        print(f"[DEBUG][add_concert_segment_services] failed to create segment for concert_id={concert_id}")
        return {"error": "Failed to create segment"}
    print(f"[DEBUG][add_concert_segment_services] created segment_id={seg_id} for concert_id={concert_id}")
    return {"segment_id": seg_id}


def get_concert_segments_services(user_obj, video_id: int):
    print(f"[DEBUG][get_concert_segments_services] user={user_obj}, video_id={video_id}")
    concert = fetch_concert_by_video_id(video_id)
    print(f"[DEBUG][get_concert_segments_services] fetched concert: {concert!r}")
    if not concert:
        print(f"[DEBUG][get_concert_segments_services] no concert found for video_id={video_id}")
        return []
    concert_id = concert.get("video_id")
    res = fetch_concert_segments_db(concert_id)
    print(f"[DEBUG][get_concert_segments_services] returning {len(res) if isinstance(res, list) else 'unknown'} segments for concert_id={concert_id}")
    return res


def update_concert_segment_services(user_obj, segment_id: int, updates: dict):
    print(f"[DEBUG][update_concert_segment_services] user={user_obj}, segment_id={segment_id}, updates={updates}")
    lvl = _extract_user_lvl(user_obj) if user_obj else None
    if lvl in (5, 6):
        print(f"[DEBUG][update_concert_segment_services] permission denied for user lvl={lvl}")
        return {"error": "Insufficient permissions to update concert metadata"}
    ok = update_concert_segment_db(segment_id, updates)
    print(f"[DEBUG][update_concert_segment_services] update result for segment_id={segment_id}: {ok}")
    return {"success": ok}


def delete_concert_segment_services(user_obj, segment_id: int):
    print(f"[DEBUG][delete_concert_segment_services] user={user_obj}, segment_id={segment_id}")
    lvl = _extract_user_lvl(user_obj) if user_obj else None
    if lvl in (5, 6):
        print(f"[DEBUG][delete_concert_segment_services] permission denied for user lvl={lvl}")
        return {"error": "Insufficient permissions to delete concert metadata"}
    ok = delete_concert_segment_db(segment_id)
    print(f"[DEBUG][delete_concert_segment_services] delete result for segment_id={segment_id}: {ok}")
    return {"success": ok}
def get_video_services(user_obj, video_id: int):
    print(f"[DEBUG][get_video_services] user={user_obj}, video_id={video_id}")
    return get_object(Video, video_id)

def update_video_services(user_obj, video_id: int, updates: dict):
    print(f"[DEBUG][update_video_services] user={user_obj}, video_id={video_id}, updates={updates}")
    video = get_object(Video, video_id)
    if not video:
        print(f"[DEBUG][update_video_services] video not found for id={video_id}")
        return {"error": "Video not found"}
    res = update_object(video, updates)
    print(f"[DEBUG][update_video_services] update result for video_id={video_id}: {res}")
    return res

def delete_video_services(user_obj, video_id: int):
    print(f"[DEBUG][delete_video_services] user={user_obj}, video_id={video_id}")
    video = get_object(Video, video_id)
    if not video:
        print(f"[DEBUG][delete_video_services] video not found for id={video_id}")
        return {"error": "Video not found"}
    res = delete_object(video)
    print(f"[DEBUG][delete_video_services] delete result for video_id={video_id}: {res}")
    return res

# ========================
# SUPPORT
# =========================
def prepare_performers(performers: list) -> list:
    """Normalize performers into a list of performer IDs.
    Accepts several shapes:
      - list of dicts: {type:'user', id: <int>} or {type:'external', name: '...'}
      - list of ints: treated as performer ids
      - list of strings: treated as usernames (try resolve to user id) or external names
    """
    result_ids = []
    # handle comma-separated single string
    items = []
    if isinstance(performers, str):
        items = [s.strip() for s in performers.split(",") if s.strip()]
    elif isinstance(performers, (list, tuple)):
        items = list(performers)
    else:
        raise ValueError("Unsupported performers container")

    from server.db.db_crud import get_or_create_performer_for_user
    for p in items:
        # handle dict entries (existing behavior)
        if isinstance(p, dict):
            if p.get("type") == "user":
                if "id" in p:
                    uid = int(p["id"])
                    # ensure performer entry exists for user
                    pid = get_or_create_performer_for_user(uid, p.get("username") or str(uid))
                    if pid is None:
                        raise ValueError(f"Unable to map user performer id {uid} to performer entry")
                    result_ids.append(pid)
                elif "username" in p:
                    # try to resolve username
                    uname = p["username"].strip()
                    uid = get_user_id_by_username(uname)
                    if uid:
                        pid = get_or_create_performer_for_user(uid, uname)
                        if pid is None:
                            raise ValueError(f"Unable to create/fetch performer for user '{uname}'")
                        result_ids.append(pid)
                    else:
                        raise ValueError(f"Unable to resolve user performer '{uname}'")
            elif p.get("type") == "external":
                name = p.get("name")
                existing = fetch_dict_entry("performers", name)
                if existing:
                    pid = existing["id"]
                else:
                    pid = create_dict_entry("performers", name)
                if pid is None:
                    raise ValueError(f"Unable to create/fetch external performer '{name}'")
                result_ids.append(pid)
            else:
                raise ValueError(f"Tipo performer non valido: {p.get('type')}")

        # handle integers (assume performer id)
        elif isinstance(p, int):
            result_ids.append(int(p))

        # handle strings: try username -> user id -> performer, otherwise treat as external name
        elif isinstance(p, str):
            pstr = p.strip()
            if not pstr:
                continue
            # comma separated list in a single string
            if "," in pstr:
                for sub in [s.strip() for s in pstr.split(',') if s.strip()]:
                    uid = get_user_id_by_username(sub)
                    if uid:
                        pid = get_or_create_performer_for_user(uid, sub)
                        if pid is None:
                            raise ValueError(f"Unable to create/fetch performer for user '{sub}'")
                        result_ids.append(pid)
                    else:
                        existing = fetch_dict_entry("performers", sub)
                        if existing:
                            result_ids.append(existing["id"])
                        else:
                            pid = create_dict_entry("performers", sub)
                            if pid is None:
                                raise ValueError(f"Unable to create/fetch external performer '{sub}'")
                            result_ids.append(pid)
                continue

            uid = get_user_id_by_username(pstr)
            if uid:
                pid = get_or_create_performer_for_user(uid, pstr)
                if pid is None:
                    raise ValueError(f"Unable to create/fetch performer for user '{pstr}'")
                result_ids.append(pid)
            else:
                # external performer fallback
                existing = fetch_dict_entry("performers", pstr)
                if existing:
                    pid = existing["id"]
                else:
                    pid = create_dict_entry("performers", pstr)
                if pid is None:
                    raise ValueError(f"Unable to create/fetch external performer '{pstr}'")
                result_ids.append(pid)

        else:
            raise ValueError("Unsupported performer format")

    # dedupe while preserving order
    seen = set()
    final = []
    for i in result_ids:
        if i not in seen:
            seen.add(i)
            final.append(i)
    return final

def get_feed_services(user_obj, search: str = "", filter_by: str = "all", offset: int = 0, limit: int = 10):
    print(f"[DEBUG] feed request received offset={offset}, limit={limit}, search='{search}', filter_by='{filter_by}'")

    # Pull a larger batch per media type (no per-type offset) then do global pagination.
    per_type_limit = max(offset + limit * 2, limit)  # fetch enough from each type to cover the requested window

    def fetch_media(cls):
        return cls.fetch_all(search=search, filter_by=filter_by, offset=0, limit=per_type_limit)

    # Prendi media separatamente dal DB (no per-type offset)
    songs = fetch_media(Song)
    videos = fetch_media(Video)
    documents = fetch_media(Document)
    concerts = fetch_media(Concert)

    # Combina risultati and include created_at for global ordering
    from server.db.db_crud import get_user_username_by_id as duck

    combined = []
    for m in songs + videos + documents + concerts:
        d = m.to_dict()
        user_id = d.get("user_id")
        username = duck(user_id)
        created = d.get("created_at")
        # normalize created_at to a comparable string if possible
        if hasattr(created, "isoformat"):
            created_iso = created.isoformat()
        else:
            created_iso = str(created) if created is not None else ""
        combined.append({
            "id": d.get("id"),
            "title": d.get("title"),
            "username": username or "Unknown",
            "thumbnail": d.get("thumbnail", "https://via.placeholder.com/100"),
            "tags": d.get("genres") or d.get("keywords") or [],
            "type": d.get("type"),
            "created_at": created_iso,
            "raw": d
        })

    # global ordering (newest first)
    combined.sort(key=lambda x: x.get("created_at") or "", reverse=True)

    total_count = len(combined)
    paged = combined[offset:offset + limit]

    # remove created_at/raw if you want to keep response small; keep them now for flexibility
    results = paged

    return {"status": "OK", "results": results, "count": total_count}

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

        # small helper: infer type when DB row misses it
        def _infer_type_from_row(row: dict) -> str:
            if not row:
                return "unknown"
            t = (row.get("type") or row.get("media_type") or "").strip().lower()
            if t:
                # normalize common synonyms
                if t in ("audio","music","song"): return "song"
                if t in ("video","movie"): return "video"
                if t in ("document","doc","pdf"): return "document"
                return t
            stored = (row.get("stored_at") ).lower()
            if any(stored.endswith(ext) for ext in (".mp3",".wav",".m4a",".ogg",".flac")) or "/songs" in stored or "/audio" in stored:
                return "song"
            if any(stored.endswith(ext) for ext in (".mp4",".mov",".webm",".avi",".mkv")) or "/videos" in stored:
                return "video"
            if any(stored.endswith(ext) for ext in (".pdf",".docx",".doc",".txt",".odt",".pptx")) or "/documents" in stored:
                return "document"
            return "unknown"

        # Normalize rows into dicts with serializable fields using Media.from_dict -> to_dict
        results = []
        for r in rows:
            try:
                media_obj = Media.from_dict(dict(r))
                media_dict = media_obj.to_dict()
                # ensure 'type' present and normalized
                media_dict["type"] = (media_dict.get("type") or _infer_type_from_row(r) or "unknown")
                results.append(media_dict)
            except Exception:
                # fallback: include raw row but ensure created_at is isoformat if present and include a type
                raw = dict(r)
                ca = raw.get("created_at")
                if hasattr(ca, "isoformat"):
                    raw["created_at"] = ca.isoformat()
                # ensure we return a 'type' field so client can pick icons like the feed
                raw["type"] = (raw.get("type") or raw.get("media_type") or _infer_type_from_row(raw) or "unknown")
                results.append(raw)

        return {"status": "OK", "results": results, "count": total_count}

    except Exception as e:
        print(f"[ERROR][get_user_publications_services] {e}")
        return {"status": "error", "error_msg": str(e)}

def get_media_services(user_obj, media_id: int):
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

        # If this media is a concert, fetch the full concert row (link, segments)
        try:
            if (m.get("type") or "").lower() == "concert":
                from server.objects.media.concert import Concert
                full = Concert.fetch_full_concert(mid)
                if full:
                    full_map = full.to_dict()
                    # merge concert-specific fields (link, segments) without removing already-computed fields
                    for k, v in full_map.items():
                        if v is not None:
                            m[k] = v
                # Concerts are external links; ensure no file metadata is exposed so clients don't try to fetch a file
                if (m.get("type") or "").lower() == "concert":
                    m["stored_at"] = None
                    m["filename"] = None
                    m["file_available"] = False

                # sanitize link (strip surrounding quotes/whitespace) and add/embed_url when applicable
                try:
                    link = m.get("link")
                    if isinstance(link, str) and link.strip():
                        cleaned = link.strip().strip('"').strip("'")
                        # normalize simple missing scheme
                        if cleaned and not cleaned.startswith(("http://","https://")):
                            cleaned = "https://" + cleaned
                        m["link"] = cleaned
                    else:
                        # fallback: look at stored_at or filename for a youtube link/id
                        cand = m.get("stored_at") or m.get("filename") or ""
                        if isinstance(cand, str) and cand.strip():
                            cc = cand.strip()
                            # try to extract a youTube id or full watch URL
                            import re
                            ytm_c = re.search(r"(?:v=|/embed/|youtu\.be/)([A-Za-z0-9_-]{11})", cc)
                            if ytm_c:
                                vid_c = ytm_c.group(1)
                                m["link"] = f"https://www.youtube.com/watch?v={vid_c}"
                            elif "youtube.com" in cc or "youtu.be" in cc:
                                # use candidate as-is
                                m["link"] = cc
                            else:
                                m["link"] = None
                        else:
                            m["link"] = None

                    # try to extract youtube id and add embed_url and verify availability via oEmbed
                    import re
                    cleaned_link = m.get("link") or ""
                    ytm = re.search(r"(?:v=|/embed/|youtu\.be/)([A-Za-z0-9_-]{11})", cleaned_link)
                    if not ytm and cleaned_link:
                        ytm = re.search(r"youtube\.com/watch\?[^#]*v=([A-Za-z0-9_-]{11})", cleaned_link)

                    if ytm:
                        vid = ytm.group(1)
                        embed_url = f"https://www.youtube.com/embed/{vid}?rel=0"
                        # verify via YouTube oEmbed to check existence/embeddability
                        try:
                            import requests
                            o = requests.get("https://www.youtube.com/oembed", params={"url": f"https://www.youtube.com/watch?v={vid}", "format": "json"}, timeout=5)
                            if o.status_code == 200:
                                m["embed_url"] = embed_url
                                m["embed_ok"] = True
                                m["embed_error"] = None
                            else:
                                m["embed_url"] = embed_url
                                m["embed_ok"] = False
                                m["embed_error"] = f"oembed status {o.status_code}"
                        except Exception as e:
                            m["embed_url"] = embed_url
                            m["embed_ok"] = False
                            m["embed_error"] = str(e)
                    else:
                        m["embed_url"] = None
                        m["embed_ok"] = False
                        m["embed_error"] = "no valid youtube id found"
                except Exception as e:
                    m["embed_url"] = None
                    m["embed_ok"] = False
                    m["embed_error"] = str(e)
        except Exception:
            pass

        try:
            if (m.get("type") or "").lower() == "concert" and m.get("link") and not m.get("linked_media"):
                try:
                    link = m.get("link")
                    entry = {"type": "link", "source": ("youtube" if "youtube" in link.lower() else "external"), "url": link, "title": m.get("title")}
                    from server.db.db_crud import update_media_db
                    update_media_db(m.get("id") or m.get("media_id"), {"linked_media": json.dumps([entry])})
                    m["linked_media"] = [entry]
                    # debug(f"[CONCERT SYNC] persisted linked_media for media_id={m.get('id') or m.get('media_id')}")
                except Exception:
                    pass
        except Exception:
            pass

        # Debug final concert link/embed state
        try:
            if (m.get("type") or "").lower() == "concert":
                print(f"[DEBUG][get_media_services] final concert media (post-merge): link='{m.get('link')}', embed_url='{m.get('embed_url')}', stored_at={m.get('stored_at')}, filename={m.get('filename')}")
        except Exception:
            pass

        return {"status": "OK", "response": m}
    except Exception as e:
        print(f"[ERROR][get_media_services] {e}")
        return {"status": "error", "error_msg": str(e)}