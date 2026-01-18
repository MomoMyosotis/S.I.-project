# first line

from flask import Blueprint, render_template, session, redirect, url_for, request
from client.services.http_helper import http_client

home_bp = Blueprint("home", __name__)

@home_bp.route("/home", methods=["GET"])
def homepage():
    if http_client.token is None:
        http_client.token = session.get("session_token")
    
    # If no token, redirect to login
    if not http_client.token:
        return redirect(url_for("auth.login"))
    
    # Get form_type from query parameters (default to feed)
    form_type = (request.args.get("form_type") or "feed").lower()
    
    # Map form_type to template and title
    template_map = {
        "feed": ("feed.html", "Feed"),
        "libraries": ("libraries.html", "Libreria"),
        "profile": ("profile.html", "Profilo"),
        "publish": ("publish.html", "Pubblica"),
        "settings": ("settings.html", "Impostazioni"),
    }
    
    if form_type not in template_map:
        form_type = "feed"
    
    content_template, title = template_map[form_type]
    
    return render_template(
        "unified.html",
        content_template=content_template,
        form_type=form_type,
        title=title,
        username=request.args.get("username")  # Pass username for profile view
    )

# last line
