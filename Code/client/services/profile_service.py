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

            is_self = (username is None) or (username == user_obj.username)
            return {"status": "OK", "user": user_dict, "self": {"is_self": is_self}, "recent_publications": normalized_pubs}
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
        args = [followed, follower]
        print(f"[DEBUG][ProfileService.follow] sending FOLLOW_USER with args={args}")
        res = http_client.send_request("FOLLOW_USER", args, require_auth=True)
        print(f"[DEBUG][ProfileService.follow] response: {res}")
        return res

    @staticmethod
    def unfollow(unfollowed, unfollower):
        args = [unfollowed, unfollower]
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