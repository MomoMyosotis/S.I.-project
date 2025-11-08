# first line

from flask import Blueprint, render_template, request, session, jsonify
from client.services.http_helper import http_client
from client.services.feed_service import FeedService
# from client.services.libraries_service import LibrariesService
# from client.services.profile_service import ProfileService

home_bp = Blueprint("home", __name__, url_prefix="/home")
"""#_______________________________________-
class User:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def to_dict(self):
        return {
            "name" : self.name,
            "surname" : self.surname
        }

@home_bp.route("/test2", methods=["GET"])
def test2():
    # creare un obj User -> chiamarlo come dizionario(to_dict) e caricarlo come stringa(jsonify)
    form_type_prova = request.args.get("form_type", "test")
    user = User("Marco", "Polo")
    return jsonify(user.to_dict())

#____________________________________
# quando vado su test viene chiamato il methods get della
@home_bp.route("/test", methods=["GET"])
def test():
    form_type_prova = request.args.get("form_type", "test")
    s = "pippo"
    p = "pluto"
    return render_template(
        "test.html",
        form_type_prova=form_type_prova,
        s=s,
        p=p,
        title="Prova - " + form_type_prova.capitalize()
    )"""


# =====================
# HOME (landing page)
# =====================
@home_bp.route("/", methods=["GET"])
def homepage():
    form_type = request.args.get("form_type", "feed")

    # mappa form_type -> template
    templates_map = {
        "feed": "feed.html",
        "profile": "profile.html",
        "libraries": "libraries.html"
    }

    selected_template = templates_map.get(form_type, "feed.html")

    return render_template(
        "home.html",
        form_type=form_type,
        content_template=selected_template,
        title="Home - " + form_type.capitalize()
    )

# =====================
# FEED DATA
# =====================
@home_bp.route("/feed/data", methods=["GET"])
def feed_data():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    search = request.args.get("search")
    filter_by = request.args.get("filter", "all")
    offset = int(request.args.get("offset", 0))
    limit = int(request.args.get("limit", 10))

    response = FeedService.get_feed(search, filter_by, offset, limit)
    if response.get("status") == "OK":
        return jsonify(response.get("data", []))
    else:
        return jsonify({"error": response.get("error_msg", "Unknown error")}), 400

# =====================
# LIBRARIES DATA
# =====================
@home_bp.route("/libraries/data", methods=["GET"])
def libraries_data():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    response = {"status": "OK", "data": []}  # placeholder
    if response.get("status") == "OK":
        return jsonify(response.get("data", []))
    else:
        return jsonify({"error": response.get("error_msg", "Unknown error")}), 400

# =====================
# PROFILE DATA
# =====================
@home_bp.route("/profile/data", methods=["GET"])
def profile_data():
    if http_client.token is None:
        http_client.token = session.get("session_token")

    response = {"status": "OK", "data": {"username": "test"}}  # placeholder
    if response.get("status") == "OK":
        return jsonify(response.get("data", {}))
    else:
        return jsonify({"error": response.get("error_msg", "Unknown error")}), 400

# last line