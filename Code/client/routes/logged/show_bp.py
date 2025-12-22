from flask import Blueprint, render_template, jsonify, request, session, current_app, send_file
from client.services.show_service import ShowService
from client.services.http_helper import http_client
from client.services.profile_service import ProfileService
from client.models.media import Media
import json


show_bp = Blueprint("show", __name__, url_prefix="/show")

@show_bp.route("/", methods=["GET"])
def show_page():
    """
    Renders template; optionally take ?media_id=... and pre-fetch media and current user
    so the template can render immediately and have correct viewer/media objects.
    """
    media_id = request.args.get("media_id") or request.args.get("id")
    initial_media = None
    server_user = None

    if http_client.token is None:
        http_client.token = session.get("session_token")

    if media_id:
        try:
            resp = ShowService.get_media(media_id)
            # reuse same normalisation logic as /data
            candidate = None
            if isinstance(resp, dict):
                status = resp.get("status")
                if status and str(status).lower() not in ("ok", "true", "accepted"):
                    candidate = None
                else:
                    for k in ("response", "result", "media"):
                        if k in resp and resp[k]:
                            candidate = resp[k]
                            break
                    if candidate is None:
                        candidate = resp
            if isinstance(candidate, dict):
                media_obj = Media.from_server(candidate)
                media_dict = media_obj.to_dict()
                # copy some legacy fields if present
                for k in ("username","tags","author_names","authors","performers","segments","subtracks","duration_display","duration_seconds","filename","file","link","description"):
                    if k in candidate and k not in media_dict:
                        media_dict[k] = candidate[k]
                initial_media = media_dict
        except Exception:
            initial_media = None

    # fetch current viewer profile if possible
    try:
        prof = ProfileService.get_profile(None)
        if isinstance(prof, dict) and prof.get("status") in (None, "OK") and isinstance(prof.get("user"), dict):
            server_user = prof["user"]
    except Exception:
        server_user = None

    return render_template("show.html",
                        INITIAL_MEDIA=json.dumps(initial_media) if initial_media is not None else "null",
                        SERVER_USER=json.dumps(server_user) if server_user is not None else "null")

@show_bp.route("/data", methods=["GET"])
def show_data():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    media_id = request.args.get("media_id") or request.args.get("id")
    if not media_id:
        return jsonify({"error": "missing media_id"}), 400

    resp = ShowService.get_media(media_id)
    current_app.logger.debug(f"[DEBUG] ShowService.get_media returned: {resp!r}")

    # Accept many server shapes and build a consistent media dict using the Media model
    try:
        candidate = None
        if isinstance(resp, dict):
            status = resp.get("status")
            if status and str(status).lower() not in ("ok", "true", "accepted", "accepted"):
                err = resp.get("error_msg") or resp.get("error") or (isinstance(resp.get("response"), dict) and resp["response"].get("error_msg"))
                return jsonify({"error": err or "Backend error"}), 400

            for k in ("response", "result", "media"):
                if k in resp and resp[k]:
                    candidate = resp[k]
                    break
            if candidate is None:
                candidate = resp
        else:
            return jsonify({"error": "invalid response from backend"}), 400

        if isinstance(candidate, dict):
            media_obj = Media.from_server(candidate)
            media_dict = media_obj.to_dict()
            if isinstance(candidate.get("username"), str):
                media_dict["username"] = candidate.get("username")
            for k in ("tags","author_names","authors","performers","segments","subtracks","duration_display","duration_seconds","filename","file","link","description"):
                if k in candidate and k not in media_dict:
                    media_dict[k] = candidate[k]

            # try to include current viewer info for convenience
            viewer = None
            try:
                prof = ProfileService.get_profile(None)
                if isinstance(prof, dict) and prof.get("status") in (None, "OK") and isinstance(prof.get("user"), dict):
                    viewer = prof["user"]
            except Exception:
                viewer = None

            return jsonify({"media": media_dict, "user": viewer})
        return jsonify({"error": "invalid response from backend"}), 400
    except Exception as e:
        current_app.logger.exception("Failed to normalize media response")
        return jsonify({"error": "internal error"}), 500

@show_bp.route("/comment", methods=["POST"])
def post_comment():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    data = request.get_json(silent=True) or {}
    media_id = data.get("media_id")
    text = data.get("text", "").strip()
    parent_comment_id = data.get("parent_comment_id") or data.get("parent_id") or None
    if not media_id or not text:
        return jsonify({"error": "missing media_id or text"}), 400

    resp = ShowService.post_comment(media_id, text, parent_comment_id=parent_comment_id)
    current_app.logger.debug(f"[DEBUG] ShowService.post_comment raw response: {resp!r}")
    # help trace shapes
    try:
        current_app.logger.debug(f"[DEBUG] ShowService.post_comment normalized status: {resp.get('status') if isinstance(resp, dict) else 'non-dict'}")
    except Exception:
        current_app.logger.exception("Could not inspect post_comment response")

    # normalize inner result
    if isinstance(resp, dict):
        inner = resp.get("response") or resp.get("result") or resp
        # success if inner indicates OK or returns a created id
        if isinstance(inner, dict) and (str(inner.get("status")).upper() == "OK" or inner.get("id") or inner.get("result") == "OK"):
            return jsonify({"status": "OK", "id": inner.get("id")}), 200
        err = inner.get("error_msg") if isinstance(inner, dict) else resp.get("error_msg", "Backend error")
        return jsonify({"status": "ERROR", "error_msg": err}), 400
    return jsonify({"status": "ERROR", "error_msg": "Invalid backend response"}), 500

@show_bp.route("/file", methods=["GET"])
def show_file():
    """
    Proxy route: fetch file bytes from API server and stream to browser.
    Query params: file_type (e.g. 'song','video','document','image'), filename (stored name or id)
    """
    if http_client.token is None:
        http_client.token = session.get("session_token")

    file_type = request.args.get("file_type")
    filename = request.args.get("filename")
    if not file_type or not filename:
        return ("", 400)

    res = http_client.send_request("FETCH_FILE", [file_type, filename], require_auth=True)
    if res.get("status") not in (None, "OK"):
        return ("", 404)

    b64 = res.get("response") or res.get("data") or res.get("file") or None
    if isinstance(b64, dict) and "response" in b64:
        b64 = b64["response"]
    if not b64:
        return ("", 404)

    try:
        import base64
        import io
        content = base64.b64decode(b64)
    except Exception:
        return ("", 500)
    import mimetypes
    mt, _ = mimetypes.guess_type(filename)
    mimetype = mt or "application/octet-stream"
    return send_file(io.BytesIO(content), mimetype=mimetype, download_name=filename)

@show_bp.route("/delete", methods=["POST"])
def delete_media():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    data = request.get_json(silent=True) or {}
    media_id = data.get("media_id")
    media_type = data.get("type") or data.get("media_type") or None
    if not media_id:
        return jsonify({"status": "ERROR", "error_msg": "missing media_id"}), 400

    # permission check: viewer must be lvl 0/1/2 or owner/publisher
    viewer = None
    try:
        prof = ProfileService.get_profile(None)
        if isinstance(prof, dict) and prof.get("status") in (None, "OK") and isinstance(prof.get("user"), dict):
            viewer = prof["user"]
    except Exception:
        viewer = None

    # fetch media to determine owner
    try:
        resp = ShowService.get_media(media_id)
        candidate = None
        if isinstance(resp, dict):
            for k in ("response","result","media"):
                if k in resp and resp[k]:
                    candidate = resp[k]; break
            if candidate is None:
                candidate = resp
        media_obj = Media.from_server(candidate if isinstance(candidate, dict) else {})
        media_dict = media_obj.to_dict()
    except Exception:
        media_dict = {}

    # normalize permissions
    viewer_lvl = None
    viewer_id = None
    if viewer:
        viewer_lvl = int(viewer.get("lvl")) if viewer.get("lvl") is not None else None
        viewer_id = str(viewer.get("id")) if viewer.get("id") is not None else None

    owner_id = media_dict.get("uploader_id") or media_dict.get("user_id") or media_dict.get("owner_id") or None
    owner_id = str(owner_id) if owner_id is not None else None

    allowed = False
    if viewer and (viewer_lvl in (0,1,2) or (viewer_id and owner_id and viewer_id == owner_id)):
        allowed = True

    if not allowed:
        return jsonify({"status":"ERROR","error_msg":"forbidden"}), 403

    res = ShowService.delete_media(media_id, media_type)
    return jsonify(res or {"status":"ERROR","error_msg":"no response from backend"})

@show_bp.route("/edit", methods=["POST"])
def edit_media():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    data = request.get_json(silent=True) or {}
    media_id = data.get("media_id")
    updates = data.get("updates") or {}
    media_type = data.get("type") or None

    if not media_id or not isinstance(updates, dict):
        return jsonify({"status":"ERROR","error_msg":"missing media_id or updates"}), 400

    # permission check same as delete
    viewer = None
    try:
        prof = ProfileService.get_profile(None)
        if isinstance(prof, dict) and prof.get("status") in (None, "OK") and isinstance(prof.get("user"), dict):
            viewer = prof["user"]
    except Exception:
        viewer = None

    try:
        resp = ShowService.get_media(media_id)
        candidate = None
        if isinstance(resp, dict):
            for k in ("response","result","media"):
                if k in resp and resp[k]:
                    candidate = resp[k]; break
            if candidate is None:
                candidate = resp
        media_obj = Media.from_server(candidate if isinstance(candidate, dict) else {})
        media_dict = media_obj.to_dict()
    except Exception:
        media_dict = {}

    viewer_lvl = None
    viewer_id = None
    if viewer:
        viewer_lvl = int(viewer.get("lvl")) if viewer.get("lvl") is not None else None
        viewer_id = str(viewer.get("id")) if viewer.get("id") is not None else None

    owner_id = media_dict.get("uploader_id") or media_dict.get("user_id") or media_dict.get("owner_id") or None
    owner_id = str(owner_id) if owner_id is not None else None

    allowed = False
    if viewer and (viewer_lvl in (0,1,2) or (viewer_id and owner_id and viewer_id == owner_id)):
        allowed = True

    if not allowed:
        return jsonify({"status":"ERROR","error_msg":"forbidden"}), 403

    # sanitize updates: strip empty strings -> None for nullable fields where appropriate
    sanitized = {}
    for k, v in updates.items():
        if isinstance(v, str):
            val = v.strip()
            sanitized[k] = (val if val != "" else None)
        else:
            sanitized[k] = v

    res = ShowService.edit_media(media_id, media_type or media_dict.get("type"), sanitized)
    return jsonify(res or {"status":"ERROR","error_msg":"no response from backend"})

@show_bp.route("/comments", methods=["GET"])
def get_comments():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    media_id = request.args.get("media_id")
    if not media_id:
        return jsonify([])

    res = ShowService.get_comments(media_id, offset=0, limit=200)
    current_app.logger.debug(f"[DEBUG] ShowService.get_comments raw response: {res!r}")

    # normalize shapes
    if isinstance(res, dict) and res.get("status") in (None, "OK"):
        payload = res.get("response") or res.get("results") or []
        if isinstance(payload, dict) and "results" in payload:
            payload = payload["results"]
        if not isinstance(payload, list):
            payload = []
        current_app.logger.debug(f"[DEBUG] ShowService.get_comments normalized payload length: {len(payload)}")
        return jsonify(payload)
    elif isinstance(res, list):
        current_app.logger.debug(f"[DEBUG] ShowService.get_comments returned list length: {len(res)}")
        return jsonify(res)
    current_app.logger.debug("[DEBUG] ShowService.get_comments returned unexpected shape; returning empty list")
    return jsonify([])

@show_bp.route("/comment/report", methods=["POST"])
def report_comment():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    data = request.get_json(silent=True) or {}
    comment_id = data.get("comment_id")
    reason = data.get("reason", "")
    if not comment_id:
        return jsonify({"status":"ERROR","error_msg":"missing comment_id"}), 400

    res = ShowService.report_comment(comment_id, reason)
    if isinstance(res, dict) and res.get("status") in (None, "OK"):
        return jsonify({"status":"OK"})
    return jsonify({"status":"ERROR","error_msg": res.get("error_msg", "Unknown error")}), 400

@show_bp.route("/open_with", methods=["POST"])
def open_with():
    """
    POST JSON: { "media_id": "<id>", "app_id": "<one of allowed ids>" }
    Allowed app_ids: default, vlc, quicktime, music, wmp
    This route downloads the single file for the media and tries to open it
    with a local external app via subprocess. Only operates on the single file
    being viewed (uses backend FETCH_FILE RPC).
    """
    if http_client.token is None:
        http_client.token = session.get("session_token")

    data = request.get_json(silent=True) or {}
    media_id = data.get("media_id")
    app_id = data.get("app_id")

    if not media_id or not app_id:
        return jsonify({"status": "ERROR", "error_msg": "missing media_id or app_id"}), 400

    try:
        from client.services.open_with_service import OpenWithService
    except Exception as e:
        current_app.logger.exception("failed importing OpenWithService")
        return jsonify({"status": "ERROR", "error_msg": "server misconfiguration: open_with service unavailable"}), 500

    res = OpenWithService.open_media(media_id, app_id)
    if res.get("status") == "OK":
        return jsonify({"status": "OK", "message": res.get("message")}), 200
    return jsonify({"status": "ERROR", "error_msg": res.get("error_msg", "Unknown error")}), 400