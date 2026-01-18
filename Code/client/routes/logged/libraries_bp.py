# first line

from flask import Blueprint, jsonify, request, session
from client.services.http_helper import http_client
from client.services.library_service import LibraryService
from client.models.media import Media

libraries_bp = Blueprint('library', __name__, url_prefix="/library")

@libraries_bp.route('/commented_media', methods=['GET'])
def get_commented_media():
    """Fetch media items that the user has commented on with pagination."""
    if http_client.token is None:
        http_client.token = session.get("session_token")

    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 10))

    print(f"[DEBUG] Fetching commented media: offset={offset}, limit={limit}")

    response = LibraryService.get_commented_media(offset, limit)

    # handle error envelope
    if isinstance(response, dict) and response.get("status") and str(response.get("status")).lower() not in ("ok", "true"):
        err = response.get("error_msg", "Unknown error")
        print(f"[ERROR] get_commented_media failed during fetch: {err}")
        return jsonify({"error": err}), 400

    # extract batch robustly
    batch = []
    if isinstance(response, dict):
        if "results" in response and isinstance(response["results"], list):
            batch = response["results"]
        elif "response" in response:
            r = response["response"]
            if isinstance(r, dict) and "results" in r and isinstance(r["results"], list):
                batch = r["results"]
            elif isinstance(r, list):
                batch = r
        elif isinstance(response.get("response"), list):
            batch = response.get("response")
    elif isinstance(response, list):
        batch = response

    batch = batch or []

    # Normalize each item via Media model
    normalized_batch = []
    for it in batch:
        try:
            if not isinstance(it, dict):
                continue
            m = Media.from_server(it)
            md = m.to_dict()
            # preserve server-side created_at so client-side date filters work
            md["created_at"] = it.get("created_at") or it.get("createdAt") or md.get("created_at")
            username = it.get("username") or it.get("owner") or it.get("uploader") or md.get("uploader_id")
            tags = it.get("tags") or md.get("tags") or it.get("genre") or []
            thumbnail = it.get("thumbnail") or it.get("thumb") or "/static/images/unknown.jpg"
            normalized_batch.append({
                "id": md.get("id") or it.get("id") or it.get("media_id"),
                "title": md.get("title") or it.get("title") or "Untitled",
                "username": username,
                "thumbnail": thumbnail,
                "tags": tags,
                "type": md.get("type") or it.get("type") or it.get("media_type") or it.get("file_type") or "unknown",
                "created_at": md.get("created_at"),
                "raw": md
            })
        except Exception as e:
            print(f"[DEBUG] media item normalization failed: {e}")
            normalized_batch.append({
                "id": it.get("id") or it.get("media_id"),
                "title": it.get("title") or it.get("name") or "Untitled",
                "username": it.get("username"),
                "thumbnail": it.get("thumbnail") or "/static/images/unknown.jpg",
                "tags": it.get("tags") or [],
                "type": it.get("type") or it.get("media_type") or "unknown",
                "raw": it
            })

    return jsonify(normalized_batch)

@libraries_bp.route('/followed_media', methods=['GET'])
def get_followed_media():
    """Fetch media items from users that the user follows with pagination."""
    if http_client.token is None:
        http_client.token = session.get("session_token")

    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 10))

    print(f"[DEBUG] Fetching followed media: offset={offset}, limit={limit}")

    response = LibraryService.get_followed_media(offset, limit)

    # handle error envelope
    if isinstance(response, dict) and response.get("status") and str(response.get("status")).lower() not in ("ok", "true"):
        err = response.get("error_msg", "Unknown error")
        print(f"[ERROR] get_followed_media failed during fetch: {err}")
        return jsonify({"error": err}), 400

    # extract batch robustly
    batch = []
    if isinstance(response, dict):
        if "results" in response and isinstance(response["results"], list):
            batch = response["results"]
        elif "response" in response:
            r = response["response"]
            if isinstance(r, dict) and "results" in r and isinstance(r["results"], list):
                batch = r["results"]
            elif isinstance(r, list):
                batch = r
        elif isinstance(response.get("response"), list):
            batch = response.get("response")
    elif isinstance(response, list):
        batch = response

    batch = batch or []

    # Normalize each item via Media model
    normalized_batch = []
    for it in batch:
        try:
            if not isinstance(it, dict):
                continue
            m = Media.from_server(it)
            md = m.to_dict()
            # preserve server-side created_at so client-side date filters work
            md["created_at"] = it.get("created_at") or it.get("createdAt") or md.get("created_at")
            username = it.get("username") or it.get("owner") or it.get("uploader") or md.get("uploader_id")
            tags = it.get("tags") or md.get("tags") or it.get("genre") or []
            thumbnail = it.get("thumbnail") or it.get("thumb") or "/static/images/unknown.jpg"
            normalized_batch.append({
                "id": md.get("id") or it.get("id") or it.get("media_id"),
                "title": md.get("title") or it.get("title") or "Untitled",
                "username": username,
                "thumbnail": thumbnail,
                "tags": tags,
                "type": md.get("type") or it.get("type") or it.get("media_type") or it.get("file_type") or "unknown",
                "created_at": md.get("created_at"),
                "raw": md
            })
        except Exception as e:
            print(f"[DEBUG] media item normalization failed: {e}")
            normalized_batch.append({
                "id": it.get("id") or it.get("media_id"),
                "title": it.get("title") or it.get("name") or "Untitled",
                "username": it.get("username"),
                "thumbnail": it.get("thumbnail") or "/static/images/unknown.jpg",
                "tags": it.get("tags") or [],
                "type": it.get("type") or it.get("media_type") or "unknown",
                "raw": it
            })

    return jsonify(normalized_batch)

# last line