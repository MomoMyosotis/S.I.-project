# first line

import socket, threading
from services.config_loader import load_config
from services.handle_client import handle_client
from services.admin_console import manual_cmd, approval_queue
from db.connection import flow


MAX_CONNECTIONS = 73
semaphore = threading.Semaphore(MAX_CONNECTIONS)

stop_event = threading.Event()
server_state = {"socket": None, "connections": []}
mode_ref = ["auto"]  # lista per passaggio by-ref del mode

def start_server(state):

    config = load_config()
    host, port = config["HOST"], config["PORT"]

    # crea socket (endpoint for sending\reciving data)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(15)
    print(f"Server listening on {host}:{port}")

    # thread per manual comads
    state["socket"] = s
    threading.Thread(target=manual_cmd, args=(state, mode_ref), daemon=True).start()

    database_status = flow()

    if database_status == True:
        print("\nconnected to the database, yay!\n>> ", end='')
        try:
            while not stop_event.is_set():
                try:
                    s.settimeout(1.0)
                    conn, addr = s.accept()
                except socket.timeout:
                    continue
                except OSError:
                    break

                state["connections"].append(conn)
                if semaphore.acquire(blocking=False):
                    print(f"Connection from {addr}")
                    threading.Thread(target=handle_client, args=(conn, addr, state, approval_queue)).start()
                else:
                    conn.sendall(b"Server is full.\n")
                    conn.close()
        except OSError:
            print("Server socket closed. exiting...\n")
    else:
        print("Database unavailable, what's the point of starting if we can't do shit?\n")
        return

def stop_server(state):
    print("Server closing...\n")
    if state["socket"]:
        try: state["socket"].close()
        except: pass
    for conn in state["connections"]:
        try: conn.close()
        except: pass
    state["socket"] = None
    state["connections"].clear()
    print("All connections closed.\n")

# last line