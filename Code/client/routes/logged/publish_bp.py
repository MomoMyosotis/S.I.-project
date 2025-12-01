from flask import Blueprint, render_template, request, jsonify, session, current_app
from client.services.http_helper import http_client
import json, base64

publish_bp = Blueprint("publish", __name__)

def _unwrap_user_response(resp):
    """
    Try to safely unwrap nested RPC envelopes and return a dict candidate
    containing user fields (lvl/username). Returns None if not found.
    """
    if not isinstance(resp, dict):
        return None

    inner = resp
    # Unwrap layers like {"response": {...}} or {"result": {...}} or {"user_obj": {...}}
    seen = set()
    while isinstance(inner, dict):
        # avoid cycles
        ident = id(inner)
        if ident in seen:
            break
        seen.add(ident)

        # prefer common envelope keys
        for key in ("response", "result", "user_obj", "user"):
            if key in inner:
                inner = inner[key]
                break
        else:
            break

    if not isinstance(inner, dict):
        return None

    # Accept many possible keys returned by server
    lvl = inner.get("lvl") if "lvl" in inner else inner.get("level") if "level" in inner else inner.get("lvl_value") if "lvl_value" in inner else None
    username = inner.get("username") or inner.get("user") or inner.get("name")
    return {"lvl": lvl, "username": username}

@publish_bp.route("/publish.html")
def publish_page():
    # ensure token from session is used if available
    if http_client.token is None:
        http_client.token = session.get("session_token")

    # conservative default: banned (no publish)
    user_level = 6
    username = None

    try:
        # ask backend for profile to get level/username (best-effort)
        profile_res = http_client.send_request("GET_PROFILE", [], require_auth=True)
        current_app.logger.debug(f"[publish_page] raw GET_PROFILE response: {profile_res!r}")

        if isinstance(profile_res, dict) and (profile_res.get("status") in (None, "OK") or "response" in profile_res):
            info = _unwrap_user_response(profile_res)
            current_app.logger.debug(f"[publish_page] unwrapped profile info: {info!r}")
            if info and isinstance(info, dict):
                # set user_level only if a valid int-like value is present
                lvl_val = info.get("lvl")
                if lvl_val is not None:
                    try:
                        user_level = int(lvl_val)
                    except (ValueError, TypeError):
                        current_app.logger.debug(f"[publish_page] invalid lvl value from server: {lvl_val!r} — keeping fallback {user_level}")
                # set username only when present and truthy
                if info.get("username"):
                    username = info.get("username")

    except Exception as e:
        # best-effort: if we can't fetch profile leave defaults (level 6 to be safe)
        current_app.logger.debug(f"[publish_page] error fetching profile: {e}")

    return render_template("publish.html", user_level=user_level, username=username)

@publish_bp.route("/content/publish", methods=["POST"])
def publish_content():
    """
    Accept multipart FormData from browser. Validate per media type, optionally save files
    via SAVE_FILE RPC and forward create command to backend.
    """
    try:
        media_type = (request.form.get("type") or "").lower()
        title = (request.form.get("title") or "").strip()
        authors = json.loads(request.form.get("authors") or "[]")
        genre = (request.form.get("genre") or "").strip()
        composition_year = request.form.get("composition_year") or None

        performers = json.loads(request.form.get("performers") or "[]")
        segments = json.loads(request.form.get("segments") or "[]")
        subtracks = json.loads(request.form.get("subtracks") or "[]")

        recording_date = request.form.get("recording_date")
        recording_location = request.form.get("recording_location", "").strip()

        document_type = request.form.get("document_type")
        document_annotations = request.form.get("document_annotations", "")

        event_title = request.form.get("event_title", "")
        concert_date = request.form.get("concert_date", "")
        concert_location = request.form.get("concert_location", "")
        link = request.form.get("link", "")

        duration = request.form.get("duration") or None
        file_format = request.form.get("file_format") or None

        # read extra checkboxes
        is_composer = bool(request.form.get("is_composer"))
        is_performer = bool(request.form.get("is_performer"))
        instruments_used = request.form.get("instruments_used", "")
        is_live = bool(request.form.get("is_live"))

        # Basic validation per media type
        if media_type in ("video", "audio"):
            if not title:
                return jsonify({"status":"ERROR","error_msg":"title required"}), 400
            if not isinstance(authors, list) or len(authors) == 0:
                return jsonify({"status":"ERROR","error_msg":"authors required"}), 400
            if not genre:
                return jsonify({"status":"ERROR","error_msg":"genre required"}), 400
            if recording_date and not recording_location:
                return jsonify({"status":"ERROR","error_msg":"recording_location required when recording_date provided"}), 400
            if is_live and (not recording_date or not recording_location):
                return jsonify({"status":"ERROR","error_msg":"live performance requires recording_date and recording_location"}), 400
            # require at least one uploaded file
            if not request.files or len(request.files.getlist("files")) == 0:
                return jsonify({"status":"ERROR","error_msg":"file upload required for audio/video"}), 400
        elif media_type == "document":
            if not title:
                return jsonify({"status":"ERROR","error_msg":"title required"}), 400
            if not request.files or len(request.files.getlist("files")) == 0:
                return jsonify({"status":"ERROR","error_msg":"document file required"}), 400
            if document_type not in ("score","lyrics","chords","other"):
                return jsonify({"status":"ERROR","error_msg":"invalid document_type"}), 400
        elif media_type == "concert":
            if not link:
                return jsonify({"status":"ERROR","error_msg":"YouTube link required for concert"}), 400
            # validate subtracks (if present) - each must have title
            for st in subtracks:
                if not st.get("title"):
                    return jsonify({"status":"ERROR","error_msg":"each subtrack must have a title"}), 400
        else:
            return jsonify({"status":"ERROR","error_msg":"unknown media type"}), 400

        # Process files: base64 encode and save via SAVE_FILE RPC if files present
        files_payload = []
        for f in request.files.getlist("files"):
            data = f.read()
            files_payload.append({
                "filename": f.filename,
                "content_b64": base64.b64encode(data).decode("ascii"),
                "content_type": f.content_type
            })

        # If files need to be stored, save them via SAVE_FILE RPC before creating media; point stored_at accordingly
        stored_at = None
        if files_payload:
            folder_map = {"song": "songs", "video": "videos", "document": "documents", "audio": "songs"}
            file_type_for_save = media_type if media_type in ("video","document","audio") else "document"
            folder = folder_map.get(file_type_for_save, "documents")
            # Save all files (stop on first failure)
            for file_obj in files_payload:
                filename = file_obj.get("filename")
                b64 = file_obj.get("content_b64")
                save_res = http_client.send_request("SAVE_FILE", [file_type_for_save, filename, b64], require_auth=True)
                if not isinstance(save_res, dict) or save_res.get("status") not in (None, "OK"):
                    return jsonify({"status":"ERROR","error_msg":f"Failed to save file {filename}: {save_res}"}), 500
            # set stored_at to first filename location (server will resolve)
            stored_at = f"server/storage/{folder}/{files_payload[0]['filename']}"

        # Build payload to forward to backend create command
        payload = {
            "title": title,
            "authors": authors,
            "genre": genre,
            "composition_year": int(composition_year) if composition_year else None,
            "type": media_type,
            "duration": float(duration) if duration else None,
            "file_format": file_format,
            "stored_at": stored_at,
            "performers": performers,
            "segments": segments,
            "subtracks": subtracks,
            "document_type": document_type,
            "document_annotations": document_annotations,
            "event_title": event_title,
            "concert_date": concert_date,
            "concert_location": concert_location,
            "link": link,
            "recording_date": recording_date,
            "recording_location": recording_location,
            "is_composer": is_composer,
            "is_performer": is_performer,
            "instruments_used": instruments_used,
            "is_live": is_live,
            # do not forward raw file bytes (we saved them via SAVE_FILE)
            "files": []
        }

        # choose backend command
        cmd_map = {
            "video": "CREATE_VIDEO",
            "audio": "CREATE_SONG",
            "document": "CREATE_DOCUMENT",
            "concert": "CREATE_CONCERT"
        }
        cmd = cmd_map.get(media_type, "CREATE_SONG")

        res = http_client.send_request(cmd, [payload], require_auth=True)
        return jsonify(res)
    except Exception as e:
        return jsonify({"status":"ERROR","error_msg": str(e)}), 500