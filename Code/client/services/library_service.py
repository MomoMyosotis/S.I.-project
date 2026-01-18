# first line

from client.services.http_helper import http_client

class LibraryService:

    @staticmethod
    def get_commented_media(offset=0, limit=10):
        """
        Fetch media items that the user has commented on.
        Uses http_helper.http_client for all server communications.
        """
        args = [offset, limit]
        res = http_client.send_request("get_commented_media", args, require_auth=True)
        
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
        
        return {"status": "OK", "results": media_list, "count": len(media_list)}

    @staticmethod
    def get_followed_media(offset=0, limit=10):
        """
        Fetch media items from users that the user follows.
        Uses http_helper.http_client for all server communications.
        """
        args = [offset, limit]
        res = http_client.send_request("get_followed_media", args, require_auth=True)
        
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
        
        return {"status": "OK", "results": media_list, "count": len(media_list)}

# last line