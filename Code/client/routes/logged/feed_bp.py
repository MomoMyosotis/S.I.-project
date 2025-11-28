# first line

from flask import Blueprint, jsonify, request, session
from client.services.http_helper import http_client
from client.services.feed_service import FeedService

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

    # flexible matching helper
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

    # We'll keep fetching remote batches and locally filter them until we have enough items
    # to satisfy offset + limit or remote is exhausted.
    accumulated = []
    remote_offset = 0
    fetch_limit = 100  # batch size per remote request (cap)
    max_iterations = 50  # safety cap to avoid infinite loops
    iterations = 0

    while len(accumulated) < offset + limit and iterations < max_iterations:
        iterations += 1
        # Ask the remote service to apply search/filter if it supports them.
        response = FeedService.get_feed(search, filter_by, remote_offset, fetch_limit)
        if response.get("status") != "OK":
            err = response.get("error_msg", "Unknown error")
            print(f"[ERROR] feed_data failed during fetch: {err}")
            return jsonify({"error": err}), 400

        inner = response.get("response", {})
        batch = inner.get("results") if isinstance(inner, dict) else inner
        batch = batch or []

        if not batch:
            # remote exhausted
            break

        # filter this batch and accumulate
        for it in batch:
            if matches(it, search, filter_by):
                accumulated.append(it)

        # If remote returned less than fetch_limit it's probably exhausted
        if len(batch) < fetch_limit:
            break

        remote_offset += fetch_limit

    # Now paginate locally using requested offset and limit
    sliced = accumulated[offset:offset + limit]
    return jsonify(sliced)

# last line