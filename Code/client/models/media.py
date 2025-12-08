# first line

from enum import Enum
from typing import Dict, Any, List, Optional
from client.services.http_helper import http_client

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
        title: str = "Untitled",
        media_type: MediaType = MediaType.UNKNOWN,
        uploader_id: Optional[Any] = None,
        tags: Optional[List[str]] = None,
        description: str = "",
        stored_at: Optional[str] = None,
        filename: Optional[str] = None,
    ):
        self.id = id
        self.title = title or "Untitled"
        self.media_type = media_type if isinstance(media_type, MediaType) else MediaType(media_type) if media_type in MediaType._value2member_map_ else MediaType.UNKNOWN
        self.uploader_id = uploader_id
        self.tags = tags or []
        self.description = description or ""
        self.stored_at = stored_at
        self.filename = filename

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

        # normalize common keys
        mid = raw.get("id") or raw.get("media_id") or raw.get("_id") or raw.get("id_media")
        title = raw.get("title") or raw.get("name") or raw.get("filename") or "Untitled"
        # infer type from multiple possible keys
        mtype_raw = (raw.get("type") or raw.get("media_type") or raw.get("file_type") or "").lower() if isinstance(raw.get("type") or raw.get("media_type") or raw.get("file_type"), str) else raw.get("type") or raw.get("media_type") or raw.get("file_type") or ""
        if isinstance(mtype_raw, str) and mtype_raw:
            mtype = MediaType(mtype_raw) if mtype_raw in MediaType._value2member_map_ else MediaType.UNKNOWN
        else:
            # try detection from path/filename
            stored = (raw.get("stored_at") or raw.get("file_path") or raw.get("file") or raw.get("link") or "").lower()
            if any(ext in stored for ext in (".mp3", ".wav", ".m4a", ".flac")):
                mtype = MediaType.SONG
            elif any(ext in stored for ext in (".mp4", ".mov", ".webm", ".avi", ".mkv")):
                mtype = MediaType.VIDEO
            elif any(ext in stored for ext in (".pdf", ".doc", ".docx", ".txt")):
                mtype = MediaType.DOCUMENT
            elif "youtube.com" in stored or "youtu.be" in stored:
                mtype = MediaType.CONCERT
            else:
                mtype = MediaType.UNKNOWN

        tags = raw.get("tags") or raw.get("genre") or raw.get("genres") or []
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",") if t.strip()]

        description = raw.get("description") or raw.get("additional_info") or ""
        stored_at = raw.get("stored_at") or raw.get("file_path") or raw.get("file") or raw.get("stored") or raw.get("link")
        filename = raw.get("filename") or (stored_at.split("/")[-1] if stored_at and "/" in stored_at else None)

        return Media(
            id=mid,
            title=title,
            media_type=mtype,
            uploader_id=raw.get("uploader_id") or raw.get("user_id") or raw.get("owner"),
            tags=tags,
            description=description,
            stored_at=stored_at,
            filename=filename
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "type": self.media_type.value if isinstance(self.media_type, MediaType) else str(self.media_type),
            "media_type": self.media_type.value if isinstance(self.media_type, MediaType) else str(self.media_type),
            "uploader_id": self.uploader_id,
            "tags": self.tags,
            "description": self.description,
            "stored_at": self.stored_at,
            "filename": self.filename
        }

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