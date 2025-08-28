# first line
"""
Script per creare il database 'boop', tutte le tabelle e renderle coerenti
con lo schema SQL originale.
"""

import json
import psycopg2
from psycopg2 import sql

# ============================================================
# Creazione database
# ============================================================
def create_database():
    with open("db/credentials.json", "r") as f:
        creds = json.load(f)

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=creds["user"],
            password=creds["password"],
            host=creds["host"],
            port=creds["port"]
        )
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s;", ("boop",))
        if cur.fetchone():
            print("Database 'boop' già esistente.")
        else:
            cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier("boop")))
            print("Database 'boop' creato correttamente!")

        cur.close()
        conn.close()
    except Exception as e:
        print("Errore durante la creazione del database:", e)
        return None

# ============================================================
# Connessione al database
# ============================================================
def connect_to_db():
    with open("db/credentials.json", "r") as f:
        creds = json.load(f)
    try:
        conn = psycopg2.connect(
            dbname="boop",
            user=creds["user"],
            password=creds["password"],
            host=creds["host"],
            port=creds["port"]
        )
        print("Connessione a 'boop' riuscita!")
        return conn
    except Exception as e:
        print("Connessione fallita:", e)
        return None

# ============================================================
# Creazione tabelle
# ============================================================
def execute_tables(conn):
    cur = conn.cursor()

    # Tabelle principali
    base_tables = [
        """
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
        """,
        """
        CREATE TABLE IF NOT EXISTS media (
            id SERIAL PRIMARY KEY,
            type VARCHAR(20) NOT NULL CHECK (type IN ('song','document','video')),
            title VARCHAR(255) NOT NULL,
            author VARCHAR(100),
            year INT,
            description TEXT,
            link VARCHAR(255),
            created_at TIMESTAMP DEFAULT NOW()
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS songs (
            id INT PRIMARY KEY REFERENCES media(id) ON DELETE CASCADE,
            duration INT,
            location VARCHAR(100),
            additional_info TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS documents (
            id INT PRIMARY KEY REFERENCES media(id) ON DELETE CASCADE,
            format VARCHAR(20),
            pages INT,
            caption TEXT,
            song_id INT REFERENCES songs(id) ON DELETE SET NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS videos (
            id INT PRIMARY KEY REFERENCES media(id) ON DELETE CASCADE,
            duration INT,
            location VARCHAR(100),
            additional_info TEXT,
            director VARCHAR(100)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS authors (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) UNIQUE NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS genres (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS instruments (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) UNIQUE NOT NULL
        );
        """,
        """
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
        """,
        """
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
        """
    ]

    # Tabelle relazioni
    rel_tables = [
        """
        CREATE TABLE IF NOT EXISTS song_genres (
            song_id INT REFERENCES songs(id) ON DELETE CASCADE,
            genre_id INT REFERENCES genres(id) ON DELETE CASCADE,
            PRIMARY KEY (song_id, genre_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS song_authors (
            song_id INT REFERENCES songs(id) ON DELETE CASCADE,
            author_id INT REFERENCES authors(id) ON DELETE CASCADE,
            PRIMARY KEY (song_id, author_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS song_performers_instruments (
            song_id INT REFERENCES songs(id) ON DELETE CASCADE,
            performer VARCHAR(100) NOT NULL,
            instrument_id INT REFERENCES instruments(id),
            PRIMARY KEY (song_id, instrument_id, performer)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS note_performers_instruments (
            note_id INT REFERENCES notes(id) ON DELETE CASCADE,
            performer VARCHAR(100) NOT NULL,
            instrument_id INT REFERENCES instruments(id),
            PRIMARY KEY (note_id, instrument_id, performer)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS follows (
            follower_id INT REFERENCES users(id) ON DELETE CASCADE,
            followed_id INT REFERENCES users(id) ON DELETE CASCADE,
            PRIMARY KEY (follower_id, followed_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS files (
            id SERIAL PRIMARY KEY,
            media_id INT REFERENCES media(id) ON DELETE CASCADE,
            file_id VARCHAR(255)
        );
        """
    ]

    # Esecuzione tabelle
    for tbl in base_tables + rel_tables:
        try:
            cur.execute(tbl)
        except Exception as e:
            print("Errore creando tabella:", e)

    # Indici utili
    try:
        cur.execute("CREATE INDEX IF NOT EXISTS idx_follows_follower ON follows(follower_id);")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_follows_followed ON follows(followed_id);")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_song_genres_song ON song_genres(song_id);")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_song_authors_song ON song_authors(song_id);")
    except Exception as e:
        print("Errore creando indici:", e)

    conn.commit()
    cur.close()

# ============================================================
# Flow principale
# ============================================================
create_database()
conn = connect_to_db()
if conn:
    execute_tables(conn)
    conn.close()

# last line