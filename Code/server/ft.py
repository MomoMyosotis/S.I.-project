import time, json, traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from services.redirect import dispatch_command

# ---------------------------
# CONFIG TEST
# ---------------------------
MAX_WORKERS = 5  # numero thread concurrent

# --- Nuove variabili globali ---
all_results = []

# ---------------------------
# UTILITY FUNCTIONS
# ---------------------------
def run_command(command_tuple, user_obj=None):
    command, args = command_tuple
    start = time.perf_counter()
    try:
        response, user_obj, token, status = dispatch_command(command, args, user_obj)
        elapsed = time.perf_counter() - start
        result = {
            "command": command,
            "status": status,
            "time": elapsed,
            "response": response,
            "error": None,
            "user_obj": user_obj,
            "token": token
        }

        # --- EXTRA DEBUG ---
        print(f"[DEBUG][{command}] STATUS={status}, TIME={elapsed:.4f}s")
        print(f"[DEBUG][{command}] ARGS={args}")
        if user_obj:
            print(f"[DEBUG][{command}] USER_OBJ ID={user_obj.get('id')}, FOLLOWERS={user_obj.get('followers_count')}, FOLLOWED={user_obj.get('followed_count')}")
        else:
            print(f"[DEBUG][{command}] USER_OBJ=None")
        print(f"[DEBUG][{command}] RESPONSE={response}\n")

    except Exception as e:
        elapsed = time.perf_counter() - start
        result = {
            "command": command,
            "status": "ERROR",
            "time": elapsed,
            "response": None,
            "error": str(e) + "\n" + traceback.format_exc(),
            "user_obj": user_obj,
            "token": None
        }
        print(f"[ERROR][{command}] {e}")
        print(traceback.format_exc())

    all_results.append(result)
    return result

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
    r = run_command(("create_song", [{"title": "Brano neutro", "year": 2020}]), user_obj=user_obj)
    song_id = json.loads(r["response"]).get("media_id")
    run_command(("get_song", [song_id]), user_obj=user_obj)
    run_command(("delete_song", [song_id]), user_obj=user_obj)

    # CASO 2: Documento digitale collegato a un brano
    r_song = run_command(("create_song", [{"title": "Brano di riferimento"}]), user_obj=user_obj)
    ref_song_id = json.loads(r_song["response"]).get("media_id")

    r_doc = run_command(("create_document", [{"title": "Resistenza", "year": 1958,
                                                "doc_type": "score", "file_format": "pdf",
                                                "references": [ref_song_id], "is_author": True}]), user_obj=user_obj)
    doc_id = json.loads(r_doc["response"]).get("media_id")
    run_command(("get_document", [doc_id]), user_obj=user_obj)
    run_command(("delete_document", [doc_id]), user_obj=user_obj)
    run_command(("delete_song", [ref_song_id]), user_obj=user_obj)

    # CASO 3: File audio
    r_audio = run_command(("create_song", [{"title": "Audio Test", "format": "mp3", "duration": 120,
                                                "performers": [{"name": "Alice", "type": "external"}],
                                                "instruments": ["Piano"],
                                                "recording_date": "2024-01-01",
                                                "recording_place": "Roma"}]), user_obj=user_obj)
    audio_id = json.loads(r_audio["response"]).get("media_id")
    run_command(("get_song", [audio_id]), user_obj=user_obj)
    run_command(("delete_song", [audio_id]), user_obj=user_obj)

    # CASO 4: Video singolo live
    r_video = run_command(("create_video", [{"title": "Video Test", "link": "https://youtu.be/test",
                                                "duration": 300,
                                                "performers": [{"name": "Alice", "type": "external"}],
                                                "instruments": ["Guitar"],
                                                "recording_date": "2024-02-01",
                                                "recording_place": "Milano"}]), user_obj=user_obj)
    video_id = json.loads(r_video["response"]).get("media_id")
    run_command(("get_video", [video_id]), user_obj=user_obj)
    run_command(("delete_video", [video_id]), user_obj=user_obj)

    # CASO 5: Concerto con tracklist
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

    # CASO 6: Brano come autore (utente registrato)
    r_author = run_command(("create_song", [{"title": "Brano Autore",
                                                "authors": [{"id": user_obj["id"], "type": "user"}],
                                                "is_author": True}]), user_obj=user_obj)
    author_song_id = json.loads(r_author["response"]).get("media_id")
    run_command(("get_song", [author_song_id]), user_obj=user_obj)
    run_command(("delete_song", [author_song_id]), user_obj=user_obj)

    # CASO 7: Brano come performer (utente registrato)
    r_performer = run_command(("create_song", [{"title": "Brano Performer",
                                                "performers": [{"id": user_obj["id"], "type": "user"}],
                                                "instruments": ["Violin"], "is_performer": True}]), user_obj=user_obj)
    performer_song_id = json.loads(r_performer["response"]).get("media_id")
    run_command(("get_song", [performer_song_id]), user_obj=user_obj)
    run_command(("delete_song", [performer_song_id]), user_obj=user_obj)

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

def print_summary(results):
    total_time = sum(r["time"] for r in results)
    avg_time = total_time / len(results) if results else 0
    errors = [r for r in results if r["status"] == "ERROR"]
    error_pct = len(errors) / len(results) * 100 if results else 0
    print("\n=== TEST SUMMARY ===")
    print(f"Total commands: {len(results)}")
    print(f"Avg time per command: {avg_time:.4f}s")
    print(f"Errors: {len(errors)} ({error_pct:.2f}%)")
    print(f"Total time: {total_time:.2f}s")
    if errors:
        print("\n--- ERROR LOG ---")
        for e in errors:
            print(f"Command: {e['command']}")
            print(f"Error: {e['error']}\n")

# ---------------------------
# MAIN
# ---------------------------
if __name__ == "__main__":
    token_alice, token_bob, user_alice, user_bob, username1, username2 = test_register_login()
    test_follow_flow(user_alice, username2)
    test_media_crud(user_alice)
    test_not_logged_in()
    concurrency_login_test(8)
    print("\n=== DONE ===")

print_summary(all_results)