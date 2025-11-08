# first line

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
            conn.commit()
            connection.close(None, conn)

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
            time.sleep(0.5)
            return True
    except Exception as e:
        print(f"[DB ERROR execute] {e}")
        conn.rollback()
        return False
    finally:
        connection.close(None, conn)

def fetch_all_media_db(media_type=None, search=None, filter_by=None, offset=0, limit=10):
    query = "SELECT * FROM media"
    params = []
    conditions = []

    if media_type:
        conditions.append("type = %s")
        params.append(media_type)

    if search:
        # qui puoi anche rendere dinamico il filtro: titolo, descrizione, autore ecc.
        conditions.append("title ILIKE %s")
        params.append(f"%{search}%")

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += " ORDER BY created_at DESC LIMIT %s OFFSET %s"
    params.extend([limit, offset])

    return fetch_all(query, tuple(params))

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
def create_media_db(data: Dict[str, Any]) -> Optional[int]:
    """
    Inserisce un record nella tabella media e nelle tabelle collegate
    (documents, concerts, media_authors, media_performances, media_genres, references).
    """
    conn = connection.connect()
    try:
        with conn.cursor() as cur:

            # 1. INSERT nella tabella media
            media_query = """
                INSERT INTO media
                    (type, title, description, duration, location, link,
                    additional_info, is_author, is_performer, year, user_id)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                RETURNING id;
            """

            media_values = (
                data.get("type"),
                data.get("title"),
                data.get("description"),
                data.get("duration"),
                data.get("stored_at"),
                data.get("link"),
                data.get("additional_info"),
                data.get("is_author", False),
                data.get("is_performer", False),
                data.get("year"),
                data.get("user_id"),
            )

            cur.execute(media_query, media_values)
            media_id = cur.fetchone()[0]
            debug(f"Inserted into media id={media_id}")

            # 2. DOCUMENTS
            if data.get("type") == "document":
                doc_query = """
                    INSERT INTO documents (media_id, format, pages, caption)
                    VALUES (%s, %s, %s, %s);
                """
                doc_values = (
                    media_id,
                    data.get("format"),
                    data.get("pages"),
                    data.get("caption"),
                )
                cur.execute(doc_query, doc_values)
                debug(f"Inserted document for media_id={media_id}")

            # 3. CONCERTI
            if data.get("type") == "concert_video":
                # Inserisci nella tabella concerts
                concert_query = """
                    INSERT INTO concerts (video_id, title, description)
                    VALUES (%s, %s, %s)
                    RETURNING id;
                """
                cur.execute(concert_query, (media_id, data.get("title"), data.get("description")))
                concert_id = cur.fetchone()[0]
                debug(f"Inserted concert id={concert_id} for media_id={media_id}")

                # Inserisci i segmenti del concerto
                for seg in data.get("tracklist", []):
                    seg_query = """
                        INSERT INTO concert_segments (concert_id, media_id, start_time, end_time, comment)
                        VALUES (%s,%s,%s,%s,%s)
                        RETURNING id;
                    """
                    cur.execute(seg_query, (
                        concert_id,
                        seg.get("media_id"),
                        seg.get("start_time"),
                        seg.get("end_time"),
                        seg.get("comment")
                    ))
                    segment_id = cur.fetchone()[0]

                    # performers del segmento
                    for performer_id in seg.get("performers", []):
                        cur.execute(
                            "INSERT INTO concert_segment_performers (segment_id, performer_id) VALUES (%s,%s);",
                            (segment_id, performer_id)
                        )
                    # instruments del segmento
                    for instrument_id in seg.get("instruments", []):
                        cur.execute(
                            "INSERT INTO concert_segment_instruments (segment_id, instrument_id) VALUES (%s,%s);",
                            (segment_id, instrument_id)
                        )
                    debug(f"Inserted segment id={segment_id} for concert_id={concert_id}")

            # 4. Inserimento relazioni: authors
            authors_list = []
            for author in data.get("authors", []):
                if isinstance(author, dict):
                    if author.get("type") == "user":
                        # collegamento ad un utente esistente
                        user_id = author["id"]
                        # cerca se già esiste un author legato a quell’utente
                        cur.execute("SELECT id FROM authors WHERE user_id=%s", (user_id,))
                        row = cur.fetchone()
                        if row:
                            author_id = row[0]
                        else:
                            # crea un record "anonimo" collegato a user_id
                            cur.execute("INSERT INTO authors (name, user_id) VALUES (%s,%s) RETURNING id",
                                        (f"user_{user_id}", user_id))
                            author_id = cur.fetchone()[0]
                    elif author.get("type") == "external":
                        # autore esterno con solo nome
                        cur.execute("SELECT id FROM authors WHERE name=%s", (author["name"],))
                        row = cur.fetchone()
                        if row:
                            author_id = row[0]
                        else:
                            cur.execute("INSERT INTO authors (name) VALUES (%s) RETURNING id", (author["name"],))
                            author_id = cur.fetchone()[0]
                    else:
                        raise ValueError("Tipo autore non valido")
                else:
                    # se è già un id numerico
                    author_id = author

                authors_list.append(author_id)
                cur.execute("INSERT INTO media_authors (media_id, author_id) VALUES (%s,%s);", (media_id, author_id))
                debug(f"Added author_id={author_id} to media_id={media_id}")

            # 5. Inserimento relazioni: performers
            for performer in data.get("performers", []):
                if performer.get("type") == "user":
                    user_id = performer["id"]
                    # cerca performer associato a user_id
                    cur.execute("SELECT id FROM performers WHERE user_id=%s", (user_id,))
                    row = cur.fetchone()
                    if row:
                        performer_id = row[0]
                    else:
                        # crea performer per l’utente
                        cur.execute(
                            "INSERT INTO performers (name, user_id) VALUES (%s,%s) RETURNING id",
                            (f"user_{user_id}", user_id)
                        )
                        performer_id = cur.fetchone()[0]

                elif performer.get("type") == "external":
                    name = performer.get("name")
                    # cerca se esiste già un performer esterno con lo stesso nome
                    cur.execute("SELECT id FROM performers WHERE name=%s", (name,))
                    row = cur.fetchone()
                    if row:
                        performer_id = row[0]  # già esistente
                    else:
                        # crea performer esterno
                        cur.execute(
                            "INSERT INTO performers (name) VALUES (%s) RETURNING id",
                            (name,)
                        )
                        performer_id = cur.fetchone()[0]

                # inserisci relazione con la media
                cur.execute(
                    "INSERT INTO media_performances (media_id, performer_id) VALUES (%s,%s);",
                    (media_id, performer_id),
                )

            # 6. Inserimento relazioni: genres
            for genre_id in data.get("genres", []):
                cur.execute(
                    "INSERT INTO media_genres (media_id, genre_id) VALUES (%s,%s);",
                    (media_id, genre_id),
                )
                debug(f"Added genre_id={genre_id} to media_id={media_id}")

            # 7. Inserimento relazioni: references
            for ref_id in data.get("references", []):
                cur.execute(
                    "INSERT INTO media_references (active_id, passive_id) VALUES (%s,%s);",
                    (media_id, ref_id),
                )
                debug(f"Linked media_id={media_id} to reference_id={ref_id}")

            conn.commit()
            return {"id": media_id}

    except Exception as e:
        conn.rollback()
        debug(f"ERROR in create_media_db: {e}")
        return None

    finally:
        conn.close()

def fetch_media_db(media_id: int) -> Optional[Dict[str, Any]]:
    query = """
    SELECT m.*, mp.performer_id, mp.additional_info
    FROM media m
    LEFT JOIN media_performances mp ON mp.media_id = m.id
    WHERE m.id=%s
    """
    row = fetch_one(query, (media_id,))
    if not row:
        return None

    # Trasforma performer_id in lista di performer
    performers = []
    if row.get("performer_id"):
        performers.append({"id": row["performer_id"], "type": "user"})

    media_dict = dict(row)
    media_dict["performers"] = performers
    return media_dict

def update_media_db(media_id: int, updates: Dict[str, Any], table: str = "media") -> bool:
    if not updates: return True
    set_clause = ", ".join(f"{k}=%s" for k in updates.keys())
    params = tuple(updates.values()) + (media_id,)
    return execute(f"UPDATE {table} SET {set_clause} WHERE id=%s", params)

def delete_media_db(media_id: Optional[int]) -> Dict[str, Any]:
    if media_id is None:
        return {"status": "ERROR", "reason": "Invalid media_id"}

    # Controlla se il media esiste
    row = fetch_one("SELECT id FROM media WHERE id=%s", (media_id,))
    if not row:
        return {"status": "NOT_FOUND", "reason": f"Media id={media_id} does not exist"}

    success = True
    try:
        for table in ["comments", "notes", "media_genres", "media_authors", "media_performances"]:
            success &= execute(f"DELETE FROM {table} WHERE media_id=%s", (media_id,))
        success &= execute("DELETE FROM media WHERE id=%s", (media_id,))
    except Exception as e:
        return {"status": "ERROR", "reason": str(e)}

    if success:
        return {"status": "OK", "media_id": media_id}
    else:
        return {"status": "ERROR", "reason": "Deletion failed"}

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
    """
    Crea un commento e ritorna l'ID appena creato.
    Aggiunta debug dettagliato per isolare errori.
    """
    # Connessione al database
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

            # Preparazione della query per l'inserimento
            placeholders = ",".join(["%s"] * len(values))
            query = f"INSERT INTO comments ({','.join(fields)}) VALUES ({placeholders}) RETURNING id"

            try:
                # Esecuzione della query
                cur.execute(query, tuple(values))
            except Exception as e:
                print(f"[create_comment_db] Execute FAILED: {e}")
                raise

            row = cur.fetchone()
            try:
                # Commit della transazione
                conn.commit()
            except Exception as e:
                print(f"[create_comment_db] Commit FAILED: {e}")
                raise

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
    print(f"[DEBUG] get_user_id_by_username called with: {username}")
    row = fetch_one("SELECT id FROM users WHERE username=%s", (username,))
    print(f"[DEBUG] fetch_one returned: {row}")
    if row:
        return row["id"]
    return None

def db_add_follow(follower_id: int, followee_id: int) -> bool:
    return execute(
        "INSERT INTO user_follow (follower_id, followed_id) VALUES (%s, %s)",
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