# first line

import os, webbrowser
from threading import Thread
from client import create_app
from client.services.config import Config

if __name__ == "__main__":
    app = create_app()

    # Apri il browser solo nel processo principale (non in quello del reloader)
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        Thread(
            target=lambda: webbrowser.open(
                f"http://{Config.FLASK_HOST}:{Config.FLASK_PORT}/auth/login"
            )
        ).start()

    # Avvia l'app Flask
    app.run(
        host=Config.FLASK_HOST,
        port=Config.FLASK_PORT,
        debug=Config.DEBUG
    )

# last line