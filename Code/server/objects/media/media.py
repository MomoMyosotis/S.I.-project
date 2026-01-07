# first line

# ============================================================
# MEDIA BASE CLASS
# ============================================================
# Qui definiamo la classe base "Media" che rappresenta un generico contenuto
# multimediale (es. canzone, documento, video). Non è pensata per essere
# usata direttamente ma come "contratto" da cui ereditano le sottoclassi.
# ============================================================

# ABC = Abstract Base Class → libreria di Python per creare classi astratte
# (cioè classi che non possono essere istanziate direttamente).
# Le classi figlie DEVONO implementare i metodi definiti come @abstractmethod.
# ============================================================
# MEDIA BASE CLASS
# ============================================================
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, List
from datetime import datetime
import json
from server.db.db_crud import create_media_db, fetch_media_db, update_media_db, delete_media_db, create_dict_entry, fetch_dict_entry_by_name, fetch_one
from server.utils.storage_manager import save_file, get_path
import base64, uuid, os
from werkzeug.utils import secure_filename
import subprocess
from typing import Optional
from PyPDF2 import PdfReader

# helper: probe duration/pages
def _format_duration(seconds: Optional[float]) -> Optional[str]:
    if seconds is None:
        return None
    s = int(round(seconds))
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    if h:
        return f"{h:02d}:{m:02d}:{sec:02d}"
    return f"{m:02d}:{sec:02d}"

def _probe_media_duration(path: str) -> Optional[float]:
    """Try ffprobe to get duration (in seconds)."""
    try:
        proc = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", path],
            capture_output=True, text=True, timeout=6
        )
        out = proc.stdout.strip()
        if not out:
            return None
        return float(out)
    except Exception:
        return None

def _probe_pdf_pages(path: str) -> Optional[int]:
    """Try PyPDF2, then pdfinfo to get page count."""
    try:
        if PdfReader:
            reader = PdfReader(path)
            # PyPDF2 v2 exposes pages as list-like
            pages = getattr(reader, "pages", None)
            if pages is not None:
                return len(pages)
            # fallback older API
            return int(reader.getNumPages())
    except Exception:
        pass
    try:
        proc = subprocess.run(["pdfinfo", path], capture_output=True, text=True, timeout=4)
        for line in proc.stdout.splitlines():
            if line.lower().startswith("pages:"):
                try:
                    return int(line.split(":")[1].strip())
                except Exception:
                    pass
    except Exception:
        pass
    return None

def _resolve_storage_file(stored_at: Optional[str], media_type: Optional[str]) -> Optional[str]:
    """
    Given a stored_at value (any of: 'folder/filename', 'server/storage/folder/filename',
    'folder' ...) try to return the absolute filesystem path to a concrete file.
    """
    if not stored_at:
        return None

    # normalize and strip server/storage prefix if present
    rel = stored_at.replace("\\", "/")
    prefix = "server/storage/"
    if rel.startswith(prefix):
        rel = rel[len(prefix):].lstrip("/")

    parts = rel.split("/")
    # if we have folder + filename -> use get_path(folder, filename)
    if len(parts) >= 2:
        folder = parts[0]
        filename = "/".join(parts[1:])
        try:
            p = get_path(folder, filename)
            if os.path.isfile(p):
                return p
        except Exception:
            pass

    # if only a filename or ambiguous -> try using media_type as folder
    basename = parts[-1]
    try:
        p = get_path((media_type or "song"), basename)
        if os.path.isfile(p):
            return p
    except Exception:
        pass

    # if stored_at points to a folder -> pick first file in that folder
    try:
        maybe_folder = os.path.join(os.getcwd(), "server", "storage", parts[0])
        if os.path.isdir(maybe_folder):
            files = [f for f in os.listdir(maybe_folder) if os.path.isfile(os.path.join(maybe_folder, f))]
            if files:
                return os.path.join(maybe_folder, files[0])
    except Exception:
        pass

    return None

class Media(ABC):
    def __init__(
        self,
        media_id: Optional[int] = None,
        type: str = None,
        user_id: Optional[int] = None,
        title: Optional[str] = None,
        year: Optional[int] = None,
        description: Optional[str] = None,
        linked_media: Optional[str] = None,
        duration: Optional[int] = None,
        location: Optional[str] = None,
        additional_info: Optional[str] = None,
        stored_at: Optional[str] = None,
        created_at: Optional[datetime] = None,
        genres: Optional[List[str]] = None,
        authors: Optional[List[int]] = None,
        performers: Optional[List[int]] = None,
        references: Optional[List[int]] = None,
        is_author: Optional[bool] = None,
        is_performer: Optional[bool] = None,
        **kwargs
    ):
        #print(f"[DEBUG][Media.__init__] Called with title={title}, type={type}, year={year}, user_id={user_id}, kwargs={kwargs}")

        # Alias tra id e media_id
        self.id = media_id or kwargs.get("id")
        self.media_id = self.id

        self.type = type
        self.title = title
        self.user_id = user_id
        self.year = year
        self.description = description
        self.linked_media = linked_media
        self.duration = duration
        self.location = location
        self.additional_info = additional_info
        self.stored_at = stored_at
        self.created_at = created_at or datetime.now()
        self.genres = genres or []
        self.authors = authors or []
        self.performers = performers or []
        self.references = references or []
        self.is_author = bool(is_author)
        self.is_performer = bool(is_performer)
        self._deleted = False

        # optional media-specific fields (provide defaults so subclasses don't crash)
        self.pages = kwargs.get("pages", None)
        self.format = kwargs.get("format", None)
        # other optional attrs may be present in kwargs and will be set below

        # Gestione extra attr
        for k, v in kwargs.items():
            #print(f"[DEBUG][Media.__init__] Extra attr: {k}={v}")
            setattr(self, k, v)

        # Gestione tracklist
        tracklist = kwargs.get("tracklist")
        if tracklist is not None:
            self.additional_info = json.dumps(tracklist)

        #print(f"[DEBUG][Media.__init__] Finished -> {self}")

    @abstractmethod
    def media_type(self) -> str:
        pass

    # =====================
    # CRUD BASE
    # =====================
    def save(self):
        """
        Persist media:
         - map authors/genres/performers names -> ids (creating entries when needed)
         - save uploaded files (base64 payloads) into storage and set stored_at
         - call create_media_db() which expects integer ids for relations
        """
        # build clean payload from object
        payload = self.to_dict()

        # helper: ensure dict table entries exist and return ids
        def ensure_ids(table: str, items):
            ids = []
            if not items:
                return ids
            for it in items:
                if it is None:
                    continue
                # already an int -> verify it exists
                if isinstance(it, int):
                    try:
                        row = fetch_one(f"SELECT id FROM {table} WHERE id=%s", (it,))
                        if row and row.get("id"):
                            ids.append(it)
                        else:
                            print(f"[Media.save] provided id={it} not found in {table}, skipping")
                    except Exception as e:
                        print(f"[Media.save] verify id error for {table} id={it}: {e}")
                    continue

                name = str(it).strip()
                if not name:
                    continue
                # try fetch existing
                try:
                    row = fetch_dict_entry_by_name(table, name)
                except Exception as e:
                    row = None
                    print(f"[Media.save] fetch_dict_entry_by_name error: {e}")

                if row and row.get("id"):
                    ids.append(row["id"])
                else:
                    # create and return new id (create_dict_entry commits)
                    try:
                        nid = create_dict_entry(table, name)
                        if nid:
                            ids.append(nid)
                            print(f"[Media.save] created {table} entry '{name}' -> id={nid}")
                        else:
                            print(f"[Media.save] failed to create {table} entry '{name}'")
                    except Exception as e:
                        print(f"[Media.save] create_dict_entry error for {table} name={name}: {e}")
            return ids

        # normalize relations from names -> ids
        try:
            payload["authors"] = ensure_ids("authors", payload.get("authors") or [])
            payload["genres"] = ensure_ids("genres", payload.get("genres") or [])
            payload["performers"] = ensure_ids("performers", payload.get("performers") or [])
        except Exception as e:
            print(f"[Media.save] relation normalization failed: {e}")

        # handle files array (client may send list of dicts with content_b64)
        files = payload.pop("files", None)
        stored_at_value = payload.get("stored_at") or None
        if files and isinstance(files, list) and len(files) > 0:
            # save first file (primary) and ignore extras for stored_at (you can adapt to keep list)
            try:
                first = files[0]
                fname = first.get("filename") or f"{uuid.uuid4().hex}"
                safe = secure_filename(fname)
                # choose folder by media type if available
                folder = (self.type or payload.get("type") or "media").lower()

                # ---- robust content extraction ----
                content = None
                # prioritized explicit fields
                if "content_bytes" in first and isinstance(first.get("content_bytes"), (bytes, bytearray)):
                    content = bytes(first.get("content_bytes"))
                elif "raw_bytes" in first and isinstance(first.get("raw_bytes"), (bytes, bytearray)):
                    content = bytes(first.get("raw_bytes"))

                # content_b64 or content may be either base64 string or raw bytes
                if content is None:
                    b = first.get("content_b64") if "content_b64" in first else first.get("content")
                    if isinstance(b, (bytes, bytearray)):
                        content = bytes(b)
                    elif isinstance(b, str) and b:
                        # try base64 decode, fallback to utf-8 bytes
                        try:
                            content = base64.b64decode(b)
                        except Exception:
                            try:
                                content = b.encode("utf-8")
                            except Exception:
                                content = None

                # file-like objects (werkzeug FileStorage, streams, etc.)
                if content is None:
                    fileobj = first.get("file") or first.get("stream") or first.get("fileobj")
                    if fileobj and hasattr(fileobj, "read"):
                        try:
                            fileobj.seek(0)
                        except Exception:
                            pass
                        try:
                            content = fileobj.read()
                            # ensure bytes type for memoryview / bytearray
                            if isinstance(content, memoryview):
                                content = content.tobytes()
                        except Exception:
                            content = None

                # If still no content, log and skip saving to avoid writing invalid files
                if not content:
                    print(f"[DEBUG][Media.save] No file content available for filename='{fname}', payload first keys={list(first.keys())}")
                else:
                    # ensure unique file name
                    unique_name = f"{uuid.uuid4().hex}_{safe}"
                    # save_file returns a message but underlying path is deterministic from storage_manager.get_path
                    save_file(folder, unique_name, content)
                    # store a relative path used by storage manager to fetch later
                    payload["stored_at"] = f"{folder}/{unique_name}"
                    # --- probe saved file to fill duration/pages ---
                    try:
                        abs_path = os.path.join(os.getcwd(), "server", "storage", folder, unique_name)
                        if (self.type or payload.get("type") or "").lower() in ("song", "video"):
                            dur = _probe_media_duration(abs_path)
                            if dur is not None:
                                payload["duration"] = int(round(dur))
                                payload["duration_seconds"] = dur
                                payload["duration_display"] = _format_duration(dur)
                        elif (self.type or payload.get("type") or "").lower() == "document":
                            pages = _probe_pdf_pages(abs_path)
                            if pages is not None:
                                payload["pages"] = pages
                    except Exception as e:
                        print(f"[DEBUG][Media.save] probing file failed: {e}")
            except Exception as e:
                print(f"[DEBUG][Media.save] file save failed: {e}")
                # continue without stored_at

        # finally call DB create/update
        if getattr(self, "id", None) is None and not payload.get("media_id"):
            # create
            result = create_media_db(payload)
            if result and isinstance(result, dict) and result.get("id"):
                self.id = result["id"]
                # also keep media_id attribute if used elsewhere
                self.media_id = result["id"]
            else:
                print(f"[DEBUG][Media.save] Result from create_media_db={result}")
                # leave id None so callers see failure
                return None
        else:
            # update path (existing id)
            mid = getattr(self, "id", None) or payload.get("media_id")
            updates = payload.copy()
            # remove keys not allowed by update_media_db
            updates.pop("id", None)
            updates.pop("media_id", None)
            update_media_db(mid, updates)
            self.id = mid

        # --- NEW: if duration/pages missing try to probe stored file and update DB ---
        try:
            need_update = {}
            st = payload.get("stored_at") or self.stored_at
            # try to resolve a real file path
            file_path = _resolve_storage_file(st, (self.type or payload.get("type")))
            if file_path:
                if (self.type or payload.get("type") or "").lower() in ("song", "video"):
                    dur = _probe_media_duration(file_path)
                    if dur is not None:
                        secs = int(round(dur))
                        need_update["duration"] = secs
                elif (self.type or payload.get("type") or "").lower() == "document":
                    pages = _probe_pdf_pages(file_path)
                    if pages is not None:
                        need_update["pages"] = pages
            if need_update and self.id:
                # split updates between media table and documents table
                media_updates = {}
                doc_updates = {}
                for k, v in need_update.items():
                    if k in ("pages", "format", "caption"):
                        doc_updates[k] = v
                    else:
                        media_updates[k] = v

                if media_updates:
                    try:
                        update_media_db(self.id, media_updates)
                        for k, v in media_updates.items():
                            setattr(self, k, v)
                    except Exception as e:
                        print(f"[DEBUG][Media.save] failed to update media table: {e}")

                if doc_updates:
                    try:
                        from server.db.db_crud import update_document_db
                        ok = update_document_db(self.id, doc_updates)
                        if ok:
                            for k, v in doc_updates.items():
                                setattr(self, k, v)
                    except Exception as e:
                        print(f"[DEBUG][Media.save] failed to update documents table: {e}")
        except Exception as e:
            print(f"[DEBUG][Media.save] post-create probing failed: {e}")

        # sync relations if subclass needs it (most handled inside create_media_db already)
        try:
            self._sync_relations()
        except Exception as e:
            print(f"[DEBUG][Media.save] _sync_relations error: {e}")

        return self.id

    def delete(self):
        print(f"[DEBUG][Media.delete] Called on {self}")
        if self._deleted:
            print(f"[DEBUG][Media.delete] Object already deleted")
            return False

        if self.media_id:
            delete_media_db(self.media_id)
            print(f"[DEBUG][Media.delete] Deleted media_id={self.media_id}")
            self.media_id = None

        self._deleted = True
        return True

    @classmethod
    def fetch(cls, media_id: int):
        print(f"[DEBUG][Media.fetch] Called cls={cls.__name__}, media_id={media_id}")
        data = fetch_media_db(media_id)
        print(f"[DEBUG][Media.fetch] Data from DB={data}")
        if not data:
            print("[DEBUG][Media.fetch] No data found -> returning None")
            return None
        obj = cls.from_dict(data)
        print(f"[DEBUG][Media.fetch] Built object={obj}")
        return obj

    @classmethod
    def fetch_all(cls, search: Optional[str] = None, filter_by: Optional[str] = None,
                offset: int = 0, limit: int = 10) -> List["Media"]:
        """
        Recupera tutti i media dal database appartenenti a questa sottoclasse
        (Song, Video, Document), con eventuale filtro di ricerca o tipo.
        """
        print(f"[DEBUG][Media.fetch_all] Called cls={cls.__name__}, search={search}, filter_by={filter_by}")

        try:
            from server.db.db_crud import fetch_all_media_db
        except ImportError as e:
            print (f"[ERROR][Media.Fetch_All] cannot import fetch_all from db_crud: {e}")
            return[]

        # Try to resolve the media type in a resilient way:
        media_type = None
        try:
            # Prefer calling as a classmethod if available
            media_type = cls.media_type()
        except TypeError:
            # If media_type is instance method, try instantiation (fall back)
            try:
                media_type = cls().media_type()
            except Exception as e:
                print(f"[DEBUG][Media.fetch_all] could not determine media_type: {e}")
                media_type = None
        except Exception as e:
            print(f"[DEBUG][Media.fetch_all] unexpected error resolving media_type: {e}")
            media_type = None

        rows = fetch_all_media_db(media_type=media_type, search=search, filter_by=filter_by, offset=offset, limit=limit
    )
        print(f"[DEBUG][Media.Fetch_all] DB returned {len(rows) if rows else 0} rows")

        result = []
        if not rows:
            return result

        for r in rows:
            try:
                obj = cls.from_dict(r)
                result.append(obj)
            except Exception as e:
                print(f"[ERROR][Media.fetch_all] failed to build obj from rows: {e}")
        print(f"[DEBUG][Media.fetch_all] Returning {len(result)} obj")
        return result

    # =====================
    # RELAZIONI M:N
    # =====================
    def _sync_relations(self):
        print(f"[DEBUG][Media._sync_relations] Called for {self}")
        # Override nelle sottoclassi per gestire relazioni come authors, performers, genres.

    def to_dict(self) -> Dict[str, Any]:
        d = {
            "id": self.media_id,
            "media_id": self.media_id,
            "type": self.type,
            "title": self.title,
            "user_id": self.user_id,
            "year": self.year,
            "description": self.description,
            "linked_media": self.linked_media,
            "duration": self.duration,
            "pages": getattr(self, "pages", None),
            "location": self.location,
            "additional_info": self.additional_info,
            "file_format": getattr(self, "file_format", None),
            "stored_at": self.stored_at,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "genres": self.genres,
            "authors": self.authors,
            "performers": self.performers,
            "references": self.references,
            "is_author": self.is_author,
            "is_performer": self.is_performer
        }
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        #print(f"[DEBUG][Media.from_dict] cls={cls.__name__}, data={data}")
        if 'id' in data:
            data['media_id'] = data.pop('id')
        if data['type'] == 'song':
            from .song import Song
            obj = Song(**data)
        elif data['type'] == 'video':
            from .video import Video
            obj = Video(**data)
        elif data['type'] == 'document':
            from .document import Document
            obj = Document(**data)
        else:
            raise ValueError (f"invalid media type: {data['type']}")
        #print(f"[DEBUG][Media.from_dict] Built object={obj}")
        return obj

    def __repr__(self) -> str:
        return f"<{self.media_type().capitalize()} id={self.media_id}, title={self.title}>"

# last line