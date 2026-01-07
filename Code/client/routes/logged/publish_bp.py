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

@publish_bp.route('/resolve_user', methods=['POST'])
def resolve_user():
    """Resolve a username to an internal user id for publish-on-behalf.
    Accepts JSON { username: '...' } and returns { status: 'OK', id: <int> } or an error.
    """
    if http_client.token is None:
        http_client.token = session.get('session_token')

    payload = request.get_json() or {}
    username = (payload.get('username') or '').strip()
    if not username:
        return jsonify({'status': 'ERROR', 'error_msg': 'Missing username'}), 400

    try:
        # Best-effort: ask profile service for the user
        from client.services.profile_service import ProfileService
        res = ProfileService.get_profile(username)
        current_app.logger.debug(f"[resolve_user] ProfileService.get_profile response: {res!r}")
        if isinstance(res, dict) and res.get('status') in (None, 'OK') and isinstance(res.get('user'), dict):
            uid = res['user'].get('id')
            if uid:
                return jsonify({'status': 'OK', 'id': uid})
        # not found
        return jsonify({'status': 'ERROR', 'error_msg': 'User not found'}), 404
    except Exception as e:
        current_app.logger.debug(f"[resolve_user] error: {e}")
        return jsonify({'status': 'ERROR', 'error_msg': str(e)}), 500

def _extract_entity_id(resp):
    # Try common patterns to extract an entity id from nested RPC responses
    try:
        inner = resp if isinstance(resp, dict) else {}
        seen = set()
        while isinstance(inner, dict):
            if id(inner) in seen:
                break
            seen.add(id(inner))
            if 'id' in inner:
                return inner.get('id')
            for key in ('response','result','media','created','entity'):
                if key in inner and isinstance(inner[key], dict):
                    inner = inner[key]
                    break
                if key in inner and isinstance(inner[key], (int,str)):
                    return inner[key]
            else:
                break
    except Exception:
        pass
    return None


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

        # Process linked files (from client-side multi-upload) if present
        linked_files_payload = []
        linked_meta = json.loads(request.form.get('linked_files_meta') or '[]')
        # create a quick lookup dict for suggested types: {filename: suggested_type}
        suggested_map = {m.get('filename'): m.get('suggested_type') for m in (linked_meta if isinstance(linked_meta, list) else [])}
        for f in request.files.getlist("linked_files"):
            data = f.read()
            linked_files_payload.append({
                "filename": f.filename,
                "content_b64": base64.b64encode(data).decode("ascii"),
                "content_type": f.content_type,
                "suggested_type": suggested_map.get(f.filename)
            })

        # If files need to be stored, save them via SAVE_FILE RPC before creating media; point stored_at accordingly
        stored_at = None
        if files_payload:
            # map logical media types to storage keys used by storage_manager (song/video/document)
            save_type_map = {"audio": "song", "song": "song", "video": "video", "document": "document"}
            folder_map = {"song": "songs", "video": "videos", "document": "documents"}
            file_type_for_save = save_type_map.get(media_type, "document")
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

        # Save linked files if present and build linked_media entries
        linked_media_entries = []
        if linked_files_payload:
            folder_map = {"song": "songs", "video": "videos", "document": "documents"}
            save_type_map = {"audio": "song", "song": "song", "video": "video", "document": "document"}
            for file_obj in linked_files_payload:
                filename = file_obj.get("filename")
                b64 = file_obj.get("content_b64")
                suggested = file_obj.get("suggested_type") or "document"
                file_type_for_save = save_type_map.get(suggested, "document")
                save_res = http_client.send_request("SAVE_FILE", [file_type_for_save, filename, b64], require_auth=True)
                if not isinstance(save_res, dict) or save_res.get("status") not in (None, "OK"):
                    return jsonify({"status":"ERROR","error_msg":f"Failed to save linked file {filename}: {save_res}"}), 500
                # build stored path (server uses folder mapping)
                folder = folder_map.get(file_type_for_save, 'documents')
                stored_path = f"server/storage/{folder}/{filename}"
                linked_media_entries.append({"filename": filename, "stored_at": stored_path, "type": file_type_for_save})

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
            "linked_media": linked_media_entries if linked_media_entries else [],
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

        # if main creation failed, return error immediately
        if not isinstance(res, dict) or res.get('status') == 'ERROR':
            return jsonify(res)

        main_id = _extract_entity_id(res) or res.get('id')

        # Create linked media entries (children) and attach linked_to / protagonist to each
        linked_children = []
        if main_id and linked_files_payload:
            child_cmd_map = {"video":"CREATE_VIDEO", "audio":"CREATE_SONG", "document":"CREATE_DOCUMENT", "concert":"CREATE_CONCERT"}
            folder_map = {"song": "songs", "video": "videos", "document": "documents"}
            save_type_map = {"audio": "song", "song": "song", "video": "video", "document": "document"}
            for file_obj in linked_files_payload:
                filename = file_obj.get('filename')
                suggested = (file_obj.get('suggested_type') or 'document')
                file_type_for_save = save_type_map.get(suggested, 'document')
                folder = folder_map.get(file_type_for_save, 'documents')
                stored_path = f"server/storage/{folder}/{filename}"

                # build a child payload that inherits logical fields from the protagonist when available
                child_payload = {
                    "title": filename,
                    "authors": [],
                    "genre": "",
                    "composition_year": None,
                    "type": suggested,
                    "stored_at": stored_path,
                    "linked_to": main_id,
                    "protagonist": main_id,
                    "files": []
                }

                # Inherit sensible fields from the main payload when they make sense
                try:
                    parent_title = payload.get("title") if isinstance(payload, dict) else None
                    if parent_title and parent_title.strip():
                        # make child title more descriptive if possible
                        child_payload["title"] = f"{parent_title} — {filename}"

                    # authors/performers/genre/description/tags
                    if payload.get("authors"):
                        child_payload["authors"] = list(payload.get("authors"))
                    if payload.get("performers") and suggested in ("audio", "song", "video"):
                        child_payload["performers"] = list(payload.get("performers"))
                    if payload.get("genre"):
                        child_payload["genre"] = payload.get("genre")
                    if payload.get("description"):
                        child_payload["description"] = payload.get("description")
                    if payload.get("tags"):
                        child_payload["tags"] = payload.get("tags")
                    if payload.get("composition_year"):
                        child_payload["composition_year"] = int(payload.get("composition_year")) if payload.get("composition_year") else None
                    if payload.get("is_live") is not None:
                        child_payload["is_live"] = bool(payload.get("is_live"))
                except Exception as e:
                    current_app.logger.debug(f"[publish_content] error while inheriting parent fields for child {filename}: {e}")

                cmd_child = child_cmd_map.get(suggested, "CREATE_DOCUMENT")
                child_res = http_client.send_request(cmd_child, [child_payload], require_auth=True)

                # try to extract created child id and attach to linked entries
                try:
                    child_id = _extract_entity_id(child_res)
                except Exception:
                    child_id = None

                entry = {"filename": filename, "stored_at": stored_path, "response": child_res}
                if child_id:
                    entry["id"] = child_id
                    # also update the linked_media_entries payload so protagonist links to child id if present
                    for lm in linked_media_entries:
                        if lm.get("filename") == filename and not lm.get("id"):
                            lm["id"] = child_id
                linked_children.append(entry)

        # attach children info to response for visibility
        if isinstance(res, dict) and linked_children:
            res['linked_children'] = linked_children

        # ensure protagonist media record contains linked_media information (try update, non-fatal on failure)
        if main_id and linked_media_entries:
            update_cmd_map = {"audio":"UPDATE_SONG", "video":"UPDATE_VIDEO", "document":"UPDATE_DOCUMENT", "concert":"UPDATE_CONCERT"}
            update_cmd = update_cmd_map.get(media_type)
            if update_cmd:
                try:
                    update_payload = {"linked_media": linked_media_entries}
                    upd_res = http_client.send_request(update_cmd, [main_id, update_payload], require_auth=True)
                    if isinstance(res, dict):
                        res['linked_media_update'] = upd_res
                except Exception as e:
                    current_app.logger.debug(f"[publish_content] failed to attach linked_media to protagonist: {e}")

        return jsonify(res)
    except Exception as e:
        return jsonify({"status":"ERROR","error_msg": str(e)}), 500

# last line