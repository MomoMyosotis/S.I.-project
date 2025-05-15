import threading
import webview
from UI.homepage import create_app

app = create_app()

def start_flask():
    app.run(debug=False, use_reloader=False)

def avvio():
    # Avvia il server Flask in un thread
    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()

    # Crea una finestra desktop che punta alla pagina di login
    webview.create_window("Puffytune Login", "http://127.0.0.1:5000", width=1024, height=640)
    webview.start()