# first line

from flask import Blueprint, jsonify, request, session
from client.services.http_helper import http_client
from client.services.feed_service import FeedService

feed_bp = Blueprint("feed", __name__, url_prefix="/feed")

@feed_bp.route("/data", methods=["GET"])
def feed_data():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    search = request.args.get("search")
    filter_by = request.args.get("filter", "all")
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 10))

    print(f"[DEBUG] Fetching feed: search={search}, filter={filter_by}, offset={offset}, limit={limit}")

    response = FeedService.get_feed(search, filter_by, offset, limit)

    if response.get("status") == "OK":
        inner = response.get("response", {})
        results = inner.get("results") if isinstance(inner, dict) else inner
        # print(f"[DEBUG] Raw feed response: {response}")
        return jsonify(results or [])
    else:
        err = response.get("error_msg", "Unknown error")
        print(f"[ERROR] feed_data failed: {err}")
        return jsonify({"error": err}), 400

# last line