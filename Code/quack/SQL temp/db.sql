
--      tabella utenti
CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    mail VARCHAR(100) UNIQUE NOT NULL,
    foto_profilo VARCHAR(255), -- il server memorizza l'url della foto non la foto in sè
    birthday DATE,
    bio TEXT,
    lvl INT DEFAULT 4 -- vedi Code\objects\dizionari\"user lvl.json"
);


--      tabella brani
CREATE TABLE IF NOT EXISTS Songs (
    id SERIAL PRIMARY KEY,
    media_name VARCHAR(100),
    title VARCHAR(100) NOT NULL,
    durata VARCHAR(10),
    year DATE,
    location VARCHAR(100),
    ulteriori_info TEXT,
    esecutore VARCHAR(100)
);

--      tabella generi (id generes)

CREATE TABLE IF NOT EXISTS Generi (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) UNIQUE NOT NULL
);

--      tabella relazione Songs-Generi (many-to-many)

CREATE TABLE IF NOT EXISTS Song_Genres (
    song_id INT REFERENCES Songs(id) ON DELETE CASCADE,
    genere_id INT REFERENCES Generi(id) ON DELETE CASCADE,
    PRIMARY KEY (song_id, genere_id)
);

--      tabella autori
--      non possiamo usare uno user lvl 2 perché non è detto che sia l'autore a pubblicare il media
CREATE TABLE IF NOT EXISTS Autori (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) UNIQUE NOT NULL
);

--      relazione Songs-Autori (many-to-many)

CREATE TABLE IF NOT EXISTS Song_Autori (
    song_id INT REFERENCES Songs(id) ON DELETE CASCADE,
    autore_id INT REFERENCES Autori(id) ON DELETE CASCADE,
    PRIMARY KEY (song_id, autore_id)
);

--      tabella strumenti

CREATE TABLE IF NOT EXISTS Strumenti (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) UNIQUE NOT NULL
);

--      tabella file associati al brano

CREATE TABLE IF NOT EXISTS File_Song (
    id SERIAL PRIMARY KEY,
    song_id INT REFERENCES Songs(id) ON DELETE CASCADE,
    file_id VARCHAR(255) -- ID da sistema esterno o UUID
);

--      tabella dati aggiuntivi esecutori/strumenti

CREATE TABLE IF NOT EXISTS Song_Esecutori_Stru (
    song_id INT REFERENCES Songs(id) ON DELETE CASCADE,
    esecutore VARCHAR(100),
    strumento_id INT REFERENCES Strumenti(id),
    PRIMARY KEY (song_id, strumento_id, esecutore)
);

--      tabella note

CREATE TABLE IF NOT EXISTS Notes (
    id SERIAL PRIMARY KEY,
    song_id INT REFERENCES Songs(id) ON DELETE CASCADE,
    coordinate_x VARCHAR(10),
    coordinate_y VARCHAR(10),
    istante_inizio VARCHAR(10),
    istante_fine VARCHAR(10),
    assoli TEXT,
    ritmo VARCHAR(50),
    link VARCHAR(255),
    commento TEXT
);

--      tabella esecutori/strumenti delle note (many-to-many)

CREATE TABLE IF NOT EXISTS Note_Esecutori_Strumenti (
    note_id INT REFERENCES Notes(id) ON DELETE CASCADE,
    esecutore VARCHAR(100),
    strumento_id INT REFERENCES Strumenti(id),
    PRIMARY KEY (note_id, strumento_id, esecutore)
);

--      tabella documenti

CREATE TABLE IF NOT EXISTS Documenti (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    autore VARCHAR(100),
    year DATE,
    link VARCHAR(255),
    id_media_riferimento INT REFERENCES Songs(id) ON DELETE SET NULL,
    didascalia TEXT
);

--      tabella commenti

CREATE TABLE IF NOT EXISTS Commenti (
    id SERIAL PRIMARY KEY,
    testo TEXT NOT NULL,
    nodo_riferimento VARCHAR(100),
    like_count INT DEFAULT 0,
    dislike_count INT DEFAULT 0
);
