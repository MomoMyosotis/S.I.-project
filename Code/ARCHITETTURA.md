Code/
├── client/                                 # Frontend Flask + GUI web
│   ├── main.py                             # Punto accesso client (avvia Flask + apre browser)
│   ├── __init__.py                         # Factory pattern per creare app Flask
│   ├── forms.py                            # Validazione form lato client (WTForms)
│   │
│   ├── routes/                             # Blueprint Flask per rotte
│   │   ├── __init__.py                     # Registrazione blueprint
│   │   ├── auth_bp.py                      # Login, registrazione, recupero password, supporto
│   │   ├── home_bp.py                      # Homepage (reindirizza a feed se autenticato)
│   │   └── logged/                         # Rotte per utenti autenticati
│   │       ├── feed_bp.py                  # Feed con search/filter
│   │       ├── libraries_bp.py             # Gestione librerie personali
│   │       ├── profile_bp.py               # Profilo utente (visualizza e modifica)
│   │       ├── publish_bp.py               # Upload/pubblica nuovi media
│   │       └── show_bp.py                  # Visualizza media con commenti
│   │
│   ├── services/                           # Servizi e client HTTP
│   │   ├── http_helper.py                  # HTTPClient per comunicazione con server
│   │   ├── auth_service.py                 # Login, register, recupero password
│   │   ├── feed_service.py                 # Fetch feed e search
│   │   ├── library_service.py              # Gestione librerie
│   │   ├── profile_service.py              # Fetch/update profilo
│   │   ├── show_service.py                 # Fetch media e commenti
│   │   ├── open_with_service.py            # Apertura file esterni
│   │   └── config.py                       # Configurazione client (host, port)
│   │
│   ├── models/                             # Model lato client (dati locali)
│   │   ├── user.py                         # Classe User locale (enumerazioni permessi)
│   │   ├── media.py                        # Classe Media locale (MediaType enum)
│   │   └── intervention.py                 # Classe Comment locale
│   │
│   ├── GUI/                                # Template HTML e asset statici
│   │   ├── templates/                      # Jinja2 template HTML
│   │   │   ├── login.html                  # Pagina login
│   │   │   ├── registration.html           # Pagina registrazione
│   │   │   ├── recover_pswd.html           # Recupero password
│   │   │   ├── assistance.html             # Pagina supporto
│   │   │   ├── home.html                   # Homepage
│   │   │   ├── feed.html                   # Feed media
│   │   │   ├── libraries.html              # Librerie personali
│   │   │   ├── profile.html                # Visualizza profilo
│   │   │   ├── profile_update.html         # Modifica profilo
│   │   │   ├── publish.html                # Upload media
│   │   │   ├── show.html                   # Visualizza media + commenti
│   │   │   ├── auth.html                   # Layout auth (login/register)
│   │   │   ├── unified.html                # Layout principale
│   │   │   ├── test.html                   # Pagina test
│   │   │   └── settings.json               # Configurazione template
│   │   │
│   │   └── static/                         # Asset CSS, JS, immagini
│   │       ├── app.js                      # JavaScript principale
│   │       ├── auth_script.js              # Script autenticazione
│   │       ├── models/
│   │       │   └── user.js                 # Model JS per utente
│   │       ├── images/                     # Immagini (logo, etc.)
│   │       ├── *_style.css                 # Stylesheet pagine (login, feed, profile, etc.)
│   │       └── style.css                   # Stylesheet globale
│   │
│   ├── app_req/                            # Controllo versioni e dipendenze
│   │   ├── requisiti.py                    # Modulo gestione requisiti
│   │   ├── version                         # File versione
│   │   └── modules_required.py             # Lista moduli richiesti
│   │
│   └── __init__.py                         # Factory per create_app()
│
├── server/                                 # Backend Flask + logica applicativa
│   ├── main.py                             # Punto di accesso server (avvia api_server)
│   │
│   ├── logic/                              # Logica del server e configurazione
│   │   ├── api_server.py                   # Flask app con endpoint /api (TCP listener)
│   │   ├── admin_console.py                # Console admin per approvazione registrazioni
│   │   ├── config_loader.py                # Caricamento configurazioni da cd.json
│   │   ├── server_logic.py                 # Logica di business interna
│   │   └── cd.json                         # File configurazione (SMTP, DB, etc.)
│   │
│   ├── services/                           # Dispatcher e servizi di business
│   │   ├── redirect.py                     # Dispatcher principale (instra i comandi)
│   │   ├── user_services.py                # Servizi utenti (login, register, profilo)
│   │   ├── media_services.py               # Servizi media (upload, search, delete)
│   │   ├── interventions_services.py       # Servizi commenti (CRUD commenti)
│   │   └── email_service.py                # Invio email (recupero password, etc.)
│   │
│   ├── objects/                            # Definizione oggetti del dominio
│   │   ├── user.py                         # Classe User con enumerazione livelli
│   │   ├── media.py                        # Classe Media (ABC per Document, Song, Video)
│   │   └── comment.py                      # Classe Comment per commenti ai media
│   │
│   ├── db/                                 # Gestione database PostgreSQL
│   │   ├── connection.py                   # Connessione al DB (psycopg2)
│   │   ├── credentials.json                # Credenziali di accesso PostgreSQL
│   │   ├── db.sql                          # Schema database
│   │   ├── db_crud.py                      # Operazioni CRUD (create, fetch, update, delete)
│   │   ├── ER.puml                         # Diagramma ER (PlantUML)
│   │   ├── __init__.py
│   │   └── pita/                           # Script per gestione database
│   │       ├── pita_make.py                # Ricrea database da db.sql
│   │       ├── pita_populate.py            # Popola database con dati di test
│   │       └── pita_tablefill.py           # Dati e moduli per populate
│   │
│   ├── storage/                            # Archiviazione fisica file media
│   │   ├── documents/                      # Documenti uploadati
│   │   ├── images/                         # Immagini (profili, etc.)
│   │   ├── songs/                          # File audio
│   │   └── videos/                         # File video
│   │
│   ├── utils/                              # Funzioni utility
│   │   ├── storage_manager.py              # Gestione upload/download/delete file
│   │   ├── generic_utils.py                # Funzioni generiche
│   │   ├── media_utils.py                  # Utility per media (durata, pagine, etc.)
│   │   └── user_utils.py                   # Utility per utenti
│   │
│   ├── logs/                               # Logging e test
│   │   ├── logger.py                       # Modulo logging
│   │   ├── tester.py                       # Test comunicazione server-client
│   │   ├── ft.py                           # Test funzionalità via dispatcher
│   │   └── esito*.md                       # Report esiti test
│   │
│   ├── decode_pswd.py                      # Decodifica password
│   ├── ft.py                               # Tester F.U.C.K. tramite dispatcher
│   └── tester.py                           # Tester comunicazione server-client
│
└── ARCHITETTURA.md                         # Questo file (documentazione struttura)


by: __Myosotis__