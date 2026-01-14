from typing import Optional, Dict, Any, List
from .media import Media
from server.db.db_crud import fetch_relations, fetch_concert_by_video_id, fetch_concert_segments_db

class Concert(Media):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = "concert"
        # concert specific
        self.link = kwargs.get("link")
        self.segments = kwargs.get("segments", [])

    def media_type(self) -> str:
        return "concert"

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "link": getattr(self, "link", None),
            "segments": getattr(self, "segments", []),
            "embed_url": getattr(self, "embed_url", None),
            "embed_ok": getattr(self, "embed_ok", None),
            "embed_error": getattr(self, "embed_error", None),
        })
        return data

    # --------------------
    # CLASS HELPERS
    # --------------------
    @classmethod
    def fetch_full_concert(cls, video_id: int) -> Optional["Concert"]:
        # fetch base media
        media_data = cls.fetch(media_id=video_id)
        if not media_data:
            return None

        # fetch concert row
        c = fetch_concert_by_video_id(video_id)
        if c:
            media_data.link = c.get("link")
            media_data.title = c.get("title") or media_data.title
            media_data.description = c.get("description") or media_data.description
            # segments
            media_data.segments = fetch_concert_segments_db(c.get("video_id"))

            # Extract YouTube embed info and verify availability via oEmbed
            try:
                # prefer explicit concert.link but fall back to stored_at/filename when missing
                link = media_data.link or media_data.stored_at or media_data.filename
                if isinstance(link, str) and link.strip():
                    import re
                    cleaned = link.strip().strip('"').strip("'")
                    ytm = re.search(r"(?:v=|/embed/|youtu\.be/)([A-Za-z0-9_-]{11})", cleaned)
                    if not ytm:
                        ytm = re.search(r"youtube\.com/watch\?[^#]*v=([A-Za-z0-9_-]{11})", cleaned)
                    if ytm:
                        vid = ytm.group(1)
                        media_data.embed_url = f"https://www.youtube.com/embed/{vid}?rel=0"
                        # ensure a canonical watch link is present
                        if not media_data.link:
                            media_data.link = f"https://www.youtube.com/watch?v={vid}"
                        try:
                            import requests
                            o = requests.get("https://www.youtube.com/oembed", params={"url": f"https://www.youtube.com/watch?v={vid}", "format": "json"}, timeout=5)
                            if o.status_code == 200:
                                media_data.embed_ok = True
                                media_data.embed_error = None
                            else:
                                media_data.embed_ok = False
                                media_data.embed_error = f"oembed status {o.status_code}"
                        except Exception as e:
                            media_data.embed_ok = False
                            media_data.embed_error = str(e)
                    else:
                        media_data.embed_url = None
                        media_data.embed_ok = False
                        media_data.embed_error = "no valid youtube id found"
                else:
                    media_data.embed_url = None
                    media_data.embed_ok = False
                    media_data.embed_error = "no link"
            except Exception as e:
                media_data.embed_url = None
                media_data.embed_ok = False
                media_data.embed_error = str(e)
        else:
            media_data.segments = []

        return media_data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Optional["Concert"]:
        if not data:
            return None
        return cls(**data)
