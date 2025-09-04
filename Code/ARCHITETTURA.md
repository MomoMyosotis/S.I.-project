Code
├── ARCHITETTURA.md                     // map of files and function
├── client
│   ├── GUI
│   │   ├── static
│   │   │   ├── app.js                  // client-side per gestire autenticazione e chiamate API
│   │   │   ├── assistance_style.css    // stile schermata assistenza
│   │   │   ├── auth.css                // fa da sfondo per la parte di login\register etc
│   │   │   ├── auth_script.js          // gestisce switch tra i form pre-login
│   │   │   ├── favicon.ico             // icona
│   │   │   ├── feed_style.css          // stile del feed
│   │   │   ├── homepage_style.css      // stile della homepage
│   │   │   ├── images
│   │   │   │   └── logo.jpg            // sempre l'icona (fa da logo, si)
│   │   │   ├── index_style.css         // stile dell'indice di ricerca
│   │   │   ├── libraries_style.css     // stile della sezione libreria
│   │   │   ├── login_style.css         // stile schermata di login
│   │   │   ├── profile_style.css       // stile profilo
│   │   │   ├── recover_pswd_style.css  // stile pagina recupero credenziali
│   │   │   └── registration_style.css  // stile pagina registrazione
│   │   └── templates
│   │       ├── assistance.html         // struttura pagina di assistenza
│   │       ├── auth.html               // struttura contenitore modulo pre-login
│   │       ├── feed.html               // struttura feed
│   │       ├── home.html               // struttura contenitore post-login
│   │       ├── index.html              // contenitore esterno moduli (?)
│   │       ├── libraries.html          // struttura pagina libreria
│   │       ├── login.html              // struttura pagina login
│   │       ├── profile.html            // struttura pagina profilo
│   │       ├── recover_pswd.html       // struttura pagina recupero credenziali
│   │       ├── registration.html       // struttura pagina registrazione
│   │       └── settings.json           // specifica cheporta usare
│   ├── __init__.py                     // crea e configura flask
│   ├── app_req
│   │   ├── modules_required.dat        // controlla che siano installati i moduli di python necessari
│   │   ├── requisiti.py                // se i moduli richiesti non ci sono li scarica
│   │   └── version                     // numero versione
│   ├── config.py                       // configura porta TCP ed IP da usare
│   ├── models
│   │   └── user.py                     // versione minimal del obj User del server (x auth)
│   ├── routes
│   │   ├── __init__.py                 // inizializza i blueprint principali che fanno da contenitori
│   │   ├── access.py                   // inizializza blueprint per contenitore accesso
│   │   ├── content.py                  // inizializza blueprint per contenitore operazioni contenuti
│   │   ├── entrata
│   │   │   ├── assistance_bp.py        // blueprint assistenza
│   │   │   ├── auth_bp.py              // blueprint contenitore autenticazione
│   │   │   ├── login_bp.py             // blueprint login
│   │   │   ├── recover_bp.py           // blueprint recupero credenziali
│   │   │   └── register_bp.py          // blueprint registrazione
│   │   ├── home.py                     // inizializza blueprint per contenitore home
│   │   └── logged
│   │       ├── feed_bp.py             // blueprint feed
│   │       ├── home_bp.py             // blueprint homepage (prima di cliccaresu uno dei 3)
│   │       ├── libraries_bp.py        // blueprint librerie
│   │       └── profile_bp.py          // blueprint profilo
│   ├── run_client.py                  // avvia app dal browser
│   └── services
│       ├── config.py                   // configura il server usando cd.json
│       └── tcp_helper.py               // client TCP thread-safe (gestisce comunicazione lato client)
├── notes.md                           // eventuali commenti su stato progetto
└── server
    ├── data
    │   └── users.json                 // trasformare in zona cache(?)
    ├── db
    │   ├── __init__.py                // inizializza connessione db usandocredentials.json
    │   ├── connection.py              // popola database
    │   ├── credentials.json           // dati database postgresql
    │   ├── db.sql                     // query SQL per creare tabelle database
    │   ├── pita.py                    // crea il database in caso venga perso
    │   ├── tablefill.py               // popola le tabelle del db (chiamato da connection.py)
    │   └── users.py                   // si occupa di comunicare col db per gestire auth
    ├── logs
    │   └── server.log                  // contiene i log del server
    ├── main.py                         // avvia il server
    ├── objects                         // OBSOLETE (to fix)
    │   ├── dizionari (obsoleto)
    │   │   ├── formati consentiti.json
    │   │   └── user lvl.json
    │   ├── files
    │   │   ├── documents.py
    │   │   └── song.py
    │   ├── interventi
    │   │   ├── comment.py
    │   │   └── notes.py
    │   └── users
    │       └── user.py
    └── services
        ├── admin_console.py          // gestisce i comandi inseribili dal terminale
        ├── auth_handler.py           // gestisce autenticazione da parte del client
        ├── cd.json                   // contiene i dati del server
        ├── config_loader.py          // configura il server usando cd.json
        ├── logger.py                 // registra esiti operazioni in server.log
        └── server_logic.py           // gestisce comportamento del server e threading dei client

by: __Myosotis__