# first line

from flask import Blueprint
from .logged.feed_bp import feed_bp
from .logged.profile_bp import profile_bp
from .logged.libraries_bp import libraries_bp

logged_bp = Blueprint('home', __name__, url_prefix='/home')

# Registrazione dei blueprint figli
logged_bp.register_blueprint(feed_bp)
logged_bp.register_blueprint(profile_bp)
logged_bp.register_blueprint(libraries_bp)

# last line