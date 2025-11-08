# first line

import os
from flask import Flask
from client.services.config import Config
from client.routes import register_blueprints

def create_app():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'GUI'))
    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, 'templates'),
        static_folder=os.path.join(base_dir, 'static'),
        static_url_path='/static'
    )

    print(f"Template folder is set to: {os.path.join(base_dir, 'templates')}")

    app.config.from_object(Config)
    app.config['DEBUG'] = True
    app.secret_key = Config.SECRET_KEY

    register_blueprints(app)  # registra le rotte (login ecc.)

    return app

# last line