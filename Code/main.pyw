# main.pyw

import threading
import webview
import os
from quack import create_app
from quack.app_req import requisiti

# crea l'app
def run_flask():
    # Crea l'app Flask
    app = create_app()

    # Configura il percorso assoluto per la cartella static
    app.config['STATIC_FOLDER'] = os.path.join(os.getcwd(), 'quack', 'GUI', 'static')

    # Carica tutto su localhost, mostra gli errori, ricarica quando si modifica il codice
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)

def main():

    #requisiti.check_dependencies()

    # Crea un thread chiamato flask_thread (il thread termina automaticamente quando il programma principale termina)
    flask_thread = threading.Thread(target=run_flask, daemon=True)

    # Avvia il server Flask in modo asincrono
    flask_thread.start()

    # Crea una finestra web-server chiamata BBGG ^^ sull'URL localhost
    webview.create_window("Boopie =^.^=", "http://127.0.0.1:5000",
                        # Stabilisce le dimensioni della finestra
                        width=1024, height=768, resizable=True)

    # Avvia l'interfaccia Webview
    webview.start()

# Se il file viene eseguito direttamente, chiama la funzione main
if __name__ == "__main__":
    main()

# last line