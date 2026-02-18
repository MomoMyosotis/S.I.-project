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

    # If the composed-query was placed in the URL without encoding, the semicolon
    # may be interpreted as a separator by the HTTP parser (e.g. ?search=tag:pop;date:2025).
    # Rebuild the full composed-query from recognized query params so the server
    # always receives the complete `search` string.
    if filter_by == 'composed_query':
        composed_keys = ['date', 'date_from', 'date_to', 'tag', 'genre', 'author', 'performer', 'instrument', 'user', 'username', 'title', 'publisher_only', 'from', 'to']
        extras = []
        for k in composed_keys:
            v = request.args.get(k)
            if v:
                # avoid duplicating if already present in the provided search string
                if f"{k}:" not in search:
                    extras.append(f"{k}:{v}")
        if extras:
            search = (search + ';' + ';'.join(extras)) if search else ';'.join(extras)

    print(f"[DEBUG][feed_bp] Fetching feed: search={search!r}, filter={filter_by}, offset={offset}, limit={limit}")

    # fetch merged feed (media + users when applicable) via FeedService which uses http_helper
    response = FeedService.get_feed(search, filter_by, offset, limit)
    # Debug: inspect raw response envelope (log server error message when available)
    try:
        if isinstance(response, dict):
            keys = list(response.keys())
            if response.get("status") and str(response.get("status")).lower() not in ("ok", "true"):
                print(f"[DEBUG][feed_bp] Server error response: {response.get('error_msg') or response.get('response')}")
            else:
                print(f"[DEBUG][feed_bp] Server response keys={keys} ")
                if isinstance(response.get('results'), list):
                    print(f"[DEBUG][feed_bp] results_count={len(response.get('results'))}")
        elif isinstance(response, list):
            print(f"[DEBUG][feed_bp] Server returned list, len={len(response)}")
        else:
            print(f"[DEBUG][feed_bp] Server returned unexpected type: {type(response)}")
    except Exception as e:
        print(f"[DEBUG][feed_bp] Error inspecting response: {e}")

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

        # Broad 'all' behaviour: require ALL provided tokens to match somewhere in the
        # same item (each token may match any searchable field). This fixes cases like
        # "2025, pop" (year matches created_at/year and genre matches tags).
        if f in ("all",):
            raw = item.get("raw") or {}

            def term_matches_single(t):
                # text fields
                if contains_any(item.get("title"), [t]) or contains_any(item.get("description"), [t]) or contains_any(item.get("username"), [t]) or contains_any(item.get("author"), [t]):
                    return True
                # file/links
                if contains_any(item.get("file"), [t]) or contains_any(item.get("filename"), [t]) or contains_any(item.get("link"), [t]):
                    return True
                # tags
                for tag in tags:
                    if t.lower() in str(tag).lower():
                        return True
                # numeric-year / created_at matching (accept YYYY)
                if len(t) == 4 and t.isdigit():
                    # check explicit year field first
                    if str(raw.get("year") or "") == t:
                        return True
                    # check created_at string (ISO or textual)
                    created = raw.get("created_at") or ""
                    try:
                        if isinstance(created, str) and created.startswith(t):
                            return True
                        if hasattr(created, "isoformat") and created.isoformat().startswith(t):
                            return True
                        if t in str(created):
                            return True
                    except Exception:
                        pass
                return False

            # ALL tokens must be satisfied somewhere in the item (AND across tokens)
            for tok in terms:
                if not term_matches_single(tok):
                    return False
            return True

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
            # require ALL provided title tokens to be present in the title (AND across tokens)
            title_val = item.get("title")
            if not title_val:
                return False
            for t in terms:
                if t.lower() not in str(title_val).lower():
                    return False
            return True

        # Tag filter
        if f == "tag":
            # require ALL provided tag terms to be present in the item's tags
            if len(terms) > 1:
                return contains_all_in_tags(tags, terms)
            for tag in tags:
                if contains_any(tag, terms):
                    return True
            return False

        # Performer filter
        if f == "performer":
            raw = item.get("raw") or {}
            performers = raw.get("performers") or item.get("performers") or []
            # normalize to list of strings
            perf_list = []
            if isinstance(performers, str):
                perf_list = [p.strip() for p in performers.split(",") if p.strip()]
            elif isinstance(performers, (list, tuple)):
                perf_list = [str(p) for p in performers]
            # multiple performer tokens -> require ALL tokens to match at least one performer
            if len(terms) > 1:
                for t in terms:
                    matched = False
                    for p in perf_list:
                        if t.lower() in str(p).lower():
                            matched = True
                            break
                    if not matched:
                        return False
                return True
            # single token -> accept if any performer matches
            for p in perf_list:
                if contains_any(p, terms):
                    return True
            return False

        # File filter
        if f == "file":
            return contains_any(item.get("file"), terms) or contains_any(item.get("filename"), terms) or contains_any(item.get("link"), terms)

        # Instrument filter
        if f == "instrument":
            raw = item.get("raw") or {}
            instruments = raw.get("instruments") or item.get("instruments") or []
            inst_list = []
            if isinstance(instruments, str):
                inst_list = [i.strip() for i in instruments.split(",") if i.strip()]
            elif isinstance(instruments, (list, tuple)):
                inst_list = [str(i) for i in instruments]
            # require ALL provided instrument tokens to match at least one instrument
            if len(terms) > 1:
                for t in terms:
                    matched = False
                    for i in inst_list:
                        if t.lower() in str(i).lower():
                            matched = True
                            break
                    if not matched:
                        return False
                return True
            # single token -> accept if any instrument matches
            for i in inst_list:
                if contains_any(i, terms):
                    return True
            return False

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
    print(f"[DEBUG][feed_bp] normalized_batch_len={len(normalized_batch)} filter_by={filter_by} search={search}")

    # For filters that are handled server-side, do not re-filter client-side
    server_side_filters = [
        'author', 'tag', 'performer', 'instrument', 'publisher', 'date', 'title', 'file', 'composed_query'
    ]
    if filter_by in server_side_filters:
        accumulated = normalized_batch
    else:
        for it in normalized_batch:
            # Trust server results and skip client-side re-filtering when:
            #  - server-side composed queries are used, or
            #  - the search contains comma-separated multi-terms (server already applied AND semantics)
            # Otherwise fall back to client-side matching.
            if filter_by == 'composed_query' or (filter_by == 'all' and isinstance(search, str) and ',' in search) or matches(it, search, filter_by):
                accumulated.append(it)

    print(f"[DEBUG][feed_bp] accumulated_len_after_filter={len(accumulated)}")

    sliced = accumulated[:limit]
    return jsonify(sliced)

# last line