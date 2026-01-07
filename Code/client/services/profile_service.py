# first line
from client.services.http_helper import http_client
from client.models.user import User

class ProfileService:
    @staticmethod
    def get_profile(username=None):
        args = [username] if username else []
        # print(f"[DEBUG][ProfileService.get_profile] sending GET_PROFILE with args={args}")
        res = http_client.send_request("GET_PROFILE", args, require_auth=True)
        # print(f"[DEBUG][ProfileService.get_profile] raw response: {res}")

        # Try to extract a user-dict from many possible server shapes
        def extract_user_dict(resp):
            if not isinstance(resp, dict):
                return None
            # common envelope keys
            for k in ("response", "result", "user", "user_obj"):
                v = resp.get(k)
                if isinstance(v, dict):
                    return v
            # sometimes the server returns the public user dict directly
            candidate_keys = {"id", "username", "mail", "bio", "profile_pic"}
            if any(k in resp for k in candidate_keys):
                return resp
            return None

        inner = extract_user_dict(res)
        if inner is None:
            # server returned unexpected shape — try to surface server error if present
            return {"status": "ERROR", "error_msg": res.get("error_msg", "Invalid response from server")}

        # create User instance and serialize for client
        user_obj = User.from_server(inner if isinstance(inner, dict) else {})
        user_dict = user_obj.to_dict()
        # expose a client URL for the profile picture (proxy)
        profile_pic_id = user_dict.get("profile_pic")
        if profile_pic_id:
            user_dict["profile_picture_url"] = f"/profile/picture/{profile_pic_id}"

        # Determine the username to fetch publications for (prefer explicit param, then returned user)
        target_username = username or user_dict.get("username") or getattr(user_obj, "username", None)
        pubs_res = None
        try:
            if target_username:
                pubs_res = http_client.send_request("GET_USER_PUBLICATIONS", [target_username, 0, 100], require_auth=True)
            else:
                pubs_res = {"status": "OK", "response": []}
            # print(f"[DEBUG][ProfileService.get_profile] pubs_res: {pubs_res}")
        except Exception as e:
            print(f"[DEBUG][ProfileService.get_profile] pubs fetch failed: {e}")
            pubs_res = {"status": "OK", "response": []}

        # normalize publications response into a list
        raw_pubs = []
        if isinstance(pubs_res, dict) and pubs_res.get("status") in (None, "OK"):
            if "response" in pubs_res and isinstance(pubs_res["response"], list):
                raw_pubs = pubs_res["response"]
            elif "results" in pubs_res and isinstance(pubs_res["results"], list):
                raw_pubs = pubs_res["results"]
            elif isinstance(pubs_res.get("response"), dict) and "results" in pubs_res.get("response"):
                raw_pubs = pubs_res["response"]["results"]
        elif isinstance(pubs_res, list):
            raw_pubs = pubs_res

        # normalize items so template can read title/description/date_published reliably
        normalized_pubs = []
        for p in raw_pubs:
            if not isinstance(p, dict):
                continue
            normalized_pubs.append({
                "id": p.get("id") or p.get("media_id"),
                "title": p.get("title") or p.get("name") or "Untitled",
                "description": p.get("description") or p.get("additional_info") or "",
                "date_published": p.get("date_published") or p.get("created_at") or p.get("createdAt") or p.get("date") or "",
                "type": p.get("type") or p.get("media_type") or p.get("file_type") or "unknown",
                "stored_at": p.get("stored_at") or p.get("file_path") or "",
                "file_type": p.get("type") or p.get("media_type") or p.get("file_type") or "unknown",
            })

        # determine publications count: prefer server 'count' if provided, else fallback
        total_count = None
        if isinstance(pubs_res, dict) and "count" in pubs_res:
            try:
                total_count = int(pubs_res["count"])
            except Exception:
                total_count = None

        try:
            current_count = int(user_dict.get("publications_count", 0) or 0)
        except (ValueError, TypeError):
            current_count = 0

        if total_count is None:
            total_count = max(current_count, len(normalized_pubs))
        user_dict["publications_count"] = total_count

        # build 'self' (viewer) object with useful fields when available
        viewer_info = {"is_self": False}
        try:
            if http_client.token:
                viewer_res = http_client.send_request("GET_PROFILE", [], require_auth=True)
                v_inner = extract_user_dict(viewer_res)
                if v_inner:
                    v_user = User.from_server(v_inner if isinstance(v_inner, dict) else {})
                    v_dict = v_user.to_dict()
                    viewer_info.update({
                        "id": v_dict.get("id"),
                        "username": v_dict.get("username"),
                        "lvl": int(v_dict.get("lvl")) if isinstance(v_dict.get("lvl"), int) else (getattr(v_dict.get("lvl"), "value", v_dict.get("lvl")) if v_dict.get("lvl") is not None else None)
                    })
                    viewer_info["is_self"] = (username is None) or (v_dict.get("username") == user_dict.get("username"))
        except Exception as e:
            print(f"[DEBUG][ProfileService.get_profile] viewer lookup failed: {e}")

        return {"status": "OK", "user": user_dict, "self": viewer_info, "recent_publications": normalized_pubs}

    @staticmethod
    def update_profile(content, target_username: str = None):
        """
        Send an update request to backend. Include target username both as:
            - a field inside the content dict (many RPC handlers expect this)
            - a second positional RPC arg (some handlers accept [content, target])
        Resolve target user ID if publish-on-behalf is requested.
        """
        if not isinstance(content, dict):
            content = {}

        if target_username:
            # resolve target user ID first
            try:
                profile_res = http_client.send_request("GET_PROFILE", [target_username], require_auth=True)
                target_user_info = {}

                # extract from nested response
                if isinstance(profile_res, dict):
                    if "response" in profile_res and isinstance(profile_res["response"], dict):
                        target_user_info = profile_res["response"]
                    elif "id" in profile_res:
                        target_user_info = profile_res

                if target_user_info.get("id"):
                    content["user_id"] = target_user_info["id"]
                    content["target_user_id"] = target_user_info["id"]
            except Exception as e:
                print(f"[DEBUG][ProfileService.update_profile] failed to resolve target user: {e}")

            # make sure both forms are present so server-side handlers that
            # look at either the payload or the positional args will apply
            content["username"] = target_username
            content["target_username"] = target_username

        candidates = ["UPDATE_USER", "EDIT_USER", "UPDATE_PROFILE", "EDIT_PROFILE", "SET_USER", "USER_UPDATE"]
        last_res = None
        for cmd in candidates:
            args = [content]
            if target_username:
                args.append(target_username)
            res = http_client.send_request(cmd, args, require_auth=True)
            last_res = res
            if isinstance(res, dict) and res.get("status") in (None, "OK"):
                return res

        # final attempt: send content with username embedded but without second arg
        final_res = http_client.send_request("UPDATE_PROFILE", [content], require_auth=True)
        return final_res or last_res or {"status": "ERROR", "error_msg": "No response from server"}

    @staticmethod
    def add_media(content):
        print(f"[DEBUG][ProfileService.add_media] sending ADD_MEDIA with content={content}")
        res = http_client.send_request("ADD_MEDIA", [content], require_auth=True)
        print(f"[DEBUG][ProfileService.add_media] response: {res}")
        return res

    @staticmethod
    def delete_post(media_id):
        print(f"[DEBUG][ProfileService.delete_post] sending DELETE_MEDIA with media_id={media_id}")
        res = http_client.send_request("DELETE_MEDIA", [media_id], require_auth=True)
        print(f"[DEBUG][ProfileService.delete_post] response: {res}")
        return res

    @staticmethod
    def follow(followed, follower):
        # send only the target username to the API; the server derives the follower from the token
        args = [followed]
        print(f"[DEBUG][ProfileService.follow] sending FOLLOW_USER with args={args}")
        res = http_client.send_request("FOLLOW_USER", args, require_auth=True)
        print(f"[DEBUG][ProfileService.follow] response: {res}")
        return res

    @staticmethod
    def unfollow(unfollowed, unfollower):
        # send only the target username to the API; the server derives the unfollower from the token
        args = [unfollowed]
        print(f"[DEBUG][ProfileService.unfollow] sending UNFOLLOW_USER with args={args}")
        res = http_client.send_request("UNFOLLOW_USER", args, require_auth=True)
        print(f"[DEBUG][ProfileService.unfollow] response: {res}")
        return res

    @staticmethod
    def get_user_publications(username, offset=0, limit=10):
        args = [username, offset, limit]
        res = http_client.send_request("GET_USER_PUBLICATIONS", args, require_auth=True)
        return res

# added methods for level management / moderation
    @staticmethod
    def change_level(username, new_level):
        print(f"[DEBUG][ProfileService.change_level] change_level username={username} -> {new_level}")
        command = "CHANGE_LVL"
        args = [username, new_level]
        res = http_client.send_request(command, args, require_auth=True)
        return res

    @staticmethod
    def ban_user(username):
        # convenience wrapper to set level to BANNED (6)
        return ProfileService.change_level(username, 6)

    @staticmethod
    def restrict_user(username):
        # convenience wrapper to set level to RESTRICTED (5)
        return ProfileService.change_level(username, 5)
# last line