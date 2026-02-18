# first line

from typing import Any, Dict, List, Optional
from enum import Enum
from client.models.user import User
from client.models.media import Media
from client.services.http_helper import http_client
class TYPEIntervention(Enum):
    TEXT = 0
    GRAPHIC = 1
    COMMENT = 2

class Intervention:
    def __init__(
        self,
        id: Optional[int],
        pubblisher: Optional[int],
        media: Optional[int],
        type: TYPEIntervention = TYPEIntervention.TEXT,
        content: str = "",
        ):
        self.id = id
        self.pubblisher = pubblisher
        self.media = media
        self.type = type if isinstance(type, TYPEIntervention) else (TYPEIntervention(type) if type is not None else TYPEIntervention.TEXT)
        self.content = content or ""

    @staticmethod
    def _unwrap_envelope(data: Any) -> Dict[str, Any]:
        if isinstance(data, dict) and "intervention" in data:
            return data["intervention"]
        return data

    @classmethod
    def from_list(cls, data_list: List[Dict[str, Any]]) -> List["Intervention"]:
        interventions = []
        for data in data_list:
            unwrapped = cls._unwrap_envelope(data)
            intervention = cls(
                id=unwrapped.get("id"),
                pubblisher=unwrapped.get("pubblisher"),
                media=unwrapped.get("media"),
                type=unwrapped.get("type"),
                content=unwrapped.get("content"),
            )
            interventions.append(intervention)
        return interventions

##############################
    @classmethod
    def make_intervention(cls, pubblisher: int, media: int, type: TYPEIntervention, content: str) -> dict:
        if type == TYPEIntervention.COMMENT:
            args = [pubblisher, media, content]
            response = http_client.send_request(command="MAKE_COMMENT", args=args, require_auth=True)
        else:
            raise ValueError(f"Invalid intervention type.\ntype: {type}")
        return response

    @classmethod
    def fetch_interventions(cls, media_id: int, intervention_type: TYPEIntervention) -> List["Intervention"]:
        if intervention_type == TYPEIntervention.COMMENT:
            response = http_client.send_request(command="FETCH_COMMENT", args=[media_id], require_auth=(http_client.token is not None))
        else:
            raise ValueError(f"Invalid intervention type.\ntype: {intervention_type}\nmedia_id: {media_id}")
        interventions_data = response.get("interventions", [])
        return cls.from_list(interventions_data)

    @classmethod
    def update_intervention(cls, intervention_id: int, new_content: str, intervention_type: TYPEIntervention) -> dict:
        if intervention_type == TYPEIntervention.COMMENT:
            args = [intervention_id, new_content]
            response = http_client.send_request(command="UPDATE_COMMENT", args=args, require_auth=True)
        else:
            raise ValueError(f"Invalid intervention type.\ntype: {intervention_type}")
        return response

    @classmethod
    def delete_intervention(cls, intervention_id: int, intervention_type: TYPEIntervention) -> dict:
        if intervention_type == TYPEIntervention.COMMENT:
            response = http_client.send_request(command="DELETE_COMMENT", args=[intervention_id], require_auth=True)
        else:
            raise ValueError(f"Invalid intervention type.\ntype: {intervention_type}\nid: {intervention_id}")
        return response
###############################

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Intervention":
        unwrapped = cls._unwrap_envelope(data)
        return cls(
            id=unwrapped.get("id"),
            pubblisher=unwrapped.get("pubblisher"),
            media=unwrapped.get("media"),
            type=unwrapped.get("type"),
            content=unwrapped.get("content"),
        )

"""CREATE TABLE notes (
    id PRIMARY KEY SERIAL,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    media_id INT REFERENCES media(id) ON DELETE CASCADE,
    -- For documents: AAAABBCC (page/line/char); for video/audio/concert: seconds
    note_start INT NOT NULL DEFAULT 00000000,
    note_end INT NOT NULL DEFAULT 00000000,
    type INT NOT NULL DEFAULT 1, -- 0=graphic, 1=text
    text TEXT, -- JSON string for structured data or base64 canvas data
    stored_at VARCHAR(255),
    page INT,
    A_point POINT,
    B_point POINT,
    private BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);
"""
class Note(Intervention):
    def __init__(
        self,
        id: Optional[int],
        pubblisher: Optional[int],
        media: Optional[int],
        type: int = 1,
        content: str = "",
        start: Any = 0,
        end: Any = 0,
        stored_at: Optional[str] = None,
        private: bool = False,
        page: Optional[int] = None,
        A_point: Optional[str] = None,
        B_point: Optional[str] = None
    ):
        super().__init__(id, pubblisher, media, type, content)
        self.start = start
        self.end = end
        self.stored_at = stored_at
        self.private = private
        self.page = page
        self.A_point = A_point
        self.B_point = B_point

    @classmethod
    def parse_text_data(cls, text: str) -> Dict[str, Any]:
        """Parse text field as JSON for structured note data."""
        if not text:
            return {}
        try:
            import json
            data = json.loads(text)
            return data if isinstance(data, dict) else {}
        except:
            return {"raw_text": text}

    @classmethod
    def build_text_data(cls, media_type: str, **kwargs) -> str:
        """Build JSON text field from performance metadata."""
        import json
        data = {}
        if media_type in ('video', 'audio', 'concert', 'song'):
            # Performance metadata
            data['performers'] = kwargs.get('performers', [])
            data['instruments'] = kwargs.get('instruments', [])
            data['length'] = kwargs.get('length')
            data['rhythms'] = kwargs.get('rhythms')
            data['solos'] = kwargs.get('solos')
            data['recording_date'] = kwargs.get('recording_date')
            data['recording_location'] = kwargs.get('recording_location')
            data['is_live'] = kwargs.get('is_live', False)
            data['notes'] = kwargs.get('notes')
            data['additional_info'] = kwargs.get('additional_info')
        elif media_type == 'document':
            # Document execution metadata
            data['performers'] = kwargs.get('performers', [])
            data['instruments'] = kwargs.get('instruments', [])
            data['rhythms'] = kwargs.get('rhythms')
            data['intensity'] = kwargs.get('intensity')
            data['comments'] = kwargs.get('comments')
            data['notes'] = kwargs.get('notes')
            data['additional_info'] = kwargs.get('additional_info')
        else:
            # Generic fallback
            data.update({k: v for k, v in kwargs.items() if v is not None})
        return json.dumps(data)

    @classmethod
    def create_note(cls, user_id: int, media_id: int, media_type: str, 
                   start: Any, end: Any, note_type: int = 1, 
                   content: str = "", stored_at: Optional[str] = None, 
                   private: bool = False, page: Optional[int] = None, A_point: Optional[str] = None, B_point: Optional[str] = None) -> dict:
        """Create a note via HTTP."""
        payload = {
            "media_id": media_id,
            "start": start,
            "end": end,
            "type": note_type,
            "text": content,
            "stored_at": stored_at,
            "private": private,
            "page": page,
            "A_point": A_point,
            "B_point": B_point
        }
        return http_client.send_request("CREATE_NOTE", [payload], require_auth=True)

    @classmethod
    def fetch_notes(cls, media_id: int) -> List["Note"]:
        """Fetch all notes for a media."""
        response = http_client.send_request("FETCH_NOTE", [media_id], require_auth=(http_client.token is not None))
        if not isinstance(response, dict):
            return []
        notes_data = response.get("notes", [])
        if not isinstance(notes_data, list):
            notes_data = [notes_data]
        return cls.from_list(notes_data)

    @classmethod
    def update_note(cls, note_id: int, **updates) -> dict:
        """Update a note."""
        return http_client.send_request("UPDATE_NOTE", [note_id, updates], require_auth=True)

    @classmethod
    def delete_note(cls, note_id: int) -> dict:
        """Delete a note."""
        return http_client.send_request("DELETE_NOTE", [note_id], require_auth=True)


# last line