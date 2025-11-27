# first line

from flask import Blueprint, jsonify, request, session
from client.services.http_helper import http_client
from client.services.profile_service import ProfileService

profile_bp = Blueprint("profile", __name__, url_prefix="/profile")

@profile_bp.route("/data", methods=["GET"])
def profile_data():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    username = request.args.get("username")
    print("[DEBUG][profile_bp.profile_data] START")
    print("[DEBUG][profile_bp.profile_data] requested username:", username)

    response = ProfileService.get_profile(username)
    print("[DEBUG][ProfileService.get_profile] response:", response)

    if response.get("status") == "OK":
        # ProfileService already returns { "user": ..., "self": ..., "recent_publications": ... }
        payload = {
            "user": response.get("user", {}),
            "self": response.get("self", {"is_self": False}),
            "recent_publications": response.get("recent_publications", [])
        }
        print("[DEBUG][profile_bp.profile_data] returning payload:", payload)
        return jsonify(payload)
    else:
        err = response.get("error_msg", "Unknown error")
        return jsonify({"error": err}), 400

@profile_bp.route("/publications", methods=["GET"])
def get_publications():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    username = request.args.get("username")
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 10))

    response = ProfileService.get_user_publications(username, offset, limit)
    # handle different server shapes: {"status":"OK","response":[...]} or {"status":"OK","results":[...]} or direct list
    pubs = []
    if isinstance(response, dict) and response.get("status") in (None, "OK"):
        if "response" in response and isinstance(response["response"], list):
            pubs = response["response"]
        elif "results" in response and isinstance(response["results"], list):
            pubs = response["results"]
        elif isinstance(response.get("response"), dict) and "results" in response.get("response"):
            pubs = response["response"].get("results", [])
    elif isinstance(response, list):
        pubs = response

    # normalize minimal fields expected by the frontend
    normalized = []
    for p in pubs:
        if not isinstance(p, dict): continue
        normalized.append({
            "id": p.get("id") or p.get("media_id"),
            "title": p.get("title") or p.get("name") or "Untitled",
            "description": p.get("description") or p.get("additional_info") or "",
            "date_published": p.get("date_published") or p.get("created_at") or ""
        })

    return jsonify(normalized)

# last line