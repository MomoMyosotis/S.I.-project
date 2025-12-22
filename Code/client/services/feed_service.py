# first line

from client.services.http_helper import http_client

class FeedService:
    @staticmethod
    def get_feed(search=None, filter_by="all", offset=0, limit=10):
        """
        Fetch feed items (media) from server; when a search term is provided and the filter
        is 'all' or 'user' also fetch matching users and merge them into the returned results.
        Uses http_helper.http_client for all server communications.
        """
        args = [search, filter_by, offset, limit]
        # Feed is public: don't require auth (allows anonymous browsing / infinite scroll)
        res = http_client.send_request("GET_FEED", args, require_auth=False)

        # pass through error responses
        if isinstance(res, dict) and res.get("status") and str(res.get("status")).lower() not in ("ok", "true"):
            return res

        # normalize media list from possible shapes
        media_list = []
        if isinstance(res, dict):
            if "results" in res and isinstance(res["results"], list):
                media_list = res["results"]
            elif "response" in res:
                r = res["response"]
                if isinstance(r, dict) and "results" in r and isinstance(r["results"], list):
                    media_list = r["results"]
                elif isinstance(r, list):
                    media_list = r
            elif isinstance(res.get("response"), list):
                media_list = res.get("response")
        elif isinstance(res, list):
            media_list = res

        # if requested, fetch user search results and append them as user-type feed items
        if search and filter_by in ("all", "user"):
            # user search should also work anonymously
            users_res = http_client.send_request("SEARCH_USERS", [search, offset, limit], require_auth=False)
            u_list = []
            if isinstance(users_res, dict) and users_res.get("status") and str(users_res.get("status")).lower() not in ("ok", "true"):
                # ignore user search errors (keep media results)
                u_list = []
            else:
                if isinstance(users_res, dict):
                    if "response" in users_res:
                        inner = users_res["response"]
                        if isinstance(inner, dict) and isinstance(inner.get("response") or inner.get("results"), list):
                            u_list = inner.get("response") or inner.get("results") or []
                        elif isinstance(inner, list):
                            u_list = inner
                    elif "results" in users_res and isinstance(users_res["results"], list):
                        u_list = users_res["results"]
                    elif isinstance(users_res.get("response"), list):
                        u_list = users_res["response"]
                elif isinstance(users_res, list):
                    u_list = users_res

            # normalize user items to feed item shape and append
            for u in u_list:
                thumb = u.get("thumbnail") or (f"/profile/picture/{u.get('profile_pic')}" if u.get("profile_pic") else "/static/images/no pp.jpg")
                media_list.append({
                    "id": f"user:{u.get('id')}",
                    "title": u.get("username") or u.get("title") or "",
                    "username": u.get("username"),
                    "type": "user",
                    "tags": [],
                    "thumbnail": thumb,
                    "description": u.get("bio") or u.get("full_bio") or u.get("description") or ""
                })

        return {"status": "OK", "results": media_list, "count": len(media_list)}

    @staticmethod
    def report_post(content):
        return http_client.send_request("REPORT_POST", [content], require_auth=True)

    @staticmethod
    def delete_post(post_id):
        return http_client.send_request("DELETE_POST", [post_id], require_auth=True)

# last line