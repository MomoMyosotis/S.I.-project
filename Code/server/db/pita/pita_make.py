# first line

import json
import psycopg2
from psycopg2 import sql
import os

# ============================================================
# Percorso del file SQL
# ============================================================
SQL_FILE = os.path.join(os.path.dirname(__file__), "..", "db.sql")

# ============================================================
# Creazione database
# ============================================================
def create_database():
    with open(os.path.join(os.path.dirname(__file__), "../credentials.json"), "r") as f:
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

# ============================================================
# Connessione al database
# ============================================================
def connect_to_db():
    with open(os.path.join(os.path.dirname(__file__), "../credentials.json"), "r") as f:
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
# Esecuzione script SQL
# ============================================================
def execute_sql_file(conn, sql_file):
    with open(sql_file, "r", encoding="utf-8") as f:
        sql_content = f.read()

    cur = conn.cursor()
    try:
        cur.execute(sql_content)
        conn.commit()
        print(f"Script SQL '{sql_file}' eseguito correttamente!")
    except Exception as e:
        conn.rollback()
        print(f"Errore eseguendo '{sql_file}':", e)
    finally:
        cur.close()

# ============================================================
# Eliminazione database esistente
# ============================================================
def drop_database_if_exists():
    with open(os.path.join(os.path.dirname(__file__), "../credentials.json"), "r") as f:
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

        # Termina eventuali connessioni attive al DB
        cur.execute("""
            SELECT pg_terminate_backend(pid)
            FROM pg_stat_activity
            WHERE datname = %s AND pid <> pg_backend_pid();
        """, ("boop",))

        cur.execute("DROP DATABASE IF EXISTS boop;")
        print("Database 'boop' eliminato (se esisteva).")

        cur.close()
        conn.close()
    except Exception as e:
        print("Errore durante l'eliminazione del database:", e)

# ============================================================
# Flow principale
# ============================================================
def flow():
    drop_database_if_exists()
    create_database()
    conn = connect_to_db()
    if conn:
        execute_sql_file(conn, SQL_FILE)
        conn.close()

flow()

# last line