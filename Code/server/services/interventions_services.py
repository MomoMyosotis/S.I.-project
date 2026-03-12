# first line
from server.objects.comment import Comment
from server.utils.media_utils import (create_dict_entry,
                                fetch_all_dict_entries,
                                delete_dict_entry)
from server.utils.generic_utils import get_commented_medias as fetch_commented_medias, get_media_by_users
from typing import List, Optional, Dict, Any
from server.objects.media import Media
from server.objects.note import Note
from server.objects.user import User
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
    return User.advanced_song_search(filters)

def search_document(user_obj: Any, **filters) -> List[Dict[str, Any]]:
    return User.advanced_document_search(filters)

def search_video(user_obj: Any, **filters) -> List[Dict[str, Any]]:
    return User.advanced_video_search(filters)

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

def create_comment(user_obj, media_id=None, text=None, parent_comment_id=None, **kwargs):

    # parsing dispatcher dict
    if isinstance(media_id, dict):
        payload = media_id
        media_id = payload.get("media_id")
        text = payload.get("text", text)
        parent_comment_id = payload.get("parent_comment_id", parent_comment_id)

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
            parent_comment_id=parent_comment_id
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
        logger.error("Comment not found with comment_id: %s", comment_id)
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
                user = User.get_user(uid)
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
            # include commenter id/username/avatar and try to expose their numeric level when available
            commenter_lvl = None
            try:
                if uid is not None and user:
                    # user may be dict or object
                    if isinstance(user, dict):
                        commenter_lvl = user.get('lvl') or user.get('level') or None
                    else:
                        commenter_lvl = getattr(user, 'lvl', None)
                        # if it's an Enum-like, try to get numeric value
                        if commenter_lvl is not None and not isinstance(commenter_lvl, int):
                            commenter_lvl = getattr(commenter_lvl, 'value', commenter_lvl)
                    if commenter_lvl is not None:
                        try:
                            commenter_lvl = int(commenter_lvl)
                        except Exception:
                            pass
            except Exception:
                commenter_lvl = None

            comment['user'] = {'id': uid, 'username': username, 'avatar': avatar, 'lvl': commenter_lvl}
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

def get_commented_medias(user_obj: Any) -> List[Dict[str, Any]]:
    user_id = get_user_id(user_obj)
    logger.debug("[get_commented_medias] START - user_id=%s", user_id)

    if not user_id:
        logger.error("Invalid user object: %s", user_obj)
        return {"status": "ERROR", "error_msg": "INVALID_USER"}

    user = User.get_user(user_id)
    if not user:
        logger.error("User not found with id: %s", user_id)
        return {"status": "ERROR", "error_msg": "USER_NOT_FOUND"}

    try:
        medias = fetch_commented_medias(user_id)
        logger.debug("[get_commented_medias] fetched %d medias", len(medias))
        return medias
    except Exception as e:
        logger.exception("Exception occurred while fetching commented medias")
        return {"status": "ERROR", "error_msg": str(e)}

def get_commented_media_paginated(user_obj: Any, offset: int = 0, limit: int = 10) -> Dict[str, Any]:
    """
    Fetch media items that the user has commented on, with pagination support.
    """
    user_id = get_user_id(user_obj)
    logger.debug("[get_commented_media_paginated] START - user_id=%s, offset=%s, limit=%s", user_id, offset, limit)

    if not user_id:
        return {"status": "ERROR", "error_msg": "INVALID_USER"}

    try:
        # Fetch all commented media for the user
        all_medias = fetch_commented_medias(user_id)
        
        # Handle both list and dict responses
        if isinstance(all_medias, dict):
            if all_medias.get("status") and str(all_medias.get("status")).lower() not in ("ok", "true"):
                return all_medias
            medias = all_medias.get("results", all_medias.get("response", []))
        else:
            medias = all_medias if isinstance(all_medias, list) else []
        
        # Apply pagination
        total = len(medias)
        paginated = medias[offset:offset + limit]
        
        logger.debug("[get_commented_media_paginated] returning %d medias (total=%d)", len(paginated), total)
        return {
            "status": "OK",
            "results": paginated,
            "count": len(paginated),
            "total": total,
            "offset": offset,
            "limit": limit
        }
    except Exception as e:
        logger.exception("Exception occurred while fetching commented media paginated")
        return {"status": "ERROR", "error_msg": str(e)}

def get_followed_media_paginated(user_obj: Any, offset: int = 0, limit: int = 10) -> Dict[str, Any]:
    """
    Fetch media items from users that the user follows, with pagination support.
    """
    user_id = get_user_id(user_obj)
    logger.debug("[get_followed_media_paginated] START - user_id=%s, offset=%s, limit=%s", user_id, offset, limit)

    if not user_id:
        return {"status": "ERROR", "error_msg": "INVALID_USER"}

    try:
        # Get list of followed users
        from server.db.db_crud import db_get_following
        followed_users = db_get_following(user_id)
        followed_ids = [u.get("id") if isinstance(u, dict) else getattr(u, "id", None) for u in followed_users]
        
        logger.debug("[get_followed_media_paginated] user follows %d users: %s", len(followed_ids), followed_ids)
        
        if not followed_ids:
            logger.debug("[get_followed_media_paginated] No followed users")
            return {"status": "OK", "results": [], "count": 0, "total": 0, "offset": offset, "limit": limit}
        
        # Fetch all media from followed users using utility function
        all_medias = get_media_by_users(followed_ids)
        
        logger.debug("[get_followed_media_paginated] fetched %d total medias from followed users", len(all_medias))
        
        # Apply pagination
        total = len(all_medias)
        paginated = all_medias[offset:offset + limit]
        
        logger.debug("[get_followed_media_paginated] returning %d medias (total=%d)", len(paginated), total)
        return {
            "status": "OK",
            "results": paginated,
            "count": len(paginated),
            "total": total,
            "offset": offset,
            "limit": limit
        }
    except Exception as e:
        logger.exception("Exception occurred while fetching followed media paginated")
        return {"status": "ERROR", "error_msg": str(e)}

# ====================
# NOTE
# ====================
def create_note(user_obj, media_id=None, start=None, end=None, type=None, text=None, stored_at=None, private=False, page=None, A_point=None, B_point=None, **kwargs):

    # parsing dispatcher dict
    if isinstance(media_id, dict):
        payload = media_id
        media_id = payload.get("media_id")
        start = payload.get("start", start)
        end = payload.get("end", end)
        type = payload.get("type", type)
        text = payload.get("text", text)
        stored_at = payload.get("stored_at", stored_at)
        private = payload.get("private", private)
        page = payload.get("page", page)
        A_point = payload.get("A_point", A_point)
        B_point = payload.get("B_point", B_point)

    # validazione base
    try:
        media_id = int(media_id)
    except (TypeError, ValueError):
        logger.error("Invalid media_id: %s", media_id)
        return {"status": "ERROR", "id": None, "error_msg": "INVALID_MEDIA_ID"}
    if type is None:
        logger.error("Type is required, but received: %s", type)
        return {"status": "ERROR", "id": None, "error_msg": "TYPE_REQUIRED"}

    user_id = get_user_id(user_obj)

    # permission: only logged users with lvl < 5 can make a note
    try:
        user_row = User.get_user(user_id) if user_id else None
        lvl = None
        if isinstance(user_row, dict):
            lvl = user_row.get('lvl')
        # coerce to int when possible
        try:
            lvl = int(lvl) if lvl is not None else None
        except Exception:
            pass
        if lvl is None or lvl >= 5:
            logger.error("User not allowed to create note: lvl=%s", lvl)
            return {"status": "ERROR", "id": None, "error_msg": "PERMISSION_DENIED"}
    except Exception:
        logger.exception("Failed to resolve user or level for permission check")
        return {"status": "ERROR", "id": None, "error_msg": "PERMISSION_CHECK_FAILED"}

    media = Media.fetch(media_id)
    if not media:
        logger.error("Media not found with media_id: %s", media_id)
        return {"status": "ERROR", "id": None, "error_msg": "ERR_404_MEDIA_NOT_FOUND"}

    # If media is a document, normalize start/end to 0 and embed spatial anchor into text when provided
    try:
        media_type = getattr(media, 'type', None) if media else None
        if media_type == 'document':
            start = 0
            end = 0
            anchor = kwargs.get('anchor') if isinstance(kwargs, dict) else None
            if anchor:
                try:
                    import json as _json
                    parsed = {}
                    if text:
                        try:
                            parsed = _json.loads(text)
                            if not isinstance(parsed, dict):
                                parsed = {'raw_text': str(text)}
                        except Exception:
                            parsed = {'raw_text': str(text)}
                    parsed['anchor'] = anchor
                    text = _json.dumps(parsed)
                except Exception:
                    pass
    except Exception:
        pass

    try:
        # create DB entry first (stored_at may be updated after file save)
        new_note = Note.create_note(user_id=user_id, media_id=media_id, start=start, end=end, type=type, text=text, stored_at=None, private=private, page=page, A_point=A_point, B_point=B_point)
        if not new_note:
            logger.error("Failed to create note")
            return {"status": "ERROR", "id": None, "error_msg": "FAIL"}

        note_id = new_note.id

        # If graphic note (type == 0 or False) and stored_at contains file content, save it under server/storage/notes/<note_id>
        if (str(type) in ("0", "False", "false") ) or (isinstance(type, (int, bool)) and int(type) == 0):
            content = None
            # bytes provided directly
            if isinstance(stored_at, (bytes, bytearray)):
                content = bytes(stored_at)
            elif isinstance(stored_at, str):
                # data URI base64
                if stored_at.startswith('data:') and ';base64,' in stored_at:
                    try:
                        import base64
                        b64 = stored_at.split(';base64,', 1)[1]
                        content = base64.b64decode(b64)
                    except Exception:
                        content = None
                else:
                    # maybe a filesystem path
                    try:
                        import os
                        if os.path.isfile(stored_at):
                            with open(stored_at, 'rb') as f:
                                content = f.read()
                    except Exception:
                        content = None

            if content:
                try:
                    from server.utils.storage_manager import save_file
                    # save under notes folder with filename equal to note id (no extension)
                    save_file('notes', str(note_id), content)
                    stored_path = f"server/storage/notes/{note_id}"
                    # update DB stored_at
                    Note.update_note(note_id, stored_at=stored_path)
                    return {"status": "OK", "id": note_id, "error_msg": None}
                except Exception as e:
                    logger.exception("Failed to save note image: %s", e)
                    return {"status": "ERROR", "id": note_id, "error_msg": "FILE_SAVE_FAILED"}
            else:
                # no content provided; return created note id but indicate missing file
                return {"status": "OK", "id": note_id, "error_msg": "NO_FILE_CONTENT"}

        # non-graphic notes
        return {"status": "OK", "id": note_id, "error_msg": None}

    except Exception as e:
        logger.exception("Exception occurred while creating note")
        return {"status": "ERROR", "id": None, "error_msg": str(e)}

def get_notes(user_obj: Any, media_id: int) -> Dict[str, Any]:
    """Fetch all notes for a media and apply visibility rules.

    Visibility rules:
      - public notes (private == False) are always returned
      - private notes returned only if viewer is the note owner OR viewer lvl < 2
    """
    try:
        media_id = int(media_id)
    except (TypeError, ValueError):
        logger.error("Invalid media_id: %s", media_id)
        return {"status": "ERROR", "notes": [], "error_msg": "INVALID_MEDIA_ID"}

    try:
        rows = Note.fetch_by_media(media_id)
        
        notes = []
        for row in (rows or []):
            note_dict = {
                "id": row.get("id"),
                "user_id": row.get("user_id"),
                "media_id": row.get("media_id"),
                "note_start": row.get("note_start"),
                "note_end": row.get("note_end"),
                "type": row.get("type"),
                "text": row.get("text"),
                "stored_at": row.get("stored_at"),
                "private": row.get("private"),
                "created_at": row.get("created_at"),
                "page": row.get("page"),
                "A_point": row.get("A_point"),
                "B_point": row.get("B_point")
            }
            notes.append(note_dict)

        # Determine viewer info
        viewer_id = get_user_id(user_obj)
        viewer_lvl = None
        try:
            if isinstance(user_obj, dict):
                viewer_lvl = user_obj.get('lvl') if user_obj.get('lvl') is not None else user_obj.get('level')
            else:
                viewer_lvl = getattr(user_obj, 'lvl', None)
            if viewer_lvl is not None:
                viewer_lvl = int(viewer_lvl)
        except Exception:
            viewer_lvl = None

        # Apply visibility rules
        visible = []
        for n in notes:
            try:
                if not n.get('private'):
                    visible.append(n); continue
                # private: only owner OR viewer lvl < 2
                if viewer_id is not None and str(viewer_id) == str(n.get('user_id')):
                    visible.append(n); continue
                if viewer_lvl is not None and viewer_lvl < 2:
                    visible.append(n); continue
            except Exception:
                continue

        # Enrich visible notes with user info (username) and normalize timestamps
        for n in visible:
            try:
                # normalize created_at to ISO string when possible
                ca = n.get('created_at')
                if ca is not None:
                    if isinstance(ca, datetime):
                        n['created_at'] = ca.isoformat()
                    elif isinstance(ca, date):
                        n['created_at'] = ca.isoformat()
                    else:
                        n['created_at'] = str(ca)

                # fetch user info when available
                uid = n.get('user_id')
                username = None
                user_obj = None
                if uid is not None:
                    try:
                        user_obj = User.get_user(uid)
                        if user_obj:
                            if isinstance(user_obj, dict):
                                username = user_obj.get('username')
                            else:
                                username = getattr(user_obj, 'username', None)
                    except Exception:
                        username = None

                n['username'] = username
                n['user'] = {'id': uid, 'username': username}
            except Exception:
                # ignore enrichment errors for individual notes
                pass

        logger.debug("[get_notes] fetched %d notes for media_id=%s (visible=%d)", len(notes), media_id, len(visible))
        return {"status": "OK", "notes": visible, "error_msg": None}
    except Exception as e:
        logger.exception("[get_notes] Exception occurred while fetching notes")
        return {"status": "ERROR", "notes": [], "error_msg": str(e)}

def update_note(user_obj: Any, note_id: int, **kwargs) -> Dict[str, Any]:
    """Update a note (only provided fields are updated)."""
    try:
        note_id = int(note_id)
    except (TypeError, ValueError):
        logger.error("Invalid note_id: %s", note_id)
        return {"status": "ERROR", "id": note_id, "error_msg": "INVALID_NOTE_ID"}

    try:
        note_row = Note.fetch_by_id(note_id)
        if not note_row:
            logger.error("Note not found with note_id: %s", note_id)
            return {"status": "ERROR", "id": note_id, "error_msg": "NOT_FOUND"}

        # Call Note.update_note which handles dynamic updates
        success = Note.update_note(note_id, **kwargs)
        if success:
            logger.debug("[update_note] updated note_id=%s with kwargs=%s", note_id, kwargs)
            return {"status": "OK", "id": note_id, "error_msg": None}
        else:
            logger.error("[update_note] failed to update note_id=%s", note_id)
            return {"status": "ERROR", "id": note_id, "error_msg": "UPDATE_FAILED"}
    except Exception as e:
        logger.exception("[update_note] Exception occurred while updating note")
        return {"status": "ERROR", "id": note_id, "error_msg": str(e)}

def delete_note(user_obj: Any, note_id: int) -> Dict[str, Any]:
    """Delete a note by id. Permission required: viewer must be the note owner AND have lvl < 2."""
    try:
        note_id = int(note_id)
    except (TypeError, ValueError):
        logger.error("Invalid note_id: %s", note_id)
        return {"status": "ERROR", "id": note_id, "error_msg": "INVALID_NOTE_ID"}

    try:
        note_row = Note.fetch_by_id(note_id)
        if not note_row:
            logger.error("Note not found with note_id: %s", note_id)
            return {"status": "ERROR", "id": note_id, "error_msg": "NOT_FOUND"}

        owner_id = note_row.get('user_id')
        viewer_id = get_user_id(user_obj)
        viewer_lvl = None
        try:
            if isinstance(user_obj, dict):
                viewer_lvl = user_obj.get('lvl') if user_obj.get('lvl') is not None else user_obj.get('level')
            else:
                viewer_lvl = getattr(user_obj, 'lvl', None)
            if viewer_lvl is not None:
                viewer_lvl = int(viewer_lvl)
        except Exception:
            viewer_lvl = None

        # Permission enforcement: allow deletion if viewer is the owner OR viewer lvl < 2
        allowed = False
        try:
            # owner may delete their own note regardless of level
            if viewer_id is not None and owner_id is not None and str(viewer_id) == str(owner_id):
                allowed = True
            # users with lvl < 2 (admins/mod) may delete any note
            if viewer_lvl is not None and viewer_lvl < 2:
                allowed = True
        except Exception:
            allowed = False

        if not allowed:
            logger.warning("[delete_note] forbidden delete attempt note_id=%s by viewer_id=%s lvl=%s", note_id, viewer_id, viewer_lvl)
            return {"status": "ERROR", "id": note_id, "error_msg": "FORBIDDEN"}

        # If note has a stored_at path, try to delete the file
        stored_at = note_row.get("stored_at")
        if stored_at and stored_at.startswith("server/storage/notes/"):
            try:
                from server.utils.storage_manager import delete_file
                delete_file("notes", str(note_id))
            except Exception as e:
                logger.warning("[delete_note] Failed to delete stored file for note_id=%s: %s", note_id, e)

        # Delete from DB
        success = Note.delete_note(note_id)
        if success:
            logger.debug("[delete_note] deleted note_id=%s", note_id)
            return {"status": "OK", "id": note_id, "error_msg": None}
        else:
            logger.error("[delete_note] failed to delete note_id=%s", note_id)
            return {"status": "ERROR", "id": note_id, "error_msg": "DELETE_FAILED"}
    except Exception as e:
        logger.exception("[delete_note] Exception occurred while deleting note")
        return {"status": "ERROR", "id": note_id, "error_msg": str(e)}

# last line