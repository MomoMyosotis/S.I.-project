# first line
from decimal import Decimal
from datetime import date
from typing import List, Optional, Dict, Any
from server.objects.interventi.comment import Comment
from server.objects.interventi.notes import Note
from server.objects.users.root import Root
from server.objects.media.media import Media
from server.logs.logger import log_event
from server.utils.media_utils import (create_dict_entry,
                                fetch_all_dict_entries,
                                fetch_relations,
                                delete_dict_entry
                                )

# ====================
# HELPER
# ====================
def get_user_id(user_obj: Any) -> Optional[int]:
    """Ritorna l'id dell'utente anche se user_obj è dict o oggetto."""
    if isinstance(user_obj, dict):
        return user_obj.get('id')
    return getattr(user_obj, 'id', None)

# ====================
# GENERIC
# ====================
def search_song(user_obj: Any, **filters) -> List[Dict[str, Any]]:
    return Root.advanced_song_search(filters)

def search_document(user_obj: Any, **filters) -> List[Dict[str, Any]]:
    return Root.advanced_document_search(filters)

def search_video(user_obj: Any, **filters) -> List[Dict[str, Any]]:
    return Root.advanced_video_search(filters)

def add_entry(user_obj: Any, table: str, name: str) -> str:
    entry_id = create_dict_entry(table, name)
    return str(entry_id) if entry_id else "ERROR"

def remove_entry(user_obj: Any, table: str, entry_id: int) -> str:
    success = delete_dict_entry(table, entry_id)
    return "OK" if success else "ERROR"

def get_entries(user_obj: Any, table: str) -> List[Dict[str, Any]]:
    return fetch_all_dict_entries(table)

# ====================
# COMMENT
# ====================
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_comment(user_obj, media_id=None, text=None, parent_comment_id=None, note_id=None, **kwargs):

    # parsing dispatcher dict
    if isinstance(media_id, dict):
        payload = media_id
        media_id = payload.get("media_id")
        text = payload.get("text", text)
        parent_comment_id = payload.get("parent_comment_id", parent_comment_id)
        note_id = payload.get("note_id", note_id)

    # validazione base
    try:
        media_id = int(media_id)
    except (TypeError, ValueError):
        logger.error("Invalid media_id: %s", media_id)
        return {"status": "ERROR", "id": None, "error_msg": "INVALID_MEDIA_ID"}
    if not text:
        logger.error("Text is required, but received: %s", text)
        return {"status": "ERROR", "id": None, "error_msg": "TEXT_REQUIRED"}

    user_id = get_user_id(user_obj)

    media = Media.fetch(media_id)
    if not media:
        logger.error("Media not found with media_id: %s", media_id)
        return {"status": "ERROR", "id": None, "error_msg": "ERR_404_MEDIA_NOT_FOUND"}

    try:
        new_comment = Comment.add_comment(
            user_id=user_id,
            media_id=media_id,
            text=text,
            parent_comment_id=parent_comment_id,
            note_id=note_id
        )
        if not new_comment:
            logger.error("Failed to create comment")
            return {"status": "ERROR", "id": None, "error_msg": "FAIL"}
        # Ricostruisci oggetto completo incluso parent_comment_id
        created_comment = Comment.fetch_by_id(new_comment.id)
        if not created_comment:
            logger.error("Failed to fetch created comment with ID: %s", new_comment.id)
            return {"status": "ERROR", "id": None, "error_msg": "FAILED_TO_FETCH_COMMENT"}
        return {"status": "OK", "id": created_comment.id, "error_msg": None}

    except Exception as e:
        logger.exception("Exception occurred while creating comment")
        return {"status": "ERROR", "id": None, "error_msg": str(e)}

def update_comment(user_obj: Any, comment_id: int, new_text: str) -> Dict[str, Any]:
    """Aggiorna il testo di un commento esistente."""
    user_id = get_user_id(user_obj)
    comment = Comment.fetch_by_id(comment_id)
    if not comment:
        logger.error("Comment not found with comment_id: %s", comment_id)  # Modifica '%d' a '%s'
        return {"status": "ERROR", "id": comment_id, "error_msg": "NOT_FOUND"}

    try:
        updated = Comment.update_comment(user_id=user_id, comment_id=comment_id, new_text=new_text)
        status = "OK" if updated else "ERROR"

        return {"status": status, "id": comment_id, "error_msg": None if updated else "NOT_FOUND"}
    except Exception as e:
        logger.exception("Exception occurred while updating comment")
        return {"status": "ERROR", "id": comment_id, "error_msg": str(e)}

def delete_comment(user_obj: Any, comment_id: int) -> Dict[str, Any]:
    """Elimina un commento esistente."""
    user_id = get_user_id(user_obj)
    comment = Comment.fetch_by_id(comment_id)
    if not comment:
        logger.error("Comment not found with comment_id: %d", comment_id)
        return {"status": "ERROR", "id": comment_id, "error_msg": "NOT_FOUND"}
    try:
        deleted = Comment.delete_comment(user_id=user_id, comment_id=comment_id)
        status = "OK" if deleted else "ERROR"
        return {"status": status, "id": comment_id, "error_msg": None if deleted else "NOT_FOUND"}
    except Exception as e:
        logger.exception("Exception occurred while deleting comment")
        return {"status": "ERROR", "id": comment_id, "error_msg": str(e)}

def get_comments(user_obj: Any, media_id: int) -> List[Dict[str, Any]]:
    """Recupera tutti i commenti di un media."""
    # Recupera i commenti dal database
    comments = Comment.fetch_by_media(media_id)
    # Modifica i commenti per serializzare le date
    for comment in comments:
        if isinstance(comment['created_at'], date):  # Verifica se 'created_at' è una data
            comment['created_at'] = comment['created_at'].strftime('%Y-%m-%d')  # Formatta la data come stringa
    return comments if comments else []

# ====================
# NOTE
# ====================
def create_note(user_obj: Any, media_id=None, note_type="regular",
                start_time: float = None, end_time: float = None,
                x_coord: float = None, y_coord: float = None,
                solos: str = None, rhythm: str = None, content: str = None,
                performers: List[int] = None, instruments: List[int] = None, **kwargs) -> Dict[str, Any]:

    # --- Parsing dispatcher dict ---
    if isinstance(media_id, dict):
        payload = media_id
        media_id = payload.get("media_id")
        note_type = payload.get("note_type", note_type)
        start_time = payload.get("start_time", start_time)
        end_time = payload.get("end_time", end_time)
        x_coord = payload.get("x_coord", x_coord)
        y_coord = payload.get("y_coord", y_coord)
        solos = payload.get("solos", solos)
        rhythm = payload.get("rhythm", rhythm)
        content = payload.get("content", content)
        performers = payload.get("performers", performers)
        instruments = payload.get("instruments", instruments)

    # --- Validazione base ---
    try:
        media_id = int(media_id)
    except (TypeError, ValueError):
        logger.error("Invalid media_id: %s", media_id)
        return {"status": "ERROR", "id": None, "error_msg": "INVALID_MEDIA_ID"}

    if content is None:
        logger.error("Content is required, but received: %s", content)
        return {"status": "ERROR", "id": None, "error_msg": "CONTENT_REQUIRED"}

    user_id = get_user_id(user_obj)
    if not user_id:
        logger.error("Invalid user object: %s", user_obj)
        return {"status": "ERROR", "id": None, "error_msg": "INVALID_USER"}

    user = Root.get_user(user_id)
    if not user:
        logger.error("User not found with id: %s", user_id)
        return {"status": "ERROR", "id": None, "error_msg": "USER_NOT_FOUND"}

    media = Media.fetch(media_id)
    if not media:
        logger.error("Media not found with media_id: %s", media_id)
        return {"status": "ERROR", "id": None, "error_msg": "MEDIA_NOT_FOUND"}

    if start_time is not None and end_time is not None and end_time < start_time:
        logger.error("Invalid time range: start_time=%s, end_time=%s", start_time, end_time)
        return {"status": "ERROR", "id": None, "error_msg": "INVALID_TIME_RANGE"}

    # --- Creazione nota ---
    try:
        note_id = Note.add_detailed_note(
            author=user_id,
            media_id=media.id,
            note_type=note_type,
            start_time=start_time,
            end_time=end_time,
            x_coord=x_coord,
            y_coord=y_coord,
            solos=solos,
            rhythm=rhythm,
            content=content,
            performers=performers,
            instruments=instruments
        )
        if not note_id:
            logger.error("Failed to create note")
            return {"status": "ERROR", "id": None, "error_msg": "FAIL"}

        created_note = Note.fetch_by_id(note_id)
        if not created_note:
            logger.error("Failed to fetch created note with ID: %s", note_id)
            return {"status": "ERROR", "id": None, "error_msg": "FAILED_TO_FETCH_NOTE"}

        return {"status": "OK", "id": created_note.id, "error_msg": None}

    except Exception as e:
        logger.exception("Exception occurred while creating note")
        return {"status": "ERROR", "id": None, "error_msg": str(e)}

def get_notes(user_obj: Any, media_id: int) -> List[Dict[str, Any]]:
    """Recupera tutte le note di un media, serializzando Decimal e date."""
    user_id = get_user_id(user_obj)
    print(f"[DEBUG get_notes] START - user_id={user_id}, media_id={media_id}")

    user = Root.get_user(user_id)
    print(f"[DEBUG get_notes] fetched user: {user}")
    if not user:
        return {"status": "ERROR", "error_msg": "USER_NOT_FOUND"}

    media = Media.fetch(media_id)
    print(f"[DEBUG get_notes] fetched media: {media}")
    if not media:
        return {"status": "ERROR", "error_msg": "MEDIA_NOT_FOUND"}

    try:
        notes = [n.to_dict() for n in Note.fetch_notes(media.id)]
        # Convert Decimal e date in valori JSON serializzabili
        for n in notes:
            if 'x_coord' in n and isinstance(n['x_coord'], Decimal):
                n['x_coord'] = float(n['x_coord'])
            if 'y_coord' in n and isinstance(n['y_coord'], Decimal):
                n['y_coord'] = float(n['y_coord'])
            if 'start_time' in n and isinstance(n['start_time'], Decimal):
                n['start_time'] = float(n['start_time'])
            if 'end_time' in n and isinstance(n['end_time'], Decimal):
                n['end_time'] = float(n['end_time'])
            if 'created_at' in n and isinstance(n['created_at'], date):
                n['created_at'] = n['created_at'].strftime('%Y-%m-%d')
        print(f"[DEBUG get_notes] fetched {len(notes)} notes")
        return notes
    except Exception as e:
        print(f"[DEBUG get_notes] ERROR: {e}")
        return {"status": "ERROR", "error_msg": str(e)}

def update_note(user_obj: Any, note_id: int, new_content: str) -> Dict[str, Any]:
    """Aggiorna il contenuto di una nota esistente."""
    user_id = get_user_id(user_obj)
    print(f"[DEBUG update_note] START - user_id={user_id}, note_id={note_id}")

    user = Root.get_user(user_id)
    if not user:
        return {"status": "ERROR", "error_msg": "USER_NOT_FOUND"}

    note = Note.fetch_by_id(note_id)
    if not note:
        return {"status": "ERROR", "error_msg": "NOTE_NOT_FOUND"}

    try:
        result = Note.update_note(user_id, note_id, new_content)
        status = "OK" if result else "ERROR"
        return {"status": status, "id": note_id, "error_msg": None if result else "UPDATE_FAILED"}
    except Exception as e:
        return {"status": "ERROR", "id": note_id, "error_msg": str(e)}

def delete_note(user_obj: Any, note_id: int) -> Dict[str, Any]:
    """Elimina una nota esistente."""
    user_id = get_user_id(user_obj)
    print(f"[DEBUG delete_note] START - user_id={user_id}, note_id={note_id}")

    user = Root.get_user(user_id)
    if not user:
        return {"status": "ERROR", "error_msg": "USER_NOT_FOUND"}

    note = Note.fetch_by_id(note_id)
    if not note:
        return {"status": "ERROR", "error_msg": "NOTE_NOT_FOUND"}

    try:
        result = Note.delete_note(user_id, note_id)
        status = "OK" if result else "ERROR"
        return {"status": status, "id": note_id, "error_msg": None if result else "DELETE_FAILED"}
    except Exception as e:
        return {"status": "ERROR", "id": note_id, "error_msg": str(e)}

# last line