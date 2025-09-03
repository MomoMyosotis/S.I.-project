# first line

import socket, threading, json, secrets
from services.config_loader import load_config
from logs.logger import log_event
from services.redirect import dispatch_command
from services.admin_console import manual_cmd, macr

MAX_CONNECTIONS = 73
semaphore = threading.Semaphore(MAX_CONNECTIONS)
stop_event = threading.Event()
server_state = {"socket": None, "connections": []}
sessions = {}  # token -> user_obj
mode_ref = ["auto"]  # contenitore mutabile della modalità server


def generate_token(length: int = 32) -> str:
    return secrets.token_hex(length // 2)


def handle_client(conn, addr):
    """Gestione di ogni singolo client."""
    with conn:
        while not stop_event.is_set():
            try:
                data = conn.recv(65536)
                if not data:
                    break
                try:
                    request = json.loads(data.decode())
                    command = request.get("command")
                    args = request.get("args", [])
                    token = request.get("token")
                except Exception:
                    conn.sendall(json.dumps({
                        "status": "ERROR",
                        "error_msg": "Invalid JSON"
                    }).encode())
                    continue

                user_obj = sessions.get(token)

                # INTERCETTA REGISTER_USER se siamo in modalità manuale
                if command == "register_user" and mode_ref[0] == "manual":
                    approved = macr(timeout=30)
                    if not approved:
                        conn.sendall(json.dumps({
                            "status": "ERROR",
                            "error_msg": "Registration denied by admin"
                        }).encode())
                        continue

                # Dispatcher principale
                response, new_user_obj, new_token = dispatch_command(command, args, user_obj)
                if new_token:
                    sessions[new_token] = new_user_obj

                conn.sendall(json.dumps({
                    "status": "OK",
                    "response": response,
                    "token": new_token
                }).encode())
            except Exception as e:
                log_event(addr[0], "unknown", "ERROR", str(e))
                break


def start_server(state: dict):
    config = load_config()
    host, port = config["HOST"], config["PORT"]

    # Thread per comandi admin (switch, stop, ecc.) UNA SOLA VOLTA
    threading.Thread(target=manual_cmd, args=(state, mode_ref), daemon=True).start()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(15)
    state["socket"] = s
    print(f"Server listening on {host}:{port}")

    while not stop_event.is_set():
        try:
            s.settimeout(1.0)
            conn, addr = s.accept()
        except socket.timeout:
            continue
        except OSError:
            break

        if semaphore.acquire(blocking=False):
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
            state["connections"].append(conn)
        else:
            conn.sendall(json.dumps({
                "status": "ERROR",
                "error_msg": "Server full"
            }).encode())
            conn.close()


def stop_server(state: dict):
    stop_event.set()
    if state["socket"]:
        try:
            state["socket"].close()
        except:
            pass
    for conn in state["connections"]:
        try:
            conn.close()
        except:
            pass
    state["connections"].clear()
    print("Server stopped.")

# last line