# first line

from client.services.http_helper import http_client

class FeedService:
    @staticmethod
    def get_feed(search=None, filter_by="all", offset=0, limit=10):
        return http_client.send_request(
            "GET_FEED", [search, filter_by, offset, limit], require_auth=True
        )

class AuthService:
    @staticmethod
    def login(username, password):
        return http_client.send_request("LOGIN", [username, password])

    @staticmethod
    def register(email, username, password, birthday):
        return http_client.send_request("REGISTER", [
            email,
            username,
            password,
            birthday,
        ])

    @staticmethod
    def recover(username):
        return http_client.send_request("RECOVER", [username])

    @staticmethod
    def assistance(username, problem):
        return http_client.send_request("ASSISTANCE", [username, problem])

# last line