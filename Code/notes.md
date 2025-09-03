Server

✅ Gestione media (song, video, documenti) con CRUD già implementata
✅ Gestione utenti (class User)
✅ Logging e tester già pronti

⚠ Mancano:

Gestione commenti e note multilivello (innestati a qualsiasi profondità)

Ruoli e permessi differenziati (root, admin, moderatore, publisher, regulare, blocked, followed, banned)

Informazioni aggiuntive per media: esecutori, strumenti, durata, luogo e data registrazione per mp3/mp4/video live

Meta-informazioni per video/link YouTube dei concerti (inizio/fine brani, strumenti, commenti)

Cancellazione commenti offensivi da parte admin o commenti altrui da parte dell’utente proprietario

Dizionari aggiornabili: strumenti, generi, autori, titoli (per ricerche e dropdown)

Client

✅ Login, registrazione base
✅ Struttura blueprint e HTML/CSS per home, feed, librerie, profili
⚠ Mancano:

Interazione reale con server per commenti/note multilivello

Interfaccia gestione ruoli/permessi

Inserimento meta-info brani live/video concerti

Player integrato per file multimediali o link YouTube

Form aggiornamento dizionari e ricerca avanzata

Streaming/Player

⚠ Streaming live è richiesto solo per YouTube o file locali. In pratica serve un player che possa riprodurre mp3/mp4/video YouTube con possibilità di annotare segmenti del brano. Questo è core per la parte multimediale, ma non deve necessariamente essere un vero “live streaming server” custom.

#####################################################
#####################################################
#####################################################

__Sprint 1: Core server__

Obiettivo: struttura dei dati e permessi completa

Gestione ruoli utenti con permessi differenziati (CRUD, commenti, gestione contenuti)

CRUD commenti e note multilivello (possibilità di innestare commenti a qualsiasi profondità)

Meta-info per media: esecutori, strumenti, durata, luogo/data registrazione

Cancellazione commenti da parte di admin o proprietario

Output: server pronto a gestire qualsiasi tipo di operazione prevista dalla consegna.

__Sprint 2: Core client__

Obiettivo: collegare server e interfaccia utente

Blueprint e HTML/CSS per feed, librerie, profili

Visualizzazione, inserimento e innesto di commenti/note multilivello

Form per inserimento meta-info su media

Validazione permessi lato client (ad esempio, utente blocked non può commentare)

Implementazione fetch/POST verso server per tutte le operazioni sopra

Output: client funzionante con dati reali, testabile su utenti e media diversi.

__Sprint 3: Funzionalità multimediali avanzate__

Obiettivo: integrare player e annotazioni segmenti

Player per mp3/mp4 e YouTube

Annotazioni su segmenti di brani/video (assoli, strumenti, ritmi)

Differenziazione commenti proprietario vs altri utenti

Meta-info concerti: inizio/fine brani, strumenti, commenti

Dizionari aggiornabili per strumenti, generi, autori, titoli

Output: esperienza completa di fruizione e annotazione multimediale.

__Sprint 4: Funzionalità opzionali / polish__

Dashboard admin/moderatore (gestione utenti, rimozione commenti)

Ricerca avanzata: titolo, autore, esecutore, genere

Caching o ottimizzazioni frontend (opzionale)

Bugfix e test di integrazione