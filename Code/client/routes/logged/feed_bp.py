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

    #print(f"[DEBUG] Fetching feed: search={search!r}, filter={filter_by}, offset={offset}, limit={limit}")

    # fetch merged feed (media + users when applicable) via FeedService which uses http_helper
    response = FeedService.get_feed(search, filter_by, offset, limit)

    # handle error envelope
    if isinstance(response, dict) and response.get("status") and str(response.get("status")).lower() not in ("ok", "true"):
        err = response.get("error_msg", "Unknown error")
        #print(f"[ERROR] feed_data failed during fetch: {err}")
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
            # preserve server-side created_at so client-side date filters work
            md["created_at"] = it.get("created_at") or it.get("createdAt") or md.get("created_at")
            # sanitize raw before exposing to client
            md_sanit = Media.sanitize_for_client(md)
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
                "raw": md_sanit
            })
        except Exception as e:
            #print(f"[DEBUG] feed item normalization failed: {e}")
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
        # support comma-separated multi-terms
        terms = [p.strip() for p in str(term).split(',') if p.strip()]
        def contains_any(val, ts):
            if not val:
                return False
            s = str(val).lower()
            return any(t.lower() in s for t in ts)
        def contains_all_in_tags(tags_list, ts):
            # each search token must match at least one tag
            if not tags_list:
                return False
            lowered = [str(t).lower() for t in tags_list]
            for t in ts:
                found = False
                for tag in lowered:
                    if t.lower() in tag:
                        found = True
                        break
                if not found:
                    return False
            return True

        tags = item.get("tags") or []

        # Broad 'all' behaviour: check title, username, author, file and tags
        if f in ("all",):
            if contains_any(item.get("title"), terms) or contains_any(item.get("username"), terms) or contains_any(item.get("author"), terms):
                return True
            if contains_any(item.get("file"), terms) or contains_any(item.get("filename"), terms) or contains_any(item.get("link"), terms):
                return True
            # for tags: if user provided multiple terms, require all present; otherwise any
            if len(terms) > 1:
                return contains_all_in_tags(tags, terms)
            else:
                for tag in tags:
                    if contains_any(tag, terms):
                        return True
            return False

        # User filter: only match user-type feed items (avoid showing user's media)
        if f == "user":
            if item.get("type") != "user":
                return False
            # multiple usernames -> return user matches for ANY of them (show both users)
            return contains_any(item.get("username"), terms)

        # Author filter: match author fields in media or username
        if f == "author":
            # multiple author terms -> all must be present (match both authors)
            if len(terms) > 1:
                for t in terms:
                    if not (contains_any(item.get("author"), [t]) or contains_any(item.get("username"), [t])):
                        return False
                return True
            return contains_any(item.get("author"), terms) or contains_any(item.get("username"), terms)

        # Title filter
        if f == "title":
            return contains_any(item.get("title"), terms)

        # Tag filter
        if f == "tag":
            # require ALL provided tag terms to be present in the item's tags
            if len(terms) > 1:
                return contains_all_in_tags(tags, terms)
            for tag in tags:
                if contains_any(tag, terms):
                    return True
            return False

        # File filter
        if f == "file":
            return contains_any(item.get("file"), terms) or contains_any(item.get("filename"), terms) or contains_any(item.get("link"), terms)

        # Publisher filter: match uploader/publisher username or id
        if f == "publisher":
            # if any username matches, accept
            if contains_any(item.get("username"), terms):
                return True
            raw = item.get("raw") or {}
            return contains_any(raw.get("user_id"), terms) or contains_any(raw.get("username"), terms) or contains_any(raw.get("uploader"), terms)

        # Date filter: match published/created date string (accept YYYY or YYYY-MM or full date)
        if f == "date":
            raw = item.get("raw") or {}
            created = raw.get("created_at") or item.get("created_at")
            # if multiple date terms passed, accept any of them (match any provided date)
            return contains_any(created, terms)

        # Fallback: match title or username
        return contains_any(item.get("title"), terms) or contains_any(item.get("username"), terms)

    accumulated = []
    for it in normalized_batch:
        if matches(it, search, filter_by):
            accumulated.append(it)

    sliced = accumulated[:limit]
    return jsonify(sliced)

# last line