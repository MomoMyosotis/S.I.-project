# first line
from typing import Dict, Any, List, Optional
from . import connection
from services.logger import log_event
import hashlib
from datetime import datetime

# ===================================
# DEBUG / LOG UTILITY
# ===================================
def debug(msg: str):
    print(f"[DEBUG] {msg}")

# ===================================
# GENERIC DB CRUD
# ===================================
def fetch_one(query: str, params: tuple = ()) -> Optional[Dict[str, Any]]:
    conn = connection.connect()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            row = cur.fetchone()
            if row:
                debug(f"fetch_one success: {row}")
                return dict(zip([desc[0] for desc in cur.description], row))
    except Exception as e:
        print(f"[DB ERROR fetch_one] {e}")
    finally:
        connection.close(None, conn)
    return None

def fetch_all(query: str, params: tuple = ()) -> List[Dict[str, Any]]:
    conn = connection.connect()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            rows = cur.fetchall()
            cols = [desc[0] for desc in cur.description]
            debug(f"fetch_all returned {len(rows)} rows")
            return [dict(zip(cols, r)) for r in rows]
    except Exception as e:
        print(f"[DB ERROR fetch_all] {e}")
        return []
    finally:
        connection.close(None, conn)

def execute(query: str, params: tuple = ()) -> bool:
    conn = connection.connect()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            conn.commit()
            debug(f"execute success: {query} {params}")
            return True
    except Exception as e:
        print(f"[DB ERROR execute] {e}")
        conn.rollback()
        return False
    finally:
        connection.close(None, conn)

# ===================================
# PASSWORD UTILS
# ===================================
def hash_pswd(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(plain: str, hashed: str) -> bool:
    return hash_pswd(plain) == hashed

# ===================================
# VALIDATION
# ===================================
def validity(user_data: List[str]) -> bool:
    today = datetime.today()
    dob = datetime.strptime(user_data[4], "%Y-%m-%d")
    if not user_data[0].strip(): return "Username"
    if len(user_data[1]) < 6: return "Pswd"
    if "@" not in user_data[2]: return "Mail"
    if (today - dob).days < 14 * 365.25: return "Age"
    if user_data[6]:
        try:
            lvl = int(user_data[6])
            if lvl not in range(5): return "Lvl"
        except ValueError:
            return "Lvl"
    return True

# ===================================
# USERS CRUD + LOGIN / REGISTER
# ===================================
def fetch_user_by_key(key: str, value: Any) -> Optional[Dict[str, Any]]:
    if key not in ("mail", "username", "id"):
        raise ValueError("Invalid key")
    return fetch_one(f"SELECT * FROM users WHERE {key}=%s", (value,))

def insert_user(username, password, mail, profile_pic, birthday, bio, lvl) -> bool:
    if fetch_user_by_key("username", username) or fetch_user_by_key("mail", mail):
        print("[WARN] Username or mail already exists")
        return False
    return execute(
        "INSERT INTO users(username,password,mail,foto_profilo,birthday,bio,lvl) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (username, hash_pswd(password), mail, profile_pic, birthday, bio, lvl)
    )

def update_user_profile(user_id, **kwargs) -> bool:
    if not kwargs: return False
    fields = ", ".join(f"{k}=%s" for k in kwargs.keys())
    values = tuple(kwargs.values()) + (user_id,)
    return execute(f"UPDATE users SET {fields} WHERE id=%s", values)

def delete_user(user_id: int) -> bool:
    return execute("DELETE FROM users WHERE id=%s", (user_id,))

def login_user(identifier, password, blacklist):
    user = fetch_user_by_key('mail' if "@" in identifier else 'username', identifier)
    if not user: return {"status": "not_found", "user": None}
    uname, mail = (str(user.get("username") or "").lower(), str(user.get("mail") or "").lower())
    bl = {str(x).lower() for x in (blacklist or [])}
    if uname in bl or mail in bl: return {"status": "blacklisted", "user": None}
    if not verify_password(password, user.get("password")): return {"status": "wrong_password", "user": None}
    return {"status": "accepted", "user": user}

def redirect(user_input: List[str], blacklist: List[str], mode: int):
    if mode == 1: return login_user(user_input[0], user_input[1], blacklist)
    elif mode == 2:
        valid = validity(user_input)
        if valid is True:
            return True if insert_user(*user_input) else "Conflict"
        return valid

# ===================================
# FOLLOW / UNFOLLOW
# ===================================
def add_follow(follower_id, followed_id):
    return execute("INSERT INTO Follows(follower_id,followed_id) VALUES (%s,%s) ON CONFLICT DO NOTHING", (follower_id, followed_id))

def remove_follow(follower_id, followed_id):
    return execute("DELETE FROM Follows WHERE follower_id=%s AND followed_id=%s", (follower_id, followed_id))

def get_followers(user_id):
    return [r["follower_id"] for r in fetch_all("SELECT follower_id FROM Follows WHERE followed_id=%s", (user_id,))]

def get_followed(user_id):
    return [r["followed_id"] for r in fetch_all("SELECT followed_id FROM Follows WHERE follower_id=%s", (user_id,))]

###########################################################
###########################################################
###########################################################

# ===================================
# GENERIC MEDIA HANDLER
# ===================================

# configurazione tabella figlia per tipo media
MEDIA_CHILD_TABLES = {
    "song": {"table": "songs", "fields": ["duration", "location", "additional_info"]},
    "document": {"table": "documents", "fields": ["format", "pages", "caption", "song_id"]},
    "video": {"table": "videos", "fields": ["duration", "location", "additional_info", "director"]}
}

def create_media(obj: Any, media_type: str) -> Optional[int]:
    """
    Crea un media generico + record nella tabella figlia.
    obj può essere dict o istanza di Media.
    Ritorna l'id creato o None se fallisce.
    """
    cfg = MEDIA_CHILD_TABLES.get(media_type)
    if not cfg:
        debug(f"create_media: tipo sconosciuto {media_type}")
        return None

    child_table, child_fields = cfg["table"], cfg["fields"]
    data = obj if isinstance(obj, dict) else obj.__dict__

    try:
        conn = connection.connect()
        with conn.cursor() as cur:
            debug(f"create_media: inserimento in media {data}")
            cur.execute(
                "INSERT INTO media (type, title, author, year, description, link) "
                "VALUES (%s,%s,%s,%s,%s,%s) RETURNING id",
                (
                    media_type,
                    data.get('title'),
                    data.get('author') or data.get('performer'),
                    data.get('year'),
                    data.get('description'),
                    data.get('link')
                )
            )
            media_id = cur.fetchone()[0]
            debug(f"create_media: media_id creato = {media_id}")

            if child_fields:
                values = [media_id] + [data.get(f) for f in child_fields]
                placeholders = ','.join(['%s'] * len(values))
                columns = ','.join(['id'] + child_fields)
                debug(f"create_media: inserimento in {child_table} con valori {values}")
                cur.execute(f"INSERT INTO {child_table} ({columns}) VALUES ({placeholders})", values)

            conn.commit()
            debug(f"create_media: commit avvenuto per media {media_id}")
            return media_id

    except Exception as e:
        if conn:
            conn.rollback()
        debug(f"[DB ERROR create_media {media_type}]: {e}")
        return None
    finally:
        connection.close(None, conn)

def fetch_media(media_type: str, media_id: int) -> Optional[Dict[str, Any]]:
    cfg = MEDIA_CHILD_TABLES.get(media_type)
    if not cfg:
        debug(f"fetch_media: tipo sconosciuto {media_type}")
        return None

    child_table, child_fields = cfg["table"], cfg["fields"]
    child_select = ','.join([f"{child_table}.{f}" for f in child_fields])
    query = f"""
        SELECT m.*, {child_select}
        FROM media m
        JOIN {child_table} ON {child_table}.id = m.id
        WHERE m.id=%s
    """
    debug(f"fetch_media: eseguo query per media_id={media_id}")
    return fetch_one(query, (media_id,))

def update_media(media_type: str, media_id: int, updates: Dict[str, Any]) -> bool:
    cfg = MEDIA_CHILD_TABLES.get(media_type)
    if not cfg:
        debug(f"update_media: tipo sconosciuto {media_type}")
        return False
    media_updates, child_updates = {}, {}
    for k, v in updates.items():
        if k in cfg["fields"]:
            child_updates[k] = v
        else:
            media_updates[k] = v
    success = True
    if media_updates:
        set_clause = ", ".join(f"{k}=%s" for k in media_updates.keys())
        params = tuple(media_updates.values()) + (media_id,)
        debug(f"update_media: aggiornamento media {media_updates}")
        success &= execute(f"UPDATE media SET {set_clause} WHERE id=%s", params)
    if child_updates:
        table = cfg["table"]
        set_clause = ", ".join(f"{k}=%s" for k in child_updates.keys())
        params = tuple(child_updates.values()) + (media_id,)
        debug(f"update_media: aggiornamento {table} {child_updates}")
        success &= execute(f"UPDATE {table} SET {set_clause} WHERE id=%s", params)
    return success

def delete_media(media_type: str, media_id: int) -> bool:
    cfg = MEDIA_CHILD_TABLES.get(media_type)
    if not cfg:
        debug(f"delete_media: tipo sconosciuto {media_type}")
        return False

    table = cfg["table"]
    debug(f"delete_media: eliminazione {table} + media {media_id}")
    success = execute(f"DELETE FROM {table} WHERE id=%s", (media_id,))
    success &= execute(f"DELETE FROM media WHERE id=%s", (media_id,))
    return success

# last line