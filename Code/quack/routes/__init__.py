# first line

from .main_routes import main
from .auth import auth_bp



def register_blueprints(app):
    app.register_blueprint(main)
    app.register_blueprint(auth_bp, url_prefix='/auth')



# last line