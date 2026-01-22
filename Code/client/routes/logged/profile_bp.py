# first line

from flask import send_file, Blueprint, jsonify, request, session, render_template
from werkzeug.utils import secure_filename
from client.services.http_helper import http_client
from client.services.profile_service import ProfileService
from client.models.media import Media
from client.models.user import User
import base64
import time
import io
import mimetypes

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
        user_data = response.get("user")
        
        # VALIDATION: Reject if no user data or user is empty
        if not user_data or not isinstance(user_data, dict) or not user_data.get("id"):
            err = response.get("error_msg", "Server returned invalid profile")
            print(f"[ERROR][profile_bp.profile_data] Invalid user data: {user_data}")
            return jsonify({"status": "ERROR", "error": err}), 400
        
        # Fetch viewer's own profile to get viewer's id, username, lvl
        viewer_profile = ProfileService.get_profile(None)  # None = fetch own profile
        viewer_data = {}
        if viewer_profile.get("status") == "OK":
            viewer_info = viewer_profile.get("user", {})
            viewer_data = {
                "id": viewer_info.get("id"),
                "username": viewer_info.get("username"),
                "lvl": viewer_info.get("lvl"),
                "is_self": response.get("self", {}).get("is_self", False)
            }
        else:
            # Fallback: if viewer profile fetch fails, at least mark is_self correctly
            viewer_data = {
                "is_self": response.get("self", {}).get("is_self", False)
            }
        
        payload = {
            "status": "OK",
            "user": user_data,
            "viewer": viewer_data,  # Include viewer's own profile data
            "recent_publications": response.get("recent_publications", [])
        }
        print("[DEBUG][profile_bp.profile_data] returning payload:", payload)
        return jsonify(payload)
    else:
        err = response.get("error_msg", "Unknown error")
        print(f"[ERROR][profile_bp.profile_data] Service error: {err}")
        return jsonify({"status": "ERROR", "error": err}), 400

@profile_bp.route("/publications", methods=["GET"])
def get_publications():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    username = request.args.get("username")
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 10))

    # If no username provided (own profile), resolve current user's username via GET_PROFILE
    if not username:
        try:
            prof = http_client.send_request("GET_PROFILE", [], require_auth=True)
            # unwrap common envelopes
            if isinstance(prof, dict):
                for k in ("response", "result", "user", "user_obj"):
                    if k in prof and isinstance(prof[k], dict):
                        prof = prof[k]
                        break
                # if still a direct user dict, keep it
                if isinstance(prof, dict):
                    username = prof.get("username") or prof.get("user") or prof.get("name")
        except Exception as e:
            username = None

    # if still no username, return empty publications (safe fallback)
    if not username:
        return jsonify({"publications": [], "count": 0})

    response = ProfileService.get_user_publications(username, offset, limit)

    # extract list robustly
    pubs = []
    total_count = None
    if isinstance(response, dict) and response.get("status") in (None, "OK"):
        if "results" in response and isinstance(response["results"], list):
            pubs = response["results"]
        elif "response" in response:
            r = response["response"]
            if isinstance(r, list):
                pubs = r
            elif isinstance(r, dict) and "results" in r:
                pubs = r["results"]
        elif isinstance(response.get("response"), list):
            pubs = response.get("response")
        # server may provide a count
        if "count" in response:
            try:
                total_count = int(response["count"])
            except Exception:
                total_count = None
    elif isinstance(response, list):
        pubs = response

    # Normalize minimal fields expected by the frontend using Media model
    normalized = []
    for p in pubs:
        if not isinstance(p, dict):
            continue
        try:
            m = Media.from_server(p)
            md = m.to_dict()
            normalized.append({
                "id": md.get("id") or p.get("id") or p.get("media_id"),
                "title": md.get("title") or p.get("title") or p.get("name") or "Untitled",
                "description": p.get("description") or md.get("description") or p.get("additional_info") or "",
                "date_published": p.get("date_published") or p.get("created_at") or p.get("date") or p.get("year") or "",
                "stored_at": p.get("stored_at") or md.get("stored_at") or p.get("file_path") or "",
                "file_name": (p.get("stored_at") or md.get("stored_at") or "").split("/")[-1] if (p.get("stored_at") or md.get("stored_at")) else None,
                "file_type": md.get("type") or p.get("type") or p.get("media_type") or "unknown",
            })
        except Exception:
            normalized.append({
                "id": p.get("id") or p.get("media_id"),
                "title": p.get("title") or p.get("name") or "Untitled",
                "description": p.get("description") or p.get("additional_info") or "",
                "date_published": p.get("created_at") or "",
                "stored_at": p.get("stored_at") or p.get("file_path") or "",
                "file_name": (p.get("stored_at") or "").split("/")[-1] if p.get("stored_at") else None,
                "file_type": p.get("type") or p.get("media_type") or "unknown",
            })

    if total_count is None:
        total_count = len(normalized)

    return jsonify({"publications": normalized, "count": total_count})

# ------------------------
# UPLOAD endpoint that accepts a browser file and forwards to API server (base64)
# ------------------------
@profile_bp.route("/edit", methods=["GET"])
def edit_profile():
    """
    Render the profile edit form (client-side will fetch current data).
    Accept optional ?username=... so admins/roots editing other users open the editor
    already targeted to that username.
    """
    if http_client.token is None:
        http_client.token = session.get("session_token")

    target_username = request.args.get("username")
    return render_template("profile_update.html", username=target_username)

@profile_bp.route("/update", methods=["POST"])
def update_profile():
    """
    Accept JSON payload with profile fields and forward to ProfileService.update_profile.
    Expects a JSON object like { display_name, full_bio, profile_pic, ... }.
    """
    if http_client.token is None:
        http_client.token = session.get("session_token")

    content = request.get_json() or {}
    if not isinstance(content, dict):
        return jsonify({"error": "Invalid payload"}), 400

    # Determine target username: prefer explicit field in payload, then query param.
    target_username = content.get("username") or request.args.get("username")

    # Ensure the target username is embedded in the content body so servers that
    # expect the username in the payload (not only as a separate arg) receive it.
    if target_username:
        content["username"] = target_username
        content["target_username"] = target_username

    res = ProfileService.update_profile(content, target_username)
    if res.get("status") in (None, "OK"):
        return jsonify({"status": "OK", "response": res.get("response", {})})
    return jsonify({"error": res.get("error_msg", "Unknown error")}), 400

# ------------------------
# DOWNLOAD endpoint: fetch base64 from API server and stream to browser
# ------------------------
@profile_bp.route("/download", methods=["GET"])
def download_file():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    file_type = request.args.get("file_type")
    filename = request.args.get("filename")
    if not file_type or not filename:
        return jsonify({"error": "Missing file_type or filename"}), 400

    res = http_client.send_request("FETCH_FILE", [file_type, filename], require_auth=True)
    if res.get("status") not in (None, "OK"):
        return jsonify({"error": res.get("error_msg", "Unknown error")}), 400

    # API returns base64 string under 'response' (see api_server/redirect)
    b64 = res.get("response") or res.get("data") or res.get("file") or res.get("response")
    # sometimes send_request returns a dict with 'response' wrapping the base64
    if isinstance(b64, dict) and "response" in b64:
        b64 = b64["response"]

    if not b64:
        return jsonify({"error": "File not found"}), 404

    try:
        content = base64.b64decode(b64)
    except Exception:
        return jsonify({"error": "Invalid base64 data returned from server"}), 500

    return send_file(io.BytesIO(content), as_attachment=True, download_name=filename, mimetype="application/octet-stream")


@profile_bp.route("/picture/<filename>")
def profile_picture(filename):
    """
    Proxy route: fetch image bytes from API server (via FETCH_FILE) and stream to browser.
    """
    if http_client.token is None:
        http_client.token = session.get("session_token")

    # ask API for the file (file_type 'image', filename is the stored id/name)
    res = http_client.send_request("FETCH_FILE", ["image", filename], require_auth=True)
    if res.get("status") not in (None, "OK"):
        return ("", 404)

    b64 = res.get("response") or res.get("data") or None
    if isinstance(b64, dict) and "response" in b64:
        b64 = b64["response"]
    if not b64:
        return ("", 404)

    try:
        content = base64.b64decode(b64)
    except Exception:
        return ("", 500)

    # guess mimetype from extension, default to image/jpeg
    mt, _ = mimetypes.guess_type(filename)
    mimetype = mt or "image/jpeg"
    return send_file(io.BytesIO(content), mimetype=mimetype)

@profile_bp.route("/upload", methods=["POST"])
def upload_profile_file():
    """
    Receive multipart file from browser, base64 it and forward to API server.
    Expects form field 'file' and optional form field 'type' (default 'image').
    """
    if http_client.token is None:
        return jsonify({"status": "error", "error_msg": "NOT_LOGGED_IN"}), 401

    file = request.files.get("file")
    if not file:
        return jsonify({"status": "error", "error_msg": "No file provided"}), 400

    filename = secure_filename(file.filename) or f"upload_{int(time.time())}"
    file_type = request.form.get("type", "image")

    try:
        content = file.read()
        b64 = base64.b64encode(content).decode("ascii")
        # Forward to API - adjust command name if your server expects a different one (eg. STORE_FILE / SAVE_FILE)
        api_res = http_client.send_request("SAVE_FILE", [file_type, filename, b64], require_auth=True)
        return jsonify(api_res)
    except Exception as e:
        return jsonify({"status": "error", "error_msg": str(e)}), 500

# ------------------------
# Follow / Unfollow endpoints used by client JS (toggleFollow)
# ------------------------
@profile_bp.route("/follow", methods=["POST"])
def follow_user():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    payload = request.get_json() or {}
    target = payload.get("username") or request.args.get("username")
    if not target:
        return jsonify({"status": "ERROR", "error_msg": "Missing username"}), 400

    res = ProfileService.follow(target, None)
    if isinstance(res, dict) and res.get("status") in (None, "OK"):
        return jsonify({"status": "OK", "response": res.get("response", {})})
    return jsonify({"status": "ERROR", "error_msg": res.get("error_msg", "Unknown error")}), 400

@profile_bp.route("/unfollow", methods=["POST"])
def unfollow_user():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    payload = request.get_json() or {}
    target = payload.get("username") or request.args.get("username")
    if not target:
        return jsonify({"status": "ERROR", "error_msg": "Missing username"}), 400

    res = ProfileService.unfollow(target, None)
    if isinstance(res, dict) and res.get("status") in (None, "OK"):
        return jsonify({"status": "OK", "response": res.get("response", {})})
    return jsonify({"status": "ERROR", "error_msg": res.get("error_msg", "Unknown error")}), 400

# ------------------------
# LEVEL / MODERATION endpoints
# ------------------------
@profile_bp.route("/set_level/<username>/<int:new_level>", methods=["POST"])
def set_user_level(username, new_level):
    if http_client.token is None:
        http_client.token = session.get("session_token")

    try:
        res = ProfileService.change_level(username, new_level)
        if isinstance(res, dict) and res.get("status") in (None, "OK"):
            return jsonify({"status": "OK", "response": res.get("response", {})})
        return jsonify({"status": "ERROR", "error_msg": res.get("error_msg", "Failed to set level")}), 400
    except Exception as e:
        return jsonify({"status": "ERROR", "error_msg": str(e)}), 500

@profile_bp.route("/ban/<username>", methods=["POST"])
def ban_user(username):
    if http_client.token is None:
        http_client.token = session.get("session_token")
    try:
        res = ProfileService.ban_user(username)
        if isinstance(res, dict) and res.get("status") in (None, "OK"):
            return jsonify({"status": "OK", "response": res.get("response", {})})
        return jsonify({"status": "ERROR", "error_msg": res.get("error_msg", "Failed to ban user")}), 400
    except Exception as e:
        return jsonify({"status": "ERROR", "error_msg": str(e)}), 500

@profile_bp.route("/upgrade/<username>", methods=["POST"])
def upgrade_user(username):
    """
    Increase privileges: numeric level decreases (e.g. 5 -> 4, 4 -> 3).
    """
    if http_client.token is None:
        http_client.token = session.get("session_token")
    try:
        prof = ProfileService.get_profile(username)
        if prof.get("status") != "OK":
            return jsonify({"status": "ERROR", "error_msg": "Cannot fetch target profile"}), 400
        target = prof.get("user", {})
        curr_lvl = int(target.get("lvl", target.get("lvl", 4) or 4))
        new_lvl = max(0, curr_lvl - 1)
        if new_lvl == curr_lvl:
            return jsonify({"status": "ERROR", "error_msg": "Already at highest level"}), 400
        return set_user_level(username, new_lvl)
    except Exception as e:
        return jsonify({"status": "ERROR", "error_msg": str(e)}), 500

@profile_bp.route("/downgrade/<username>", methods=["POST"])
def downgrade_user(username):
    """
    Decrease privileges: numeric level increases (e.g. 3 -> 4, 4 -> 5).
    """
    if http_client.token is None:
        http_client.token = session.get("session_token")
    try:
        prof = ProfileService.get_profile(username)
        if prof.get("status") != "OK":
            return jsonify({"status": "ERROR", "error_msg": "Cannot fetch target profile"}), 400
        target = prof.get("user", {})
        curr_lvl = int(target.get("lvl", target.get("lvl", 4) or 4))
        new_lvl = min(6, curr_lvl + 1)
        if new_lvl == curr_lvl:
            return jsonify({"status": "ERROR", "error_msg": "Already at lowest level"}), 400
        return set_user_level(username, new_lvl)
    except Exception as e:
        return jsonify({"status": "ERROR", "error_msg": str(e)}), 500

# ----------------------
# Followers / Following endpoints
# ----------------------
@profile_bp.route("/followers", methods=["GET"])
def get_followers_list():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    username = request.args.get("username")
    if not username:
        return jsonify({"status": "ERROR", "error_msg": "Missing username"}), 400

    response = ProfileService.get_followers(username)
    
    # Extract followers list robustly from nested response structure
    followers = []
    if isinstance(response, dict) and response.get("status") in (None, "OK"):
        # Server returns: {'response': {'response': [...], 'status': 'OK'}, 'status': 'OK'}
        # First unwrap the outer response
        inner_response = response.get("response")
        if isinstance(inner_response, dict):
            # Now extract from the inner response
            data = inner_response.get("response") or inner_response.get("data") or inner_response.get("followers") or []
            if isinstance(data, list):
                followers = data
        elif isinstance(inner_response, list):
            followers = inner_response
    elif isinstance(response, list):
        followers = response
    
    # Normalize to list of username strings
    normalized = []
    for f in followers:
        if isinstance(f, dict):
            username_val = f.get("username") or f.get("user") or f.get("name")
            if username_val:
                normalized.append(username_val)
        elif isinstance(f, str):
            normalized.append(f)
    
    return jsonify({"status": "OK", "followers": normalized})

@profile_bp.route("/following", methods=["GET"])
def get_following_list():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    username = request.args.get("username")
    if not username:
        return jsonify({"status": "ERROR", "error_msg": "Missing username"}), 400

    response = ProfileService.get_following(username)
    
    # Extract following list robustly from nested response structure
    following = []
    if isinstance(response, dict) and response.get("status") in (None, "OK"):
        # Server returns: {'response': {'response': [...], 'status': 'OK'}, 'status': 'OK'}
        # First unwrap the outer response
        inner_response = response.get("response")
        if isinstance(inner_response, dict):
            # Now extract from the inner response
            data = inner_response.get("response") or inner_response.get("data") or inner_response.get("following") or []
            if isinstance(data, list):
                following = data
        elif isinstance(inner_response, list):
            following = inner_response
    elif isinstance(response, list):
        following = response
    
    # Normalize to list of username strings
    normalized = []
    for f in following:
        if isinstance(f, dict):
            username_val = f.get("username") or f.get("user") or f.get("name")
            if username_val:
                normalized.append(username_val)
        elif isinstance(f, str):
            normalized.append(f)
    
    return jsonify({"status": "OK", "following": normalized})

@profile_bp.route("/", methods=["GET"])
@profile_bp.route("", methods=["GET"])
def profile_page():
    """
    Serve the profile HTML page. The frontend will call /profile/data and
    /profile/publications to populate the page; accept optional ?username=...
    so links like /profile?username=Anna work.
    """
    if http_client.token is None:
        http_client.token = session.get("session_token")
    target_username = request.args.get("username")
    return render_template("profile.html", username=target_username)