# first line

import json, psycopg2

# Connects with the server
def connect():
    # Connessione al server di PostgreSQL

        # Open the credentials file and load the JSON data
    with open("server/db/credentials.json", "r") as nooty:
        pruty = json.load(nooty)
    try:
        # ** -> scompone il dict in parametri
        conn = psycopg2.connect(**pruty)
        return conn
    except Exception as e:
        print("Failed to establish connection:\n", e)
        return None

# last line