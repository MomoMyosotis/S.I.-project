# first line
from server.objects.interventi.comment import Comment
from server.utils.media_utils import (create_dict_entry,
                                fetch_all_dict_entries,
                                delete_dict_entry)
from server.objects.interventi.notes import Note
from typing import List, Optional, Dict, Any
from server.objects.media.media import Media
from server.objects.users.root import Root
from decimal import Decimal
from datetime import date, datetime
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# ====================
# HELPER
# ====================
def get_user_id(user_obj: Any) -> Optional[int]:
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

    comments = Comment.fetch_by_media(media_id) or []
    logger.debug("[get_comments] fetched %d raw comments for media_id=%s", len(comments), media_id)

    avatar_keys = ['avatar','avatar_url','profile_pic','picture','image','photo','gravatar','profile_image']
    enriched = []
    for comment in comments:
        # make created_at JSON serializable and preserve time when available
        ca = comment.get('created_at')
        if ca is not None:
            if isinstance(ca, datetime):
                comment['created_at'] = ca.isoformat()
            elif isinstance(ca, date):
                # date only (no time) -> keep ISO date string
                comment['created_at'] = ca.isoformat()
            else:
                comment['created_at'] = str(ca)

        # determine best username/display_name and avatar
        try:
            uid = comment.get('user_id')
            username = comment.get('username') or comment.get('author_username') or None
            avatar = None

            # if we have a user_id, prefer authoritative lookup
            if uid is not None:
                user = Root.get_user(uid)
                logger.debug("[get_comments] lookup user for user_id=%s -> %r", uid, user)
                if user:
                    if isinstance(user, dict):
                        username = user.get('username') or username
                        for k in avatar_keys:
                            if not avatar and user.get(k):
                                avatar = user.get(k)
                    else:
                        username = getattr(user, 'username', None) or username
                        for k in avatar_keys:
                            if not avatar and getattr(user, k, None):
                                avatar = getattr(user, k, None)

            # display_name fallback logic (preserve legacy fields)
            display_name = username or comment.get('author') or comment.get('name') or 'Anonimo'

            # canonicalize onto comment
            comment['username'] = username  # may be None when unknown
            comment['display_name'] = display_name
            comment['user'] = {'id': uid, 'username': username, 'avatar': avatar}
            if avatar:
                comment['avatar'] = avatar
            # normalize identifier fields for client compatibility
            cid = comment.get('id') or comment.get('comment_id') or None
            parent_val = comment.get('parent_comment_id') or comment.get('parent') or comment.get('parent_id') or comment.get('reply_to') or None
            comment['comment_id'] = cid
            # keep the canonical naming triplet so various clients/legacy UIs can find it
            comment['parent_comment_id'] = parent_val
            comment['parent'] = parent_val
            comment['parent_id'] = parent_val
            logger.debug("[get_comments] normalized ids for comment %r -> comment_id=%r parent=%r", cid, cid, parent_val)
        except Exception as e:
            logger.exception("Failed to enrich comment with user info: %s", e)

        enriched.append(comment)

    logger.debug("[get_comments] returning %d enriched comments for media_id=%s", len(enriched), media_id)
    return enriched

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
            # preserve full timestamp when available
            ca = n.get('created_at')
            if ca is not None:
                if isinstance(ca, datetime):
                    n['created_at'] = ca.isoformat()
                elif isinstance(ca, date):
                    n['created_at'] = ca.isoformat()
                else:
                    n['created_at'] = str(ca)
        print(f"[DEBUG get_notes] fetched {len(notes)} notes")
        return notes
    except Exception as e:
        print(f"[DEBUG get_notes] ERROR: {e}")
        return {"status": "ERROR", "error_msg": str(e)}

def update_note(user_obj: Any, note_id: int, new_content: str) -> Dict[str, Any]:
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