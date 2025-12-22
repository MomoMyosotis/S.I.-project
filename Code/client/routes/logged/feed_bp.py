# first line

from flask import Blueprint, jsonify, request, session
from client.services.http_helper import http_client
from client.services.feed_service import FeedService
from client.models.media import Media

feed_bp = Blueprint("feed", __name__, url_prefix="/feed")

@feed_bp.route("/data", methods=["GET"])
def feed_data():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    search = (request.args.get("search") or "").strip()
    filter_by = (request.args.get("filter") or "all").lower()
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 10))

    print(f"[DEBUG] Fetching feed: search={search!r}, filter={filter_by}, offset={offset}, limit={limit}")

    # fetch merged feed (media + users when applicable) via FeedService which uses http_helper
    response = FeedService.get_feed(search, filter_by, offset, limit)

    # handle error envelope
    if isinstance(response, dict) and response.get("status") and str(response.get("status")).lower() not in ("ok", "true"):
        err = response.get("error_msg", "Unknown error")
        print(f"[ERROR] feed_data failed during fetch: {err}")
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

    # Normalize each item via Media model where appropriate
    normalized_batch = []
    for it in batch:
        try:
            if not isinstance(it, dict):
                continue
            # build Media model from server-provided item (tolerant)
            if it.get("type") == "user":
                # user card already shaped by FeedService; keep it as-is
                normalized_batch.append({
                    "id": it.get("id"),
                    "title": it.get("title") or it.get("username"),
                    "username": it.get("username"),
                    "thumbnail": it.get("thumbnail") or "/static/images/no pp.jpg",
                    "tags": it.get("tags") or [],
                    "type": "user",
                    "raw": it
                })
                continue

            m = Media.from_server(it)
            md = m.to_dict()
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
                "raw": md
            })
        except Exception as e:
            print(f"[DEBUG] feed item normalization failed: {e}")
            normalized_batch.append({
                "id": it.get("id") or it.get("media_id"),
                "title": it.get("title") or it.get("name") or "Untitled",
                "username": it.get("username"),
                "thumbnail": it.get("thumbnail") or "/static/images/unknown.jpg",
                "tags": it.get("tags") or [],
                "type": it.get("type") or it.get("media_type") or "unknown",
                "raw": it
            })

    # filter locally and return paged slice
    def matches(item, term, f):
        if not term:
            return True
        t = term.lower()
        def contains(val):
            return bool(val) and t in str(val).lower()
        tags = item.get("tags") or []
        if f in ("all",):
            if contains(item.get("title")) or contains(item.get("username")) or contains(item.get("author")):
                return True
            if contains(item.get("file")) or contains(item.get("filename")) or contains(item.get("link")):
                return True
            for tag in tags:
                if contains(tag):
                    return True
            return False
        if f == "user" or f == "author":
            return contains(item.get("username")) or contains(item.get("author"))
        if f == "title":
            return contains(item.get("title"))
        if f == "tag":
            for tag in tags:
                if contains(tag):
                    return True
            return False
        if f == "file":
            return contains(item.get("file")) or contains(item.get("filename")) or contains(item.get("link"))
        return contains(item.get("title")) or contains(item.get("username"))

    accumulated = []
    for it in normalized_batch:
        if matches(it, search, filter_by):
            accumulated.append(it)

    sliced = accumulated[:limit]
    return jsonify(sliced)

# last line