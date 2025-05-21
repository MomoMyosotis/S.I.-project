# first line

from flask import Blueprint, render_template
import os

static_folder = os.path.join('GUI', 'static')  # senza virgola
print("Static folder resolved to:", os.path.abspath(static_folder))  # <-- debug


homepage_bp = Blueprint('homepage', __name__,
                        template_folder='../GUI/templates',
                        static_folder='../GUI/static')

@homepage_bp.route('/home')
def home():
    return render_template('login.html')  # Quando esisterà

# last line