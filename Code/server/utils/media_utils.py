# first line

from typing import Dict, Any, Optional, List
from server.objects.media import Media
import server.db.db_crud as db_crud

# ---------------------------
# Dizionari (genres, authors, instruments, performers)
# ---------------------------
def add_dict_entry(table: str, name: str) -> Optional[int]:
    return db_crud.create_dict_entry(table, name)

def create_dict_entry(table: str, name: str) -> Optional[int]:
    return db_crud.create_dict_entry(table, name)

def fetch_dict_entry(table: str, name: str) -> Optional[Dict[str, Any]]:
    return db_crud.fetch_dict_entry_by_name(table, name)

def fetch_all_dict_entries(table: str) -> List[Dict[str, Any]]:
    return db_crud.fetch_all_dict_entries(table)

def update_dict_entry(table: str, entry_id: int, new_name: str) -> bool:
    return db_crud.update_dict_entry(table, entry_id, new_name)

def delete_dict_entry(table: str, entry_id: int) -> bool:
    return db_crud.delete_dict_entry(table, entry_id)

# ---------------------------
# Relazioni tra media e dizionari
# ---------------------------
def create_relation_entry(table: str, fields: tuple, values: tuple) -> bool:
    return db_crud.create_relation(table, fields, values)

def fetch_relations_entry(table: str, where_field: str, where_value: Any) -> List[Dict[str, Any]]:
    return db_crud.fetch_relations(table, where_field, where_value)

def delete_relation_entry(table: str, conditions: Dict[str, Any]) -> bool:
    return db_crud.delete_relation(table, conditions)

# ---------------------------
# Helper combinati / utility
# ---------------------------
def set_execution_details(media_id: int, duration_sec: int = None,
                        recorded_at: Optional[str] = None,
                        location: Optional[str] = None) -> bool:
    updates = {}
    if duration_sec is not None: updates["duration_sec"] = duration_sec
    if recorded_at is not None:  updates["recorded_at"] = recorded_at
    if location is not None:     updates["location"] = location
    return Media.update_media(media_id, updates, table="executions")

def create_concert_video(media_data: Dict[str, Any]) -> Optional[int]:
    media_data["type"] = "concert"
    #print(f"[DEBUG][create_concert_video] media_data={media_data}")
    try:
        from server.services.media_services import create_concert_services
        obj = create_concert_services(None, media_data)
        #print(f"[DEBUG][create_concert_video] created object: {obj!r}")
        # return media id if object created
        return getattr(obj, "id", None) if obj else None
    except Exception as e:
        #print(f"[DEBUG][create_concert_video] failed: {e}")
        return None

def add_concert_segment(concert_media_id: int, start_time: float, end_time: float,
                        song_title: str, song_id: Optional[int]=None,
                        performers: List[int]=None, instruments: List[int]=None) -> Optional[int]:
    #print(f"[DEBUG][add_concert_segment] concert_media_id={concert_media_id}, start={start_time}, end={end_time}, song_title={song_title}, song_id={song_id}, performers={performers}, instruments={instruments}")
    try:
        from server.db.db_crud import create_concert_segment_db
        seg_id = create_concert_segment_db(concert_media_id, song_id, song_title, start_time, end_time, None, performers, instruments)
        #print(f"[DEBUG][add_concert_segment] created seg_id={seg_id}")
        return seg_id
    except Exception as e:
        #print(f"[DEBUG][add_concert_segment] failed: {e}")
        return None

def fetch_concert_segments(concert_media_id: int) -> List[Dict[str, Any]]:
    #print(f"[DEBUG][fetch_concert_segments] concert_media_id={concert_media_id}")
    try:
        from server.db.db_crud import fetch_concert_segments_db
        res = fetch_concert_segments_db(concert_media_id)
        #print(f"[DEBUG][fetch_concert_segments] returned {len(res) if isinstance(res, list) else 'unknown'} items")
        return res
    except Exception as e:
        #print(f"[DEBUG][fetch_concert_segments] fallback fetch_relations due to: {e}")
        return db_crud.fetch_relations("concert_segments", "concert_id", concert_media_id)

# last line