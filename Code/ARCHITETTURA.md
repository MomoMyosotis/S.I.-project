Code/
├── server/                             # Backend e logica del server
│   ├── db/                             # Gestione database
│   │   ├── ER.puml                     # Bozza ER basata su db.sql
│   │   ├── __init__.py
│   │   ├── connection.py               # Connessione al DB
│   │   ├── credentials.json            # Credenziali PostgreSQL
│   │   ├── db.sql                      # Struttura del database
│   │   ├── db_crud.py                  # Operazioni CRUD sugli oggetti
│   │   └── pita/                       # Script di gestione DB
│   │       ├── pita_make.py            # Ricrea il database
│   │       ├── pita_populate.py        # Popola il database
│   │       └── pita_tablefill.py       # Moduli e dati richiamati da pita_populate
│   │
│   ├── logs/                           # Gestione log server
│   │   ├── esito tester.MD             # Esiti tester
│   │   ├── esito ft.md                 # Esiti test ft.py
│   │   ├── logger.py                   # Modulo logging
│   │   ├── server.log                  # File di log generico
│   │   └── sm.py                        # Tester Storage Manager
│   │
│   ├── objects/                         # Definizione oggetti del dominio
│   │   ├── interventi/                  # Note e commenti
│   │   │   ├── comment.py
│   │   │   └── notes.py
│   │   ├── media/                        # Tipi di media
│   │   │   ├── media.py                 # ABC dei media
│   │   │   ├── document.py
│   │   │   ├── song.py
│   │   │   └── video.py
│   │   └── users/                        # Ruoli utente
│   │       ├── root.py
│   │       ├── admin.py
│   │       ├── mod.py
│   │       ├── publisher.py
│   │       ├── regular.py
│   │       ├── restricted.py
│   │       └── banned.py
│   │
│   ├── services/                        # Logica applicativa e dispatcher
│   │   ├── redirect.py                  # Dispatcher principale
│   │   ├── user_services.py             # Servizi utenti
│   │   ├── media_services.py            # Servizi media
│   │   ├── interventions_services.py    # Servizi note/commenti
│   │   ├── server_logic.py              # Logica interna server
│   │   ├── admin_console.py             # Operazioni admin/root da terminale
│   │   ├── config_loader.py             # Caricamento configurazioni server
│   │   └── cd.json                       # Dati di configurazione
│   │
│   ├── storage/                          # Archiviazione fisica dei file
│   │   ├── documents/
│   │   ├── notes/
│   │   ├── songs/
│   │   └── videos/
│   │
│   ├── tmp_download/                     # File temporanei per test
│   │   ├── note1.txt
│   │   ├── note2.txt
│   │   ├── song1.mp3
│   │   ├── song2.midi
│   │   ├── test1.pdf
│   │   ├── test2.odt
│   │   ├── video1.mp4
│   │   └── video2.youtube
│   │
│   ├── utils/                            # Funzioni di utilità
│   │   ├── generic_utils.py
│   │   ├── media_utils.py
│   │   ├── storage_manager.py           # Gestione file effettiva
│   │   └── user_utils.py
│   │
│   ├── main.py                           # Punto di accesso server
│   ├── ft.py                             # Tester F.U.C.K. tramite dispatcher
│   └── tester.py                         # Tester comunicazione server-client
│
├── client/                               # Frontend e interfaccia utente
│   ├── __init__.py
│   ├── run_client.py                     # Avvio applicazione client
│   ├── forms.py                          # Validazione form lato client
│   ├── services/                          # Logica client e connessione server
│   │   ├── auth_service.py
│   │   ├── config.py
│   │   └── tcp_helper.py
│   │
│   ├── routes/                            # Gestione rotte Flask
│   │   ├── __init__.py                   # Registrazione blueprint
│   │   ├── auth_bp.py                     # Rotte auth e support
│   │   ├── content.py                     # Visualizzazione contenuti
│   │   ├── home.py                        # Rotte homepage
│   │   └── logged/
│   │       ├── feed_bp.py
│   │       ├── home_bp.py
│   │       ├── libraries_bp.py
│   │       └── profile_bp.py
│   │
│   ├── models/
│   │   └── user.py                        # Pseudo-oggetto User lato client
│   │
│   ├── GUI/
│   │   ├── static/                        # CSS, JS, immagini
│   │   │   ├── images/logo.jpg
│   │   │   ├── app.js
│   │   │   ├── auth_script.js
│   │   │   ├── assistance_style.css
│   │   │   ├── auth.css
│   │   │   ├── feed_style.css
│   │   │   ├── homepage_style.css
│   │   │   ├── index_style.css
│   │   │   ├── libraries_style.css
│   │   │   ├── login_style.css
│   │   │   ├── profile_style.css
│   │   │   ├── recover_pswd_style.css
│   │   │   ├── registration_style.css
│   │   │   └── favicon.ico
│   │   └── templates/                      # Template HTML
│   │       ├── assistance.html
│   │       ├── auth.html
│   │       ├── feed.html
│   │       ├── home.html
│   │       ├── index.html
│   │       ├── libraries.html
│   │       ├── login.html
│   │       ├── recover_pswd.html
│   │       ├── registration.html
│   │       └── settings.json
│   │
│   └── app_req/                            # Controllo dipendenze e versioni
│       ├── modules_required.py
│       ├── requisiti.py
│       └── version
│
├── Architettura/                          # Documentazione architetturale
└── notes.md                               # Note sul progresso


by: __Myosotis__