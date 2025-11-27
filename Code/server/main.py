# fist line

from server.logic.api_server import app, mode_ref, sessions

# The admin TCP console is started in api_server (non-blocking).
# If you want the old stdin console, import manual_cmd from
# server.logic.admin_console and start it here instead.

if __name__ == "__main__":
    print("Server Flask con /api in ascolto su 127.0.0.1:8000")
    app.run(host="127.0.0.1", port=8000, debug=True)

# last line