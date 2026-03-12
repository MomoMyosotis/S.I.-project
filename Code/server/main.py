# fist line

from server.logic.api_server import app, mode_ref, sessions
import os, webbrowser, threading, time

# The admin TCP console is started in api_server (non-blocking).
# If you want the old stdin console, import manual_cmd from
# server.logic.admin_console and start it here instead.


def _open_admin_ui(url: str = "http://127.0.0.1:8000/admin", delay: float = 0.8):
    time.sleep(delay)
    try:
        webbrowser.open(url)
    except Exception:
        pass


if __name__ == "__main__":
    #print("Server Flask con /api in ascolto su 127.0.0.1:8000")
    # Start WSGI server via api_server control so we can stop/start it later.
    import server.logic.api_server as api_server
    started = api_server.start_wsgi_server(host='127.0.0.1', port=8000)
    if started:
        # open admin login in browser once server is started
        t = threading.Thread(target=_open_admin_ui, args=("http://127.0.0.1:8000/admin/login", 0.8), daemon=True)
        t.start()
        # keep the main thread alive while the server thread runs
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            api_server.stop_wsgi_server()
    else:
        print("Server already running or failed to start.")

# last line