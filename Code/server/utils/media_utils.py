# first line

from typing import Dict, Any, Optional, List
from db.db_crud import (
    create_dict_entry,
    fetch_dict_entry_by_name,
    fetch_all_dict_entries,
    update_dict_entry,
    delete_dict_entry,
    create_relation,
    fetch_relations,
    delete_relation,
)
from objects.media.media import Media

# ---------------------------
# Dizionari (genres, authors, instruments, performers)
# ---------------------------
def add_dict_entry(table: str, name: str) -> Optional[int]:
    return create_dict_entry(table, name)

def fetch_dict_entry(table: str, name: str) -> Optional[Dict[str, Any]]:
    return fetch_dict_entry_by_name(table, name)

def fetch_all_dict_entries(table: str) -> List[Dict[str, Any]]:
    return fetch_all_dict_entries(table)

def update_dict_entry(table: str, entry_id: int, new_name: str) -> bool:
    return update_dict_entry(table, entry_id, new_name)

def delete_dict_entry(table: str, entry_id: int) -> bool:
    return delete_dict_entry(table, entry_id)

# ---------------------------
# Relazioni tra media e dizionari
# ---------------------------
def create_relation_entry(table: str, fields: tuple, values: tuple) -> bool:
    return create_relation(table, fields, values)

def fetch_relations_entry(table: str, where_field: str, where_value: Any) -> List[Dict[str, Any]]:
    return fetch_relations(table, where_field, where_value)

def delete_relation_entry(table: str, conditions: Dict[str, Any]) -> bool:
    return delete_relation(table, conditions)

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
    return Media.create_media(media_data, child_table="videos", child_fields=("duration_sec","link"))

def add_concert_segment(concert_media_id: int, start_time: float, end_time: float,
                        song_title: str, song_id: Optional[int]=None,
                        performers: List[int]=None, instruments: List[int]=None) -> Optional[int]:
    fields = ("concert_id","start_time","end_time","song_id","song_title")
    values = (concert_media_id, start_time, end_time, song_id, song_title)
    seg_id = create_relation("concert_segments", fields, values)
    if performers:
        for pid in performers:
            create_relation("segment_performers", ("segment_id","performer_id"), (seg_id, pid))
    if instruments:
        for iid in instruments:
            create_relation("segment_instruments", ("segment_id","instrument_id"), (seg_id, iid))
    return seg_id

def fetch_concert_segments(concert_media_id: int) -> List[Dict[str, Any]]:
    return fetch_relations("concert_segments", "concert_id", concert_media_id)
# last line