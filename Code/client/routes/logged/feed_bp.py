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
    print("[DEBUG] about to fetch feed")
    response = FeedService.get_feed(search, filter_by, offset, limit)
    if response.get("status") == "OK":
        return jsonify(response.get("data", []))
    else:
        return jsonify({"error": response.get("error_msg", "Unknown error")}), 400

# last line