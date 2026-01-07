from client.services.http_helper import http_client

class ShowService:

    # media block

    @staticmethod
    def get_media(media_id):
        return http_client.send_request("GET_MEDIA", [media_id], require_auth=True)

    @staticmethod
    def delete_media(media_id, media_type=None):
        # map media type to backend delete command
        t = (media_type or "").lower()
        cmd = "DELETE_SONG" if t == "song" else ("DELETE_VIDEO" if t == "video" else ("DELETE_DOCUMENT" if t == "document" else "DELETE_SONG"))
        return http_client.send_request(cmd, [media_id], require_auth=True)

    @staticmethod
    def edit_media(media_id, media_type, updates: dict):
        # map media type to backend update command (fallback to generic UPDATE_MEDIA)
        t = (media_type or "").lower()
        if t == "song":
            cmd = "UPDATE_SONG"
        elif t == "video":
            cmd = "UPDATE_VIDEO"
        elif t == "document":
            cmd = "UPDATE_DOCUMENT"
        else:
            cmd = "UPDATE_MEDIA"
        # Many handlers accept either [media_id, updates] or [updates, media_id]; try primary then fallback
        res = http_client.send_request(cmd, [media_id, updates], require_auth=True)
        if res is None:
            res = http_client.send_request(cmd, [updates, media_id], require_auth=True)
        return res

    # comment block
    @staticmethod
    def post_comment(media_id, text, parent_comment_id: int = None):
        # server expects create_comment; pass a single dict so dispatch_command can unpack kwargs safely
        payload = {"media_id": media_id, "text": text}
        # include multiple parent keys to maximize compatibility with different backend shapes
        if parent_comment_id is not None:
            payload["parent_comment_id"] = parent_comment_id
            payload["parent_id"] = parent_comment_id
            payload["parent"] = parent_comment_id
        return http_client.send_request("CREATE_COMMENT", [payload], require_auth=True)

    @staticmethod
    def get_comments(media_id, offset=0, limit=20):
        # server 'fetch_comment' expects just media_id (extra args can cause TypeError on the server)
        return http_client.send_request("FETCH_COMMENT", [media_id], require_auth=True)

    @staticmethod
    def delete_comment(comment_id):
        return http_client.send_request("DELETE_COMMENT", [comment_id], require_auth=True)

    @staticmethod
    def edit_comment(comment_id, new_text):
        return http_client.send_request("UPDATE_COMMENT", [comment_id, new_text], require_auth=True)

    # related media block
    @staticmethod
    def get_related_media(media_id, offset=0, limit=20):
        return http_client.send_request("GET_RELATED_MEDIA", [media_id, offset, limit], require_auth=True)

# last line