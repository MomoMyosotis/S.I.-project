# first line

from flask import Blueprint, render_template

content_bp = Blueprint('content', __name__, url_prefix='/content')

@content_bp.route('/<content_id>')
def view_content(content_id):
    # esempio di render, sostituire con il template reale
    return render_template('content.html', content_id=content_id)

# last line