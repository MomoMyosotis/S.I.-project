# first line

from flask import Blueprint, render_template
import os

static_folder = os.path.join('GUI', 'static')  # senza virgola
print("Static folder resolved to:", os.path.abspath(static_folder))  # <-- debug

# routes/startpage.py
startpage_bp = Blueprint('startpage', __name__,
                         template_folder='../GUI/templates',
                         static_folder='../GUI/static')

@startpage_bp.route('/')
def index():
    return render_template('index.html')


# last line