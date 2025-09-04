-- ========================================
-- Tabelle per gestione utenti e ruoli
-- ========================================

-- Tabella dei livelli/ruoli utente
CREATE TABLE user_levels (
    id INT PRIMARY KEY,            -- corrisponde a UserLevel Enum
    name VARCHAR(50) NOT NULL,     -- es. 'ROOT', 'ADMIN', 'MOD', 'PUBLISHER', 'REGULAR', 'BANNED'
    description TEXT
);

-- Tabella degli utenti
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    mail VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    birthday DATE NOT NULL,
    bio TEXT,
    profile_pic VARCHAR(255),
    lvl INT NOT NULL DEFAULT 4,    -- REGULAR per default
    FOREIGN KEY (lvl) REFERENCES user_levels(id)
);

-- Tabella per followers/followed (relazione molti-a-molti tra utenti)
CREATE TABLE user_follow (
    follower_id INT NOT NULL,
    followed_id INT NOT NULL,
    PRIMARY KEY (follower_id, followed_id),
    FOREIGN KEY (follower_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (followed_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Tabella dei permessi
CREATE TABLE permissions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,    -- es. 'manage_content', 'comment', 'view_content'
    description TEXT
);

-- Tabella relazione ruolo-permesso (molti-a-molti)
CREATE TABLE role_permissions (
    lvl_id INT NOT NULL,
    permission_id INT NOT NULL,
    PRIMARY KEY (lvl_id, permission_id),
    FOREIGN KEY (lvl_id) REFERENCES user_levels(id) ON DELETE CASCADE,
    FOREIGN KEY (permission_id) REFERENCES permissions(id) ON DELETE CASCADE
);

-- ============================================================
-- MEDIA (contenitore generico)
-- ============================================================
CREATE TABLE media (
    id SERIAL PRIMARY KEY,
    type VARCHAR(20) NOT NULL CHECK (type IN ('song','document','video')),
    user_id INT REFERENCES users(id),  -- autore/interprete
    title VARCHAR(255) NOT NULL,
    year INT,
    description TEXT,
    link VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);

-- ============================================================
-- SONGS (estensione di MEDIA)
-- ============================================================
CREATE TABLE songs (
    id INT PRIMARY KEY REFERENCES media(id) ON DELETE CASCADE,
    duration INT,
    recording_date DATE,
    location VARCHAR(100),
    additional_info TEXT,
    is_author BOOLEAN DEFAULT FALSE,
    is_performer BOOLEAN DEFAULT FALSE
);

-- ============================================================
-- DOCUMENTS (estensione di MEDIA)
-- ============================================================
CREATE TABLE documents (
    id INT PRIMARY KEY REFERENCES media(id) ON DELETE CASCADE,
    format VARCHAR(10),
    pages INT,
    caption TEXT,
    song_id INT REFERENCES songs(id) ON DELETE SET NULL
);

-- ============================================================
-- VIDEOS (estensione di MEDIA)
-- ============================================================
CREATE TABLE videos (
    id INT PRIMARY KEY REFERENCES media(id) ON DELETE CASCADE,
    duration INT,
    location VARCHAR(100),
    additional_info TEXT,
    director VARCHAR(100)
);

-- ============================================================
-- GENERI
-- ============================================================
CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE song_genres (
    song_id INT REFERENCES songs(id) ON DELETE CASCADE,
    genre_id INT REFERENCES genres(id) ON DELETE CASCADE,
    PRIMARY KEY (song_id, genre_id)
);

-- ============================================================
-- AUTORI
-- ============================================================
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE song_authors (
    song_id INT REFERENCES songs(id) ON DELETE CASCADE,
    author_id INT REFERENCES authors(id) ON DELETE CASCADE,
    PRIMARY KEY (song_id, author_id)
);

-- ============================================================
-- STRUMENTI
-- ============================================================
CREATE TABLE instruments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- ============================================================
-- ESECUTORI
-- ============================================================
CREATE TABLE performers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE song_performances (
    id SERIAL PRIMARY KEY,
    song_id INT REFERENCES songs(id) ON DELETE CASCADE,
    performer_id INT REFERENCES performers(id) ON DELETE CASCADE,
    instrument_id INT REFERENCES instruments(id),
    duration INT,
    recording_date DATE,
    recording_location VARCHAR(50),
    additional_info TEXT
);

-- tabella many-to-many per associare strumenti alle performance
CREATE TABLE performance_instruments (
    performance_id INT NOT NULL REFERENCES song_performances(id) ON DELETE CASCADE,
    instrument_id INT NOT NULL REFERENCES instruments(id) ON DELETE CASCADE,
    PRIMARY KEY (performance_id, instrument_id),
    FOREIGN KEY (performance_id) REFERENCES song_performances(id) ON DELETE CASCADE,
    FOREIGN KEY (instrument_id) REFERENCES instruments(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS UserMediaLibrary (
    user_id INT NOT NULL,
    media_id INT NOT NULL,
    added_at TIMESTAMP NOT NULL,
    PRIMARY KEY(user_id, media_id),
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY(media_id) REFERENCES media(id) ON DELETE CASCADE
);

-- ============================================================
-- FILE ASSOCIATI
-- ============================================================
CREATE TABLE files (
    id SERIAL PRIMARY KEY,
    media_id INT REFERENCES media(id) ON DELETE CASCADE,
    file_id VARCHAR(255) -- UUID o ID esterno
);

-- ============================================================
-- NOTE SU SEGMENTI DI ESECUZIONE
-- ============================================================
CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    media_id INT REFERENCES media(id) ON DELETE CASCADE,
    x_coord NUMERIC(6,2),
    y_coord NUMERIC(6,2),
    start_time NUMERIC(6,2),
    end_time NUMERIC(6,2),
    solos TEXT,
    rhythm VARCHAR(50),
    link VARCHAR(255),
    comment TEXT
);

CREATE TABLE note_performers_instruments (
    note_id INT REFERENCES notes(id) ON DELETE CASCADE,
    performer_id INT REFERENCES performers(id),
    instrument_id INT REFERENCES instruments(id),
    PRIMARY KEY (note_id, performer_id, instrument_id)
);

-- ============================================================
-- COMMENTI
-- ============================================================
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    media_id INT REFERENCES media(id) ON DELETE CASCADE,
    note_id INT REFERENCES notes(id) ON DELETE CASCADE,
    parent_comment_id INT REFERENCES comments(id) ON DELETE CASCADE,
    text TEXT NOT NULL,
    like_count INT DEFAULT 0,
    dislike_count INT DEFAULT 0,
    CHECK (
        (media_id IS NOT NULL AND note_id IS NULL) OR
        (media_id IS NULL AND note_id IS NOT NULL)
    )
);

-- ============================================================
-- CONCERTI E SEGMENTI VIDEO
-- ============================================================
CREATE TABLE concerts (
    id SERIAL PRIMARY KEY,
    video_id INT REFERENCES videos(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE concert_segments (
    id SERIAL PRIMARY KEY,
    concert_id INT REFERENCES concerts(id) ON DELETE CASCADE,
    song_id INT REFERENCES songs(id) ON DELETE CASCADE,
    start_time NUMERIC(6,2),
    end_time NUMERIC(6,2),
    performers JSONB,  -- elenco performer
    instruments JSONB, -- elenco strumenti
    comment TEXT
);

-- ============================================================
-- INDICI UTILI
-- ============================================================
CREATE INDEX idx_users_lvl ON users(lvl);
CREATE INDEX idx_user_follow_follower ON user_follow(follower_id);
CREATE INDEX idx_user_follow_followed ON user_follow(followed_id);
CREATE INDEX idx_song_genres_song ON song_genres(song_id);
CREATE INDEX idx_song_authors_song ON song_authors(song_id);
CREATE INDEX idx_song_perf_song ON song_performances(song_id);
CREATE INDEX idx_comments_parent ON comments(parent_comment_id);