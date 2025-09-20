# fist line

from server.logic.api_server import app, mode_ref, sessions, manual_cmd
import threading

# Avvio thread admin console (manual mode)
threading.Thread(target=manual_cmd, args=(None, mode_ref), daemon=True).start()

if __name__ == "__main__":
    print("Server Flask con /api in ascolto su 127.0.0.1:8000")
    app.run(host="127.0.0.1", port=8000, debug=True)

# last line