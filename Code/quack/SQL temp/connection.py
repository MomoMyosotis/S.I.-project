# first line

import time
import os
import psycopg2
import json
from tabulate import tabulate

def close(cur, cnt):
    cur.close()
    cnt.close()

# print table
def tprint (cur, tname):
    # per stampare i risultati
    try:
        # Esegui la query per ottenere tutti i dati dalla tabella
        cur.execute(f"SELECT * FROM {tname};")
        rows = cur.fetchall()
        if rows:
            # Stampa la tabella con `tabulate`
            print(tabulate(rows, headers=[], tablefmt="psql"))
        else:
            print(f"No data found in table {tname}.")
    except Exception as e:
        print(f"Error fetching data from table {tname}: {str(e)}")

#   create the db - just a bunch of empty tables
def make_db(cur):
    #   apre il file in lettura e copia il contenuto come fosse una stringa
    with open('db.sql') as file:
        db = file.read()
    #   passa la stringa come comando
    cur.execute(db)
    print("tables created, now gotta populate 'em")

# Connects with the server
def connect():
    # Connessione al server di PostgreSQL

        # Open the credentials file and load the JSON data
    with open("credentials.json", "r") as nooty:
        pruty = json.load(nooty)
    try:
        # ** -> scompone il dict in parametri
        conn = psycopg2.connect(**pruty)
        return conn
    except Exception as e:
        print("Failed to establish connection:\n", e)
        return None

#   first interation with the db
def first_connection():

    cnt = connect()
    if cnt is None:
        print ("couldn't connect to db or somme other shit you gotta check.\nfile is connection.py")
        return
    else:
        print ("Connection established correctly, yay!")
        cur = cnt.cursor()
        make_db(cur)
        # commit() è un modulo  di connect
        cnt.commit()
    return cnt, cur

#   fills the db's tables
def populate(cnt, cur):
    def fill_query(miao, cur):
        if miao == 0:
            print("starting loop")
            return 1

        if miao == 1:
            # tabella owner
            try:
                with open("Users tablefill.sql") as file:
                    quack = file.read()
                    quack = str(quack)
                    cur.execute(quack)
                file.close()
            except Exception as e:
                print("error 9.\n " + str(e))
                return None
            else:
                print("\nowner table... done")

                time.sleep(2)
                os.system("clear")
                tprint(cur, "owners")
                cnt.commit()
                return "quack"

    print("we're populating")

# this wa used for automatic population of the database. will need to be modified
# see Code\objects\modifica.py

    bl = 0
    while bl in [0, 1, 2, 3]:
        checking = fill_query(bl, cur)
        bl +=1
        if checking is None:
            return

# flow
def flow():
    connessione, cursore = first_connection()
    cur = populate(connessione, cursore)
    time.sleep(2)
    os.system("clear")

flow()
# last line