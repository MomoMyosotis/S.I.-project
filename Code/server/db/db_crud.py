# ...existing code...
from typing import Dict, Any, List, Optional
from . import connection
import hashlib, time
import psycopg2.extras

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
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query, params)
            row = cur.fetchone()   # leggi PRIMA di commit
            if row:
                debug(f"fetch_one success: {row}")
                return dict(row)
            return None
    except Exception as e:
        print(f"[DB ERROR fetch_one] {e}")
        return None
    finally:
        if conn:
            connection.close(None, conn)

def fetch_all(query: str, params: tuple = ()) -> List[Dict[str, Any]]:
    conn = connection.connect()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query, params)
            rows = cur.fetchall()
            debug(f"fetch_all returned {len(rows)} rows")
            # RealDictCursor yields dict-like rows already
            return [dict(r) for r in rows]
    except Exception as e:
        print(f"[DB ERROR fetch_all] {e}")
        return []
    finally:
        if conn:
            connection.close(None, conn)

def execute(query: str, params: tuple = ()) -> bool:
    conn = connection.connect()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            conn.commit()
            debug(f"execute success: {query} {params}")
            # small pause for DB consistency if necessary (kept for compatibility)
            time.sleep(0.1)
            return True
    except Exception as e:
        print(f"[DB ERROR execute] {e}")
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
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
            user_id_row = cur.fetchone()
            user_id = user_id_row[0] if user_id_row else None

            if child_table and child_fields and user_id:
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
        if conn:
            connection.close(None, conn)

def fetch_user_db(user_id: Optional[int] = None, child_table: str = None,
                    child_fields: List[str] = None, filters: Optional[Dict[str, Any]] = None
                    ) -> Optional[Any]:
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

    # return single dict for id lookup, list for general fetch
    if user_id:
        return fetch_one(query, tuple(params))
    return fetch_all(query, tuple(params))

def fetch_user_roles_db(user_id: int) -> List[str]:
    """
    Return a list of role codes for the user. The DB uses user_levels/lvl_id on users table.
    This will return the single level code assigned to the user (as list for compatibility).
    """
    query = """
        SELECT ul.code
        FROM users u
        JOIN user_levels ul ON u.lvl_id = ul.id
        WHERE u.id = %s
    """
    row = fetch_one(query, (user_id,))
    return [row['code']] if row and 'code' in row else []

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
def update_document_db(media_id: int, updates: Dict[str, Any]) -> bool:
    if not updates:
        return True
    set_clause = ", ".join(f"{k}=%s" for k in updates.keys())
    params = list(updates.values()) + [media_id]
    return execute(f"UPDATE documents SET {set_clause} WHERE media_id=%s", tuple(params))

def create_media_db(data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor() as cur:

            # --- BASE MEDIA ---
            cur.execute("""
                INSERT INTO media (
                    type, user_id, title, year, description, link, duration,
                    recording_date, location, additional_info, stored_at,
                    is_author, is_performer
                ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                RETURNING id;
            """, (
                data.get("type"),
                data.get("user_id"),
                data.get("title"),
                data.get("year"),
                data.get("description"),
                data.get("link"),
                data.get("duration"),
                data.get("recording_date"),
                data.get("location"),
                data.get("additional_info"),
                data.get("stored_at"),
                data.get("is_author", False),
                data.get("is_performer", False),
            ))
            media_id_row = cur.fetchone()
            media_id = media_id_row[0] if media_id_row else None
            debug(f"[DB][CREATE] media_id={media_id}")

            if not media_id:
                conn.commit()
                return None

            # --- AUTHORS ---
            for author_id in data.get("authors", []):
                cur.execute("""
                    INSERT INTO media_authors (media_id, author_id)
                    VALUES (%s,%s)
                    ON CONFLICT DO NOTHING;
                """, (media_id, author_id))
                debug(f"[DB][AUTHOR] linked {author_id}")

            # --- PERFORMERS ---
            for performer_id in data.get("performers", []):
                cur.execute("""
                    INSERT INTO media_performances (media_id, performer_id)
                    VALUES (%s,%s)
                    ON CONFLICT DO NOTHING;
                """, (media_id, performer_id))
                debug(f"[DB][PERF] linked {performer_id}")

            # --- GENRES ---
            for genre_id in data.get("genres", []):
                cur.execute("""
                    INSERT INTO media_genres (media_id, genre_id)
                    VALUES (%s,%s)
                    ON CONFLICT DO NOTHING;
                """, (media_id, genre_id))
                debug(f"[DB][GENRE] linked {genre_id}")

            # --- REFERENCES ---
            for ref_id in data.get("references", []):
                cur.execute("""
                    INSERT INTO media_references (active_id, passive_id)
                    VALUES (%s,%s)
                    ON CONFLICT DO NOTHING;
                """, (media_id, ref_id))
                debug(f"[DB][REF] linked {ref_id}")

            # --- DOCUMENTI (solo se type=document) ---
            if data.get("type") == "document":
                cur.execute("""
                    INSERT INTO documents (media_id, format, pages, caption)
                    VALUES (%s,%s,%s,%s)
                    ON CONFLICT DO NOTHING;
                """, (
                    media_id,
                    data.get("format"),
                    data.get("pages"),
                    data.get("caption"),
                ))
                debug(f"[DB][DOC] document for media_id={media_id}")

            conn.commit()
            return {"id": media_id}

    except Exception as e:
        if conn:
            conn.rollback()
        debug(f"[ERROR][create_media_db] {e}")
        return None
    finally:
        if conn:
            connection.close(None, conn)

def fetch_media_db(media_id: int) -> Optional[Dict[str, Any]]:
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("SELECT * FROM media WHERE id=%s;", (media_id,))
            row = cur.fetchone()
            if not row:
                return None

            media = dict(row)

            # relazioni
            cur.execute("SELECT author_id FROM media_authors WHERE media_id=%s;", (media_id,))
            media["authors"] = [r["author_id"] for r in cur.fetchall()]

            cur.execute("SELECT performer_id FROM media_performances WHERE media_id=%s;", (media_id,))
            media["performers"] = [r["performer_id"] for r in cur.fetchall()]

            cur.execute("SELECT genre_id FROM media_genres WHERE media_id=%s;", (media_id,))
            media["genres"] = [r["genre_id"] for r in cur.fetchall()]

            cur.execute("SELECT passive_id FROM media_references WHERE active_id=%s;", (media_id,))
            media["references"] = [r["passive_id"] for r in cur.fetchall()]

            return media
    except Exception as e:
        debug(f"[ERROR][fetch_media_db] {e}")
        return None
    finally:
        if conn:
            connection.close(None, conn)

def fetch_all_media_db(
    media_type: Optional[str] = None,
    search: Optional[str] = None,
    filter_by: Optional[str] = None,
    offset: int = 0,
    limit: int = 10,
) -> List[Dict[str, Any]]:
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            query = "SELECT * FROM media WHERE TRUE"
            params = []

            if media_type:
                query += " AND type=%s"
                params.append(media_type)

            if search:
                query += " AND (title ILIKE %s OR description ILIKE %s)"
                params.extend([f"%{search}%", f"%{search}%"])

            if filter_by and filter_by != "all":
                query += " AND type=%s"
                params.append(filter_by)

            query += " ORDER BY created_at DESC OFFSET %s LIMIT %s;"
            params.extend([offset, limit])

            cur.execute(query, tuple(params))
            rows = cur.fetchall()
            if not rows:
                return []

            result = [dict(r) for r in rows]
            return result

    except Exception as e:
        debug(f"[ERROR][fetch_all_media_db] {e}")
        return []
    finally:
        if conn:
            connection.close(None, conn)

def update_media_db(media_id: int, updates: Dict[str, Any]) -> bool:
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor() as cur:
            set_clause = ", ".join(f"{k}=%s" for k in updates.keys())
            params = list(updates.values()) + [media_id]
            cur.execute(f"UPDATE media SET {set_clause} WHERE id=%s;", params)
        conn.commit()
        return True
    except Exception as e:
        if conn:
            conn.rollback()
        debug(f"[ERROR][update_media_db] {e}")
        return False
    finally:
        if conn:
            connection.close(None, conn)

def delete_media_db(media_id: int) -> bool:
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM media WHERE id=%s;", (media_id,))
        conn.commit()
        debug(f"[DB][DELETE] media_id={media_id}")
        return True
    except Exception as e:
        if conn:
            conn.rollback()
        debug(f"[ERROR][delete_media_db] {e}")
        return False
    finally:
        if conn:
            connection.close(None, conn)

# =====================
# NOTES CRUD
# =====================
def create_note_db(author: int, media_id: int, note_type: str, **kwargs) -> Optional[int]:
    conn = connection.connect()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            # Controllo utente
            user_row = fetch_one("SELECT id FROM users WHERE id=%s", (author,))
            if not user_row:
                print(f"[create_note_db] User id={author} does not exist!")
                return None

            # Controllo media
            media_row = fetch_one("SELECT id FROM media WHERE id=%s", (media_id,))
            if not media_row:
                print(f"[create_note_db] Media id={media_id} does not exist!")
                return None

            fields = ["author", "media_id", "note_type"]
            values = [author, media_id, note_type]

            for k, v in kwargs.items():
                fields.append(k)
                values.append(v)

            placeholders = ",".join(["%s"] * len(values))
            query = f"INSERT INTO notes ({','.join(fields)}) VALUES ({placeholders}) RETURNING id"

            cur.execute(query, tuple(values))
            row = cur.fetchone()
            conn.commit()

            return row["id"] if row and "id" in row else None

    except Exception as e:
        if conn: conn.rollback()
        print(f"[DB ERROR create_note_db]: {e}")
        return None
    finally:
        if conn:
            connection.close(None, conn)

def fetch_note_db(where_field: str, where_value: Any) -> List[Dict[str, Any]]:
    return fetch_all(f"SELECT * FROM notes WHERE {where_field}=%s ORDER BY id ASC", (where_value,))

ALLOWED_NOTE_FIELDS = {
    "note_type", "start_time", "end_time", "x_coord", "y_coord",
    "page", "solos", "rhythm", "content", "stored_at"
}

def update_note_db(note_id: int, field: str, value: Any) -> bool:
    if field not in ALLOWED_NOTE_FIELDS:
        print(f"[update_note_db] Invalid field: {field}")
        return False
    return execute(f"UPDATE notes SET {field}=%s WHERE id=%s", (value, note_id))

def delete_note_db(note_id: int) -> bool:
    return execute("DELETE FROM notes WHERE id=%s", (note_id,))

# =====================
# COMMENTS CRUD
# =====================
def create_comment_db(user_id: int, text: str, media_id: Optional[int] = None,
                        note_id: Optional[int] = None, parent_comment_id: Optional[int] = None) -> Optional[int]:
    conn = connection.connect()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            # Controllo se l'utente esiste
            user_row = fetch_one("SELECT id FROM users WHERE id=%s", (user_id,))
            if not user_row:
                print(f"[create_comment_db] User id={user_id} does not exist!")
                return None
            fields = ["user_id", "text"]
            values = [user_id, text]

            # Controllo se il media esiste
            if media_id is not None:
                media_row = fetch_one("SELECT id FROM media WHERE id=%s", (media_id,))
                if not media_row:
                    print(f"[create_comment_db] Media id={media_id} does not exist!")
                    return None
                fields.append("media_id")
                values.append(media_id)

            # Controllo se la nota esiste
            if note_id is not None:
                note_row = fetch_one("SELECT id FROM notes WHERE id=%s", (note_id,))
                if not note_row:
                    print(f"[create_comment_db] Note id={note_id} does not exist!")
                    return None
                fields.append("note_id")
                values.append(note_id)

            # Controllo se il commento parent esiste
            if parent_comment_id is not None:
                parent_row = fetch_one("SELECT id FROM comments WHERE id=%s", (parent_comment_id,))
                if not parent_row:
                    print(f"[create_comment_db] Parent comment id={parent_comment_id} does not exist!")
                    return None
                fields.append("parent_comment_id")
                values.append(parent_comment_id)

            placeholders = ",".join(["%s"] * len(values))
            query = f"INSERT INTO comments ({','.join(fields)}) VALUES ({placeholders}) RETURNING id"

            cur.execute(query, tuple(values))
            row = cur.fetchone()
            conn.commit()

            if row and "id" in row:
                return row["id"]
            else:
                print(f"[create_comment_db] No ID returned after insert")
                return None

    except Exception as e:
        if conn: conn.rollback()
        print(f"[DB ERROR create_comment_db]: {e}")
        return None
    finally:
        if conn:
            connection.close(None, conn)

def fetch_comment_db(where_field: str, where_value: Any) -> List[Dict[str, Any]]:
    comments = fetch_all(f"SELECT * FROM comments WHERE {where_field}=%s ORDER BY id ASC", (where_value,))
    return comments

def fetch_comments_by_media_db(media_id: int) -> List[Dict[str, Any]]:
    comments = fetch_all("SELECT * FROM comments WHERE media_id=%s ORDER BY id ASC", (media_id,))
    return comments

def fetch_comments_by_note_db(note_id: int) -> List[Dict[str, Any]]:
    comments = fetch_all("SELECT * FROM comments WHERE note_id=%s ORDER BY id ASC", (note_id,))
    return comments

def fetch_comment_replies_db(parent_comment_id: int) -> List[Dict[str, Any]]:
    replies = fetch_all("SELECT * FROM comments WHERE parent_comment_id=%s ORDER BY id ASC", (parent_comment_id,))
    return replies

def update_comment_db(comment_id: int, field: str, value: Any) -> bool:
    try:
        result = execute(f"UPDATE comments SET {field}=%s WHERE id=%s", (value, comment_id))
        return result
    except Exception as e:
        print(f"[update_comment_db] Error while updating comment_id={comment_id}: {e}")
        return False

def delete_comment_db(comment_id: int) -> bool:
    try:
        result = execute("DELETE FROM comments WHERE id=%s", (comment_id,))
        return result
    except Exception as e:
        print(f"[delete_comment_db] Error while deleting comment_id={comment_id}: {e}")
        return False

# =====================
# DICTIONARY CRUD
# =====================
def create_dict_entry(table: str, name: str) -> Optional[int]:
    """
    Ensure a row with given name exists in `table`. If present return id,
    otherwise INSERT and COMMIT and return the new id.
    This avoids race/visibility problems when other connections try to use the id.
    """
    conn = None
    try:
        # First try to fetch existing entry using a dedicated connection
        conn = connection.connect()
        with conn.cursor() as cur:
            cur.execute(f"SELECT id FROM {table} WHERE name = %s FOR UPDATE", (name,))
            row = cur.fetchone()
            if row:
                return row[0]
            # not present -> insert and commit so other connections can see it
            cur.execute(f"INSERT INTO {table} (name) VALUES (%s) RETURNING id", (name,))
            new_row = cur.fetchone()
            conn.commit()
            return new_row[0] if new_row else None
    except Exception as e:
        if conn:
            conn.rollback()
        debug(f"[DB ERROR create_dict_entry]: {e}")
        return None
    finally:
        if conn:
            connection.close(None, conn)

def fetch_dict_entry_by_name(table: str, name: str) -> Optional[Dict[str, Any]]:
    return fetch_one(f"SELECT * FROM {table} WHERE name=%s", (name,))

def fetch_dict_entry(table: str, name: str) -> Optional[Dict[str, Any]]:
    return fetch_dict_entry_by_name(table, name)

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
def advanced_song_search_db(filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    query = "SELECT DISTINCT s.* FROM songs s"
    joins, conditions, params = [], [], []

    if filters.get("author_ids"):
        joins.append("JOIN media_authors sa ON sa.media_id = s.id")
        conditions.append("sa.author_id = ANY(%s)")
        params.append(filters["author_ids"])

    if filters.get("genre_ids"):
        joins.append("JOIN media_genres sg ON sg.media_id = s.id")
        conditions.append("sg.genre_id = ANY(%s)")
        params.append(filters["genre_ids"])

    if filters.get("performer_ids"):
        joins.append("JOIN media_performances sp ON sp.media_id = s.id")
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
        SELECT m.id, m.title, m.year, m.description, m.link, d.format, d.pages, d.caption, d.media_id
        FROM documents d
        JOIN media m ON d.media_id = m.id
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
def get_user_username_by_id(id_):
    row = fetch_one("SELECT username FROM users WHERE id=%s", (id_,))
    if row:
        return row.get("username")
    return None

def get_user_id_by_username(username: str) -> Optional[int]:
    """Restituisce l'id di un utente dato lo username."""
    print(f"[DEBUG] get_user_id_by_username called with: {username}")
    row = fetch_one("SELECT id FROM users WHERE username=%s", (username,))
    print(f"[DEBUG] fetch_one returned: {row}")
    if row:
        return row["id"]
    return None

def db_add_follow(follower_id: int, followee_id: int) -> bool:
    return execute(
        "INSERT INTO user_follow (follower_id, followed_id) VALUES (%s, %s) ON CONFLICT DO NOTHING",
        (follower_id, followee_id)
    )

def db_remove_follow(follower_id: int, followee_id: int) -> bool:
    return execute(
        "DELETE FROM user_follow WHERE follower_id = %s AND followed_id = %s",
        (follower_id, followee_id)
    )

def db_get_following(user_id: int) -> List[Dict[str, Any]]:
    sql = """
        SELECT u.id, u.username, u.mail
        FROM users u
        JOIN user_follow uf ON u.id = uf.followed_id
        WHERE uf.follower_id = %s
    """
    return fetch_all(sql, (user_id,))

def db_get_followers(user_id: int) -> List[Dict[str, Any]]:
    sql = """
        SELECT u.id, u.username, u.mail
        FROM users u
        JOIN user_follow uf ON u.id = uf.follower_id
        WHERE uf.followed_id = %s
    """
    return fetch_all(sql, (user_id,))

# last line