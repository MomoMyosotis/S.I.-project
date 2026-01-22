# first line
from server.objects.comment import Comment
from server.utils.media_utils import (create_dict_entry,
                                fetch_all_dict_entries,
                                delete_dict_entry)
from server.utils.generic_utils import get_commented_medias as fetch_commented_medias, get_media_by_users
from typing import List, Optional, Dict, Any
from server.objects.media import Media
from server.objects.user import User
from datetime import date, datetime
from decimal import Decimal
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

# last line