# first line

from typing import List, Optional, Dict, Any
from objects.interventi.comment import Comment
from objects.interventi.notes import Note
from objects.media.song import Song
from objects.media.document import Document
from objects.media.video import Video
from logs.logger import log_event
from utils.user_utils import fetch_relations
from utils.media_utils import (create_dict_entry,
                                delete_dict_entry,
                                fetch_all_dict_entries
                                )
# ====================
# GENERIC
# ====================
def search_song(user_obj: Any, **filters) -> List[Dict[str, Any]]:
    return Song.advanced_song_search(filters)

def search_document(user_obj: Any, **filters) -> List[Dict[str, Any]]:
    return Document.advanced_document_search(filters)

def search_video(user_obj: Any, **filters) -> List[Dict[str, Any]]:
    return Video.advanced_video_search(filters)

def add_entry(user_obj: Any, table: str, name: str) -> str:
    entry_id = create_dict_entry(table, name)
    return str(entry_id) if entry_id else "ERROR"

def remove_entry(user_obj: Any, table: str, entry_id: int) -> str:
    success = delete_dict_entry(table, entry_id)
    return "OK" if success else "ERROR"

def get_entries(user_obj: Any, table: str) -> List[Dict[str, Any]]:
    return fetch_all_dict_entries(table)

# =====================
# COMMENTI
# =====================

def build_comment_tree(comments: List[Dict[str, Any]],
                        depth: Optional[int] = None) -> List[Dict[str, Any]]:
    # Trasforma una lista piatta di commenti in un albero annidato
    lookup = {c["id"]: {**c, "children": []} for c in comments}
    roots = []

    for c in lookup.values():
        parent_id = c.get("parent_id")
        if parent_id and parent_id in lookup:
            lookup[parent_id]["children"].append(c)
        else:
            roots.append(c)

    if depth is not None:
        def trim_depth(nodes, current_depth):
            if current_depth >= depth:
                for n in nodes:
                    n["children"] = []
            else:
                for n in nodes:
                    trim_depth(n["children"], current_depth + 1)
        trim_depth(roots, 0)

    return roots

def create_comment(user_obj: Any, media_id: int, content: str, parent_id: Optional[int] = None) -> Dict[str, Any]:
    if user_obj.lvl > 4:
        return {"status": "ERROR", "id": None, "error_msg": "PERMISSION_DENIED"}
    try:
        comment_id = Comment.add_comment(user_obj.id, media_id, content, parent_id)

        # log warning se non autore/interprete
        if comment_id:
            authors = fetch_relations("song_authors", "song_id", media_id)
            performers = fetch_relations("song_performances", "song_id", media_id)
            is_author = any(a["author_id"] == user_obj.id for a in authors)
            is_performer = any(p["performer_id"] == user_obj.id for p in performers)

            if not (is_author or is_performer):
                log_event(user_obj.username, media_id, "COMMENT", "User commented without being author/performer")

        if comment_id:
            return {"status": "OK", "id": comment_id, "error_msg": None}
        return {"status": "ERROR", "id": None, "error_msg": "FAILED_TO_CREATE"}
    except Exception as e:
        return {"status": "ERROR", "id": None, "error_msg": str(e)}

def get_comments(user_obj: Any, media_id: int, depth: Optional[int] = None) -> List[Dict[str, Any]]:
    flat_comments = Comment.fetch_comments(media_id)
    return build_comment_tree(flat_comments, depth)

def update_comment(user_obj: Any, comment_id: int, new_content: str) -> Dict[str, Any]:
    try:
        success = Comment.update_comment(user_obj.id, comment_id, new_content)
        return {"status": "OK" if success else "ERROR", "id": comment_id, "error_msg": None}
    except PermissionError as e:
        return {"status": "ERROR", "id": comment_id, "error_msg": str(e)}

def delete_comment(user_obj: Any, comment_id: int) -> Dict[str, Any]:
    try:
        success = Comment.delete_comment(user_obj.id, comment_id)
        return {"status": "OK" if success else "ERROR", "id": comment_id, "error_msg": None}
    except PermissionError as e:
        return {"status": "ERROR", "id": comment_id, "error_msg": str(e)}

# =====================
# NOTE
# =====================

def create_note(user_obj: Any, media_id: int, start_time: float, end_time: float, content: str,
                        performers: List[int] = None, instruments: List[int] = None) -> Dict[str, Any]:
    if user_obj.lvl > 4:
        return {"status": "ERROR", "id": None, "error_msg": "PERMISSION_DENIED"}
    try:
        if performers or instruments:
            note_id = Note.add_detailed_note(user_obj.id, media_id, start_time, end_time, content, performers, instruments)
        else:
            note_id = Note.add_note(user_obj.id, media_id, start_time, end_time, content)
        if note_id:
            return {"status": "OK", "id": note_id, "error_msg": None}
        return {"status": "ERROR", "id": None, "error_msg": "FAILED_TO_CREATE"}
    except Exception as e:
        return {"status": "ERROR", "id": None, "error_msg": str(e)}

def get_note(user_obj: Any, media_id: int) -> List[Dict[str, Any]]:
    return Note.fetch_note(media_id)

def update_note(user_obj: Any, note_id: int, new_content: str) -> Dict[str, Any]:
    try:
        success = Note.update_note(note_id, new_content)
        return {"status": "OK" if success else "ERROR", "id": note_id, "error_msg": None}
    except PermissionError as e:
        return {"status": "ERROR", "id": note_id, "error_msg": str(e)}

def delete_note(user_obj: Any, note_id: int) -> Dict[str, Any]:
    try:
        success = Note.delete_note(note_id)
        return {"status": "OK" if success else "ERROR", "id": note_id, "error_msg": None}
    except PermissionError as e:
        return {"status": "ERROR", "id": note_id, "error_msg": str(e)}

# last line