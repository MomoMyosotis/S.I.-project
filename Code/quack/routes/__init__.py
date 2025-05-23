# first line

from .main_routes import main
from .auth import auth_bp
from .homepage import home_bp

def register_blueprints(app):
    app.register_blueprint(main)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(home_bp, url_prefix='/home')

# last line