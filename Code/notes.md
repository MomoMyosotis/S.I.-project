note:

- i folder models e objects benché simili hanno scopi !=

- models    -> contiene le entità così come vengono usate a lvl applicativo
            -> quello che viene effettivamente usato per fare le operazioni

- objects   -> contiene gli stessi obj main modi più complessi
            -> destinato all'uso interno del sistema o da parte di root


================================================
what's been done:
- objects defined with attributes (yet to do methods)
- defined folder && file organization
- flask app initialization
- SQL prototype ready to use (sort of, gotta reconfigure it first)
- UI:
    - routes defined for authentification - login, recover pswd, registration, assistance
    - form .html and .css for - login, recover pswd, registration, assistance
    - module "auth" that contains said modules
- protoype of model for user
=================================================

to do list:

##############################################
##############################################
__UI__

- modulo home che contiene:
    - pagina profilo
    - pagina ricerca
    - feed - (lazy loading)
            JS che rileva quando sei in fondo alla pagina
            Route Flask per dare nuovi contenuti in formato JSON
            Un backend che restituisce “pagine” (es: 10 post alla volta)

- modulo interventions che contiene:
    - sezione notifiche
    - sezione video commentati

- modulo tendina che contiene:
    - sezione per i commenti sotto ai video
    - sezione per le note nei file

- modulo visualize che contiene:
    - pagina per i documenti
    - sezione video commentati
    - pulsante x form "report" (form simile a contact assistance?)

- modulo lvl
    - finestra invisibile che a seconda del livello dell'utente facomparire determinati pulsanti
        - block user
        - deleate content || account
        - costumize note || cmment
        - add info (4 files)
        - hide content based on lvl (?)


requisiti struttura __UI__:
modulo autentificazione
- login -> collegato a recover credentials e registration form
- recover credentials -> collegato solo a login
- registration -> collegato a login e assistance
- assistance -> collegato a login

effettuato il login -> carica la home
home struttura:
- 3 finestre tra cui si può shiftare come con ig o whatsapp
- sx -> profilo
- centro -> feed -> pulsante per il form di ricerca
- dx -> libreria (da implementare una logica per salvare gli id dei brani piaciuti)

resto yet to define

##############################################
##############################################

__backend__:
define all the modules
    - user
    - comment
    - note
    - song
    - concert
    - file

configure the database
    - convert "SQL temp" folder
    - prepare an input listener -> converts requests into query
                                -> returns the SQL data into acceptable format i.e. dict

configure the objects methods

prepare a logic for differnt users

prepare a logic for the concerts



| **Aspetto**             | `auth_service.py`                                                   | `db.py`                                                          |
| ----------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Ruolo**               | Interfaccia logica di alto livello (service layer)                  | Gestione utenti e accesso ai dati                                |
| **Responsabilità**      | Orchestrare il login, registrazione ecc. usando funzioni di `db.py` | Gestire utenti: caricarli, salvarli, validarli, hashare password |
| **Accesso ai dati**     | *Non diretto* (delega a `db.py`)                                    | Diretto (carica/salva da JSON)                                   |
| **Login demo (grezzo)** | Sperimentale, senza hashing, solo per fake\_user.json               | Completo, con `check_password_hash()`                            |
| **Hashing password**    | ❌ Non gestito                                                       | ✅ Gestito con `werkzeug.security`                                |
| **Modello utente**      | Dict semplice                                                       | Oggetti `User`, con `.to_dict()` e validazione                   |
