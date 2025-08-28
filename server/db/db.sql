-- ============================================================
-- UTENTI
-- ============================================================
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    mail VARCHAR(100) UNIQUE NOT NULL,
    foto_profilo VARCHAR(255),
    birthday DATE,
    bio TEXT,
    lvl INT DEFAULT 4
);

-- ============================================================
-- MEDIA (contenitore generico per brani, documenti, video, ecc.)
-- ============================================================
CREATE TABLE IF NOT EXISTS media (
    id SERIAL PRIMARY KEY,
    type VARCHAR(20) NOT NULL CHECK (type IN ('song','document','video')),
    title VARCHAR(255) NOT NULL,
    year INT,
    description TEXT,
    link VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);

-- ============================================================
-- SONGS (estensione di MEDIA)
-- ============================================================
CREATE TABLE IF NOT EXISTS songs (
    id INT PRIMARY KEY REFERENCES media(id) ON DELETE CASCADE,
    duration INT,                -- in secondi
    recording_date DATE,
    location VARCHAR(100),
    additional_info TEXT
);

-- ============================================================
-- DOCUMENTS (estensione di MEDIA)
-- ============================================================
CREATE TABLE IF NOT EXISTS documents (
    id INT PRIMARY KEY REFERENCES media(id) ON DELETE CASCADE,
    format VARCHAR(20),
    pages INT,
    caption TEXT,
    song_id INT REFERENCES songs(id) ON DELETE SET NULL
);

-- ============================================================
-- VIDEOS (estensione di MEDIA)
-- ============================================================
CREATE TABLE IF NOT EXISTS videos (
    id INT PRIMARY KEY REFERENCES media(id) ON DELETE CASCADE,
    duration INT,
    location VARCHAR(100),
    additional_info TEXT,
    director VARCHAR(100)
);

-- ============================================================
-- GENERI
-- ============================================================
CREATE TABLE IF NOT EXISTS genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS song_genres (
    song_id INT REFERENCES songs(id) ON DELETE CASCADE,
    genre_id INT REFERENCES genres(id) ON DELETE CASCADE,
    PRIMARY KEY (song_id, genre_id)
);

-- ============================================================
-- AUTORI (collettivi, co-autori, ecc.)
-- ============================================================
CREATE TABLE IF NOT EXISTS authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS song_authors (
    song_id INT REFERENCES songs(id) ON DELETE CASCADE,
    author_id INT REFERENCES authors(id) ON DELETE CASCADE,
    PRIMARY KEY (song_id, author_id)
);

-- ============================================================
-- STRUMENTI
-- ============================================================
CREATE TABLE IF NOT EXISTS instruments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- ============================================================
-- ESECUTORI
-- ============================================================
CREATE TABLE IF NOT EXISTS performers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- legame brano ↔ esecutore ↔ strumento
CREATE TABLE IF NOT EXISTS song_performances (
    song_id INT REFERENCES songs(id) ON DELETE CASCADE,
    performer_id INT REFERENCES performers(id) ON DELETE CASCADE,
    instrument_id INT REFERENCES instruments(id),
    PRIMARY KEY (song_id, performer_id, instrument_id)
);

-- ============================================================
-- FILE ASSOCIATI (generico, non solo song)
-- ============================================================
CREATE TABLE IF NOT EXISTS files (
    id SERIAL PRIMARY KEY,
    media_id INT REFERENCES media(id) ON DELETE CASCADE,
    file_id VARCHAR(255)                   -- UUID o ID esterno
);

-- ============================================================
-- NOTE (annotazioni su brani)
-- ============================================================
CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    song_id INT REFERENCES songs(id) ON DELETE CASCADE,
    x_coord NUMERIC(6,2),
    y_coord NUMERIC(6,2),
    start_time NUMERIC(6,2),
    end_time NUMERIC(6,2),
    solos TEXT,
    rhythm VARCHAR(50),
    link VARCHAR(255),
    comment TEXT
);

CREATE TABLE IF NOT EXISTS note_performers_instruments (
    note_id INT REFERENCES notes(id) ON DELETE CASCADE,
    performer_id INT REFERENCES performers(id),
    instrument_id INT REFERENCES instruments(id),
    PRIMARY KEY (note_id, performer_id, instrument_id)
);

-- ============================================================
-- COMMENTI
-- ============================================================
CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    media_id INT REFERENCES media(id) ON DELETE CASCADE,
    note_id INT REFERENCES notes(id) ON DELETE CASCADE,
    text TEXT NOT NULL,
    like_count INT DEFAULT 0,
    dislike_count INT DEFAULT 0,
    CHECK (
        (media_id IS NOT NULL AND note_id IS NULL) OR
        (media_id IS NULL AND note_id IS NOT NULL)
    )
);

-- ============================================================
-- RELAZIONE FOLLOW
-- ============================================================
CREATE TABLE IF NOT EXISTS follows (
    follower_id INT REFERENCES users(id) ON DELETE CASCADE,
    followed_id INT REFERENCES users(id) ON DELETE CASCADE,
    PRIMARY KEY (follower_id, followed_id)
);

-- ============================================================
-- INDICI UTILI
-- ============================================================
CREATE INDEX IF NOT EXISTS idx_follows_follower ON follows(follower_id);
CREATE INDEX IF NOT EXISTS idx_follows_followed ON follows(followed_id);
CREATE INDEX IF NOT EXISTS idx_song_genres_song ON song_genres(song_id);
CREATE INDEX IF NOT EXISTS idx_song_authors_song ON song_authors(song_id);
CREATE INDEX IF NOT EXISTS idx_song_perf_song ON song_performances(song_id);