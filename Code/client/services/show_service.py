from client.services.http_helper import http_client

class ShowService:
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

    @staticmethod
    def post_comment(media_id, text, parent_comment_id: int = None):
        # server expects create_comment; pass a single dict so dispatch_command can unpack kwargs safely
        payload = {"media_id": media_id, "text": text}
        if parent_comment_id:
            payload["parent_comment_id"] = parent_comment_id
        return http_client.send_request("CREATE_COMMENT", [payload], require_auth=True)

    @staticmethod
    def like_media(media_id):
        return http_client.send_request("LIKE_MEDIA", [media_id], require_auth=True)

    @staticmethod
    def unlike_media(media_id):
        return http_client.send_request("UNLIKE_MEDIA", [media_id], require_auth=True)

    @staticmethod
    def get_comments(media_id, offset=0, limit=20):
        # server 'fetch_comment' expects just media_id (extra args can cause TypeError on the server)
        return http_client.send_request("FETCH_COMMENT", [media_id], require_auth=True)

    @staticmethod
    def get_likes(media_id, offset=0, limit=20):
        return http_client.send_request("GET_LIKES", [media_id, offset, limit], require_auth=True)

    @staticmethod
    def delete_comment(comment_id):
        return http_client.send_request("DELETE_COMMENT", [comment_id], require_auth=True)

    @staticmethod
    def edit_comment(comment_id, new_text):
        return http_client.send_request("UPDATE_COMMENT", [comment_id, new_text], require_auth=True)

    @staticmethod
    def report_media(media_id, reason):
        return http_client.send_request("REPORT_MEDIA", [media_id, reason], require_auth=True)

    @staticmethod
    def share_media(media_id, platform):
        return http_client.send_request("SHARE_MEDIA", [media_id, platform], require_auth=True)

    @staticmethod
    def bookmark_media(media_id):
        return http_client.send_request("BOOKMARK_MEDIA", [media_id], require_auth=True)

    @staticmethod
    def remove_bookmark(media_id):
        return http_client.send_request("REMOVE_BOOKMARK", [media_id], require_auth=True)

    @staticmethod
    def get_bookmarks(offset=0, limit=20):
        return http_client.send_request("GET_BOOKMARKS", [offset, limit], require_auth=True)

    @staticmethod
    def get_media_stats(media_id):
        return http_client.send_request("GET_MEDIA_STATS", [media_id], require_auth=True)

    @staticmethod
    def update_media_info(media_id, info_dict):
        return http_client.send_request("UPDATE_MEDIA_INFO", [media_id, info_dict], require_auth=True)

    @staticmethod
    def get_related_media(media_id, offset=0, limit=20):
        return http_client.send_request("GET_RELATED_MEDIA", [media_id, offset, limit], require_auth=True)

    @staticmethod
    def report_comment(comment_id, reason):
        return http_client.send_request("REPORT_COMMENT", [comment_id, reason], require_auth=True)

    @staticmethod
    def pin_comment(comment_id):
        return http_client.send_request("PIN_COMMENT", [comment_id], require_auth=True)

    @staticmethod
    def unpin_comment(comment_id):
        return http_client.send_request("UNPIN_COMMENT", [comment_id], require_auth=True)

    @staticmethod
    def get_pinned_comments(media_id):
        return http_client.send_request("GET_PINNED_COMMENTS", [media_id], require_auth=True)

    @staticmethod
    def get_media_tags(media_id):
        return http_client.send_request("GET_MEDIA_TAGS", [media_id], require_auth=True)

    @staticmethod
    def add_media_tag(media_id, tag):
        return http_client.send_request("ADD_MEDIA_TAG", [media_id, tag], require_auth=True)

    @staticmethod
    def remove_media_tag(media_id, tag):
        return http_client.send_request("REMOVE_MEDIA_TAG", [media_id, tag], require_auth=True)

    @staticmethod
    def get_media_reactions(media_id, offset=0, limit=20):
        return http_client.send_request("GET_MEDIA_REACTIONS", [media_id, offset, limit], require_auth=True)

    @staticmethod
    def react_to_media(media_id, reaction_type):
        return http_client.send_request("REACT_TO_MEDIA", [media_id, reaction_type], require_auth=True)

    @staticmethod
    def remove_media_reaction(media_id):
        return http_client.send_request("REMOVE_MEDIA_REACTION", [media_id], require_auth=True)

    @staticmethod
    def get_media_shares(media_id, offset=0, limit=20):
        return http_client.send_request("GET_MEDIA_SHARES", [media_id, offset, limit], require_auth=True)

    @staticmethod
    def get_media_audience(media_id):
        return http_client.send_request("GET_MEDIA_AUDIENCE", [media_id], require_auth=True)

    @staticmethod
    def get_media_location(media_id):
        return http_client.send_request("GET_MEDIA_LOCATION", [media_id], require_auth=True)

    @staticmethod
    def update_media_location(media_id, location_info):
        return http_client.send_request("UPDATE_MEDIA_LOCATION", [media_id, location_info], require_auth=True)

# last line