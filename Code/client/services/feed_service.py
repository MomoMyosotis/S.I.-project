# first line

from client.services.http_helper import http_client

class FeedService:
    @staticmethod
    def get_feed(search=None, filter_by="all", offset=0, limit=10):
        args = [search, filter_by, offset, limit]
        return http_client.send_request("GET_FEED", args, require_auth=True)

    @staticmethod
    def add_post(content):
        return http_client.send_request("ADD_POST", [content], require_auth=True)

    @staticmethod
    def delete_post(post_id):
        return http_client.send_request("DELETE_POST", [post_id], require_auth=True)

# last line