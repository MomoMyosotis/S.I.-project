from flask import Blueprint, render_template

publish_bp = Blueprint("publish", __name__)

@publish_bp.route("/publish.html")
def publish_page():
    # serve il template client/GUI/templates/publish.html
    return render_template("publish.html")