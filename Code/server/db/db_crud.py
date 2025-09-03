# first line

from typing import Dict, Any, List, Optional
from . import connection
import hashlib

# =====================
# DEBUG
# =====================
def debug(msg: str):
    print(f"[DEBUG] {msg}")

# =====================
# GENERIC CRUD
# =====================
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
            print("[DEBUG] db_get_following result:", rows)
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

# =====================
# PASSWORD
# =====================
def hash_pswd(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(plain: str, hashed: str) -> bool:
    return hash_pswd(plain) == hashed

# =====================
# USER CRUD
# =====================
def create_user_db(main_fields: tuple, child_table: str = None, child_fields: tuple = ()) -> Optional[int]:
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO users (mail, username, password_hash, birthday, bio, profile_pic)
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
            """, main_fields)
            user_id = cur.fetchone()[0]

            if child_table and child_fields:
                placeholders = ",".join(['%s'] * (len(child_fields) + 1))
                columns = ','.join(['id'] + list(child_fields))
                cur.execute(f"INSERT INTO {child_table} ({columns}) VALUES ({placeholders})", (user_id, *child_fields))
            conn.commit()
            return user_id
    except Exception as e:
        if conn: conn.rollback()
        debug(f"[DB ERROR create_user_db]: {e}")
        return None
    finally:
        if conn: connection.close(None, conn)

def fetch_user_db(user_id: Optional[int] = None, child_table: str = None,
                    child_fields: List[str] = None, filters: Optional[Dict[str, Any]] = None
                    ) -> List[Dict[str, Any]]:
    base_query = "SELECT u.*"
    joins = ""
    conditions = []
    params = []

    if child_table and child_fields:
        child_select = ','.join([f"{child_table}.{f}" for f in child_fields])
        base_query += f", {child_select}"
        joins = f" JOIN {child_table} ON {child_table}.id = u.id"

    query = f"{base_query} FROM users u {joins}"

    if user_id is not None:
        conditions.append("u.id = %s")
        params.append(user_id)

    if filters:
        for key, value in filters.items():
            conditions.append(f"u.{key} = %s")
            params.append(value)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    return fetch_one(query, tuple(params)) if user_id else fetch_all(query, tuple(params))

def fetch_user_roles_db(user_id: int) -> List[str]:
    query = "SELECT role FROM user_roles WHERE user_id = %s"
    rows = fetch_all(query, (user_id,))
    return [row['role'] for row in rows]

def update_user_db(user_id: int, updates: Dict[str, Any], table: str = "users") -> bool:
    if not updates: return True
    set_clause = ", ".join(f"{k}=%s" for k in updates.keys())
    params = tuple(updates.values()) + (user_id,)
    return execute(f"UPDATE {table} SET {set_clause} WHERE id=%s", params)

def delete_user_db(user_id: int, child_table: Optional[str] = None) -> bool:
    success = True
    if child_table:
        success &= execute(f"DELETE FROM {child_table} WHERE id=%s", (user_id,))
    success &= execute("DELETE FROM users WHERE id=%s", (user_id,))
    return success

# =====================
# MEDIA CRUD
# =====================
def create_media_db(main_fields: tuple, child_table: str = None, child_fields: tuple = ()) -> Optional[int]:
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO media (type, title, year, description, link, created_at)
                VALUES (%s,%s,%s,%s,%s,%s) RETURNING id
            """, main_fields)
            media_id = cur.fetchone()[0]

            if child_table and child_fields:
                placeholders = ','.join(['%s'] * (len(child_fields) + 1))
                columns = ','.join(['id'] + list(child_fields))
                cur.execute(f"INSERT INTO {child_table} ({columns}) VALUES ({placeholders})", (media_id, *child_fields))
            conn.commit()
            return media_id
    except Exception as e:
        if conn: conn.rollback()
        debug(f"[DB ERROR create_media_db]: {e}")
        return None
    finally:
        if conn: connection.close(None, conn)

def fetch_media_db(media_id: int, child_table: str = None, child_fields: List[str] = None) -> Optional[Dict[str, Any]]:
    if child_table and child_fields:
        child_select = ','.join([f"{child_table}.{f}" for f in child_fields])
        query = f"SELECT m.*, {child_select} FROM media m JOIN {child_table} ON {child_table}.id = m.id WHERE m.id=%s"
    else:
        query = "SELECT * FROM media WHERE id=%s"
    return fetch_one(query, (media_id,))

def update_media_db(media_id: int, updates: Dict[str, Any], table: str = "media") -> bool:
    if not updates: return True
    set_clause = ", ".join(f"{k}=%s" for k in updates.keys())
    params = tuple(updates.values()) + (media_id,)
    return execute(f"UPDATE {table} SET {set_clause} WHERE id=%s", params)

def delete_media_db(media_id: int) -> bool:
    success = True
    for table in ["comments", "notes"]:
        success &= execute(f"DELETE FROM {table} WHERE media_id=%s", (media_id,))
    for table in ["song_genres", "song_authors", "song_performances"]:
        success &= execute(f"DELETE FROM {table} WHERE song_id=%s", (media_id,))
    success &= execute("DELETE FROM media WHERE id=%s", (media_id,))
    return success

# =====================
# INTERVENTIONS CRUD
# =====================
def create_intervention_db(table: str, fields: tuple, values: tuple) -> Optional[int]:
    placeholders = ','.join(['%s'] * len(values))
    cols = ','.join(fields)
    query = f"INSERT INTO {table} ({cols}) VALUES ({placeholders}) RETURNING id"
    row = fetch_one(query, values)
    return row.get("id") if row else None

def fetch_interventions_db(table: str, where_field: str, where_value: Any, order_by: str = "id ASC") -> List[Dict[str, Any]]:
    return fetch_all(f"SELECT * FROM {table} WHERE {where_field}=%s ORDER BY {order_by}", (where_value,))

def update_intervention_db(table: str, intervention_id: int, field: str, content: str) -> bool:
    return execute(f"UPDATE {table} SET {field}=%s WHERE id=%s", (content, intervention_id))

def delete_intervention_db(table: str, intervention_id: int) -> bool:
    return execute(f"DELETE FROM {table} WHERE id=%s", (intervention_id,))

def fetch_comments_db(media_id: int) -> List[Dict[str, Any]]:
    query = """
        SELECT id, user_id, media_id, content, parent_id, created_at
        FROM comments
        WHERE media_id = %s
        ORDER BY created_at ASC
    """
    return fetch_all(query, (media_id,))

# =====================
# DICTIONARY CRUD
# =====================
def create_dict_entry(table: str, name: str) -> Optional[int]:
    existing = fetch_one(f"SELECT id FROM {table} WHERE name = %s", (name,))
    if existing: return None
    row = fetch_one(f"INSERT INTO {table} (name) VALUES (%s) RETURNING id", (name,))
    return row.get("id") if row else None

def fetch_dict_entry_by_name(table: str, name: str) -> Optional[Dict[str, Any]]:
    return fetch_one(f"SELECT * FROM {table} WHERE name=%s", (name,))

def fetch_all_dict_entries(table: str) -> List[Dict[str, Any]]:
    return fetch_all(f"SELECT * FROM {table} ORDER BY name")

def update_dict_entry(table: str, entry_id: int, new_name: str) -> bool:
    return execute(f"UPDATE {table} SET name=%s WHERE id=%s", (new_name, entry_id))

def delete_dict_entry(table: str, entry_id: int) -> bool:
    return execute(f"DELETE FROM {table} WHERE id=%s", (entry_id,))

# =====================
# RELATIONS CRUD
# =====================
def create_relation(table: str, fields: tuple, values: tuple) -> bool:
    cols = ','.join(fields)
    placeholders = ','.join(['%s'] * len(values))
    return execute(f"INSERT INTO {table} ({cols}) VALUES ({placeholders})", values)

def fetch_relations(table: str, where_field: str, where_value: Any) -> List[Dict[str, Any]]:
    return fetch_all(f"SELECT * FROM {table} WHERE {where_field}=%s", (where_value,))

def delete_relation(table: str, conditions: Dict[str, Any]) -> bool:
    where_clause = " AND ".join(f"{k}=%s" for k in conditions.keys())
    params = tuple(conditions.values())
    return execute(f"DELETE FROM {table} WHERE {where_clause}", params)

# =====================
# ADVANCED SEARCH
# =====================
def advanced_song_search(filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    query = "SELECT DISTINCT s.* FROM songs s"
    joins, conditions, params = [], [], []

    if filters.get("author_ids"):
        joins.append("JOIN song_authors sa ON sa.song_id = s.id")
        conditions.append("sa.author_id = ANY(%s)")
        params.append(filters["author_ids"])

    if filters.get("genre_ids"):
        joins.append("JOIN song_genres sg ON sg.song_id = s.id")
        conditions.append("sg.genre_id = ANY(%s)")
        params.append(filters["genre_ids"])

    if filters.get("performer_ids"):
        joins.append("JOIN song_performances sp ON sp.song_id = s.id")
        conditions.append("sp.performer_id = ANY(%s)")
        params.append(filters["performer_ids"])

    if filters.get("title"):
        conditions.append("s.title ILIKE %s")
        params.append(f"%{filters['title']}%")

    if joins: query += " " + " ".join(joins)
    if conditions: query += " WHERE " + " AND ".join(conditions)
    query += " ORDER BY s.title"

    return fetch_all(query, tuple(params))

def advanced_document_search_db(filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    base_query = """
        SELECT m.id, m.title, m.year, m.description, m.link, d.format, d.pages, d.caption, d.song_id
        FROM documents d
        JOIN media m ON d.id = m.id
        WHERE m.type = 'document'
    """
    params, conditions = [], []

    if "title" in filters: conditions.append("m.title ILIKE %s"); params.append(f"%{filters['title']}%")
    if "year" in filters: conditions.append("m.year = %s"); params.append(filters["year"])
    if "format" in filters: conditions.append("d.format = %s"); params.append(filters["format"])
    if "pages_min" in filters: conditions.append("d.pages >= %s"); params.append(filters["pages_min"])
    if "pages_max" in filters: conditions.append("d.pages <= %s"); params.append(filters["pages_max"])

    if conditions: base_query += " AND " + " AND ".join(conditions)
    return fetch_all(base_query, tuple(params))

def advanced_video_search_db(filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    base_query = """
        SELECT m.id, m.title, m.year, m.description, m.link,
                v.duration, v.location, v.additional_info, v.director
        FROM videos v
        JOIN media m ON v.id = m.id
        WHERE m.type = 'video'
    """
    params, conditions = [], []

    if "title" in filters: conditions.append("m.title ILIKE %s"); params.append(f"%{filters['title']}%")
    if "year" in filters: conditions.append("m.year = %s"); params.append(filters["year"])
    if "location" in filters: conditions.append("v.location ILIKE %s"); params.append(f"%{filters['location']}%")
    if "director" in filters: conditions.append("v.director ILIKE %s"); params.append(f"%{filters['director']}%")
    if "duration_min" in filters: conditions.append("v.duration >= %s"); params.append(filters["duration_min"])
    if "duration_max" in filters: conditions.append("v.duration <= %s"); params.append(filters["duration_max"])

    if conditions: base_query += " AND " + " AND ".join(conditions)
    return fetch_all(base_query, tuple(params))

# =====================
# FOLLOWERS
# =====================

def get_user_id_by_username(username: str) -> Optional[int]:
    """Restituisce l'id di un utente dato lo username."""
    row = fetch_one("SELECT id FROM users WHERE username=%s", (username,))
    if row:
        return row["id"]
    return None

def follow_user(follower_id_or_username: Any, followed_id_or_username: Any) -> bool:
    """
    follower_id_or_username / followed_id_or_username possono essere ID (int) o username (str).
    Recupera l'ID se serve.
    """
    if isinstance(follower_id_or_username, str):
        follower_id = get_user_id_by_username(follower_id_or_username)
    else:
        follower_id = follower_id_or_username

    if isinstance(followed_id_or_username, str):
        followed_id = get_user_id_by_username(followed_id_or_username)
    else:
        followed_id = followed_id_or_username

    if follower_id is None or followed_id is None:
        return False

    return execute(
        "INSERT INTO user_follow (follower_id, followed_id) VALUES (%s, %s)",
        (follower_id, followed_id)
    )

def unfollow_user(follower_id_or_username: Any, followed_id_or_username: Any) -> bool:
    if isinstance(follower_id_or_username, str):
        follower_id = get_user_id_by_username(follower_id_or_username)
    else:
        follower_id = follower_id_or_username

    if isinstance(followed_id_or_username, str):
        followed_id = get_user_id_by_username(followed_id_or_username)
    else:
        followed_id = followed_id_or_username

    if follower_id is None or followed_id is None:
        return False

    return execute(
        "DELETE FROM user_follow WHERE follower_id=%s AND followed_id=%s",
        (follower_id, followed_id)
    )

def db_get_following(user_id_or_username: Any) -> List[Dict[str, Any]]:
    if isinstance(user_id_or_username, str):
        user_id = get_user_id_by_username(user_id_or_username)
    else:
        user_id = user_id_or_username
    if user_id is None:
        return []
    return fetch_all(
        "SELECT u.id, u.username, u.mail "
        "FROM users u "
        "JOIN user_follow uf ON u.id = uf.followed_id "
        "WHERE uf.follower_id = %s",
        (user_id,)
    )

def db_get_followers(user_id_or_username: Any) -> List[Dict[str, Any]]:
    if isinstance(user_id_or_username, str):
        user_id = get_user_id_by_username(user_id_or_username)
    else:
        user_id = user_id_or_username
    if user_id is None:
        return []
    return fetch_all(
        "SELECT u.id, u.username, u.mail "
        "FROM users u "
        "JOIN user_follow uf ON u.id = uf.follower_id "
        "WHERE uf.followed_id = %s",
        (user_id,)
    )

# last line