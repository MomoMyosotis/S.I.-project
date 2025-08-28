# first line

import queue, threading
from services.logger import log_event

# soon with it's own GUI!

approval_queue = queue.Queue()
accepted_list = ['y', 'ok', 'k', 'accept', 'yes']
denied_list   = ['n', 'no', 'deny']
menu_list     = ['menu', 'lista', 'm']

def macr(timeout=30):
    req = {"event": threading.Event(), "result": None}
    approval_queue.put(req)
    print("waiting for admin's approval... \n")

    if not req["event"].wait(timeout):
        print("Admin approval timeout reached.")
        req["result"] = None
        req["event"].set()
    return req["result"]

def manual_cmd(state, mode_ref):
    while True:
        try:
            cmd = input(">> ").strip().lower()
        except EOFError:
            stop_server(state)
            break

        if cmd == 'stop' or cmd == 'c':
            stop_server(state)
            break
        elif cmd in menu_list:
            _print_menu()
        elif cmd in accepted_list or cmd in denied_list:
            _process_approval(cmd)
        elif cmd == 'switch':
            mode_ref[0] = 'manual' if mode_ref[0] == 'auto' else 'auto'
            print(f"mode switched to: [{mode_ref[0]}]", flush=True)
        elif cmd == 'mode' or cmd == 'status':
            print(f"Currently on [{mode_ref[0]}] mode.\n", flush=True)
        else:
            print("Invalid input.\n", flush=True)

def _process_approval(cmd):
    try:
        req = approval_queue.get_nowait()
    except queue.Empty:
        print("No pending approval requests.\n", flush=True)
        return
    req["result"] = (cmd in accepted_list)
    req["event"].set()
    print(f"Richiesta {'ACCETTATA' if req['result'] else 'RIFIUTATA'}.")

def _print_menu():
    print("""Currently you can do the following:
==========================
1. stop -> stop the server.
2. k -> accept a connection request.
3. no -> deny a connection request.
4. switch -> change server mode auto-manual.
5. menu -> this menu.
==========================.
""", flush=True)

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