import time, json, traceback, random
from concurrent.futures import ThreadPoolExecutor, as_completed
from server.services.redirect import dispatch_command

MAX_USERS = 10
THREADS_PER_USER = 20
LOOPS_PER_THREAD = 3

all_results = []

EXPECTED_ERRORS = [
    "User is not logged in",
    "Username already exists",
    "Invalid credentials",
    "Access denied",
    "Media not found",
    "Document not found",
    "Video not found",
    "Song not found",
    "Already following",
    "Not following",
    "Invalid token",
    "Missing required field",
    "Unsupported format",
]

def is_expected_error(error_msg):
    if not error_msg:
        return False
    return any(exp in error_msg for exp in EXPECTED_ERRORS)

def run_command(command_tuple, user_obj=None):
    command, args = command_tuple
    start = time.perf_counter()
    try:
        response, user_obj, token, status = dispatch_command(command, args, user_obj)
        elapsed = time.perf_counter() - start
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
        tag = "EXPECTED" if result["expected"] else "ERROR" if status=="ERROR" else "OK"
        print(f"[DEBUG][{command}] STATUS={status}, TIME={elapsed:.4f}s, TAG={tag}")
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
    all_results.append(result)
    return result

def unique_user(base_name):
    ts = int(time.time() * 1000) % 100000
    uname = f"{base_name[:10]}{ts}"
    email = f"{uname}@example.com"
    return email, uname

def chaos_worker(user_obj):
    """
    Crea/legge/aggiorna/cancella media, commenti e note in loop, per stress test.
    """
    for _ in range(LOOPS_PER_THREAD):
        try:
            # Media random
            media_type = random.choice(["song", "video", "document"])
            title = f"Media_{random.randint(1000,9999)}"
            args = [{"title": title, "year": random.randint(2000,2025)}]
            cmd_create = f"create_{media_type}"
            r_create = run_command((cmd_create, args), user_obj=user_obj)
            media_id = None
            try:
                media_id = json.loads(r_create["response"]).get("media_id")
            except Exception:
                media_id = None

            if not media_id:
                continue

            # Commenti e note random
            for _ in range(2):
                r_comment = run_command(("create_comment", [media_id, f"Commento {random.randint(0,999)}"]), user_obj=user_obj)
                comment_id = None
                try:
                    comment_id = json.loads(r_comment["response"]).get("id")
                except Exception:
                    comment_id = None
                if comment_id:
                    run_command(("update_comment", [comment_id, f"Aggiornato {random.randint(0,999)}"]), user_obj=user_obj)
                    run_command(("delete_comment", [comment_id]), user_obj=user_obj)

            r_note = run_command(("create_note", [media_id, "regular", random.random()*10, random.random()*10, None, None, None, None, f"Nota {random.randint(0,999)}"]), user_obj=user_obj)
            note_id = None
            try:
                note_id = json.loads(r_note["response"]).get("id")
            except Exception:
                note_id = None
            if note_id:
                run_command(("update_note", [note_id, f"Nota aggiornata {random.randint(0,999)}"]), user_obj=user_obj)
                run_command(("delete_note", [note_id]), user_obj=user_obj)

            # Leggi e poi cancella media
            run_command((f"get_{media_type}", [media_id]), user_obj=user_obj)
            run_command((f"delete_{media_type}", [media_id]), user_obj=user_obj)

        except Exception as e:
            print(f"[WORKER EXCEPTION] {e}")

if __name__ == "__main__":
    print("=== STARTING CHAOS STRESS TEST ===")

    # Registrazione/login multipla
    users = []
    tokens = []
    for i in range(MAX_USERS):
        email, uname = unique_user(f"user{i}")
        run_command(("register", [email, uname, "pass1234", "2000-01-01"]))
        r_login = run_command(("login", [uname, "pass1234"]))
        if r_login["token"]:
            tokens.append(r_login["token"])
            users.append(r_login["user_obj"])

    # ThreadPool per caos multi-utente
    with ThreadPoolExecutor(max_workers=MAX_USERS*THREADS_PER_USER) as executor:
        futures = []
        for user in users:
            for _ in range(THREADS_PER_USER):
                futures.append(executor.submit(chaos_worker, user))
        for f in as_completed(futures):
            pass

    # Riepilogo finale
    total_time = sum(r["time"] for r in all_results)
    avg_time = total_time / len(all_results) if all_results else 0
    real_errors = [r for r in all_results if r["status"]=="ERROR" and not r.get("expected")]
    expected_errors = [r for r in all_results if r["status"]=="ERROR" and r.get("expected")]
    print("\n=== CHAOS TEST SUMMARY ===")
    print(f"Total commands: {len(all_results)}")
    print(f"Avg time per command: {avg_time:.4f}s")
    print(f"Expected errors: {len(expected_errors)}")
    print(f"Real errors: {len(real_errors)}")
    print(f"Total time: {total_time:.2f}s")
    # =========================
    # DIAGNOSTICA ERRORI
    # =========================
    if real_errors:
        print("\n--- REAL ERROR LOG (DETAILED) ---")
        for e in real_errors:
            print(f"\nCommand: {e['command']}")
            print(f"Args: {e['args']}")
            print(f"Error: {e['error']}")
            print(f"Response: {e['response']}")

        # Riassunto per tipo di errore
        from collections import Counter
        error_types = [str(e['error']).splitlines()[0] if e['error'] else "Unknown" for e in real_errors]
        counter = Counter(error_types)
        print("\n--- REAL ERROR TYPES SUMMARY ---")
        for err, count in counter.most_common():
            print(f"{count}x {err}")
    else:
        print("\nNo real errors detected!")

# last line