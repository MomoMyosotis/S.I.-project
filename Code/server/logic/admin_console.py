# first line

import queue, threading
import socketserver, socket, typing, sys

# soon with its own GUI!
approval_queue = queue.Queue()
accepted_list = ['y', 'ok', 'k', 'accept', 'yes']
denied_list   = ['n', 'no', 'deny']
menu_list     = ['menu', 'lista', 'm']

_mode_ref: typing.Optional[list] = None
_admin_server = None
_stop_callback = None

def macr(timeout=30):
    """
    Aspetta la decisione dell'admin per una registrazione.
    Ritorna True se approvata, False se rifiutata, None se timeout.
    """
    req = {"event": threading.Event(), "result": None}
    approval_queue.put(req)
    print("Waiting for admin's approval...\n")

    if not req["event"].wait(timeout):
        print("Admin approval timeout reached.")
        req["result"] = None
        req["event"].set()
    return req["result"]

def manual_cmd(state, mode_ref):
    """
    Thread principale per comandi manuali dell'admin.
    (Kept for backward compatibility; it is discouraged: use start_admin_server instead.)
    state: reference al server_state
    mode_ref: lista con un solo elemento che rappresenta la modalità corrente ['auto'/'manual']
    """
    # Simple wrapper to keep compatibility: run a blocking loop reading stdin.
    while True:
        try:
            cmd = input("\n>> ").strip().lower()
            if cmd in ['stop', 'exit', 'quit', 'c']:
                if state: stop_server(state)
                break
            elif cmd in menu_list:
                _print_menu()
                continue
            elif cmd in accepted_list + denied_list:
                _process_approval(cmd)
                continue
            elif cmd == 'switch':
                mode_ref[0] = 'manual' if mode_ref[0] == 'auto' else 'auto'
                print(f"Mode switched to: [{mode_ref[0]}]", flush=True)
                continue
            elif cmd in ['mode', 'status']:
                print(f"Currently on [{mode_ref[0]}] mode.\n", flush=True)
                continue
            else:
                print("Invalid input. Type 'menu' to see options.\n", flush=True)
                continue
        except EOFError:
            print("EOF detected, stopping console thread.", flush=True)
            if state: stop_server(state)
            break
        except Exception as e:
            print(f"Unexpected error: {e}", flush=True)
            if state: stop_server(state)
            break

def _process_approval(cmd):
    try:
        req = approval_queue.get_nowait()
    except queue.Empty:
        print("No pending approval requests.\n", flush=True)
        return
    req["result"] = (cmd in accepted_list)
    req["event"].set()
    print(f"Request {'ACCEPTED' if req['result'] else 'DENIED'}.\n", flush=True)

def _print_menu():
    print("""Currently you can do the following:
==========================
1. stop/exit/quit -> stop the server
2. k/yes/ok -> approve a registration
3. n/no/deny -> reject a registration
4. switch -> change server mode auto/manual
5. menu -> this menu
==========================
""", flush=True)

class _AdminTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        global _mode_ref, _stop_callback
        self.wfile.write(b"Admin console connected. Type 'menu' for options.\n")
        for raw in self.rfile:
            try:
                cmd = raw.decode('utf-8', 'ignore').strip().lower()
            except Exception:
                cmd = ''
            if not cmd:
                continue
            if cmd in ['stop', 'exit', 'quit', 'c']:
                self.wfile.write(b"Stopping server (if stop callback registered).\n")
                if callable(_stop_callback):
                    try:
                        _stop_callback()
                        self.wfile.write(b"Stop callback executed.\n")
                    except Exception as e:
                        self.wfile.write(f"Error running stop callback: {e}\n".encode())
                else:
                    self.wfile.write(b"No stop callback registered.\n")
                break
            elif cmd in menu_list:
                self.wfile.write(b"Available commands: stop, k/yes/ok, n/no/deny, switch, mode, menu\n")
                continue
            elif cmd in accepted_list + denied_list:
                _process_approval(cmd)
                self.wfile.write(f"Processed approval command: {cmd}\n".encode())
                continue
            elif cmd == 'switch':
                if _mode_ref is not None:
                    _mode_ref[0] = 'manual' if _mode_ref[0] == 'auto' else 'auto'
                    self.wfile.write(f"Mode switched to: [{_mode_ref[0]}]\n".encode())
                else:
                    self.wfile.write(b"Mode not configured.\n")
                continue
            elif cmd in ['mode', 'status']:
                if _mode_ref is not None:
                    self.wfile.write(f"Currently on [{_mode_ref[0]}] mode.\n".encode())
                else:
                    self.wfile.write(b"Mode not configured.\n")
                continue
            else:
                self.wfile.write(b"Invalid input. Type 'menu' to see options.\n")
                continue

def start_admin_server(mode_ref: list, host: str = '127.0.0.1', port: int = 60000):
    """
    Start a small TCP admin server on localhost. Returns the server object.
    Connect with: `nc 127.0.0.1 60000` or `telnet 127.0.0.1 60000`.
    """
    global _mode_ref, _admin_server
    _mode_ref = mode_ref
    class ThreadedTCP(socketserver.ThreadingTCPServer):
        allow_reuse_address = True
    try:
        _admin_server = ThreadedTCP((host, port), _AdminTCPHandler)
    except OSError as e:
        raise
    thread = threading.Thread(target=_admin_server.serve_forever, kwargs={'poll_interval': 0.5}, daemon=True)
    thread.start()
    print(f"Admin TCP console listening on {host}:{port}")
    return _admin_server

def register_stop_callback(func):
    """Register a callable that will be invoked when admin issues 'stop'."""
    global _stop_callback
    _stop_callback = func

def stop_server(state):
    print("Server closing...\n", flush=True)
    if not state:
        print("State not initialized, nothing to close.", flush=True)
        return
    if state.get("socket"):
        try: state["socket"].close()
        except: pass
    for conn in state.get("connections", []):
        try: conn.close()
        except: pass
    state["socket"] = None
    state["connections"] = []
    print("All connections closed.\n", flush=True)

# last line