Code
├── server
│   ├── main.py                        // entry point server
│   ├── tester.py                       // stress test server
│   ├── services
│   │   ├── server_logic.py             // gestisce operazioni server
│   │   ├── redirect.py                 // gestione utenti e interazione comandi
│   │   ├── media_crud.py               // CRUD oggetti media
│   │   ├── handle_obj.py               // validatore generico media prima del CRUD
│   │   ├── handle_client.py            // gestisce client e sessioni utente
│   │   ├── config_loader.py            // configura il server
│   │   ├── cd.json                      // info configurazione server
│   │   └── admin_console.py            // console gestione manuale server
│   ├── objects
│   │   ├── interventi
│   │   │   ├── comment.py              // costruttore oggetto commento
│   │   │   └── note.py                 // costruttore oggetto nota
│   │   ├── media
│   │   │   ├── document.py             // costruttore oggetto figlio documento (da media)
│   │   │   ├── media.py                // costruttore oggetto generico media
│   │   │   ├── song.py                 // costruttore oggetto figlio song (da media)
│   │   │   └── video.py                // costruttore oggetto figlio video (da media)
│   │   └── users
│   │       └── user.py                 // costruttore oggetto user
│   ├── logs
│   │   ├── esito_test                  // esito stress test server\tester.py
│   │   ├── logger.py                   // registra eventi (registrazione, connessione…)
│   │   └── server.log                  // log degli eventi
│   ├── db
│   │   ├── __init__.py                 // connessione db PostgreSQL
│   │   ├── connection.py               // tester integrità db
│   │   ├── credentials.json            // credenziali db PostgreSQL
│   │   ├── db.sql                       // query SQL per creare database
│   │   ├── handle_obj_low.py           // accesso e logica db
│   │   └── pita
│   │       ├── pita_make.py            // script per ricreare db da zero
│   │       ├── pita_populate.py        // logica popolamento db
│   │       └── pita_tablefill.py       // query e dati per popolare db
│   └── cache                           // (vuota, da valutare se rimuovere)
│
├── client
│   ├── __init__.py                     // configurazione app
│   ├── forms.py                         // logica validazione form client (frontend)
│   ├── run_client.py                    // esecuzione app
│   ├── services
│   │   ├── auth_service.py              // logica autenticazione
│   │   ├── config.py                    // info configurazione client
│   │   └── tcp_helper.py                // connessione TCP + invio/ricezione dati client-server
│   ├── routes
│   │   ├── __init__.py                  // registra blueprint Flask
│   │   ├── auth_bp.py                   // rotte auth e support
│   │   ├── content.py                   // rotte visualizzazione contenuti multimediali
│   │   ├── home.py                      // rotte homepage
│   │   └── logged
│   │       ├── feed_bp.py               // rotte feed
│   │       ├── home_bp.py               // rotte home
│   │       ├── libraries_bp.py          // rotte librerie
│   │       └── profile_bp.py            // rotte profile
│   ├── models
│   │   └── user.py                      // pseudo oggetto user lato client
│   ├── GUI
│   │   ├── static
│   │   │   ├── images
│   │   │   │   └── logo.jpg             // logo app
│   │   │   ├── app.js                    // gestisce login, token e fetch verso API Flask
│   │   │   ├── assistance_style.css     // stile pagina assistance.html
│   │   │   ├── auth_script.js            // manipolazione DOM lato client
│   │   │   ├── auth_style.css            // stile auth.html
│   │   │   ├── favicon.ico               // icona logo
│   │   │   ├── feed_style.css            // stile feed.html
│   │   │   ├── homepage_style.css        // stile homepage.html
│   │   │   ├── index_style.css           // stile index.html
│   │   │   ├── libraries_style.css       // stile libraries.html
│   │   │   ├── login_style.css           // stile login.html
│   │   │   ├── recover_pswd_style.css    // stile recover_pswd.html
│   │   │   └── registration_style.css   // stile registration.html
│   │   └── templates
│   │       ├── assistance.html           // pagina assistenza
│   │       ├── auth.html                 // contenitore pagine autenticazione
│   │       ├── feed.html                 // pagina feed
│   │       ├── home.html                 // contenitore pagine homepage
│   │       ├── index.html                // contenitore home e auth
│   │       ├── libraries.html            // pagina libreria
│   │       ├── login.html                // pagina login
│   │       ├── recover_pswd.html         // pagina recupero credenziali
│   │       ├── registration.html         // pagina registrazione
│   │       └── setting.json              // connessione Flask-server
│   └── app_req
│       ├── modules_required.py           // moduli Python richiesti (scaricabili se mancanti)
│       ├── requisiti.py                  // controlla versione aggiornata moduli
│       └── version                       // versione
├── Architettura                          // tu che dici?
└── notes.md                              // note sul progresso raggiunto

by: __Myosotis__