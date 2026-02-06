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
    target_username = None

    # Check if user is trying to publish on behalf of another user
    # This is read from the query param ?username=... passed from profile.html
    target_username = request.args.get("username")

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

    return render_template("publish.html", user_level=user_level, username=username, target_username=target_username)

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
    
    SECURITY: Validates that only users with admin/mod level (0-1) can publish on behalf
    of other users.
    """
    try:
        # Ensure authentication token is set
        if http_client.token is None:
            http_client.token = session.get("session_token")
        
        # SECURITY: Get logged-in user's profile to validate "publish on behalf" permission
        logged_user_info = None
        logged_user_level = None
        try:
            profile_res = http_client.send_request("GET_PROFILE", [], require_auth=True)
            if isinstance(profile_res, dict) and profile_res.get("status") in (None, "OK"):
                info = _unwrap_user_response(profile_res)
                if info and isinstance(info, dict):
                    logged_user_info = info
                    try:
                        logged_user_level = int(info.get("lvl"))
                    except (ValueError, TypeError):
                        pass
            current_app.logger.debug(f"[publish_content] logged user level: {logged_user_level!r}")
        except Exception as e:
            current_app.logger.debug(f"[publish_content] error fetching logged user profile: {e}")
        
        # Check if attempting to publish on behalf of another user
        target_username = (request.form.get("target_username") or "").strip()
        if target_username and logged_user_info and logged_user_info.get("username"):
            logged_username = logged_user_info.get("username")
            # If target_username differs from logged username, user is attempting publish-on-behalf
            if target_username != logged_username:
                # SECURITY: Only level 0 (admin) or 1 (moderator) can publish on behalf
                if logged_user_level is None or logged_user_level not in (0, 1):
                    current_app.logger.warning(
                        f"[publish_content] SECURITY: User '{logged_username}' (level {logged_user_level}) "
                        f"attempted to publish on behalf of '{target_username}' without permission"
                    )
                    return jsonify({
                        "status": "ERROR",
                        "error_msg": "Permission denied: Only administrators (level 0) and moderators (level 1) can publish on behalf of other users."
                    }), 403
        
        media_type = (request.form.get("type") or "").lower()
        title = (request.form.get("title") or "").strip()
        authors = json.loads(request.form.get("authors") or "[]")
        genres = (request.form.get("genres") or "").strip()
        year = request.form.get("year") or None

        performers = json.loads(request.form.get("performers") or "[]")
        segments = json.loads(request.form.get("segments") or "[]")
        subtracks = json.loads(request.form.get("subtracks") or "[]")
        
        # Capture description from form (used for all media types including concerts)
        description = (request.form.get("description") or "").strip()

        recording_date = request.form.get("recording_date")
        location = request.form.get("location", "").strip()

        format = request.form.get("format")
        additional_info = request.form.get("additional_info", "")

        event_title = request.form.get("event_title", "")
        concert_date = request.form.get("concert_date", "")
        concert_location = request.form.get("concert_location", "")
        link = request.form.get("link", "")
        
        # Extract publication_date for concerts
        publication_date = request.form.get("publication_date")
        # If year is not provided but publication_date is, extract year from it
        if not year and publication_date:
            try:
                year_from_date = publication_date.split('-')[0]
                year = int(year_from_date) if year_from_date.isdigit() else None
                print(f"[DEBUG][publish_content] Extracted year from publication_date: {year}")
            except Exception as e:
                print(f"[DEBUG][publish_content] Failed to extract year from publication_date: {e}")

        # optional helper: when publishing a concert we will build a linked_media entry for the YouTube link
        link_entry = None

        duration = request.form.get("duration") or None
        file_format = request.form.get("file_format") or None

        # read extra checkboxes
        is_author = bool(request.form.get("is_author"))
        is_performer = bool(request.form.get("is_performer"))
        instruments_used = request.form.get("instruments_used", "")
        is_live = bool(request.form.get("is_live"))

        # ===== DEBUG: Log all form fields extracted =====
        print(f"\n[DEBUG][publish_content] ===== FORM EXTRACTION START =====")
        print(f"[DEBUG][publish_content] media_type: {media_type}")
        print(f"[DEBUG][publish_content] title: {title}")
        print(f"[DEBUG][publish_content] year: {year}")
        print(f"[DEBUG][publish_content] publication_date: {publication_date}")
        print(f"[DEBUG][publish_content] duration: {duration}")
        print(f"[DEBUG][publish_content] description: {description}")
        print(f"[DEBUG][publish_content] recording_date: {recording_date}")
        print(f"[DEBUG][publish_content] location: {location}")
        print(f"[DEBUG][publish_content] is_author: {is_author}")
        print(f"[DEBUG][publish_content] is_performer: {is_performer}")
        print(f"[DEBUG][publish_content] authors: {authors}")
        print(f"[DEBUG][publish_content] performers: {performers}")
        print(f"[DEBUG][publish_content] genres: {genres}")
        # Normalize genres string into a list of tags (split on comma) to match server expectations
        if genres and isinstance(genres, str):
            try:
                genres = [s.strip() for s in genres.split(",") if s.strip()]
                print(f"[DEBUG][publish_content] normalized genres -> {genres}")
            except Exception as e:
                print(f"[DEBUG][publish_content] failed to normalize genres: {e}")
                genres = []

        # Normalize instruments string into a list
        instruments_list = []
        if isinstance(instruments_used, str):
            try:
                instruments_list = [s.strip() for s in instruments_used.split(",") if s.strip()]
                print(f"[DEBUG][publish_content] normalized instruments -> {instruments_list}")
            except Exception as e:
                print(f"[DEBUG][publish_content] failed to normalize instruments: {e}")
                instruments_list = []
        elif isinstance(instruments_used, list):
            instruments_list = instruments_used

        # If user declared performer, instruments are required
        if is_performer and not instruments_list:
            return jsonify({"status":"ERROR","error_msg":"You declared yourself performer: 'instruments_used' must be provided (comma separated)"}), 400

        print(f"[DEBUG][publish_content] link: {link}")
        print(f"[DEBUG][publish_content] additional_info: {additional_info}")
        print(f"[DEBUG][publish_content] ===== FORM EXTRACTION COMPLETE =====\n")

        # Basic validation per media type
        if media_type == "concert":
            if not link:
                return jsonify({"status":"ERROR","error_msg":"YouTube link required for concert"}), 400
            # sanitize + validate YouTube link
            try:
                cleaned = link.strip().strip('"').strip("'")
                current_app.logger.debug(f"[publish_content][concert] cleaned link (post trim): {cleaned!r}")
                if cleaned and not cleaned.startswith(("http://","https://")):
                    cleaned = "https://" + cleaned
                    current_app.logger.debug(f"[publish_content][concert] prefixed scheme: {cleaned!r}")
                import re
                ytm = re.search(r"(?:v=|/embed/|youtu\.be/)([A-Za-z0-9_-]{11})", cleaned)
                current_app.logger.debug(f"[publish_content][concert] primary regex match: {ytm}")
                if not ytm:
                    ytm = re.search(r"youtube\.com/watch\?[^#]*v=([A-Za-z0-9_-]{11})", cleaned)
                    current_app.logger.debug(f"[publish_content][concert] secondary regex match: {ytm}")
                if not ytm:
                    return jsonify({"status":"ERROR","error_msg":"Invalid YouTube link"}), 400
                # normalized link (server/backend will also sanitize); use cleaned
                link = cleaned

                # Extract video id and add an embed entry to linked_media so it gets persisted with the media record
                try:
                    vid = ytm.group(1)
                    embed_url = f"https://www.youtube.com/embed/{vid}?rel=0"
                    link_entry = {"type": "link", "source": "youtube", "url": link, "embed_url": embed_url, "youtube_id": vid, "title": event_title or title}
                except Exception as e_inner:
                    current_app.logger.debug(f"[publish_content][concert] failed to build link_entry: {e_inner}", exc_info=True)
                    # non-fatal: leave link_entry as None
                    link_entry = None
            except Exception as e:
                current_app.logger.debug(f"[publish_content][concert] error while validating youtube link: {e}", exc_info=True)
                return jsonify({"status":"ERROR","error_msg":"Invalid YouTube link"}), 400
            # validate subtracks (if present) - each must have title
            for st in subtracks:
                if not st.get("title"):
                    return jsonify({"status":"ERROR","error_msg":"each subtrack must have a title"}), 400
        elif media_type not in ("video", "audio", "document", "image", "song"):
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

        # Attach YouTube link entry (if any) so it persists under media.linked_media
        if link_entry:
            # Put link first so it's obvious client-side
            linked_media_entries.insert(0, link_entry)
            current_app.logger.debug(f"[publish_content][concert] inserted link_entry into linked_media_entries: {link_entry!r}; linked_media_entries now: {linked_media_entries!r}")

        # Build payload to forward to backend create command
        payload = {
            "title": title,
            "authors": authors,
            "genres": genres,
            "year": int(year) if year else None,
            "type": media_type,
            "duration": float(duration) if duration else None,
            "format": file_format,
            "stored_at": stored_at,
            "performers": performers,
            "segments": segments,
            "subtracks": subtracks,
            "description": description,
            "additional_info": additional_info,
            "event_title": event_title,
            "recording_date": recording_date,
            "location": location,
            "link": link,
            "is_author": is_author,
            "is_performer": is_performer,
            "instruments": instruments_list,
            "is_live": is_live,
            "linked_media": linked_media_entries if linked_media_entries else [],
            # do not forward raw file bytes (we saved them via SAVE_FILE)
            "files": [],
            # Include target_username for publish-on-behalf: server will use this instead of logged user
            "target_username": target_username if target_username else None
        }

        # ===== DEBUG: Log complete payload before sending =====
        print(f"\n[DEBUG][publish_content] ===== PAYLOAD BUILDING COMPLETE =====")
        print(f"[DEBUG][publish_content] Payload keys: {list(payload.keys())}")
        print(f"[DEBUG][publish_content] CRITICAL FIELDS IN PAYLOAD:")
        print(f"[DEBUG][publish_content]   - year: {payload.get('year')}")
        print(f"[DEBUG][publish_content]   - description: {payload.get('description')}")
        print(f"[DEBUG][publish_content]   - recording_date: {payload.get('recording_date')}")
        print(f"[DEBUG][publish_content]   - location: {payload.get('location')}")
        print(f"[DEBUG][publish_content]   - is_author: {payload.get('is_author')}")
        print(f"[DEBUG][publish_content]   - is_performer: {payload.get('is_performer')}")
        print(f"[DEBUG][publish_content] FULL PAYLOAD: {payload}")
        print(f"[DEBUG][publish_content] ===== READY TO SEND =====\n")

        # choose backend command
        cmd_map = {
            "video": "CREATE_VIDEO",
            "audio": "CREATE_SONG",
            "document": "CREATE_DOCUMENT",
            "concert": "CREATE_CONCERT"
        }
        cmd = cmd_map.get(media_type, "CREATE_SONG")
        # debug for concert payload and linked_media
        if media_type == 'concert':
            try:
                current_app.logger.debug(f"[publish_content][concert] CREATE payload keys: {list(payload.keys())}; linked_media: {payload.get('linked_media')!r}")
            except Exception as e_log:
                current_app.logger.debug(f"[publish_content][concert] failed logging payload: {e_log}")
        current_app.logger.debug(f"[publish_content] sending CREATE command {cmd} for type={media_type}")
        
        print(f"\n[DEBUG][publish_content] ===== SENDING TO BACKEND =====")
        print(f"[DEBUG][publish_content] Command: {cmd}")
        print(f"[DEBUG][publish_content] Media type: {media_type}")
        print(f"[DEBUG][publish_content] Payload keys being sent: {list(payload.keys())}")
        print(f"[DEBUG][publish_content] Critical fields in outgoing payload:")
        print(f"[DEBUG][publish_content]   - year: {payload.get('year')}")
        print(f"[DEBUG][publish_content]   - description: {payload.get('description')}")
        print(f"[DEBUG][publish_content]   - recording_date: {payload.get('recording_date')}")
        print(f"[DEBUG][publish_content]   - is_author: {payload.get('is_author')}")
        print(f"[DEBUG][publish_content]   - is_performer: {payload.get('is_performer')}")
        print(f"[DEBUG][publish_content] ===== SENDING NOW =====\n")
        
        res = http_client.send_request(cmd, [payload], require_auth=True)
        
        print(f"\n[DEBUG][publish_content] ===== RESPONSE RECEIVED =====")
        print(f"[DEBUG][publish_content] Response: {res}")
        print(f"[DEBUG][publish_content] ===== END RESPONSE =====\n")
        
        current_app.logger.debug(f"[publish_content] CREATE {cmd} response: {res!r}")
        
        # ===== DEBUG: Analyze response from backend =====
        print(f"\n[DEBUG][publish_content] ===== BACKEND RESPONSE ANALYSIS =====")
        if isinstance(res, dict):
            print(f"[DEBUG][publish_content] Response keys: {list(res.keys())}")
            print(f"[DEBUG][publish_content] Response status: {res.get('status')}")
            print(f"[DEBUG][publish_content] Response ID/main_id: {res.get('id')}")
            print(f"[DEBUG][publish_content] Fields RETURNED by backend:")
            print(f"[DEBUG][publish_content]   - year: {res.get('year')}")
            print(f"[DEBUG][publish_content]   - description: {res.get('description')}")
            print(f"[DEBUG][publish_content]   - recording_date: {res.get('recording_date')}")
            print(f"[DEBUG][publish_content]   - location: {res.get('location')}")
            print(f"[DEBUG][publish_content]   - is_author: {res.get('is_author')}")
            print(f"[DEBUG][publish_content]   - is_performer: {res.get('is_performer')}")
            print(f"[DEBUG][publish_content]   - additional_info: {res.get('additional_info')}")
            print(f"[DEBUG][publish_content] Full response: {res}")
        else:
            print(f"[DEBUG][publish_content] Response is not dict: {type(res)} = {res}")
        print(f"[DEBUG][publish_content] ===== END RESPONSE ANALYSIS =====\n")

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
                    "genres": "",
                    "year": None,
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

                    # authors/performers/genres/description
                    if payload.get("authors"):
                        child_payload["authors"] = list(payload.get("authors"))
                    if payload.get("performers") and suggested in ("audio", "song", "video"):
                        child_payload["performers"] = list(payload.get("performers"))
                    if payload.get("genres"):
                        child_payload["genres"] = payload.get("genres")
                    if payload.get("description"):
                        child_payload["description"] = payload.get("description")
                    if payload.get("year"):
                        child_payload["year"] = int(payload.get("year")) if payload.get("year") else None
                    if payload.get("is_live") is not None:
                        child_payload["is_live"] = bool(payload.get("is_live"))
                except Exception as e:
                    current_app.logger.debug(f"[publish_content] error while inheriting parent fields for child {filename}: {e}")

                cmd_child = child_cmd_map.get(suggested, "CREATE_DOCUMENT")
                child_res = http_client.send_request(cmd_child, [child_payload], require_auth=True)
                current_app.logger.debug(f"[publish_content] child create ({filename}) response: {child_res!r}")

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

        # attempt to persist subtracks (concert segments) when publishing a concert
        if main_id and subtracks and isinstance(subtracks, list) and media_type == 'concert':
            created_segments = []
            for st in subtracks:
                seg_payload = {
                    "song_title": st.get("title"),
                    "start_time": float(st.get("start") or 0),
                    "end_time": float(st.get("end") or 0),
                    "performers": st.get("performers") or [],
                    "instruments": st.get("instruments") or [],
                    "comment": st.get("comments") or ''
                }
                try:
                    seg_res = http_client.send_request("ADD_CONCERT_SEGMENT", [main_id, seg_payload], require_auth=True)
                    created_segments.append(seg_res)
                except Exception as e:
                    current_app.logger.debug(f"[publish_content] failed creating concert subtrack: {e}")
            if isinstance(res, dict):
                res['subtracks_created'] = created_segments
        return jsonify(res)
    except Exception as e:
        return jsonify({"status":"ERROR","error_msg": str(e)}), 500

# last line