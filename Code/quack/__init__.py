# first line

import os
from flask import Flask
from quack.routes import register_blueprints
from quack.extensions import init_extensions
from quack.config import Config

def create_app():

    # Trova la posizione assoluta del folder GUI perché i folder template e static sono predefiniti da Flask
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'quack','GUI'))
    app = Flask(__name__,
                template_folder=os.path.join(base_dir, 'templates'),
                static_folder=os.path.join(base_dir, 'static'),
                static_url_path='/static')

    print(f"Template folder is set to: {os.path.join(base_dir, 'templates')}")

    app.config.from_object(Config)
    app.config['DEBUG'] = True
    app.secret_key = Config.SECRET_KEY

    '''
        # Inizializza le estensioni (login_manager, ecc.)
        init_extensions(app)
    '''

    # Registra i blueprint (route)
    register_blueprints(app)

    return app

# last linea