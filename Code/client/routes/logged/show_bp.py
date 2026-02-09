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
                for k in ("username","tags","author_names","authors","performers","segments","subtracks","duration_display","duration_seconds","filename","file","link","description","embed_url","embed_ok","embed_error"):
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

    # Build concise objects the template expects: logged, publisher, commenter
    logged = None
    if server_user and isinstance(server_user, dict):
        try:
            logged = {
                "id": server_user.get("id"),
                "username": server_user.get("username"),
                "lvl": int(server_user.get("lvl")) if server_user.get("lvl") is not None else None
            }
        except Exception:
            logged = {"id": server_user.get("id"), "username": server_user.get("username"), "lvl": server_user.get("lvl")}

    publisher = None
    if initial_media and isinstance(initial_media, dict):
        pub_id = initial_media.get("uploader_id") or initial_media.get("user_id") or initial_media.get("owner_id") or None
        pub_username = initial_media.get("username") or initial_media.get("uploader") or None
        # try to fetch publisher profile when we have a username
        if pub_username:
            try:
                pprof = ProfileService.get_profile(pub_username)
                if isinstance(pprof, dict) and pprof.get("status") in (None, "OK") and isinstance(pprof.get("user"), dict):
                    pu = pprof["user"]
                    publisher = {"id": pu.get("id"), "username": pu.get("username"), "lvl": int(pu.get("lvl")) if pu.get("lvl") is not None else None}
                else:
                    publisher = {"id": pub_id, "username": pub_username, "lvl": None}
            except Exception:
                publisher = {"id": pub_id, "username": pub_username, "lvl": None}
        elif pub_id:
            publisher = {"id": pub_id, "username": None, "lvl": None}

    # commenter not known at page render time; leave as null placeholder
    commenter = None

    return render_template("show.html",
                        INITIAL_MEDIA=json.dumps(initial_media) if initial_media is not None else "null",
                        SERVER_USER=json.dumps(server_user) if server_user is not None else "null",
                        SERVER_LOGGED=json.dumps(logged) if logged is not None else "null",
                        SERVER_PUBLISHER=json.dumps(publisher) if publisher is not None else "null",
                        SERVER_COMMENTER=json.dumps(commenter) if commenter is not None else "null")

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
            for k in ("tags","author_names","authors","performers","segments","subtracks","duration_display","duration_seconds","filename","file","link","description","embed_url","embed_ok","embed_error"):
                if k in candidate and k not in media_dict:
                    media_dict[k] = candidate[k]

            # concert detection debug
            if media_dict.get('type') == 'concert' or (media_dict.get('link') and 'youtube' in str(media_dict.get('link')).lower()):
                current_app.logger.debug(f"[DEBUG][show_data] Detected concert media_id={media_id}, type={media_dict.get('type')}, link={media_dict.get('link')}")

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
    if not isinstance(res, dict) or res.get("status") not in (None, "OK"):
        return ("", 404)

    # Unwrap possible nested envelopes and extract base64 payload
    b64 = None
    if isinstance(res, dict):
        b64 = res.get("response") or res.get("data") or res.get("file") or None
        if isinstance(b64, dict) and "response" in b64:
            b64 = b64.get("response")

    if not b64:
        current_app.logger.debug(f"[show_file] no file data returned for {file_type}/{filename}: {res!r}")
        return ("", 404)

    try:
        import base64, io, mimetypes
        content = base64.b64decode(b64)
    except Exception:
        current_app.logger.exception("Failed to decode file content")
        return ("", 500)

    mt, _ = mimetypes.guess_type(filename)
    mimetype = mt or "application/octet-stream"
    return send_file(io.BytesIO(content), mimetype=mimetype, download_name=filename) 

# --------------------
# CONCERT SEGMENTS (proxy endpoints for client-side JS)
# --------------------
@show_bp.route('/segments', methods=['GET'])
def list_segments():
    if http_client.token is None:
        http_client.token = session.get('session_token')
    media_id = request.args.get('media_id') or request.args.get('video_id')
    if not media_id:
        return jsonify({'error': 'missing media_id'}), 400
    try:
        current_app.logger.debug(f"[DEBUG][list_segments] media_id={media_id}")
        res = ShowService.get_concert_segments(media_id)
        current_app.logger.debug(f"[DEBUG][list_segments] result: {res!r}")
        return jsonify(res)
    except Exception as e:
        current_app.logger.exception('Failed to fetch concert segments')
        return jsonify({'error': str(e)}), 500

@show_bp.route('/segments', methods=['POST'])
def create_segment():
    if http_client.token is None:
        http_client.token = session.get('session_token')
    payload = request.get_json(silent=True) or {}
    video_id = payload.get('video_id') or payload.get('media_id')
    segment = payload.get('segment') or {}
    if not video_id or not isinstance(segment, dict):
        return jsonify({'error': 'missing video_id or segment'}), 400
    try:
        current_app.logger.debug(f"[DEBUG][create_segment] video_id={video_id}, segment={segment}")
        res = ShowService.add_concert_segment(video_id, segment)
        current_app.logger.debug(f"[DEBUG][create_segment] result: {res!r}")
        return jsonify(res)
    except Exception as e:
        current_app.logger.exception('Failed to add segment')
        return jsonify({'error': str(e)}), 500

@show_bp.route('/segments/<int:segment_id>', methods=['PUT'])
def update_segment(segment_id):
    if http_client.token is None:
        http_client.token = session.get('session_token')
    updates = request.get_json(silent=True) or {}
    try:
        current_app.logger.debug(f"[DEBUG][update_segment] segment_id={segment_id}, updates={updates}")
        res = ShowService.update_concert_segment(segment_id, updates)
        current_app.logger.debug(f"[DEBUG][update_segment] result: {res!r}")
        return jsonify(res)
    except Exception as e:
        current_app.logger.exception('Failed to update segment')
        return jsonify({'error': str(e)}), 500


@show_bp.route('/notes', methods=['GET'])
def list_notes():
    """Fetch notes for a media and return normalized JSON list."""
    if http_client.token is None:
        http_client.token = session.get('session_token')
    media_id = request.args.get('media_id') or request.args.get('id')
    if not media_id:
        return jsonify({'notes': []})
    try:
        current_app.logger.debug(f"[DEBUG][list_notes] media_id={media_id}")
        response = http_client.send_request("FETCH_NOTE", [media_id], require_auth=True)
        current_app.logger.debug(f"[DEBUG][list_notes] raw response: {response!r}")
        # Normalize shapes: expect {'status':'OK','notes':[...]} or direct list
        notes = []
        if isinstance(response, dict):
            if response.get('status') not in (None, 'OK'):
                return jsonify({'notes': []})
            payload = response.get('notes') or response.get('response') or response.get('results') or []
            if isinstance(payload, list):
                notes = payload
            elif isinstance(payload, dict) and 'notes' in payload and isinstance(payload['notes'], list):
                notes = payload['notes']
        elif isinstance(response, list):
            notes = response
        # ensure list
        if not isinstance(notes, list): notes = []
        return jsonify({'notes': notes})
    except Exception as e:
        current_app.logger.exception('Failed to fetch notes')
        return jsonify({'notes': []})

    if http_client.token is None:
        http_client.token = session.get('session_token')
    updates = request.get_json(silent=True) or {}
    try:
        current_app.logger.debug(f"[DEBUG][update_segment] segment_id={segment_id}, updates={updates}")
        res = ShowService.update_concert_segment(segment_id, updates)
        current_app.logger.debug(f"[DEBUG][update_segment] result: {res!r}")
        return jsonify(res)
    except Exception as e:
        current_app.logger.exception('Failed to update segment')
        return jsonify({'error': str(e)}), 500

@show_bp.route('/segments/<int:segment_id>', methods=['DELETE'])
def delete_segment(segment_id):
    if http_client.token is None:
        http_client.token = session.get('session_token')
    try:
        current_app.logger.debug(f"[DEBUG][delete_segment] segment_id={segment_id}")
        res = ShowService.delete_concert_segment(segment_id)
        current_app.logger.debug(f"[DEBUG][delete_segment] result: {res!r}")
        return jsonify(res)
    except Exception as e:
        current_app.logger.exception('Failed to delete segment')
        return jsonify({'error': str(e)}), 500


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

    # If updating a link, sanitize and validate YouTube links when applicable
    if 'link' in sanitized and sanitized.get('link'):
        raw_link = str(sanitized.get('link'))
        cleaned = raw_link.strip().strip('"').strip("'")
        if cleaned and not cleaned.startswith(("http://","https://")):
            cleaned = "https://" + cleaned
        # If it looks like YouTube, ensure we can extract a valid 11-char id
        try:
            import re
            if re.search(r"youtube\.com|youtu\.be", cleaned, flags=re.I):
                ytm = re.search(r"(?:v=|/embed/|youtu\.be/)([A-Za-z0-9_-]{11})", cleaned)
                if not ytm:
                    ytm = re.search(r"youtube\.com/watch\?[^#]*v=([A-Za-z0-9_-]{11})", cleaned)
                if not ytm:
                    return jsonify({"status":"ERROR","error_msg":"Invalid YouTube link"}), 400
        except Exception:
            return jsonify({"status":"ERROR","error_msg":"Invalid link"}), 400
        sanitized['link'] = cleaned

    res = ShowService.edit_media(media_id, media_type or media_dict.get("type"), sanitized)
    return jsonify(res or {"status":"ERROR","error_msg":"no response from backend"})

@show_bp.route('/validate_youtube', methods=['POST'])
def validate_youtube():
    """Validate a YouTube URL and return a canonical video id + embed url.
    Accepts JSON { url: '...' } and returns { status:'OK', video_id:'...', embed_url:'...' } or a 400 with error.
    """
    data = request.get_json(silent=True) or {}
    url = (data.get('url') or '').strip()
    if not url:
        return jsonify({'status':'ERROR','error_msg':'missing url'}), 400
    cleaned = url.strip().strip('"').strip("'")
    if cleaned and not cleaned.startswith(("http://","https://")):
        cleaned = "https://" + cleaned
    try:
        import re
        ytm = re.search(r"(?:v=|/embed/|youtu\.be/)([A-Za-z0-9_-]{11})", cleaned)
        if not ytm:
            ytm = re.search(r"youtube\.com/watch\?[^#]*v=([A-Za-z0-9_-]{11})", cleaned)
        if not ytm:
            return jsonify({'status':'ERROR','error_msg':'invalid youtube url'}), 400
        vid = ytm.group(1)
        current_app.logger.debug(f"[DEBUG][validate_youtube] cleaned={cleaned}, vid={vid}")
        return jsonify({'status':'OK','video_id':vid,'embed_url':f'https://www.youtube.com/embed/{vid}?rel=0','cleaned':cleaned})
    except Exception as e:
        return jsonify({'status':'ERROR','error_msg':str(e)}), 400


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

        # --- ENRICH: ensure top-level comments have commenter level when possible ---
        try:
            # collect all comments missing level by username / id (include replies)
            to_query = {}  # key -> [comment_dicts]
            for c in payload:
                try:
                    if not isinstance(c, dict):
                        continue

                    # already has level?
                    lvl = None
                    if isinstance(c.get('user'), dict):
                        lvl = c['user'].get('lvl') if c['user'].get('lvl') is not None else c['user'].get('level')
                    if lvl is None:
                        lvl = c.get('lvl') if c.get('lvl') is not None else c.get('level')
                    if lvl is not None:
                        continue

                    # extract identifier
                    uname = None
                    uid = None
                    if isinstance(c.get('user'), dict):
                        uname = c['user'].get('username') or uname
                        uid = c['user'].get('id') or c['user'].get('user_id') or uid
                    uname = uname or c.get('username') or c.get('author') or c.get('author_username')
                    uid = uid or c.get('user_id') or c.get('author_id')

                    if uname:
                        to_query.setdefault(('username', str(uname)), []).append(c)
                    elif uid:
                        to_query.setdefault(('user_id', str(uid)), []).append(c)
                except Exception:
                    current_app.logger.debug("skipping malformed comment while preparing level enrichment", exc_info=True)

            # query profile service for each distinct identifier and write back lvl
            for (kind, ident), clist in to_query.items():
                try:
                    prof = ProfileService.get_profile(ident)
                    if isinstance(prof, dict) and prof.get("status") in (None, "OK") and isinstance(prof.get("user"), dict):
                        u = prof["user"]
                        lvl_val = u.get("lvl") if u.get("lvl") is not None else u.get("level")
                        if lvl_val is not None:
                            try:
                                lvl_val = int(lvl_val)
                            except Exception:
                                pass
                            for c in clist:
                                if 'user' not in c or not isinstance(c['user'], dict):
                                    c['user'] = {}
                                c['user']['lvl'] = lvl_val
                                c['lvl'] = lvl_val
                except Exception:
                    current_app.logger.debug(f"failed to fetch profile for {ident}", exc_info=True)
        except Exception:
            current_app.logger.exception("failed to enrich comment levels")

        # --- ANNOTATE: assign a 'type' to each comment based on commenter and media info ---
        try:
            # fetch media once and normalize
            media_resp = ShowService.get_media(media_id)
            candidate = None
            if isinstance(media_resp, dict):
                status = media_resp.get("status")
                if status and str(status).lower() not in ("ok", "true", "accepted"):
                    candidate = None
                else:
                    for k in ("response", "result", "media"):
                        if isinstance(media_resp.get(k), dict):
                            candidate = media_resp.get(k)
                            break
            if isinstance(candidate, dict):
                media_obj = Media.from_server(candidate)
                media_dict = media_obj.to_dict()
            else:
                media_dict = {}
        except Exception:
            media_dict = {}

        def _get_commenter_info(c):
            uid = None
            lvl = None
            if isinstance(c.get('user'), dict):
                uid = c['user'].get('id') or c['user'].get('user_id')
                lvl = c['user'].get('lvl') if c['user'].get('lvl') is not None else c['user'].get('level')
            uid = uid or c.get('user_id') or c.get('author_id')
            if lvl is None:
                lvl = c.get('lvl') if c.get('lvl') is not None else c.get('level')
            try:
                if lvl is not None:
                    lvl = int(lvl)
            except Exception:
                pass
            return (str(uid) if uid is not None else None, lvl)

        # collect potential artist ids from common keys
        artist_ids = set()
        for key in ('authors', 'author_ids', 'author', 'performers', 'interpreters', 'interpreter'):
            val = media_dict.get(key)
            if not val:
                continue
            if isinstance(val, list):
                for v in val:
                    if isinstance(v, dict):
                        vid = v.get('id') or v.get('user_id') or v.get('author_id')
                        if vid is not None:
                            artist_ids.add(str(vid))
                    else:
                        artist_ids.add(str(v))
            else:
                artist_ids.add(str(val))

        publisher_id = media_dict.get('uploader_id') or media_dict.get('user_id') or media_dict.get('owner_id') or media_dict.get('publisher_id')
        publisher_id = str(publisher_id) if publisher_id is not None else None

        for c in payload:
            try:
                commenter_id, commenter_lvl = _get_commenter_info(c)
                ctype = None
                # 1. publisher
                if commenter_id and publisher_id and commenter_id == publisher_id:
                    ctype = 'publisher'
                # 2. admin (levels 0 or 1)
                elif commenter_lvl in (0,1):
                    ctype = 'admin'
                # 3. mod
                elif commenter_lvl == 2:
                    ctype = 'mod'
                # 4. artist
                elif commenter_id and commenter_id in artist_ids:
                    ctype = 'artist'
                # 5. regular lvl 4
                elif commenter_lvl == 4:
                    ctype = 'regular'
                # 6. lvl 3 but not publisher -> regular
                elif commenter_lvl == 3 and (not commenter_id or commenter_id != publisher_id):
                    ctype = 'regular'
                else:
                    ctype = 'regular'
                c['type'] = ctype
            except Exception:
                # be conservative: do not fail comment listing on errors
                continue

        return jsonify(payload)
    elif isinstance(res, list):
        current_app.logger.debug(f"[DEBUG] ShowService.get_comments returned list length: {len(res)}")
        return jsonify(res)
    current_app.logger.debug("[DEBUG] ShowService.get_comments returned unexpected shape; returning empty list")
    return jsonify([])

@show_bp.route('/comment/delete', methods=['POST'])
def delete_comment():
    if http_client.token is None:
        http_client.token = session.get('session_token')
    data = request.get_json(silent=True) or {}
    comment_id = data.get('comment_id')
    if not comment_id:
        return jsonify({'status':'ERROR','error_msg':'missing comment_id'}), 400
    res = ShowService.delete_comment(comment_id)
    current_app.logger.debug(f"[DEBUG] ShowService.delete_comment returned: {res!r}")
    if isinstance(res, dict) and res.get('status') in (None, 'OK'):
        return jsonify({'status':'OK'})
    err = res.get('error_msg') if isinstance(res, dict) else 'Backend error'
    return jsonify({'status':'ERROR','error_msg':err}), 400

@show_bp.route('/comment/edit', methods=['POST'])
def edit_comment():
    if http_client.token is None:
        http_client.token = session.get('session_token')
    data = request.get_json(silent=True) or {}
    comment_id = data.get('comment_id')
    new_text = (data.get('new_text') or data.get('text') or '').strip()
    if not comment_id or not new_text:
        return jsonify({'status':'ERROR','error_msg':'missing comment_id or text'}), 400
    res = ShowService.edit_comment(comment_id, new_text)
    current_app.logger.debug(f"[DEBUG] ShowService.edit_comment returned: {res!r}")
    if isinstance(res, dict) and res.get('status') in (None, 'OK'):
        return jsonify({'status':'OK'})
    err = res.get('error_msg') if isinstance(res, dict) else 'Backend error'
    return jsonify({'status':'ERROR','error_msg':err}), 400

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


@show_bp.route("/note/create", methods=["POST"])
def create_note():
    if http_client.token is None:
        http_client.token = session.get('session_token')

    data = request.get_json(silent=True) or {}
    media_id = data.get('media_id')
    note_type = data.get('type', 1)  # 0=graphic, 1=text
    start = data.get('start')
    end = data.get('end')
    text = data.get('text', "")
    private = data.get('private', False)
    media_type = data.get('media_type')
    stored_at = data.get('stored_at', None)  # optional base64 data URI for graphic notes

    if not media_id:
        return jsonify({"status": "ERROR", "error_msg": "Missing required field: media_id"}), 400

    try:
        # For document notes, normalize start/end to 0 and embed spatial anchor into text
        if media_type == 'document':
            start = 0
            end = 0
            anchor = data.get('anchor') or None
            if anchor:
                try:
                    import json as _json
                    parsed = {}
                    if text:
                        try:
                            parsed = _json.loads(text)
                            if not isinstance(parsed, dict):
                                parsed = {'raw_text': str(text)}
                        except Exception:
                            parsed = {'raw_text': str(text)}
                    parsed['anchor'] = anchor
                    text = _json.dumps(parsed)
                except Exception:
                    # if embedding anchor fails, continue with original text
                    pass

        # Build payload for backend CREATE_NOTE
        payload = {
            "media_id": media_id,
            "start": start,
            "end": end,
            "type": note_type,
            "text": text,
            "private": private,
            "stored_at": stored_at,
            "stored_at": stored_at
        }


        response = http_client.send_request("CREATE_NOTE", [payload], require_auth=True)
        current_app.logger.debug(f"[DEBUG] create_note response: {response!r}")

        if isinstance(response, dict):
            if response.get("status") in (None, "OK"):
                # backend may return 'id' or 'note_id'
                note_id = response.get('id') or response.get('note_id') or None
                return jsonify({"status": "OK", "note_id": note_id}), 200
            else:
                return jsonify({"status": "ERROR", "error_msg": response.get("error_msg", "Failed to create note")}), 400

        return jsonify({"status": "OK"}), 200
    except Exception as e:
        current_app.logger.exception("Error creating note")
        return jsonify({"status": "ERROR", "error_msg": str(e)}), 500


@show_bp.route('/note/delete', methods=['POST'])
def delete_note():
    if http_client.token is None:
        http_client.token = session.get('session_token')

    data = request.get_json(silent=True) or {}
    note_id = data.get('note_id') or data.get('id')
    if not note_id:
        return jsonify({'status': 'ERROR', 'error_msg': 'missing note_id'}), 400

    try:
        res = http_client.send_request('DELETE_NOTE', [note_id], require_auth=True)
        current_app.logger.debug(f"[DEBUG] DELETE_NOTE response: {res!r}")
        if isinstance(res, dict) and res.get('status') in (None, 'OK'):
            return jsonify({'status': 'OK', 'id': note_id}), 200
        err = res.get('error_msg') if isinstance(res, dict) else 'Backend error'
        return jsonify({'status': 'ERROR', 'error_msg': err}), 400
    except Exception as e:
        current_app.logger.exception('Failed to delete note')
        return jsonify({'status': 'ERROR', 'error_msg': str(e)}), 500


@show_bp.route('/fix_metadata', methods=['POST'])
def fix_metadata():
    if http_client.token is None:
        http_client.token = session.get('session_token')

    data = request.get_json(silent=True) or {}
    media_id = data.get('media_id') or request.args.get('media_id')
    if not media_id:
        return jsonify({"status": "ERROR", "error_msg": "media_id required"}), 400

    try:
        # Ask backend to probe and persist document metadata
        res = http_client.send_request('FIX_DOCUMENT_METADATA', [int(media_id)], require_auth=True)
        current_app.logger.debug(f"[fix_metadata] FIX_DOCUMENT_METADATA response: {res!r}")
    except Exception as e:
        current_app.logger.debug(f"[fix_metadata] error calling FIX_DOCUMENT_METADATA: {e}")
        return jsonify({"status": "ERROR", "error_msg": str(e)}), 500

    # Return fresh media data so client can update immediately
    try:
        media_resp = ShowService.get_media(media_id)
        current_app.logger.debug(f"[fix_metadata] raw fresh media: {media_resp!r}")
        # Normalize shapes the same way /show/data does so client receives consistent media dict
        candidate = None
        if isinstance(media_resp, dict):
            status = media_resp.get("status")
            if status and str(status).lower() not in ("ok", "true", "accepted"):
                # backend returned error; still return fix result
                return jsonify({"status": "OK", "fix_result": res, "media": None}), 200
            for k in ("response", "result", "media"):
                if k in media_resp and media_resp[k]:
                    candidate = media_resp[k]
                    break
            if candidate is None:
                candidate = media_resp
        else:
            candidate = None

        media_dict = None
        if isinstance(candidate, dict):
            media_obj = Media.from_server(candidate)
            media_dict = media_obj.to_dict()
            # copy legacy fields if present
            for k in ("tags","author_names","authors","performers","segments","subtracks","duration_display","duration_seconds","filename","file","link","description","embed_url","embed_ok","embed_error","username"):
                if k in candidate and k not in media_dict:
                    media_dict[k] = candidate[k]

        return jsonify({"status": "OK", "fix_result": res, "media": media_dict}), 200
    except Exception as e:
        current_app.logger.debug(f"[fix_metadata] error fetching media after fix: {e}")
        return jsonify({"status": "OK", "fix_result": res}), 200
    """Create a note for a media item."""
    if http_client.token is None:
        return jsonify({"status": "ERROR", "error_msg": "Non autenticato"}), 401

    data = request.get_json(silent=True) or {}
    media_id = data.get("media_id")
    note_type = data.get("type", 1)  # 0=graphic, 1=text
    start = data.get("start")
    end = data.get("end")
    text = data.get("text", "")
    private = data.get("private", False)
    media_type = data.get("media_type")

    if not media_id or start is None or end is None:
        return jsonify({"status": "ERROR", "error_msg": "Missing required fields: media_id, start, end"}), 400

    try:
        # Call the backend API to create the note
        payload = {
            "media_id": media_id,
            "start": start,
            "end": end,
            "type": note_type,
            "text": text,
            "private": private
        }
        
        response = http_client.send_request("CREATE_NOTE", [payload], require_auth=True)
        current_app.logger.debug(f"[DEBUG] create_note response: {response!r}")
        
        if isinstance(response, dict):
            if response.get("status") in (None, "OK"):
                return jsonify({"status": "OK", "note_id": response.get("note_id")}), 200
            else:
                return jsonify({"status": "ERROR", "error_msg": response.get("error_msg", "Failed to create note")}), 400
        
        return jsonify({"status": "OK"}), 200
    except Exception as e:
        current_app.logger.exception("Error creating note")
        return jsonify({"status": "ERROR", "error_msg": str(e)}), 500
