# first line

from .auth_bp import auth_bp
from .logged.home_bp import home_bp
from .content import content_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp, url_prefix='/home')
    app.register_blueprint(content_bp, url_prefix='/content')


# last line