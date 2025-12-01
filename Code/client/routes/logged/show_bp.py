from flask import Blueprint, render_template, jsonify, request, session, current_app, send_file
from client.services.show_service import ShowService
from client.services.http_helper import http_client
import base64, io, mimetypes, os

show_bp = Blueprint("show", __name__, url_prefix="/show")

@show_bp.route("/", methods=["GET"])
def show_page():
    # Renders the template; the JS in the template will request /show/data?media_id=...
    return render_template("show.html")

@show_bp.route("/data", methods=["GET"])
def show_data():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    media_id = request.args.get("media_id") or request.args.get("id")
    if not media_id:
        return jsonify({"error": "missing media_id"}), 400

    resp = ShowService.get_media(media_id)
    current_app.logger.debug(f"[DEBUG] ShowService.get_media returned: {resp!r}")

    # Robustly unwrap nested RPC envelopes like {"response": {...}} or {"response": {"response": {...}}}
    inner = resp
    if isinstance(inner, dict):
        # If top-level status indicates error, prefer error path
        if inner.get("status") and str(inner.get("status")).lower() != "ok":
            # try to find nested error message
            err = None
            if isinstance(inner.get("response"), dict):
                err = inner["response"].get("error_msg") or inner["response"].get("error")
            err = err or inner.get("error_msg") or inner.get("error") or "Unknown error"
            return jsonify({"error": err}), 400

        # unwrap layers
        seen = set()
        while isinstance(inner, dict) and ("response" in inner or "result" in inner or "media" in inner):
            candidate = inner.get("response") or inner.get("result") or inner.get("media")
            # guard against infinite loops
            key_id = id(candidate)
            if candidate is None or key_id in seen:
                break
            seen.add(key_id)
            inner = candidate

        # now `inner` should be the media dict or something similar
        if not isinstance(inner, dict):
            return jsonify({"error": "invalid response from backend"}), 400

        # normalize common fields so the client JS can rely on them
        # map media_id -> id
        if "media_id" in inner and "id" not in inner:
            inner["id"] = inner.get("media_id")

        # map stored_at -> file/filename
        stored = inner.get("stored_at") or inner.get("stored") or inner.get("file_path")
        if stored:
            inner["file"] = inner.get("file") or stored
            inner["filename"] = inner.get("filename") or os.path.basename(stored)

        # if server used 'stored_at' under different key 'stored_at'
        if "stored_at" in inner and not inner.get("file"):
            inner["file"] = inner.get("stored_at")
            inner["filename"] = inner.get("filename") or os.path.basename(inner.get("stored_at") or "")

        # ensure type/title present
        if not any(k in inner for k in ("id","media_id","title","type")):
            return jsonify({"error": "media not found"}), 400

        return jsonify(inner)

    # fallback
    return jsonify({"error": "invalid response from backend"}), 400

@show_bp.route("/comment", methods=["POST"])
def post_comment():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    data = request.get_json(silent=True) or {}
    media_id = data.get("media_id")
    text = data.get("text", "").strip()
    if not media_id or not text:
        return jsonify({"error": "missing media_id or text"}), 400

    resp = ShowService.post_comment(media_id, text)
    current_app.logger.debug(f"[DEBUG] ShowService.post_comment returned: {resp!r}")
    # accept many shapes; consider success if backend returns status OK or numeric success
    if isinstance(resp, dict) and (resp.get("status") == "OK" or resp.get("result") == "OK" or resp.get("success") is True):
        return jsonify({"status": "OK"}), 200
    # fallback: if backend returned 200 but payload unknown, return 200 anyway
    return jsonify({"status": "posted"}), 200

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
        content = base64.b64decode(b64)
    except Exception:
        return ("", 500)

    mt, _ = mimetypes.guess_type(filename)
    mimetype = mt or "application/octet-stream"
    return send_file(io.BytesIO(content), mimetype=mimetype, download_name=filename)

@show_bp.route("/comments", methods=["GET"])
def get_comments():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    media_id = request.args.get("media_id")
    if not media_id:
        return jsonify([])

    res = ShowService.get_comments(media_id, offset=0, limit=200)
    # normalize shapes
    if isinstance(res, dict) and res.get("status") in (None, "OK"):
        payload = res.get("response") or res.get("results") or []
        if isinstance(payload, dict) and "results" in payload:
            payload = payload["results"]
        if not isinstance(payload, list):
            payload = []
        return jsonify(payload)
    elif isinstance(res, list):
        return jsonify(res)
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