from client.services.http_helper import http_client

class ShowService:
    @staticmethod
    def get_media(media_id):
        # RPC to remote service; adjust method/args if your remote expects different payload
        return http_client.send_request("GET_MEDIA", [media_id], require_auth=True)

    @staticmethod
    def post_comment(media_id, text):
        # send comment to backend; adjust command name/args to match server API
        return http_client.send_request("POST_COMMENT", [media_id, text], require_auth=True)

    @staticmethod
    def like_media(media_id):
        # send like action to backend; adjust command name/args to match server API
        return http_client.send_request("LIKE_MEDIA", [media_id], require_auth=True)
    @staticmethod
    def unlike_media(media_id):
        # send unlike action to backend; adjust command name/args to match server API
        return http_client.send_request("UNLIKE_MEDIA", [media_id], require_auth=True)
    @staticmethod
    def get_comments(media_id, offset=0, limit=20):
        # fetch comments for a media item; adjust command name/args to match server API
        return http_client.send_request("GET_COMMENTS", [media_id, offset, limit], require_auth=True)
    @staticmethod
    def get_likes(media_id, offset=0, limit=20):
        # fetch likes for a media item; adjust command name/args to match server API
        return http_client.send_request("GET_LIKES", [media_id, offset, limit], require_auth=True)
    @staticmethod
    def delete_comment(comment_id):
        # delete a comment; adjust command name/args to match server API
        return http_client.send_request("DELETE_COMMENT", [comment_id], require_auth=True)
    @staticmethod
    def edit_comment(comment_id, new_text):
        # edit a comment; adjust command name/args to match server API
        return http_client.send_request("EDIT_COMMENT", [comment_id, new_text], require_auth=True)
    @staticmethod
    def report_media(media_id, reason):
        # report a media item; adjust command name/args to match server API
        return http_client.send_request("REPORT_MEDIA", [media_id, reason], require_auth=True)
    @staticmethod
    def share_media(media_id, platform):
        # share a media item; adjust command name/args to match server API
        return http_client.send_request("SHARE_MEDIA", [media_id, platform], require_auth=True)
    @staticmethod
    def bookmark_media(media_id):
        # bookmark a media item; adjust command name/args to match server API
        return http_client.send_request("BOOKMARK_MEDIA", [media_id], require_auth=True)
    @staticmethod
    def remove_bookmark(media_id):
        # remove bookmark from a media item; adjust command name/args to match server API
        return http_client.send_request("REMOVE_BOOKMARK", [media_id], require_auth=True)
    @staticmethod
    def get_bookmarks(offset=0, limit=20):
        # fetch bookmarked media items; adjust command name/args to match server API
        return http_client.send_request("GET_BOOKMARKS", [offset, limit], require_auth=True)
    @staticmethod
    def get_media_stats(media_id):
        # fetch media statistics; adjust command name/args to match server API
        return http_client.send_request("GET_MEDIA_STATS", [media_id], require_auth=True)
    @staticmethod
    def update_media_info(media_id, info_dict):
        # update media information; adjust command name/args to match server API
        return http_client.send_request("UPDATE_MEDIA_INFO", [media_id, info_dict], require_auth=True)
    @staticmethod
    def get_related_media(media_id, offset=0, limit=20):
        # fetch related media items; adjust command name/args to match server API
        return http_client.send_request("GET_RELATED_MEDIA", [media_id, offset, limit], require_auth=True)
    @staticmethod
    def report_comment(comment_id, reason):
        # report a comment; adjust command name/args to match server API
        return http_client.send_request("REPORT_COMMENT", [comment_id, reason], require_auth=True)
    @staticmethod
    def pin_comment(comment_id):
        # pin a comment; adjust command name/args to match server API
        return http_client.send_request("PIN_COMMENT", [comment_id], require_auth=True)
    @staticmethod
    def unpin_comment(comment_id):
        # unpin a comment; adjust command name/args to match server API
        return http_client.send_request("UNPIN_COMMENT", [comment_id], require_auth=True)
    @staticmethod
    def get_pinned_comments(media_id):
        # fetch pinned comments for a media item; adjust command name/args to match server API
        return http_client.send_request("GET_PINNED_COMMENTS", [media_id], require_auth=True)
    @staticmethod
    def get_media_tags(media_id):
        # fetch tags for a media item; adjust command name/args to match server API
        return http_client.send_request("GET_MEDIA_TAGS", [media_id], require_auth=True)
    @staticmethod
    def add_media_tag(media_id, tag):
        # add a tag to a media item; adjust command name/args to match server API
        return http_client.send_request("ADD_MEDIA_TAG", [media_id, tag], require_auth=True)
    @staticmethod
    def remove_media_tag(media_id, tag):
        # remove a tag from a media item; adjust command name/args to match server API
        return http_client.send_request("REMOVE_MEDIA_TAG", [media_id, tag], require_auth=True)
    @staticmethod
    def get_media_reactions(media_id, offset=0, limit=20):
        # fetch reactions for a media item; adjust command name/args to match server API
        return http_client.send_request("GET_MEDIA_REACTIONS", [media_id, offset, limit], require_auth=True)
    @staticmethod
    def react_to_media(media_id, reaction_type):
        # react to a media item; adjust command name/args to match server API
        return http_client.send_request("REACT_TO_MEDIA", [media_id, reaction_type], require_auth=True)
    @staticmethod
    def remove_media_reaction(media_id):
        # remove reaction from a media item; adjust command name/args to match server API
        return http_client.send_request("REMOVE_MEDIA_REACTION", [media_id], require_auth=True)
    @staticmethod
    def get_media_shares(media_id, offset=0, limit=20):
        # fetch shares for a media item; adjust command name/args to match server API
        return http_client.send_request("GET_MEDIA_SHARES", [media_id, offset, limit], require_auth=True)
    @staticmethod
    def get_media_audience(media_id):
        # fetch audience information for a media item; adjust command name/args to match server API
        return http_client.send_request("GET_MEDIA_AUDIENCE", [media_id], require_auth=True)
    @staticmethod
    def get_media_location(media_id):
        # fetch location information for a media item; adjust command name/args to match server API
        return http_client.send_request("GET_MEDIA_LOCATION", [media_id], require_auth=True)
    @staticmethod
    def update_media_location(media_id, location_info):
        # update location information for a media item; adjust command name/args to match server API
        return http_client.send_request("UPDATE_MEDIA_LOCATION", [media_id, location_info], require_auth=True)
