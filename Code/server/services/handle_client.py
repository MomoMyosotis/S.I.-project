# first line

import uuid
from datetime import datetime
from objects.users.user import User, UserLevel
from db.handle_obj_low import fetch_user_by_key
from services import redirect  # <- dispatcher centrale
from services.logger import log_event

sessions = {}  # token -> User
mode = None    # auto | manual
mode_ref = {"mode": mode}

def handle_client(conn, addr, config, approval_queue):
    ip = addr[0]
    try:
        data = conn.recv(2048).decode().strip()
        if not data:
            conn.sendall(b"ERROR: Empty request\n")
            return

        parts = data.split("|")
        print(f"[DEBUG] Ricevuto da {ip}: {parts}")

        token = None
        user_obj = None
        if parts[0] in sessions:
            token = parts.pop(0)
            user_obj = sessions[token]

        command = parts[0].upper()
        args = parts[1:]

        # --- dispatch command ---
        global mode

        response, new_user_obj, new_token = redirect.dispatch_command(
            command=command,
            args=args,
            conn=conn,
            ip=ip,
            user_obj=user_obj,
            config=config,
            sessions=sessions,
            mode_ref=mode_ref,            # non serve
            approval_queue=approval_queue
        )


        if new_user_obj and new_token:
            sessions[new_token] = new_user_obj
            mode = mode_ref["mode"]

        if response:
            conn.sendall(response.encode())

    except Exception as e:
        print(f"[ERROR handle_client] {ip} : {e}")
        try:
            conn.sendall(b"ERROR: Internal server error\n")
        except:
            pass
    finally:
        conn.close()


# === helper per costruire User (rimane qui se serve ancora) ===

def build_user(user_data: dict) -> User:
    if not user_data:
        return None
    bday_value = user_data.get("birthday")
    birthday = datetime.strptime(bday_value, "%Y-%m-%d").date() if isinstance(bday_value, str) else bday_value
    return User(
        id=user_data.get("id"),
        mail=user_data.get("mail"),
        username=user_data.get("username"),
        password_hash=user_data.get("password"),
        birthday=birthday,
        bio=user_data.get("bio"),
        profile_pic=user_data.get("foto_profilo"),
        lvl=UserLevel(user_data.get("lvl"))
    )

# last line