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
            response = http_client.send_request(command="FETCH_COMMENT", args=[media_id], require_auth=True)
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

# last line