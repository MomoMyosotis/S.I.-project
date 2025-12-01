# first line
from client.services.http_helper import http_client
from client.models.user import User

class ProfileService:
    @staticmethod
    def get_profile(username=None):
        args = [username] if username else []
        print(f"[DEBUG][ProfileService.get_profile] sending GET_PROFILE with args={args}")
        res = http_client.send_request("GET_PROFILE", args, require_auth=True)
        print(f"[DEBUG][ProfileService.get_profile] raw response: {res}")

        # tolerate server responses where 'status' may be None but 'response' contains data
        if res.get("status") in (None, "OK") and "response" in res:
            inner = res["response"]
            # create User instance and serialize for client
            user_obj = User.from_server(inner if isinstance(inner, dict) else {})
            user_dict = user_obj.to_dict()
            # expose a client URL for the profile picture (proxy)
            profile_pic_id = user_dict.get("profile_pic")
            if profile_pic_id:
                user_dict["profile_picture_url"] = f"/profile/picture/{profile_pic_id}"
            # fetch recent publications (best-effort, ignore errors)
            # request a larger limit so we can infer a sensible publications_count
            pubs_res = http_client.send_request("GET_USER_PUBLICATIONS", [user_obj.username, 0, 100], require_auth=True)
            print(f"[DEBUG][ProfileService.get_profile] pubs_res: {pubs_res}")

            # support multiple server shapes: 'response', 'results', or direct list
            raw_pubs = []
            if isinstance(pubs_res, dict) and pubs_res.get("status") in (None, "OK"):
                if "response" in pubs_res and isinstance(pubs_res["response"], list):
                    raw_pubs = pubs_res["response"]
                elif "results" in pubs_res and isinstance(pubs_res["results"], list):
                    raw_pubs = pubs_res["results"]
                elif isinstance(pubs_res.get("response"), dict) and "results" in pubs_res.get("response"):
                    # nested shape
                    raw_pubs = pubs_res["response"].get("results", [])
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
                    "date_published": p.get("date_published") or p.get("created_at") or p.get("createdAt") or ""
                })

            # determine publications count: prefer server 'count' if provided, else max(current, fetched)
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
            # if we have an auth token, try to fetch the current logged user to provide id/lvl/username
            try:
                if http_client.token:
                    viewer_res = http_client.send_request("GET_PROFILE", [], require_auth=True)
                    if isinstance(viewer_res, dict) and viewer_res.get("status") in (None, "OK") and "response" in viewer_res:
                        v_inner = viewer_res["response"]
                        v_user = User.from_server(v_inner if isinstance(v_inner, dict) else {})
                        v_dict = v_user.to_dict()
                        viewer_info.update({
                            "id": v_dict.get("id"),
                            "username": v_dict.get("username"),
                            "lvl": int(v_dict.get("lvl")) if isinstance(v_dict.get("lvl"), int) else (getattr(v_dict.get("lvl"), "value", v_dict.get("lvl")) if v_dict.get("lvl") is not None else None)
                        })
                        # determine ownership by comparing the logged-in username with the target profile username
                        viewer_info["is_self"] = (username is None) or (v_dict.get("username") == user_obj.username)
            except Exception as e:
                print(f"[DEBUG][ProfileService.get_profile] viewer lookup failed: {e}")

            return {"status": "OK", "user": user_dict, "self": viewer_info, "recent_publications": normalized_pubs}
        else:
            return {"status": "ERROR", "error_msg": res.get("error_msg", "Unknown error")}

    @staticmethod
    def update_profile(content):
        print(f"[DEBUG][ProfileService.update_profile] sending UPDATE_USER with content={content}")
        # try a list of candidate command names until one succeeds
        candidates = ["UPDATE_USER", "EDIT_USER", "UPDATE_PROFILE", "EDIT_PROFILE", "SET_USER", "USER_UPDATE"]
        last_res = None
        for cmd in candidates:
            print(f"[DEBUG][ProfileService.update_profile] trying command: {cmd}")
            res = http_client.send_request(cmd, [content], require_auth=True)
            print(f"[DEBUG][ProfileService.update_profile] response for {cmd}: {res}")
            last_res = res
            if isinstance(res, dict) and res.get("status") in (None, "OK"):
                print(f"[DEBUG][ProfileService.update_profile] succeeded with {cmd}")
                return res

        print("[DEBUG][ProfileService.update_profile] all candidate commands failed")
        return last_res or {"status": "ERROR", "error_msg": "No response from server"}

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

# last line