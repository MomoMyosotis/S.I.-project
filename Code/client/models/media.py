# first line

from enum import Enum
from typing import Dict, Any, List, Optional
from client.services.http_helper import http_client
import json

class MediaType(Enum):
    IMAGE = "image"
    VIDEO = "video"
    SONG = "song"
    DOCUMENT = "document"
    CONCERT = "concert"
    UNKNOWN = "unknown"

class Media:
    def __init__(
        self,
        id: Optional[Any],
        type: str = None,
        user_id: Optional[Any] = None,
        title: str = "Untitled",
        year: Optional[int] = None,
        description: str = "",
        location: Optional[str] = None,
        additional_info: Optional[str] = None,
        stored_at: Optional[str] = None,
        duration: Optional[int] = None,
        created_at: Optional[str] = None,
        genres: Optional[List[str]] = None,
        authors: Optional[List[str]] = None,
        performers: Optional[List[str]] = None,
        linked_media: Optional[List[Dict[str, Any]]] = None,
        is_author: Optional[bool] = None,
        is_performer: Optional[bool] = None,
    ):
        self.id = id
        self.type = type
        self.user_id = user_id
        self.title = title or "Untitled"
        self.year = year
        self.description = description or ""
        self.location = location
        self.additional_info = additional_info
        self.stored_at = stored_at
        self.duration = duration
        self.created_at = created_at
        self.genres = genres or []
        self.authors = authors or []
        self.performers = performers or []
        self.linked_media = linked_media or []
        self.is_author = bool(is_author) if is_author is not None else False
        self.is_performer = bool(is_performer) if is_performer is not None else False

    @staticmethod
    def _unwrap_envelope(data: Any) -> Dict[str, Any]:
        # unwind nested envelopes like {"response": {...}} or {"result": {...}}
        inner = data if isinstance(data, dict) else {}
        seen = set()
        while isinstance(inner, dict):
            if id(inner) in seen:
                break
            seen.add(id(inner))
            for key in ("response", "result", "media"):
                if key in inner and isinstance(inner[key], (dict, list)):
                    inner = inner[key]
                    break
            else:
                break
        return inner if isinstance(inner, dict) else {}

    @staticmethod
    def from_server(data: Dict[str, Any]) -> "Media":
        raw = Media._unwrap_envelope(data)

        # ===== DEBUG: Log received data structure =====
        print(f"\n[DEBUG][Media.from_server] ===== RECEIVED FROM SERVER =====")
        print(f"[DEBUG][Media.from_server] Raw keys: {list(raw.keys()) if isinstance(raw, dict) else 'NOT A DICT'}")
        print(f"[DEBUG][Media.from_server] Critical fields in server response:")
        print(f"[DEBUG][Media.from_server]   - year: {raw.get('year')}")
        print(f"[DEBUG][Media.from_server]   - description: {raw.get('description')}")
        print(f"[DEBUG][Media.from_server]   - recording_date: {raw.get('recording_date')}")
        print(f"[DEBUG][Media.from_server]   - location: {raw.get('location')}")
        print(f"[DEBUG][Media.from_server]   - is_author: {raw.get('is_author')}")
        print(f"[DEBUG][Media.from_server]   - is_performer: {raw.get('is_performer')}")
        print(f"[DEBUG][Media.from_server]   - additional_info: {raw.get('additional_info')}")
        print(f"[DEBUG][Media.from_server] Full raw data: {raw}")
        print(f"[DEBUG][Media.from_server] ===== END RECEIVED DATA =====\n")

        # Extract canonical fields using server field names
        mid = raw.get("id") or raw.get("media_id") or raw.get("_id") or raw.get("id_media")
        title = raw.get("title") or raw.get("name") or "Untitled"
        
        # Use canonical 'type' field
        mtype = (raw.get("type") or raw.get("media_type") or raw.get("file_type") or "unknown").lower()
        
        # Extract all canonical fields with fallbacks
        user_id = raw.get("user_id") or raw.get("uploader_id") or raw.get("owner_id") or raw.get("owner")
        year = raw.get("year") or None
        if year and isinstance(year, str):
            try:
                year = int(year)
            except (ValueError, TypeError):
                year = None
        
        description = raw.get("description") or ""
        location = raw.get("location") or raw.get("recording_location") or None
        additional_info = raw.get("additional_info") or raw.get("document_annotations") or ""
        stored_at = raw.get("stored_at") or raw.get("file_path") or raw.get("file") or raw.get("stored") or None
        
        # Extract duration (may be string or int)
        duration = raw.get("duration") or raw.get("duration_seconds") or None
        if duration and isinstance(duration, str):
            try:
                duration = int(duration)
            except (ValueError, TypeError):
                duration = None
        
        created_at = raw.get("created_at") or raw.get("date") or None
        
        # Extract genres (handle both 'genres' and 'tags')
        genres = raw.get("genres") or raw.get("tags") or []
        if isinstance(genres, str):
            genres = [g.strip() for g in genres.split(",") if g.strip()]
        
        # Extract authors and performers (may be lists or comma-separated strings)
        authors = raw.get("authors") or raw.get("author_names") or []
        if isinstance(authors, str):
            authors = [a.strip() for a in authors.split(",") if a.strip()]
        
        performers = raw.get("performers") or []
        if isinstance(performers, str):
            performers = [p.strip() for p in performers.split(",") if p.strip()]
        
        # Extract linked_media
        raw_linked = raw.get("linked_media") or raw.get("linked") or []
        linked_media = []
        if raw_linked:
            if isinstance(raw_linked, str):
                try:
                    linked_media = json.loads(raw_linked)
                    if not isinstance(linked_media, list):
                        linked_media = [linked_media]
                except Exception:
                    linked_media = []
            elif isinstance(raw_linked, list):
                linked_media = raw_linked
            elif isinstance(raw_linked, dict):
                linked_media = [raw_linked]

        # Extract boolean flags
        is_author = bool(raw.get("is_author"))
        is_performer = bool(raw.get("is_performer"))
        
        # SPECIAL CASE: For concerts with no direct link but with linked_media containing YouTube URLs,
        # extract the YouTube URL from linked_media to populate the stored_at field
        if mtype == "concert" and not stored_at and linked_media:
            # Try to find a YouTube link in the first linked_media entry
            first_linked = linked_media[0] if isinstance(linked_media, list) and len(linked_media) > 0 else None
            if isinstance(first_linked, dict):
                # Prefer embed_url for direct embedding, fallback to url
                yt_url = first_linked.get("embed_url") or first_linked.get("url")
                if yt_url:
                    # Store the YouTube URL so show.html can use it
                    stored_at = yt_url
                    print(f"[DEBUG][Media.from_server] Concert: extracted YouTube URL from linked_media: {yt_url}")

        return Media(
            id=mid,
            type=mtype,
            user_id=user_id,
            title=title,
            year=year,
            description=description,
            location=location,
            additional_info=additional_info,
            stored_at=stored_at,
            duration=duration,
            created_at=created_at,
            genres=genres,
            authors=authors,
            performers=performers,
            linked_media=linked_media,
            is_author=is_author,
            is_performer=is_performer
        )

    def to_dict(self) -> Dict[str, Any]:
        result = {
            "id": self.id,
            "type": self.type,
            "user_id": self.user_id,
            "title": self.title,
            "year": self.year,
            "description": self.description,
            "location": self.location,
            "additional_info": self.additional_info,
            "stored_at": self.stored_at,
            "duration": self.duration,
            "created_at": self.created_at,
            "genres": self.genres,
            "authors": self.authors,
            "performers": self.performers,
            "linked_media": self.linked_media,
            "is_author": self.is_author,
            "is_performer": self.is_performer,
        }
        return result

    # Network helper methods (optional; call RPCs via shared http_client)
    def upload_media(self) -> Dict[str, Any]:
        """
        Try to create/upload the media by calling the server RPC.
        Returns server response dict.
        """
        payload = self.to_dict()
        try:
            res = http_client.send_request("UPLOAD_MEDIA", [payload], require_auth=True)
            return res
        except Exception as e:
            return {"status": "ERROR", "error_msg": str(e)}

    def delete_media(self) -> Dict[str, Any]:
        try:
            res = http_client.send_request("DELETE_MEDIA", [self.id], require_auth=True)
            return res
        except Exception as e:
            return {"status": "ERROR", "error_msg": str(e)}

    # backward-compatible aliases (fix spelling)
    def deleate_media(self) -> Dict[str, Any]:
        return self.delete_media()

    def comment_on_media(self, user_id: Any, comment_text: str) -> Dict[str, Any]:
        try:
            res = http_client.send_request("POST_COMMENT", [self.id, comment_text], require_auth=True)
            return res
        except Exception as e:
            return {"status": "ERROR", "error_msg": str(e)}