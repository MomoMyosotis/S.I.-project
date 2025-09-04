# first line

import time
from tabulate import tabulate
from db.pita.pita_make import connect_to_db as connect
from db.pita.pita_tablefill import (
    user_levels_tablefill as ul,
    permissions_tablefill as pm,
    role_permissions_tablefill as rp,
    user_tablefill as ut,
    # instruments_tablefill as it,
    # performers_tablefill as pt,
    # genres_tablefill as gt,
    # authors_tablefill as at,
    songs_tablefill as st,
    documents_tablefill as dt,
    videos_tablefill as vt,
    # song_performances_tablefill as spt
)

# =========================
# Funzione per stampare le prime 10 righe di una tabella (debug)
# =========================
def tprint(cur, tname, limit=10):
    try:
        cur.execute(f"SELECT * FROM {tname} LIMIT {limit};")
        rows = cur.fetchall()
        if rows:
            headers = [desc[0] for desc in cur.description]
            print(tabulate(rows, headers=headers, tablefmt="psql"))
        else:
            print(f"No data found in table {tname}.")
    except Exception as e:
        print(f"Error fetching data from table {tname}: {str(e)}")

# =========================
# Popolamento ordinato
# =========================
def populate(cnt, cur):
    tables = [
        ("User Levels", ul, "user_levels"),
        ("Permissions", pm, "permissions"),
        ("Role-Permissions", rp, "role_permissions"),
        ("Users", ut, "users"),
#         ("Instruments", it, "instruments"),
#         ("Performers", pt, "performers"),
#         ("Genres", gt, "genres"),
#         ("Authors", at, "authors"),
        ("Media (Songs)", st, "songs"),
        ("Media (Documents)", dt, "documents"),
        ("Media (Videos)", vt, "videos"),
#         ("Song Performances", spt, "song_performances")
    ]

    print("Starting database population...\n")

    for name, func, tname in tables:
        try:
            print(f"Populating {name}...")
            func(cnt, cur)  # passiamo connessione e cursore
            cnt.commit()
            tprint(cur, tname)
            print(f"{name} populated successfully.\n")
        except Exception as e:
            cnt.rollback()
            print(f"Error populating {name}: {e}\n")

# =========================
# Connessione iniziale
# =========================
def first_connection():
    print("first_connection() start")
    cnt = connect()
    if cnt is None:
        print("Couldn't connect to the DB. Check credentials.")
        return None, None

    cur = cnt.cursor()
    populate(cnt, cur)
    print("first_connection() ended")
    return cnt, cur

# =========================
# Flow principale
# =========================
def flow():
    print("flow() started")
    conn, cur = first_connection()
    if not conn or not cur:
        print("Flow aborted due to connection error.")
        return False

    time.sleep(1)
    cur.close()
    conn.close()
    print("flow() ended")
    return True

flow()

# last line