import socket
import threading
import time
from typing import Optional, Tuple, List

HOST = "127.0.0.1"
PORT = 8000

# -------------------------------
# Helpers base
# -------------------------------
def send_command(cmd: str, recv_size: int = 65536) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(cmd.encode() + b"\n")
        resp = s.recv(recv_size).decode(errors="replace").strip()
    return resp

def section(title: str):
    print("\n" + "="*20 + f" {title} " + "="*20)

def show(cmd: str, resp: str):
    print(f">> {cmd}")
    print(f"<< {resp}")

def try_cmd(cmd: str, expect: Optional[str] = None) -> str:
    resp = send_command(cmd)
    show(cmd, resp)
    if expect is not None and expect not in resp:
        raise AssertionError(f"Expected '{expect}' in response but got: {resp}")
    return resp

def parse_token(resp: str) -> Optional[str]:
    if resp.startswith("OK|"):
        parts = resp.split("|", 1)
        return parts[1]
    return None

def parse_id(resp: str) -> Optional[str]:
    if resp.startswith("OK|"):
        parts = resp.split("|", 1)
        return parts[1]
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

    resp1 = try_cmd(f"REGISTER|{email1}|{username1}|pass1234|2000-01-01")
    resp2 = try_cmd(f"REGISTER|{email2}|{username2}|pass1234|2000-01-01")

    assert "ERROR" not in resp1, f"Register fallito: {resp1}"
    assert "ERROR" not in resp2, f"Register fallito: {resp2}"

    # Login
    token_alice = parse_token(try_cmd(f"LOGIN|{username1}|pass1234", expect="OK|"))
    token_bob = parse_token(try_cmd(f"LOGIN|{username2}|pass1234", expect="OK|"))
    assert token_alice and token_bob, "Login fallito"

    # Wrong password / not found
    try:
        try_cmd(f"LOGIN|{username1}|wrongpassword", expect="WRONG_PASSWORD")
        try_cmd("LOGIN|nonexistent|pass1234", expect="404")
    except AssertionError as e:
        print("[Expected error] ", e)

    return token_alice, token_bob, username1, username2

def test_follow_flow(token_alice: str, token_bob: str, username_alice: str, username_bob: str):
    section("FOLLOW / FOLLOWERS / FOLLOWED")
    try_cmd(f"{token_alice}|USER_FOLLOW|{username_bob}", expect="FOLLOWED")
    try_cmd(f"{token_alice}|USER_GET_FOLLOWED")
    try_cmd(f"{token_bob}|USER_GET_FOLLOWERS")
    try_cmd(f"{token_alice}|USER_UNFOLLOW|{username_bob}", expect="UNFOLLOWED")
    try_cmd(f"{token_alice}|USER_GET_FOLLOWED")
    try_cmd(f"{token_bob}|USER_GET_FOLLOWERS")

def test_media_crud(token_alice: str):
    section("MEDIA CRUD - SONG")
    r = try_cmd(f"{token_alice}|SONG_CREATE|Imagine|John Lennon|1971", expect="OK|")
    song_id = parse_id(r)
    assert song_id, "Creazione canzone fallita"

    try_cmd(f"{token_alice}|SONG_GET|{song_id}")
    try_cmd(f"{token_alice}|SONG_UPDATE|{song_id}|title|Imagine (Remastered)", expect="OK")
    try_cmd(f"{token_alice}|SONG_DELETE|{song_id}", expect="OK")

    section("MEDIA CRUD - DOCUMENT")
    r = try_cmd(f"{token_alice}|DOC_CREATE|Resistenza|Primo Levi|1958", expect="OK|")
    doc_id = parse_id(r)
    assert doc_id
    try_cmd(f"{token_alice}|DOC_GET|{doc_id}")
    try_cmd(f"{token_alice}|DOC_DELETE|{doc_id}", expect="OK")

    section("MEDIA CRUD - VIDEO")
    r = try_cmd(f"{token_alice}|VIDEO_CREATE|Metropolis|Fritz Lang|1927", expect="OK|")
    vid_id = parse_id(r)
    assert vid_id
    try_cmd(f"{token_alice}|VIDEO_GET|{vid_id}")
    try_cmd(f"{token_alice}|VIDEO_DELETE|{vid_id}", expect="OK")

def test_not_logged_in():
    section("ACCESS WITHOUT LOGIN")
    try:
        try_cmd("USER_GET_FOLLOWERS", expect="ERROR: NOT_LOGGED_IN")
        try_cmd("SONG_CREATE|x|y|z", expect="ERROR: NOT_LOGGED_IN")
    except AssertionError as e:
        print("[Expected error] ", e)

def concurrency_login_test(users: int = 5):
    section(f"CONCURRENCY - {users} parallel logins")
    tokens: List[str] = []
    lock = threading.Lock()

    def worker(i: int):
        email, uname = unique_user(f"user{i}")
        try_cmd(f"REGISTER|{email}|{uname}|pass1234|2000-01-01")
        resp = try_cmd(f"LOGIN|{uname}|pass1234", expect="OK|")
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
