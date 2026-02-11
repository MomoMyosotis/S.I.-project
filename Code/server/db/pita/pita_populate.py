# first line

import time
from tabulate import tabulate
from server.db.pita.pita_make import connect_to_db as connect
from server.db.pita.pita_tablefill import (
    fill_user_levels as ul,
    fill_permissions as pm,
    fill_role_permissions as rp,
    fill_users as ut,
    fill_media as mt,
)

# =========================
# print prime 10 righe di una tabella (debug)
# =========================
def tprint(cur, tname, limit=10):
    try:
        cur.execute(f"SELECT * FROM {tname} LIMIT {limit};")
        rows = cur.fetchall()
        if rows:
            headers = [desc[0] for desc in cur.description]
            #print(tabulate(rows, headers=headers, tablefmt="psql"))
        else:
            print(f"No data found in table {tname}.")
    except Exception as e:
        print(f"Error fetching data from table {tname}: {str(e)}")

# =========================
# Popolamento
# =========================
def populate(cnt, cur):
    tables = [
        ("User Levels", ul, "user_levels"),
        ("Permissions", pm, "permissions"),
        ("Role-Permissions", rp, "role_permissions"),
        ("Users", ut, "users"),
        ("Media", mt, "media")
    ]


    #print("Starting database population...\n")

    for name, func, tname in tables:
        try:
            #print(f"Populating {name}...")
            func(cnt, cur)  # passiamo connessione e cursore
            cnt.commit()
            tprint(cur, tname)
            #print(f"{name} populated successfully.\n")
        except Exception as e:
            cnt.rollback()
            #print(f"Error populating {name}: {e}\n")

# =========================
# Connessione iniziale
# =========================
def first_connection():
    #print("first_connection() start")
    cnt = connect()
    if cnt is None:
        #print("Couldn't connect to the DB. Check credentials.")
        return None, None

    cur = cnt.cursor()
    populate(cnt, cur)
    #print("first_connection() ended")
    return cnt, cur

# =========================
# Flow principale
# =========================
def flow():
    #print("flow() started")
    conn, cur = first_connection()
    if not conn or not cur:
        #print("Flow aborted due to connection error.")
        return False

    time.sleep(1)
    cur.close()
    conn.close()
    #print("flow() ended")
    return True

flow()

# last line