# first line

import queue, threading

# soon with its own GUI!
approval_queue = queue.Queue()
accepted_list = ['y', 'ok', 'k', 'accept', 'yes']
denied_list   = ['n', 'no', 'deny']
menu_list     = ['menu', 'lista', 'm']

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
    state: reference al server_state
    mode_ref: lista con un solo elemento che rappresenta la modalità corrente ['auto'/'manual']
    """
    while True:
        try:
            cmd = input("\n>> ").strip().lower()
            if cmd in ['stop', 'exit', 'quit', 'c']:
                if state: stop_server(state)
                break
            elif cmd in menu_list:
                _print_menu()
                return
            elif cmd in accepted_list + denied_list:
                _process_approval(cmd)
                return
            elif cmd == 'switch':
                mode_ref[0] = 'manual' if mode_ref[0] == 'auto' else 'auto'
                print(f"Mode switched to: [{mode_ref[0]}]", flush=True)
                return
            elif cmd in ['mode', 'status']:
                print(f"Currently on [{mode_ref[0]}] mode.\n", flush=True)
                return
            else:
                print("Invalid input. Type 'menu' to see options.\n", flush=True)
                return
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