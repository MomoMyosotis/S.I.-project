# first line

import time
from db import connect
from tabulate import tabulate

def close(cur=None, cnt=None):
    if cur:
        try:
            cur.close()
        except Exception as e:
            print(f"[WARN] closing cursor failed: {e}")
    if cnt:
        try:
            cnt.close()
        except Exception as e:
            print(f"[WARN] closing connection failed: {e}")


# print table contents
def tprint(cur, tname):
    try:
        cur.execute(f"SELECT * FROM {tname};")
        rows = cur.fetchall()
        if rows:
            print(tabulate(rows, headers=[], tablefmt="psql"))
            return True
        else:
            print(f"No data found in table {tname}.")
            return False
    except Exception as e:
        print(f"Error fetching data from table {tname}: {str(e)}")
        return False

# check if the db has required tables and data
def check_db(cur, required_tables):
    try:
        # ottieni l’elenco delle tabelle
        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public';
        """)
        tables = {row[0] for row in cur.fetchall()}

        # controlla che tutte le tabelle richieste ci siano
        for t in required_tables:
            if t not in tables:
                print(f"Missing table: {t}")
                return False

        # controlla che non siano vuote
        for t in required_tables:
            if not tprint(cur, t):
                print(f"Table {t} exists but has no data.")
                return False

        return True
    except Exception as e:
        print(f"Error during DB check: {str(e)}")
        return False

# main flow
def flow():
    print("flow() started")
    cnt = connect()
    if cnt is None:
        print("Couldn't connect to DB.")
        return False

    cur = cnt.cursor()
    required_tables = ["users", "songs", "documents"]

    result = check_db(cur, required_tables)

    close(cur, cnt)
    print("flow() ended")
    return result

if __name__ == "__main__":
    status = flow()
    print(f"Database check result: {status}")


# last line