import time, json, traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from services.redirect import dispatch_command

# ---------------------------
# CONFIG TEST
# ---------------------------
MAX_WORKERS = 5  # numero thread concurrent
all_results = []

EXPECTED_ERRORS = [
    "User is not logged in",
    "Username already exists",
    "Invalid credentials",
    "Access denied",                     # es. se un utente prova ad accedere a risorse non sue
    "Media not found",                   # get_song/get_video/delete su ID inesistente
    "Document not found",
    "Video not found",
    "Song not found",
    "Already following",                 # follow_user duplicato
    "Not following",                     # unfollow_user quando non segui
    "Invalid token",                     # login/sessione scaduta
    "Missing required field",            # es. title mancante in create_song
    "Unsupported format",                # formati file non validi
]

def is_expected_error(error_msg: str) -> bool:
    """Controlla se un messaggio d'errore è tra quelli previsti (expected)."""
    if not error_msg:
        return False
    return any(exp in error_msg for exp in EXPECTED_ERRORS)

# ---------------------------
# UTILITY FUNCTIONS
# ---------------------------
def run_command(command_tuple, user_obj=None):
    """
    Esegue un singolo comando tramite dispatch_command e salva il risultato.
    """
    command, args = command_tuple
    start = time.perf_counter()
    try:
        response, user_obj, token, status = dispatch_command(command, args, user_obj)
        elapsed = time.perf_counter() - start

        # Se il backend ha già dato errore, estrailo
        error_info = None
        if status == "ERROR":
            try:
                parsed = json.loads(response) if response else {}
                error_info = parsed.get("error") or parsed.get("message") or str(response)
            except Exception:
                error_info = str(response)

        result = {
            "command": command,
            "args": args,
            "status": status,
            "time": elapsed,
            "response": response,
            "error": error_info,
            "user_obj": user_obj,
            "token": token,
            "expected": is_expected_error(str(error_info))
        }

        # Log compatto live
        tag = "EXPECTED" if result["expected"] else "ERROR" if status == "ERROR" else "OK"
        print(f"[DEBUG][{command}] STATUS={status}, TIME={elapsed:.4f}s, TAG={tag}, ERROR={error_info}")

    except Exception as e:
        elapsed = time.perf_counter() - start
        result = {
            "command": command,
            "args": args,
            "status": "ERROR",
            "time": elapsed,
            "response": None,
            "error": f"{e}\n{traceback.format_exc()}",
            "user_obj": user_obj,
            "token": None,
            "expected": False
        }
        print(f"[EXCEPTION][{command}] {e}")
        print(traceback.format_exc())

    all_results.append(result)
    return result


def print_summary(results):
    """
    Stampa il riepilogo dei test eseguiti, separando errori attesi da errori reali.
    """
    total_time = sum(r["time"] for r in results)
    avg_time = total_time / len(results) if results else 0

    real_errors = [r for r in results if r["status"] == "ERROR" and not r.get("expected")]
    expected_errors = [r for r in results if r["status"] == "ERROR" and r.get("expected")]

    error_pct = len(real_errors) / len(results) * 100 if results else 0

    print("\n=== TEST SUMMARY ===")
    print(f"Total commands: {len(results)}")
    print(f"Avg time per command: {avg_time:.4f}s")
    print(f"Expected errors: {len(expected_errors)} (ok)")
    print(f"Real errors: {len(real_errors)} ({error_pct:.2f}%)")
    print(f"Total time: {total_time:.2f}s")

    if real_errors:
        print("\n--- REAL ERROR LOG ---")
        for e in real_errors:
            print(f"\nCommand: {e['command']}")
            print(f"Args: {e['args']}")
            print(f"Error: {e['error']}")
            print(f"Response: {e['response']}\n")

def unique_user(base_name: str):
    ts = int(time.time() * 1000) % 10000
    uname = f"{base_name[:15]}{ts}"
    email = f"{uname}@example.com"
    return email, uname

# ---------------------------
# SCENARI DI TEST
# ---------------------------
def test_register_login():
    print("\n=== REGISTER / LOGIN ===")
    email1, username1 = unique_user("quackerina")
    email2, username2 = unique_user("bassettina")

    r1 = run_command(("register_user", [email1, username1, "pass1234", "2000-01-01"]))
    r2 = run_command(("register_user", [email2, username2, "pass1234", "2000-01-01"]))

    r1 = run_command(("login_user", [username1, "pass1234"]))
    r2 = run_command(("login_user", [username2, "pass1234"]))

    token_alice = r1["token"]
    token_bob = r2["token"]
    user_alice = r1["user_obj"]
    user_bob = r2["user_obj"]

    return token_alice, token_bob, user_alice, user_bob, username1, username2

def test_follow_flow(user_alice, username_bob):
    print("\n=== FOLLOW / FOLLOWERS / FOLLOWED ===")
    
    print("[TEST] Follow user")
    r = run_command(("follow_user", [username_bob]), user_obj=user_alice)
    print(f"[RESULT] After follow, user_obj: {r['user_obj']}\n")

    print("[TEST] Get followed")
    r = run_command(("get_followed", []), user_obj=user_alice)
    print(f"[RESULT] Followed list: {r['response']}\n")

    print("[TEST] Get followers (as None user)")
    r = run_command(("get_followers", []), user_obj=None)
    print(f"[RESULT] Followers list: {r['response']}\n")

    print("[TEST] Unfollow user")
    r = run_command(("unfollow_user", [username_bob]), user_obj=user_alice)
    print(f"[RESULT] After unfollow, user_obj: {r['user_obj']}\n")

def test_media_crud(user_obj):
    print("\n=== MEDIA CRUD ===")

    # CASO 1: Brano neutro (senza autore/performer)
    print("\nMEDIA CASE_1\n")
    r = run_command(("create_song", [{"title": "Brano neutro", "year": 2020}]), user_obj=user_obj)
    song_id = json.loads(r["response"]).get("media_id")
    run_command(("get_song", [song_id]), user_obj=user_obj)
    run_command(("delete_song", [song_id]), user_obj=user_obj)
    print("\n\n_________________________________________________________________\n\n")

    # CASO 2: Documento digitale collegato a un brano
    print("\nMEDIA CASE_2\n")
    r_song = run_command(("create_song", [{"title": "Brano di riferimento"}]), user_obj=user_obj)
    ref_song_id = json.loads(r_song["response"]).get("media_id")

    r_doc = run_command(("create_document", [{"title": "Resistenza", "year": 1958,
                                                "doc_type": "score", "file_format": "pdf",
                                                "references": [ref_song_id], "is_author": True}]), user_obj=user_obj)
    doc_id = json.loads(r_doc["response"]).get("media_id")
    run_command(("get_document", [doc_id]), user_obj=user_obj)
    run_command(("delete_document", [doc_id]), user_obj=user_obj)
    run_command(("delete_song", [ref_song_id]), user_obj=user_obj)
    print("\n\n_________________________________________________________________\n\n")


    # CASO 3: File audio
    print("\nMEDIA CASE_3\n")
    r_audio = run_command(("create_song", [{"title": "Audio Test", "format": "mp3", "duration": 120,
                                                "performers": [{"name": "Alice", "type": "external"}],
                                                "instruments": ["Piano"],
                                                "recording_date": "2024-01-01",
                                                "recording_place": "Roma"}]), user_obj=user_obj)
    audio_id = json.loads(r_audio["response"]).get("media_id")
    run_command(("get_song", [audio_id]), user_obj=user_obj)
    run_command(("delete_song", [audio_id]), user_obj=user_obj)
    print("\n\n_________________________________________________________________\n\n")


    # CASO 4: Video singolo live
    print("\nMEDIA CASE_4\n")
    r_video = run_command(("create_video", [{"title": "Video Test", "link": "https://youtu.be/test",
                                                "duration": 300,
                                                "performers": [{"name": "Alice", "type": "external"}],
                                                "instruments": ["Guitar"],
                                                "recording_date": "2024-02-01",
                                                "recording_place": "Milano"}]), user_obj=user_obj)
    video_id = json.loads(r_video["response"]).get("media_id")
    run_command(("get_video", [video_id]), user_obj=user_obj)
    run_command(("delete_video", [video_id]), user_obj=user_obj)
    print("\n\n_________________________________________________________________\n\n")


    # CASO 5: Concerto con tracklist
    print("\nMEDIA CASE_5\n")
    tracklist = [
        {"song_title": "Song1", "start_time": 0, "end_time": 200,
        "performers": [{"name": "Alice", "type": "external"}], "instruments": ["Guitar"]},
        {"song_title": "Song2", "start_time": 200, "end_time": 400,
        "performers": [{"name": "Alice", "type": "external"}], "instruments": ["Piano"]}
    ]
    r_concert = run_command(("create_video", [{"title": "Concerto Test", "link": "https://youtu.be/concert",
                                                "duration": 400, "recording_date": "2024-01-01",
                                                "recording_place": "Milano", "tracklist": tracklist,
                                                "is_performer": True}]), user_obj=user_obj)
    concert_id = json.loads(r_concert["response"]).get("media_id")
    run_command(("get_video", [concert_id]), user_obj=user_obj)
    run_command(("delete_video", [concert_id]), user_obj=user_obj)
    print("\n\n_________________________________________________________________\n\n")


    # CASO 6: Brano come autore (utente registrato)
    print("\nMEDIA CASE_6\n")
    r_author = run_command(("create_song", [{"title": "Brano Autore",
                                                "authors": [{"id": user_obj["id"], "type": "user"}],
                                                "is_author": True}]), user_obj=user_obj)
    author_song_id = json.loads(r_author["response"]).get("media_id")
    run_command(("get_song", [author_song_id]), user_obj=user_obj)
    run_command(("delete_song", [author_song_id]), user_obj=user_obj)
    print("\n\n_________________________________________________________________\n\n")


    # CASO 7: Brano come performer (utente registrato)
    print("\nMEDIA CASE_7\n")
    r_performer = run_command(("create_song", [{"title": "Brano Performer",
                                                "performers": [{"id": user_obj["id"], "type": "user"}],
                                                "instruments": ["Violin"], "is_performer": True}]), user_obj=user_obj)
    performer_song_id = json.loads(r_performer["response"]).get("media_id")
    run_command(("get_song", [performer_song_id]), user_obj=user_obj)
    run_command(("delete_song", [performer_song_id]), user_obj=user_obj)
    print("\n\n_________________________________________________________________\n\n")


def test_not_logged_in():
    print("\n=== ACCESS WITHOUT LOGIN ===")
    run_command(("get_followers", []), user_obj=None)
    run_command(("create_song", [{"title": "X", "year": 0}]), user_obj=None)

def concurrency_login_test(users: int = 5):
    print(f"\n=== CONCURRENCY LOGIN ({users} parallel) ===")
    tokens = []
    user_objs = []

    def worker(i):
        email, uname = unique_user(f"user{i}")
        run_command(("register_user", [email, uname, "pass1234", "2000-01-01"]))
        r2 = run_command(("login_user", [uname, "pass1234"]))
        if r2["token"]:
            tokens.append(r2["token"])
            user_objs.append(r2["user_obj"])

    with ThreadPoolExecutor(max_workers=users) as executor:
        futures = [executor.submit(worker, i) for i in range(users)]
        for f in as_completed(futures):
            pass

    print(f"Got {len(tokens)} tokens out of {users}")

# ---------------------------
# MAIN
# ---------------------------
if __name__ == "__main__":
    # 1. Test base: registrazione e login
    token_alice, token_bob, user_alice, user_bob, username1, username2 = test_register_login()

    # 2. Follow / followers / unfollow
    test_follow_flow(user_alice, username2)

    # 3. CRUD multimediale (su Alice)
    test_media_crud(user_alice)

    # 4. Accesso senza login
    test_not_logged_in()

    # 5. Concurrency login
    concurrency_login_test(5)

    # Riepilogo finale
    print_summary(all_results)
