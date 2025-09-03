# first line

import socket
import threading
import time
import json
from typing import Optional, Tuple, List

HOST = "127.0.0.1"
PORT = 8000

# -------------------------------
# Helpers base
# -------------------------------
def send_command(cmd_dict: dict, recv_size: int = 65536) -> str:
    """Invia un dizionario come JSON al server e riceve la risposta."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        payload = json.dumps(cmd_dict).encode() + b"\n"
        s.sendall(payload)
        resp = s.recv(recv_size).decode(errors="replace").strip()
    return resp

def section(title: str):
    print("\n" + "="*20 + f" {title} " + "="*20)

def show(cmd_dict: dict, resp: str):
    print(f">> {json.dumps(cmd_dict)}")
    print(f"<< {resp}")

def try_cmd_json(cmd_dict: dict, expect: Optional[str] = None) -> str:
    resp = send_command(cmd_dict)
    show(cmd_dict, resp)
    if expect is not None and expect not in resp:
        raise AssertionError(f"Expected '{expect}' in response but got: {resp}")
    return resp

def parse_token(resp: str) -> Optional[str]:
    """Estrae il token da una risposta di login/register"""
    try:
        data = json.loads(resp)
        return data.get("token")
    except:
        return None

def parse_id(resp: str) -> Optional[str]:
    """Estrae l'ID da una risposta di creazione media"""
    try:
        data = json.loads(resp)
        if "response" in data and isinstance(data["response"], dict):
            return data["response"].get("id")
    except:
        pass
    return None

def unique_user(base_name: str) -> Tuple[str, str]:
    ts = int(time.time() * 1000) % 10000  # ultime 4 cifre dei millisecondi
    uname = f"{base_name[:15]}{ts}"       # max 15 caratteri + 4 = 19
    email = f"{uname}@example.com"
    return email, uname

# -------------------------------
# Test scenari
# -------------------------------
def test_register_login() -> Tuple[str, str, str, str]:
    section("REGISTER / LOGIN - Happy path")
    email1, username1 = unique_user("quackerina")
    email2, username2 = unique_user("bassettina")

    # Registrazione
    resp1 = try_cmd_json({
        "command": "register_user",
        "args": [email1, username1, "pass1234", "2000-01-01"]
    })
    resp2 = try_cmd_json({
        "command": "register_user",
        "args": [email2, username2, "pass1234", "2000-01-01"]
    })

    token_alice = parse_token(resp1)
    token_bob = parse_token(resp2)
    assert token_alice and token_bob, "Register fallito"

    # Login
    resp1 = try_cmd_json({
        "command": "login_user",
        "args": [username1, "pass1234"]
    })
    resp2 = try_cmd_json({
        "command": "login_user",
        "args": [username2, "pass1234"]
    })
    token_alice = parse_token(resp1)
    token_bob = parse_token(resp2)
    assert token_alice and token_bob, "Login fallito"

    # Wrong password / not found
    try:
        try_cmd_json({"command": "login_user", "args": [username1, "wrongpassword"]}, expect="WRONG_PASSWORD")
        try_cmd_json({"command": "login_user", "args": ["nonexistent", "pass1234"]}, expect="404")
    except AssertionError as e:
        print("[Expected error] ", e)

    return token_alice, token_bob, username1, username2

def test_follow_flow(token_alice: str, token_bob: str, username_alice: str, username_bob: str):
    section("FOLLOW / FOLLOWERS / FOLLOWED")
    try_cmd_json({"command": "follow_user", "args": [username_bob], "token": token_alice}, expect="FOLLOWED")
    try_cmd_json({"command": "get_followed", "args": [], "token": token_alice})
    try_cmd_json({"command": "get_followers", "args": [], "token": token_bob})
    try_cmd_json({"command": "unfollow_user", "args": [username_bob], "token": token_alice}, expect="UNFOLLOWED")
    try_cmd_json({"command": "get_followed", "args": [], "token": token_alice})
    try_cmd_json({"command": "get_followers", "args": [], "token": token_bob})

def test_media_crud(token_alice: str):
    section("MEDIA CRUD - SONG")
    r = try_cmd_json({"command": "create_song", "args": ["Imagine", "John Lennon", 1971], "token": token_alice}, expect="OK")
    song_id = parse_id(r)
    assert song_id, "Creazione canzone fallita"
    try_cmd_json({"command": "get_song", "args": [song_id], "token": token_alice})
    try_cmd_json({"command": "update_song", "args": [song_id, "title", "Imagine (Remastered)"], "token": token_alice}, expect="OK")
    try_cmd_json({"command": "delete_song", "args": [song_id], "token": token_alice}, expect="OK")

    section("MEDIA CRUD - DOCUMENT")
    r = try_cmd_json({"command": "create_document", "args": ["Resistenza", "Primo Levi", 1958], "token": token_alice}, expect="OK")
    doc_id = parse_id(r)
    assert doc_id
    try_cmd_json({"command": "get_document", "args": [doc_id], "token": token_alice})
    try_cmd_json({"command": "delete_document", "args": [doc_id], "token": token_alice}, expect="OK")

    section("MEDIA CRUD - VIDEO")
    r = try_cmd_json({"command": "create_video", "args": ["Metropolis", "Fritz Lang", 1927], "token": token_alice}, expect="OK")
    vid_id = parse_id(r)
    assert vid_id
    try_cmd_json({"command": "get_video", "args": [vid_id], "token": token_alice})
    try_cmd_json({"command": "delete_video", "args": [vid_id], "token": token_alice}, expect="OK")

def test_not_logged_in():
    section("ACCESS WITHOUT LOGIN")
    try:
        try_cmd_json({"command": "get_followers", "args": []}, expect="ERROR: NOT_LOGGED_IN")
        try_cmd_json({"command": "create_song", "args": ["x","y",0]}, expect="ERROR: NOT_LOGGED_IN")
    except AssertionError as e:
        print("[Expected error] ", e)

def concurrency_login_test(users: int = 5):
    section(f"CONCURRENCY - {users} parallel logins")
    tokens: List[str] = []
    lock = threading.Lock()

    def worker(i: int):
        email, uname = unique_user(f"user{i}")
        try_cmd_json({"command": "register_user", "args": [email, uname, "pass1234", "2000-01-01"]})
        resp = try_cmd_json({"command": "login_user", "args": [uname, "pass1234"]}, expect="OK")
        t = parse_token(resp)
        if t:
            with lock:
                tokens.append(t)

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(users)]
    for th in threads: th.start()
    for th in threads: th.join()

    print(f"Got {len(tokens)} tokens.")
    assert len(tokens) == users, "Non tutti i login hanno prodotto token"

# -------------------------------
# MAIN
# -------------------------------
if __name__ == '__main__':
    section("SERVER MEGA TESTER")
    token_alice, token_bob, username_alice, username_bob = test_register_login()
    test_follow_flow(token_alice, token_bob, username_alice, username_bob)
    test_media_crud(token_alice)
    test_not_logged_in()
    concurrency_login_test(8)
    section("DONE")


# last line