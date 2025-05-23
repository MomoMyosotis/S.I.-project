Progetto_Ingegneria
├── README.md                           # Documentazione principale del progetto
└── Code
   ├── ARCHITETTURA.md                      # Descrizione tecnica dell'architettura del sistema
   ├── main.pyw                             # File principale per avviare l'app (modalità GUI)
   ├── notes.md                             # Appunti di sviluppo e idee
   └── quack                                # Package principale dell'applicazione
       ├── GUI                              # Interfaccia grafica (frontend)
       │   ├── static                       # File statici: CSS, JS, immagini
       │   │   ├── assistance_style.css     # Stile per la pagina di assistenza
       │   │   ├── auth.css                 # Stile per le pagine di autenticazione
       │   │   ├── auth_script.js           # Script JS per la gestione autenticazione
       │   │   ├── favicon.ico              # Icona del sito
       │   │   ├── index_style.css          # Stile della homepage
       │   │   ├── login_style.css          # Stile della pagina di login
       │   │   ├── recover_pswd_style.css   # Stile per il recupero password
       │   │   └── registration_style.css   # Stile per la registrazione utenti
       │   └── templates                    # Template HTML per il rendering delle pagine
       │       ├── assistance.html          # Pagina di assistenza
       │       ├── auth.html                # Template generico per autenticazione
       │       ├── homepage.html            # Pagina principale utente loggato
       │       ├── index.html               # Landing page o homepage iniziale
       │       ├── login.html               # Pagina di login
       │       ├── profile.html             # Pagina profilo utente
       │       ├── recover_pswd.html        # Pagina recupero password
       │       ├── registration.html        # Pagina di registrazione
       │       └── settings.json            # Configurazioni per i template (es. temi)
       ├── SQL temp                         # Script e configurazioni database
       │   ├── __init__.py                  # Rende la cartella un modulo Python
       │   ├── connection.py                # Gestione della connessione al DB
       │   ├── credentials.json             # Credenziali di accesso al DB
       │   ├── db.sql                       # Script SQL per la creazione del database
       │   ├── info.md                      # Informazioni sul database
       │   └── user tablefill.sql           # Script per popolare la tabella utenti
       ├── __init__.py                      # Rende 'quack' un modulo Python
       ├── config.py                        # File di configurazione globale del progetto
       ├── data
       │   └── users.json                   # Dati statici sugli utenti (mock o test)
       ├── extensions.py                    # Estensioni Flask o plugin usati nell'app
       ├── models                           # Modelli dati (ORM o strutture)
       │   └── user.py                      # Modello per l'entità "Utente"
       ├── objects                          # Componenti logici dell'app
       │   ├── dizionari (obsoleto)         # Vecchi dizionari (non più in uso)
       │   │   ├── formati consentiti.json  # Formati file accettati
       │   │   └── user lvl.json             # Livelli utenti
       │   ├── files                         # Gestione file/documenti
       │   │   ├── documents.py              # Funzioni per documenti caricati
       │   │   └── song.py                   # Gestione file audio
       │   ├── interventi                    # Gestione interventi o commenti
       │   │   ├── comment.py                # Logica per i commenti
       │   │   └── notes.py                  # Note/interventi utente
       │   └── users
       │       └── user.py                  # Gestione avanzata utenti (custom object)
       ├── routes                           # Definizione delle rotte Flask
       │   ├── __init__.py                  # Rende la cartella un modulo
       │   ├── auth.py                      # Rotte per login, logout, registrazione
       │   ├── homepage.py                  # Rotta e logica della homepage
       │   ├── main_routes.py               # Rotte principali condivise
       │   ├── startpage.py                 # Rotta per la pagina iniziale (index)
       │   └── storage.py                   # Rotte legate alla gestione file/storage
       └── services                         # Logica applicativa (business logic)
           ├── auth_service.py              # Servizi per l'autenticazione
           ├── db.py                        # Utility per interagire con il DB
           └── user_service.py              # Logica utenti (registrazione, aggiornamento, ecc.)


- __myosotis__