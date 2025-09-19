# first line

from .auth_bp import auth_bp
from .home_bp import home_bp
from .content import content_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(content_bp, url_prefix='/content')

# last line