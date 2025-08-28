# first line

class Config:
    SECRET_KEY = "quack"  # da cambiare con qualcosa di sicuro e serio
    DEBUG = True

    # Config TCP server
    TCP_HOST = "127.0.0.1"   # Indirizzo server TCP
    TCP_PORT = 8000          # Porta server TCP

    # Config Flask (GUI client locale)
    FLASK_HOST = "127.0.0.1"
    FLASK_PORT = 5000

# last line