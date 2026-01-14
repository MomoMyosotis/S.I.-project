-- ========================================
-- UTENTI E RUOLI
-- ========================================
CREATE TABLE user_levels (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,   -- es. ROOT, ADMIN, MOD, PUBLISHER, REGULAR, BANNED
    description TEXT
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    mail VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    birthday DATE NOT NULL,
    bio TEXT,
    profile_pic VARCHAR(255), -- la sua posizione nello storage
    lvl_id INT NOT NULL REFERENCES user_levels(id) DEFAULT 4
);

CREATE TABLE user_follow (
    follower_id INT NOT NULL,
    followed_id INT NOT NULL,
    PRIMARY KEY (follower_id, followed_id),
    FOREIGN KEY (follower_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (followed_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE permissions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE role_permissions (
    lvl_id INT NOT NULL REFERENCES user_levels(id) ON DELETE CASCADE,
    permission_id INT NOT NULL REFERENCES permissions(id) ON DELETE CASCADE,
    PRIMARY KEY (lvl_id, permission_id)
);

-- ========================================
-- MEDIA GENERICO (unica tabella per song e video)
-- ========================================
CREATE TABLE media (
    id SERIAL PRIMARY KEY,
    type VARCHAR(20) NOT NULL CHECK (type IN ('song','video','document','concert')), -- identifica il tipo
    user_id INT REFERENCES users(id),
    title VARCHAR(255) NOT NULL,
    year INT,
    description TEXT,
    linked_media TEXT,
    duration INT,
    recording_date DATE,
    location VARCHAR(100),
    additional_info TEXT,
    stored_at VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW(),
    is_author BOOLEAN DEFAULT FALSE,
    is_performer BOOLEAN DEFAULT FALSE
);

-- ========================================
-- GENRES
-- ========================================
CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE media_genres (
    media_id INT REFERENCES media(id) ON DELETE CASCADE,
    genre_id INT REFERENCES genres(id) ON DELETE CASCADE,
    PRIMARY KEY (media_id, genre_id)
);

-- ========================================
-- AUTHORS
-- ========================================
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) UNIQUE NOT NULL,
    user_id INT REFERENCES users(id) -- se registrato nel sistema
);

CREATE TABLE media_authors (
    media_id INT REFERENCES media(id) ON DELETE CASCADE,
    author_id INT REFERENCES authors(id) ON DELETE CASCADE,
    PRIMARY KEY (media_id, author_id)
);

-- ========================================
-- INSTRUMENTS
-- ========================================
CREATE TABLE instruments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- ========================================
-- PERFORMERS
-- ========================================
CREATE TABLE performers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) UNIQUE NOT NULL,
    user_id INT REFERENCES users(id) UNIQUE
);

-- ========================================
-- PERFORMANCE (molti-a-molti: media <-> performer con strumenti)
-- ========================================
CREATE TABLE media_performances (
    id SERIAL PRIMARY KEY,
    media_id INT REFERENCES media(id) ON DELETE CASCADE,
    performer_id INT REFERENCES performers(id) ON DELETE CASCADE,
    additional_info TEXT,
    CONSTRAINT media_perf_unique UNIQUE (media_id, performer_id)
);

CREATE TABLE performance_instruments (
    performance_id INT REFERENCES media_performances(id) ON DELETE CASCADE,
    instrument_id INT REFERENCES instruments(id) ON DELETE CASCADE,
    PRIMARY KEY (performance_id, instrument_id)
);

-- ========================================
-- DOCUMENTS
-- ========================================
CREATE TABLE documents (
    media_id INT PRIMARY KEY REFERENCES media(id) ON DELETE CASCADE,
    format VARCHAR(20),
    pages INT,
    caption TEXT
);

-- ========================================
-- LIBRERIA UTENTI
-- ========================================
CREATE TABLE user_media_library (
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    media_id INT NOT NULL REFERENCES media(id) ON DELETE CASCADE,
    added_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY(user_id, media_id)
);

-- ========================================
-- MEDIA REFERENZIATI (collegamenti tra media)
-- ========================================
CREATE TABLE media_references (
    active_id INT NOT NULL REFERENCES media(id) ON DELETE CASCADE, -- il media che referenzia
    passive_id INT NOT NULL REFERENCES media(id) ON DELETE CASCADE, -- il media che viene referenziato
    PRIMARY KEY (active_id, passive_id)
);

-- ========================================
-- NOTE SU SEGMENTI (segnaposti temporali o grafici)
-- ========================================
CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    author INT REFERENCES users(id),
    is_public BOOLEAN DEFAULT TRUE,
    media_id INT REFERENCES media(id) ON DELETE CASCADE,
    note_type VARCHAR(20) CHECK (note_type IN ('regular','graphic')),
    start_time NUMERIC(8,2),
    end_time NUMERIC(8,2),
    x_coord NUMERIC(8,2),
    y_coord NUMERIC(8,2),
    page INT,
    solos TEXT,
    rhythm VARCHAR(50),
    content TEXT,
    stored_at VARCHAR(255)
);

CREATE TABLE note_performers_instruments (
    note_id INT REFERENCES notes(id) ON DELETE CASCADE,
    performer_id INT REFERENCES performers(id),
    instrument_id INT REFERENCES instruments(id),
    PRIMARY KEY (note_id, performer_id, instrument_id)
);

-- ========================================
-- COMMENTI ANNIDATI
-- ========================================
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    media_id INT REFERENCES media(id) ON DELETE CASCADE,
    note_id INT REFERENCES notes(id) ON DELETE CASCADE,
    parent_comment_id INT REFERENCES comments(id) ON DELETE CASCADE,
    text TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ========================================
-- CONCERTI (sottoclasse di video)
-- ========================================
CREATE TABLE concerts (
    link VARCHAR(255),
    video_id INT PRIMARY KEY REFERENCES media(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE concert_segments (
    id SERIAL PRIMARY KEY,
    concert_id INT REFERENCES concerts(id) ON DELETE CASCADE,
    media_id INT REFERENCES media(id) ON DELETE CASCADE, -- tipo song
    song_title VARCHAR(255),
    start_time NUMERIC(8,2),
    end_time NUMERIC(8,2),
    comment TEXT
);

CREATE TABLE concert_segment_performers (
    segment_id INT REFERENCES concert_segments(id) ON DELETE CASCADE,
    performer_id INT REFERENCES performers(id) ON DELETE CASCADE,
    PRIMARY KEY (segment_id, performer_id)
);

CREATE TABLE concert_segment_instruments (
    segment_id INT REFERENCES concert_segments(id) ON DELETE CASCADE,
    instrument_id INT REFERENCES instruments(id) ON DELETE CASCADE,
    PRIMARY KEY (segment_id, instrument_id)
);

-- ========================================
-- INDICI
-- ========================================
CREATE INDEX idx_users_lvl ON users(lvl_id);
CREATE INDEX idx_user_follow_follower ON user_follow(follower_id);
CREATE INDEX idx_user_follow_followed ON user_follow(followed_id);
CREATE INDEX idx_media_genres_media ON media_genres(media_id);
CREATE INDEX idx_media_authors_media ON media_authors(media_id);
CREATE INDEX idx_media_perf_media ON media_performances(media_id);
CREATE INDEX idx_comments_parent ON comments(parent_comment_id);

-- ========================================
-- POPOLO TABELLA USER LVL
-- ========================================
INSERT INTO user_levels (id, code, description) VALUES
(0, 'ROOT', 'Super user'),
(1, 'ADMIN', 'Administrator'),
(2, 'MOD', 'Moderator'),
(3, 'PUBLISHER', 'Content publisher'),
(4, 'REGULAR', 'Regular user'),
(5, 'RESTRICTED', 'Restricted user'),
(6, 'BANNED', 'Banned user');