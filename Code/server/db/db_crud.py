# first line
from typing import Dict, Any, List, Optional
from . import connection
import json
import hashlib, time
import psycopg2.extras
from datetime import datetime

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
        #print(f"[DB ERROR fetch_one] {e}")
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
        #print(f"[DB ERROR fetch_all] {e}")
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
        #print(f"[DB ERROR execute] {e}")
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

            # --- CRITICAL FIX: Convert date strings to datetime objects ---
            DATE_FIELDS = {"recording_date", "concert_date"}
            prepared_data = data.copy()
            for date_field in DATE_FIELDS:
                if date_field in prepared_data and prepared_data[date_field] is not None:
                    val = prepared_data[date_field]
                    if isinstance(val, str):
                        try:
                            # Try ISO format first (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)
                            if "T" in val:
                                prepared_data[date_field] = datetime.fromisoformat(val)
                                debug(f"[DB][create_media_db] Converted ISO date '{val}' for field '{date_field}'")
                            elif len(val) == 8 and val.isdigit():
                                # Handle DDMMYYYY format for concert dates
                                day, month, year_part = val[0:2], val[2:4], val[4:8]
                                prepared_data[date_field] = datetime.strptime(f"{year_part}-{month}-{day}", "%Y-%m-%d")
                                debug(f"[DB][create_media_db] Converted DDMMYYYY date '{val}' to {prepared_data[date_field]} for field '{date_field}'")
                            else:
                                # Try standard YYYY-MM-DD
                                prepared_data[date_field] = datetime.strptime(val, "%Y-%m-%d")
                                debug(f"[DB][create_media_db] Converted YYYY-MM-DD date '{val}' for field '{date_field}'")
                        except Exception as e:
                            debug(f"[DB][create_media_db] Failed to convert date string '{val}' for field '{date_field}': {e}")
                            # Leave as-is if conversion fails, DB will handle or error appropriately

            # --- BASE MEDIA ---
            # Ensure linked_media is stored as JSON/text (avoid passing raw dict/list to DB driver)
            linked_media_val = prepared_data.get("linked_media")
            if isinstance(linked_media_val, (dict, list)):
                try:
                    linked_media_serialized = json.dumps(linked_media_val)
                except Exception:
                    linked_media_serialized = str(linked_media_val)
            else:
                linked_media_serialized = linked_media_val

            cur.execute("""
                INSERT INTO media (
                    type, user_id, title, year, description, linked_media, duration,
                    recording_date, location, additional_info, stored_at,
                    is_author, is_performer
                ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                RETURNING id;
            """, (
                prepared_data.get("type"),
                prepared_data.get("user_id"),
                prepared_data.get("title"),
                prepared_data.get("year"),
                prepared_data.get("description"),
                linked_media_serialized,
                prepared_data.get("duration"),
                prepared_data.get("recording_date"),
                prepared_data.get("location"),
                prepared_data.get("additional_info"),
                prepared_data.get("stored_at"),
                prepared_data.get("is_author", False),
                prepared_data.get("is_performer", False),
            ))
            
            # DEBUG: Log what was actually inserted
            debug(f"[DB][create_media_db] ===== INSERT VALUES =====")
            debug(f"[DB][create_media_db] type={prepared_data.get('type')}")
            debug(f"[DB][create_media_db] user_id={prepared_data.get('user_id')}")
            debug(f"[DB][create_media_db] title={prepared_data.get('title')}")
            debug(f"[DB][create_media_db] year={prepared_data.get('year')}")
            debug(f"[DB][create_media_db] description={prepared_data.get('description')}")
            debug(f"[DB][create_media_db] duration={prepared_data.get('duration')}")
            debug(f"[DB][create_media_db] recording_date={prepared_data.get('recording_date')}")
            debug(f"[DB][create_media_db] location={prepared_data.get('location')}")
            debug(f"[DB][create_media_db] additional_info={prepared_data.get('additional_info')}")
            debug(f"[DB][create_media_db] stored_at={prepared_data.get('stored_at')}")
            debug(f"[DB][create_media_db] is_author={prepared_data.get('is_author', False)}")
            debug(f"[DB][create_media_db] is_performer={prepared_data.get('is_performer', False)}")
            debug(f"[DB][create_media_db] ===== END VALUES =====")
            
            media_id_row = cur.fetchone()
            media_id = media_id_row[0] if media_id_row else None
            debug(f"[DB][CREATE] media_id={media_id}")

            if not media_id:
                conn.commit()
                return None

            # Helper to normalize incoming relation items (ids or names or comma separated strings)
            def _normalize_ids(table_name, raw_items):
                ids = []
                seen = set()
                if raw_items is None:
                    return ids
                # Normalize nested lists/tuples and strings
                parts = []
                if isinstance(raw_items, str):
                    parts = [p.strip() for p in raw_items.split(",") if p.strip()]
                elif isinstance(raw_items, (list, tuple)):
                    for part in raw_items:
                        if isinstance(part, (list, tuple)):
                            for sub in part:
                                parts.append(sub)
                        else:
                            parts.append(part)
                else:
                    parts = [raw_items]

                for it in parts:
                    if it is None:
                        continue
                    try:
                        nid = None
                        # Special resolution for author identifiers: an int may refer to a users.id
                        if isinstance(it, int):
                            if table_name == "authors":
                                # prefer explicit authors.id if present
                                arow = fetch_one("SELECT id FROM authors WHERE id=%s", (it,))
                                if arow and arow.get("id"):
                                    nid = int(arow.get("id"))
                                else:
                                    # try resolving as users.id -> create or fetch author linked to that user
                                    urow = fetch_one("SELECT id, username FROM users WHERE id=%s", (it,))
                                    if urow and urow.get("id"):
                                        nid = create_author_with_user(int(it), urow.get("username") or f"user_{it}")
                                    else:
                                        debug(f"[DB][create_media_db] author identifier {it} not found in authors or users")
                                        continue
                            else:
                                nid = int(it)
                        elif isinstance(it, dict):
                            if it.get("id"):
                                nid = int(it.get("id"))
                            else:
                                name = it.get("name") or it.get("username") or it.get("performer")
                                if not name:
                                    continue
                                nid = create_dict_entry(table_name, str(name).strip())
                        else:
                            # string or other scalar
                            name = str(it).strip()
                            if not name:
                                continue
                            nid = create_dict_entry(table_name, name)

                        if nid and nid not in seen:
                            ids.append(nid)
                            seen.add(nid)
                    except Exception as e:
                        debug(f"[DB][create_media_db] normalization failed for table={table_name} item={it}: {e}")
                return ids

            # --- AUTHORS ---
            for author_id in _normalize_ids("authors", data.get("authors", [])):
                # avoid inserting duplicate relations without relying on a unique constraint
                cur.execute("""
                    INSERT INTO media_authors (media_id, author_id)
                    SELECT %s, %s
                    WHERE NOT EXISTS (SELECT 1 FROM media_authors WHERE media_id=%s AND author_id=%s);
                    """, (media_id, author_id, media_id, author_id))
                debug(f"[DB][AUTHOR] linked {author_id}")

            # --- PERFORMERS ---
            performer_ids = _normalize_ids("performers", data.get("performers", []))
            for performer_id in performer_ids:
                cur.execute("""
                    INSERT INTO media_performances (media_id, performer_id)
                    SELECT %s, %s
                    WHERE NOT EXISTS (SELECT 1 FROM media_performances WHERE media_id=%s AND performer_id=%s);
                    """, (media_id, performer_id, media_id, performer_id))
                debug(f"[DB][PERF] linked {performer_id}")

            # --- INSTRUMENTS ---
            try:
                instr_raw = prepared_data.get("instruments") if "instruments" in prepared_data else prepared_data.get("instruments_used")
                instr_ids = _normalize_ids("instruments", instr_raw)
                if instr_ids:
                    for pid in performer_ids:
                        cur.execute("SELECT id FROM media_performances WHERE media_id=%s AND performer_id=%s", (media_id, pid))
                        row = cur.fetchone()
                        perf_id = row[0] if row else None
                        if perf_id:
                            for iid in instr_ids:
                                cur.execute("INSERT INTO performance_instruments (performance_id, instrument_id) VALUES (%s,%s) ON CONFLICT DO NOTHING", (perf_id, iid))
                            debug(f"[DB][INST] attached instruments {instr_ids} to performer {pid}")
            except Exception as e:
                debug(f"[DB][INST] failed to attach instruments: {e}")

            # --- GENRES ---
            for genre_id in _normalize_ids("genres", data.get("genres", [])):
                cur.execute("""
                    INSERT INTO media_genres (media_id, genre_id)
                    SELECT %s, %s
                    WHERE NOT EXISTS (SELECT 1 FROM media_genres WHERE media_id=%s AND genre_id=%s);
                    """, (media_id, genre_id, media_id, genre_id))
                debug(f"[DB][GENRE] linked {genre_id}")

            # --- REFERENCES ---
            refs = data.get("references", [])
            if isinstance(refs, str):
                refs = [r.strip() for r in refs.split(",") if r.strip()]
            elif not isinstance(refs, (list, tuple)):
                refs = [refs]
            seen_refs = set()
            for ref in refs:
                try:
                    refid = int(ref)
                    if refid in seen_refs:
                        continue
                    cur.execute("""
                        INSERT INTO media_references (active_id, passive_id)
                        VALUES (%s,%s)
                        ON CONFLICT DO NOTHING;
                    """, (media_id, refid))
                    debug(f"[DB][REF] linked {refid}")
                    seen_refs.add(refid)
                except Exception as e:
                    debug(f"[DB][REF] skip invalid reference {ref}: {e}")

            # --- DOCUMENTI (solo se type=document) ---
            if data.get("type") == "document":
                cur.execute("""
                    INSERT INTO documents (media_id, format, pages)
                    VALUES (%s,%s,%s,%s)
                    ON CONFLICT DO NOTHING;
                """, (
                    media_id,
                    data.get("format"),
                    data.get("pages")
                ))
                debug(f"[DB][DOC] document for media_id={media_id}")

            # --- CONCERTI (sottoclasse di video) ---
            if data.get("type") == "concert":
                try:
                    cur.execute("""
                        INSERT INTO concerts (video_id, link, title, description)
                        VALUES (%s,%s,%s,%s)
                        ON CONFLICT (video_id) DO UPDATE SET link=EXCLUDED.link, title=EXCLUDED.title, description=EXCLUDED.description;
                    """, (
                        media_id,
                        data.get("link"),
                        data.get("title"),
                        data.get("description"),
                    ))
                    debug(f"[DB][CONCERT] concert for video_id={media_id}")
                except Exception as e:
                    debug(f"[DB][CONCERT] insert failed for video_id={media_id}: {e}")

                # If a link was provided, make sure media.linked_media includes a matching external link entry
                try:
                    link = data.get("link")
                    if link:
                        # read current linked_media
                        cur.execute("SELECT linked_media FROM media WHERE id=%s", (media_id,))
                        row = cur.fetchone()
                        existing = row[0] if row and row[0] else None
                        try:
                            lm = json.loads(existing) if existing else []
                        except Exception:
                            lm = []
                        if not isinstance(lm, list):
                            lm = [lm]
                        entry = {"type": "link", "source": ("youtube" if "youtube" in link.lower() else "external"), "url": link, "title": data.get("title")}
                        # avoid duplicates by url
                        if not any(isinstance(i, dict) and i.get("url") == link for i in lm):
                            lm.append(entry)
                            cur.execute("UPDATE media SET linked_media=%s WHERE id=%s", (json.dumps(lm), media_id))
                            debug(f"[DB][CONCERT] updated media.linked_media for media_id={media_id}")
                except Exception as e:
                    debug(f"[DB][CONCERT] updating linked_media failed: {e}")

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
            # For documents, join the documents table to get pages/format
            cur.execute(
                "SELECT m.*, COALESCE(d.pages, m.duration) as pages, d.format "
                "FROM media m "
                "LEFT JOIN documents d ON d.media_id = m.id "
                "WHERE m.id=%s;",
                (media_id,)
            )
            row = cur.fetchone()
            if not row:
                return None

            media = dict(row)

            # relazioni - fetch BOTH IDs and names/details from joined tables
            # Authors: fetch ID and name
            cur.execute(
                "SELECT ma.author_id, a.name as author_name FROM media_authors ma "
                "JOIN authors a ON a.id = ma.author_id WHERE ma.media_id=%s;",
                (media_id,)
            )
            author_rows = cur.fetchall()
            media["authors"] = [r["author_id"] for r in author_rows]
            media["author_names"] = [r["author_name"] for r in author_rows]

            # Performers: fetch ID and name
            cur.execute(
                "SELECT mp.performer_id, p.name as performer_name FROM media_performances mp "
                "JOIN performers p ON p.id = mp.performer_id WHERE mp.media_id=%s;",
                (media_id,)
            )
            performer_rows = cur.fetchall()
            media["performers"] = [r["performer_id"] for r in performer_rows]
            media["performer_names"] = [r["performer_name"] for r in performer_rows]

            # Genres: fetch ID and name
            cur.execute(
                "SELECT mg.genre_id, g.name as genre_name FROM media_genres mg "
                "JOIN genres g ON g.id = mg.genre_id WHERE mg.media_id=%s;",
                (media_id,)
            )
            genre_rows = cur.fetchall()
            media["genres"] = [r["genre_id"] for r in genre_rows]
            media["tags"] = [r["genre_name"] for r in genre_rows]  # "tags" is the display-ready field

            cur.execute("SELECT passive_id FROM media_references WHERE active_id=%s;", (media_id,))
            media["references"] = [r["passive_id"] for r in cur.fetchall()]

            # CRITICAL FIX: Fill year from recording_date if year is None
            if media.get("year") is None and media.get("recording_date") is not None:
                try:
                    from datetime import date
                    rec_date = media["recording_date"]
                    if isinstance(rec_date, date):
                        media["year"] = rec_date.year
                    elif isinstance(rec_date, str):
                        # try to parse string like '2021-02-04'
                        media["year"] = int(rec_date.split("-")[0])
                except Exception as e:
                    debug(f"[WARNING][fetch_media_db] Failed to extract year from recording_date: {e}")

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
            query = ("SELECT m.*, COALESCE(array_agg(g.name) FILTER (WHERE g.name IS NOT NULL), ARRAY[]::text[]) AS genres "
                     "FROM media m "
                     "LEFT JOIN media_genres mg ON mg.media_id = m.id "
                     "LEFT JOIN genres g ON g.id = mg.genre_id "
                     "WHERE TRUE")
            params = []

            if media_type:
                query += " AND m.type=%s"
                params.append(media_type)

            # Apply advanced search/filter logic
            if filter_by and filter_by != "all":
                fb = filter_by.lower()
            else:
                fb = (filter_by or "all").lower()

            # helper to split multi-terms (comma-separated)
            def split_terms(s):
                if not s or not isinstance(s, str):
                    return []
                parts = [p.strip() for p in s.split(",") if p.strip()]
                return parts if parts else [s]

            if fb == "title" or fb == "name":
                query += " AND m.title ILIKE %s"
                params.append(f"%{search}%")

            elif fb == "tag":
                fb = "genres" # for coherence with db
                # match genre names or IDs (accept comma-separated list)
                terms = split_terms(search)
                sub_clauses = []
                for t in terms:
                    if t.isdigit():
                        sub_clauses.append("EXISTS(SELECT 1 FROM media_genres mg JOIN genres g ON g.id=mg.genre_id WHERE mg.media_id = m.id AND g.id = %s)")
                        params.append(int(t))
                    else:
                        sub_clauses.append("EXISTS(SELECT 1 FROM media_genres mg JOIN genres g ON g.id=mg.genre_id WHERE mg.media_id = m.id AND g.name ILIKE %s)")
                        params.append(f"%{t}%")
                if sub_clauses:
                    query += " AND (" + " OR ".join(sub_clauses) + ")"

            elif fb == "date":
                import re, datetime
                s = str(search or "").strip()
                # accept YEAR, YEAR-MONTH or YEAR-MONTH-DAY first
                m = re.match(r"^(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?$", s)
                if m:
                    y = int(m.group(1))
                    mm = m.group(2)
                    dd = m.group(3)
                    if mm is None:
                        start = datetime.datetime(y,1,1)
                        end = datetime.datetime(y+1,1,1)
                        extra_match = str(y)
                        query += " AND ((m.created_at >= %s AND m.created_at < %s) OR to_char(m.created_at,'YYYY') = %s)"
                        params.extend([start, end, extra_match])
                    elif dd is None:
                        month = int(mm)
                        if month == 12:
                            start = datetime.datetime(y,month,1)
                            end = datetime.datetime(y+1,1,1)
                        else:
                            start = datetime.datetime(y,month,1)
                            end = datetime.datetime(y,month+1,1)
                        extra_match = f"{y:04d}-{month:02d}"
                        query += " AND ((m.created_at >= %s AND m.created_at < %s) OR to_char(m.created_at,'YYYY-MM') = %s)"
                        params.extend([start, end, extra_match])
                    else:
                        start = datetime.datetime(y,int(mm),int(dd))
                        end = start + datetime.timedelta(days=1)
                        extra_match = f"{y:04d}-{int(mm):02d}-{int(dd):02d}"
                        query += " AND ((m.created_at >= %s AND m.created_at < %s) OR to_char(m.created_at,'YYYY-MM-DD') = %s)"
                        params.extend([start, end, extra_match])
                    debug(f"[DEBUG][fetch_all_media_db] date filter range {start} - {end} (search={search})")
                else:
                    # try several ISO / common timestamp formats (handle trailing Z, T, microseconds etc.)
                    parsed = None
                    # try robust fromisoformat with minor normalization
                    try:
                        s2 = s.replace('T', ' ').replace('Z', '+00:00')
                        dt = datetime.datetime.fromisoformat(s2)
                        # if tz-aware, convert to UTC naive for comparison
                        if dt.tzinfo:
                            try:
                                dt = dt.astimezone(datetime.timezone.utc).replace(tzinfo=None)
                            except Exception:
                                dt = dt.replace(tzinfo=None)
                        parsed = dt
                    except Exception:
                        parsed = None
                    # fallback to strptime variants
                    if parsed is None:
                        for fmt in ("%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
                            try:
                                dt = datetime.datetime.strptime(s, fmt)
                                parsed = dt
                                break
                            except Exception:
                                continue
                    if parsed:
                        dt = parsed
                        if ":" not in s and "T" not in s:
                            start = datetime.datetime(dt.year, dt.month, dt.day)
                            end = start + datetime.timedelta(days=1)
                            query += " AND (m.created_at >= %s AND m.created_at < %s)"
                            params.extend([start, end])
                        else:
                            start = dt
                            end = start + datetime.timedelta(seconds=1)
                            query += " AND (m.created_at >= %s AND m.created_at < %s)"
                            params.extend([start, end])
                        debug(f"[DEBUG][fetch_all_media_db] parsed timestamp match {start} - {end} (search={search})")
                    else:
                        # fallback to title/description match if date parsing fails
                        query += " AND (m.title ILIKE %s OR m.description ILIKE %s)"
                        params.extend([f"%{search}%", f"%{search}%"])
            elif fb == "publisher":
                # match uploader username or id
                if str(search or "").isdigit():
                    query += " AND m.user_id = %s"
                    params.append(int(search))
                else:
                    query += " AND EXISTS(SELECT 1 FROM users u WHERE u.id = m.user_id AND u.username ILIKE %s)"
                    params.append(f"%{search}%")

            elif fb == "author":
                # match authors by name or user_id, allow comma-separated list
                # require ALL provided author terms to be present (match both authors)
                terms = split_terms(search)
                sub_clauses = []
                for t in terms:
                    if t.isdigit():
                        sub_clauses.append("EXISTS(SELECT 1 FROM media_authors ma JOIN authors a ON a.id=ma.author_id WHERE ma.media_id = m.id AND a.user_id = %s)")
                        params.append(int(t))
                    else:
                        sub_clauses.append("EXISTS(SELECT 1 FROM media_authors ma JOIN authors a ON a.id=ma.author_id WHERE ma.media_id = m.id AND a.name ILIKE %s)")
                        params.append(f"%{t}%")
                if sub_clauses:
                    query += " AND (" + " AND ".join(sub_clauses) + ")"

            elif fb == "performer":
                # match performers by name or user id
                # require ALL provided performer terms to be present (match multiple performers)
                terms = split_terms(search)
                sub_clauses = []
                for t in terms:
                    if t.isdigit():
                        sub_clauses.append("EXISTS(SELECT 1 FROM media_performances mp JOIN performers p ON p.id=mp.performer_id WHERE mp.media_id = m.id AND p.user_id = %s)")
                        params.append(int(t))
                    else:
                        sub_clauses.append("EXISTS(SELECT 1 FROM media_performances mp JOIN performers p ON p.id=mp.performer_id WHERE mp.media_id = m.id AND p.name ILIKE %s)")
                        params.append(f"%{t}%")
                if sub_clauses:
                    query += " AND (" + " AND ".join(sub_clauses) + ")"

            elif fb == "instrument":
                # match instruments via performance_instruments -> instruments
                # ALSO check concert segments (concerts -> concert_segments -> concert_segment_instruments)
                terms = split_terms(search)
                sub_clauses = []
                for t in terms:
                    # instruments attached to regular media performances
                    sub_clauses.append("EXISTS(SELECT 1 FROM media_performances mp JOIN performance_instruments pi ON pi.performance_id = mp.id JOIN instruments i ON i.id = pi.instrument_id WHERE mp.media_id = m.id AND i.name ILIKE %s)")
                    params.append(f"%{t}%")
                    # instruments attached to concert segments for concert-type media
                    sub_clauses.append("EXISTS(SELECT 1 FROM concerts c JOIN concert_segments cs ON cs.concert_id = c.video_id JOIN concert_segment_instruments csi ON csi.segment_id = cs.id JOIN instruments i ON i.id = csi.instrument_id WHERE c.video_id = m.id AND i.name ILIKE %s)")
                    params.append(f"%{t}%")
                if sub_clauses:
                    query += " AND (" + " OR ".join(sub_clauses) + ")"

            elif fb == "file":
                query += " AND (m.stored_at ILIKE %s)"
                params.extend([f"%{search}%"])

            else:
                # default: 'all' — broad match across common fields and relations
                or_parts = ["m.title ILIKE %s", "m.description ILIKE %s", "m.stored_at ILIKE %s", "EXISTS(SELECT 1 FROM users u WHERE u.id = m.user_id AND u.username ILIKE %s)"]
                params.extend([f"%{search}%"] * 4)
                # genres
                or_parts.append("EXISTS(SELECT 1 FROM media_genres mg JOIN genres g ON g.id=mg.genre_id WHERE mg.media_id = m.id AND g.name ILIKE %s)")
                params.append(f"%{search}%")
                # authors
                or_parts.append("EXISTS(SELECT 1 FROM media_authors ma JOIN authors a ON a.id=ma.author_id WHERE ma.media_id = m.id AND a.name ILIKE %s)")
                params.append(f"%{search}%")
                # performers
                or_parts.append("EXISTS(SELECT 1 FROM media_performances mp JOIN performers p ON p.id=mp.performer_id WHERE mp.media_id = m.id AND p.name ILIKE %s)")
                params.append(f"%{search}%")
                # instruments (performances)
                or_parts.append("EXISTS(SELECT 1 FROM media_performances mp JOIN performance_instruments pi ON pi.performance_id = mp.id JOIN instruments i ON i.id = pi.instrument_id WHERE mp.media_id = m.id AND i.name ILIKE %s)")
                params.append(f"%{search}%")
                # instruments referenced inside concert segments (concert media)
                or_parts.append("EXISTS(SELECT 1 FROM concerts c JOIN concert_segments cs ON cs.concert_id = c.video_id JOIN concert_segment_instruments csi ON csi.segment_id = cs.id JOIN instruments i ON i.id = csi.instrument_id WHERE c.video_id = m.id AND i.name ILIKE %s)")
                params.append(f"%{search}%")

                query += " AND (" + " OR ".join(or_parts) + ")"

            # if filter_by selected a type, also ensure type matches
            if filter_by and filter_by != "all" and filter_by in ("audio","song","video","document","concert"):
                query += " AND m.type=%s"
                params.append(filter_by)

            query += " GROUP BY m.id ORDER BY m.created_at DESC OFFSET %s LIMIT %s;"
            params.extend([offset, limit])

            cur.execute(query, tuple(params))
            rows = cur.fetchall()
            if not rows:
                return []

            result = [dict(r) for r in rows]
            
            # CRITICAL FIX: Fill year from recording_date if year is None for all rows
            try:
                from datetime import date
                for item in result:
                    if item.get("year") is None and item.get("recording_date") is not None:
                        rec_date = item["recording_date"]
                        if isinstance(rec_date, date):
                            item["year"] = rec_date.year
                        elif isinstance(rec_date, str):
                            # try to parse string like '2021-02-04'
                            item["year"] = int(rec_date.split("-")[0])
            except Exception as e:
                debug(f"[WARNING][fetch_all_media_db] Failed to extract year from recording_date: {e}")
            
            return result

    except Exception as e:
        debug(f"[ERROR][fetch_all_media_db] {e}")
        return []
    finally:
        if conn:
            connection.close(None, conn)

def update_media_db(media_id: int, updates: Dict[str, Any]) -> bool:
    """
    Update media record, preserving existing values for fields not explicitly provided.
    CRITICAL FIXES:
    1. Filter out None values to prevent overwriting with NULL
    2. Convert date strings to proper datetime objects
    3. Serialize linked_media to JSON string
    4. Skip relational fields (handled separately)
    """
    conn = None
    try:
        # CRITICAL FIX 1: Skip None values to preserve existing data
        # Only include fields that are explicitly set (not None)
        filtered_updates = {}
        for k, v in updates.items():
            if v is None:
                debug(f"[DB][update_media_db] Skipping None value for field '{k}' to preserve existing data")
                continue
            filtered_updates[k] = v
        
        # CRITICAL FIX 2: Skip relational fields (handled separately via relation tables)
        RELATIONAL_FIELDS = {"authors", "performers", "genres", "references"}
        for rel_field in RELATIONAL_FIELDS:
            if rel_field in filtered_updates:
                debug(f"[DB][update_media_db] Skipping relational field '{rel_field}' - must be updated via relation tables")
                del filtered_updates[rel_field]

        if not filtered_updates:
            debug(f"[DB][update_media_db] No non-None fields to update for id={media_id}")
            return True

        # CRITICAL FIX 3: Convert date strings to datetime objects
        DATE_FIELDS = {"recording_date", "concert_date", "created_at"}
        for date_field in DATE_FIELDS:
            if date_field in filtered_updates and filtered_updates[date_field] is not None:
                val = filtered_updates[date_field]
                if isinstance(val, str):
                    try:
                        # Try ISO format first (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)
                        if "T" in val:
                            filtered_updates[date_field] = datetime.fromisoformat(val)
                        else:
                            filtered_updates[date_field] = datetime.strptime(val, "%Y-%m-%d")
                        debug(f"[DB][update_media_db] Converted date string '{val}' to datetime for field '{date_field}'")
                    except Exception as e:
                        debug(f"[DB][update_media_db] Failed to convert date string '{val}' for field '{date_field}': {e}")
                        # Leave as-is if conversion fails, DB will handle or error appropriately
                elif not isinstance(val, datetime):
                    debug(f"[DB][update_media_db] Date field '{date_field}' is not string or datetime: {type(val)}")

        # CRITICAL FIX 4: Ensure linked_media is serialized when passing to DB
        if 'linked_media' in filtered_updates and filtered_updates['linked_media'] is not None:
            lm_val = filtered_updates['linked_media']
            if isinstance(lm_val, (dict, list)):
                try:
                    filtered_updates['linked_media'] = json.dumps(lm_val)
                    debug(f"[DB][update_media_db] Serialized linked_media to JSON")
                except Exception:
                    filtered_updates['linked_media'] = str(lm_val)
                    debug(f"[DB][update_media_db] Converted linked_media to string")

        debug(f"[DB][update_media_db] id={media_id}, filtered_updates={filtered_updates}")
        conn = connection.connect()
        with conn.cursor() as cur:
            set_clause = ", ".join(f"{k}=%s" for k in filtered_updates.keys())
            params = list(filtered_updates.values()) + [media_id]
            cur.execute(f"UPDATE media SET {set_clause} WHERE id=%s;", params)
        conn.commit()
        debug(f"[DB][update_media_db] success id={media_id}")
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
# COMMENTS CRUD
# =====================
def create_comment_db(user_id: int, text: str, media_id: Optional[int] = None,
                        parent_comment_id: Optional[int] = None) -> Optional[int]:
    conn = connection.connect()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            # Controllo se l'utente esiste
            user_row = fetch_one("SELECT id FROM users WHERE id=%s", (user_id,))
            if not user_row:
                #print(f"[create_comment_db] User id={user_id} does not exist!")
                return None
            fields = ["user_id", "text"]
            values = [user_id, text]

            # Controllo se il media esiste
            if media_id is not None:
                media_row = fetch_one("SELECT id FROM media WHERE id=%s", (media_id,))
                if not media_row:
                    #print(f"[create_comment_db] Media id={media_id} does not exist!")
                    return None
                fields.append("media_id")
                values.append(media_id)

            # Controllo se il commento parent esiste
            if parent_comment_id is not None:
                parent_row = fetch_one("SELECT id FROM comments WHERE id=%s", (parent_comment_id,))
                if not parent_row:
                    #print(f"[create_comment_db] Parent comment id={parent_comment_id} does not exist!")
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
                #print(f"[create_comment_db] No ID returned after insert")
                return None

    except Exception as e:
        if conn: conn.rollback()
        #print(f"[DB ERROR create_comment_db]: {e}")
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

def fetch_comment_replies_db(parent_comment_id: int) -> List[Dict[str, Any]]:
    replies = fetch_all("SELECT * FROM comments WHERE parent_comment_id=%s ORDER BY id ASC", (parent_comment_id,))
    return replies

def update_comment_db(comment_id: int, field: str, value: Any) -> bool:
    try:
        result = execute(f"UPDATE comments SET {field}=%s WHERE id=%s", (value, comment_id))
        return result
    except Exception as e:
        #print(f"[update_comment_db] Error while updating comment_id={comment_id}: {e}")
        return False

def delete_comment_db(comment_id: int) -> bool:
    try:
        result = execute("DELETE FROM comments WHERE id=%s", (comment_id,))
        return result
    except Exception as e:
        #print(f"[delete_comment_db] Error while deleting comment_id={comment_id}: {e}")
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
            # Normalize and strip name to avoid duplicates caused by leading/trailing whitespace
            norm_name = name.strip() if isinstance(name, str) else name
            # Case-insensitive lookup to prevent duplicates like 'Science' vs 'science'
            cur.execute(f"SELECT id FROM {table} WHERE lower(name) = lower(%s) FOR UPDATE", (norm_name,))
            row = cur.fetchone()
            if row:
                return row[0]
            # not present -> insert and commit so other connections can see it
            cur.execute(f"INSERT INTO {table} (name) VALUES (%s) RETURNING id", (norm_name,))
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
    # Case-insensitive lookup and strip whitespace to match create_dict_entry normalization
    if not isinstance(name, str):
        return fetch_one(f"SELECT * FROM {table} WHERE name=%s", (name,))
    norm_name = name.strip()
    return fetch_one(f"SELECT * FROM {table} WHERE lower(name)=lower(%s)", (norm_name,))

def fetch_dict_entry(table: str, name: str) -> Optional[Dict[str, Any]]:
    return fetch_dict_entry_by_name(table, name)

def fetch_all_dict_entries(table: str) -> List[Dict[str, Any]]:
    # Order case-insensitively for consistent listing
    return fetch_all(f"SELECT * FROM {table} ORDER BY lower(name)")

# ---------------------
# PERFORMER helpers
# ---------------------
def get_performer_by_user_id(user_id: int) -> Optional[Dict[str, Any]]:
    """Return performer row for a given user_id if exists."""
    return fetch_one("SELECT id, name, user_id FROM performers WHERE user_id=%s", (user_id,))

def create_performer_with_user(user_id: int, name: str) -> Optional[int]:
    """Try to create a performer row for a given user. If a performer with the
    same name exists return it; otherwise insert name and user_id and return id."""
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor() as cur:
            try:
                cur.execute("INSERT INTO performers (name, user_id) VALUES (%s,%s) RETURNING id", (name, user_id))
                new = cur.fetchone()
                conn.commit()
                return new[0] if new else None
            except Exception:
                # possibly name already exists -> try to fetch by name
                cur.execute("SELECT id FROM performers WHERE name=%s", (name,))
                row = cur.fetchone()
                if row:
                    return row[0]
                return None
    except Exception as e:
        if conn:
            conn.rollback()
        debug(f"[DB ERROR create_performer_with_user]: {e}")
        return None
    finally:
        if conn:
            connection.close(None, conn)

# ---------------------
# INSTRUMENT helpers
# ---------------------
def get_instrument_by_name(name: str) -> Optional[Dict[str, Any]]:
    """Return instrument row for a given name if exists."""
    return fetch_one("SELECT id, name FROM instruments WHERE lower(name)=lower(%s)", (name.strip(),))

def create_instrument(name: str) -> Optional[int]:
    """Try to create an instrument row with the given name. If an instrument with the
    same name exists return it; otherwise insert and return new id."""
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor() as cur:
            try:
                cur.execute("INSERT INTO instruments (name) VALUES (%s) RETURNING id", (name.strip(),))
                new = cur.fetchone()
                conn.commit()
                return new[0] if new else None
            except Exception:
                # possibly name already exists -> try to fetch by name
                cur.execute("SELECT id FROM instruments WHERE lower(name)=lower(%s)", (name.strip(),))
                row = cur.fetchone()
                if row:
                    return row[0]
                return None
    except Exception as e:
        if conn:
            conn.rollback()
        debug(f"[DB ERROR create_instrument]: {e}")
        return None
    finally:
        if conn:
            connection.close(None, conn)

# ---------------------
# AUTHOR helpers
# ---------------------
def get_author_by_user_id(user_id: int) -> Optional[Dict[str, Any]]:
    """Return author row for a given user_id if exists."""
    return fetch_one("SELECT id, name, user_id FROM authors WHERE user_id=%s", (user_id,))

def create_author_with_user(user_id: int, name: str) -> Optional[int]:
    """Create an author row linked to a user. If an author with same user_id
    exists return it; if insertion by (name,user_id) fails, try to find by user_id or name."""
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor() as cur:
            try:
                cur.execute("INSERT INTO authors (name, user_id) VALUES (%s,%s) RETURNING id", (name, user_id))
                new = cur.fetchone()
                conn.commit()
                return new[0] if new else None
            except Exception:
                # fallback: check by user_id first
                cur.execute("SELECT id FROM authors WHERE user_id=%s", (user_id,))
                row = cur.fetchone()
                if row:
                    return row[0]
                # fallback: check by name
                cur.execute("SELECT id FROM authors WHERE name=%s", (name,))
                row = cur.fetchone()
                if row:
                    return row[0]
                return None
    except Exception as e:
        if conn:
            conn.rollback()
        debug(f"[DB ERROR create_author_with_user]: {e}")
        return None
    finally:
        if conn:
            connection.close(None, conn)

def get_or_create_performer_for_user(user_id: int, username: str) -> Optional[int]:
    """Ensure a performer entry exists for a given user_id and return performer id."""
    if not user_id:
        return None
    existing = get_performer_by_user_id(user_id)
    if existing and existing.get("id"):
        return existing["id"]
    # fallback try insert using username as name
    try:
        pid = create_performer_with_user(user_id, username)
        return pid
    except Exception as e:
        debug(f"[DB][performer] failed to create performer for user {user_id}: {e}")
        return None

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
        SELECT m.id, m.title, m.year, m.description, m.linked_media, d.format, d.pages, d.media_id
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
        SELECT m.id, m.title, m.year, m.description, m.linked_media,
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

def get_commented_medias_db(user_id: int) -> List[Dict[str, Any]]:
    query = """
        SELECT DISTINCT m.*, u.username
        FROM media m
        JOIN comments c ON c.media_id = m.id
        JOIN users u ON u.id = m.user_id
        WHERE c.user_id = %s
        ORDER BY m.created_at DESC
    """
    return fetch_all(query, (user_id,))

# =====================
# CONCERTS & SEGMENTS CRUD
# =====================
def create_concert_db(media_id: int, link: Optional[str] = None, title: Optional[str] = None, description: Optional[str] = None) -> bool:
    """Insert a row in concerts referencing the provided media_id (video)."""
    if not media_id:
        return False
    return execute("""
        INSERT INTO concerts (video_id, link, title, description)
        VALUES (%s,%s,%s,%s)
        ON CONFLICT (video_id) DO UPDATE SET link=EXCLUDED.link, title=EXCLUDED.title, description=EXCLUDED.description;
    """, (media_id, link, title, description))

def fetch_concert_by_video_id(video_id: int) -> Optional[Dict[str, Any]]:
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("SELECT * FROM concerts WHERE video_id=%s", (video_id,))
            row = cur.fetchone()
            if row:
                return dict(row)
            return None
    except Exception as e:
        debug(f"[ERROR][fetch_concert_by_video_id] {e}")
        return None
    finally:
        if conn:
            connection.close(None, conn)

def create_concert_segment_db(concert_id: int, media_id: Optional[int] = None, song_title: Optional[str] = None,
                              start_time: Optional[float] = None, end_time: Optional[float] = None,
                              comment: Optional[str] = None, performers: Optional[list] = None,
                              instruments: Optional[list] = None) -> Optional[int]:
    """Create a concert segment and optionally link performers/instruments. Returns segment_id."""
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO concert_segments (concert_id, media_id, song_title, start_time, end_time, comment)
                VALUES (%s,%s,%s,%s,%s,%s) RETURNING id
            """, (concert_id, media_id, song_title, start_time, end_time, comment))
            row = cur.fetchone()
            seg_id = row[0] if row else None
            if not seg_id:
                conn.commit()
                return None

            # performers
            if performers:
                for pid in performers:
                    try:
                        cur.execute("INSERT INTO concert_segment_performers (segment_id, performer_id) VALUES (%s,%s) ON CONFLICT DO NOTHING", (seg_id, pid))
                    except Exception as e:
                        debug(f"[DB][create_concert_segment] performer link failed: {e}")

            # instruments
            if instruments:
                for iid in instruments:
                    try:
                        cur.execute("INSERT INTO concert_segment_instruments (segment_id, instrument_id) VALUES (%s,%s) ON CONFLICT DO NOTHING", (seg_id, iid))
                    except Exception as e:
                        debug(f"[DB][create_concert_segment] instrument link failed: {e}")

            conn.commit()
            return seg_id
    except Exception as e:
        if conn:
            conn.rollback()
        debug(f"[ERROR][create_concert_segment_db] {e}")
        return None
    finally:
        if conn:
            connection.close(None, conn)

def fetch_concert_segments_db(concert_id: int) -> List[Dict[str, Any]]:
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("SELECT * FROM concert_segments WHERE concert_id=%s ORDER BY start_time NULLS FIRST", (concert_id,))
            rows = cur.fetchall()
            result = []
            for r in rows:
                seg = dict(r)
                # performers with names
                cur.execute("SELECT p.id as performer_id, p.name FROM concert_segment_performers csp JOIN performers p ON p.id = csp.performer_id WHERE csp.segment_id=%s", (seg['id'],))
                seg['performers'] = [dict(r) for r in cur.fetchall()]
                # instruments with names
                cur.execute("SELECT i.id as instrument_id, i.name FROM concert_segment_instruments csi JOIN instruments i ON i.id = csi.instrument_id WHERE csi.segment_id=%s", (seg['id'],))
                seg['instruments'] = [dict(r) for r in cur.fetchall()]
                result.append(seg)
            return result
    except Exception as e:
        debug(f"[ERROR][fetch_concert_segments_db] {e}")
        return []
    finally:
        if conn:
            connection.close(None, conn)

def update_concert_segment_db(segment_id: int, updates: Dict[str, Any]) -> bool:
    if not updates:
        return True
    # allowed keys
    allowed = {'media_id', 'song_title', 'start_time', 'end_time', 'comment'}
    set_items = {k: v for k, v in updates.items() if k in allowed}
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor() as cur:
            if set_items:
                set_clause = ", ".join(f"{k}=%s" for k in set_items.keys())
                params = list(set_items.values()) + [segment_id]
                cur.execute(f"UPDATE concert_segments SET {set_clause} WHERE id=%s", tuple(params))

            # update performers/instruments if provided
            if 'performers' in updates:
                cur.execute("DELETE FROM concert_segment_performers WHERE segment_id=%s", (segment_id,))
                for pid in updates['performers'] or []:
                    cur.execute("INSERT INTO concert_segment_performers (segment_id, performer_id) VALUES (%s,%s) ON CONFLICT DO NOTHING", (segment_id, pid))
            if 'instruments' in updates:
                cur.execute("DELETE FROM concert_segment_instruments WHERE segment_id=%s", (segment_id,))
                for iid in updates['instruments'] or []:
                    cur.execute("INSERT INTO concert_segment_instruments (segment_id, instrument_id) VALUES (%s,%s) ON CONFLICT DO NOTHING", (segment_id, iid))

            conn.commit()
            return True
    except Exception as e:
        if conn:
            conn.rollback()
        debug(f"[ERROR][update_concert_segment_db] {e}")
        return False
    finally:
        if conn:
            connection.close(None, conn)

def delete_concert_segment_db(segment_id: int) -> bool:
    return execute("DELETE FROM concert_segments WHERE id=%s", (segment_id,))

# =====================
# NOTES
# =====================
def create_note_db(user_id: int, media_id: int, note_start: float, note_end: float, type: bool = True, text: Optional[str] = None, stored_at: Optional[str] = None, private: bool = False, page: Optional[int] = None, A_point: Optional[str] = None, B_point: Optional[str] = None) -> Optional[int]:
    """Insert a note and return the new note id, or None on failure."""
    conn = None

    # Coerce 'type' to a proper boolean since DB column is BOOLEAN
    try:
        if isinstance(type, bool):
            type_val = type
        else:
            try:
                type_val = bool(int(type))
            except Exception:
                s = str(type).strip().lower() if type is not None else ''
                type_val = s in ('true', 't', '1', 'yes', 'y')
    except Exception:
        type_val = True

    try:
        conn = connection.connect()
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO notes (
                        user_id,
                        media_id,
                        "note_start",
                        "note_end",
                        "type",
                        "text",
                        "stored_at",
                        "private",
                        "page",
                        "A_point",
                        "B_point"
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id""",
                        (user_id, media_id, note_start, note_end, type_val, text, stored_at, private, page, A_point, B_point))
            new_id = cur.fetchone()[0]
            conn.commit()
            return new_id
    except Exception as e:
        debug(f"[ERROR][create_note_db] {e}")
        if conn:
            conn.rollback()
        return None

def fetch_note_db(user_id: int, media_id: int):
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("""
                SELECT id, note_start, note_end, type, text, stored_at, private, page, A_point, B_point
                FROM notes
                WHERE media_id=%s
                AND (user_id=%s OR private=false)
                """, (media_id, user_id))
            rows = cur.fetchall()
        return [dict(r) for r in rows]
    except Exception as e:
        print (f"[ERROR][fetch_notes_db] {e}")
        return []
    finally:
        if conn:
            connection.close(None, conn)

def update_note_db(note_id: int, start: Optional[float] = None, end: Optional[float] = None, text: Optional[str] = None, private: Optional[bool] = None, stored_at: Optional[str] = None, page: Optional[int] = None, A_point: Optional[str] = None, B_point: Optional[str] = None) -> bool:
    """Update provided fields on a note. Only non-None args are updated."""
    conn = None
    try:
        updates = []
        params = []
        if start is not None:
            updates.append("start=%s"); params.append(start)
        if end is not None:
            updates.append("\"end\"=%s"); params.append(end)
        if text is not None:
            updates.append("\"text\"=%s"); params.append(text)
        if private is not None:
            updates.append("\"private\"=%s"); params.append(private)
        if stored_at is not None:
            updates.append("\"stored_at\"=%s"); params.append(stored_at)
        if page is not None:
            updates.append("page=%s"); params.append(page)
        if A_point is not None:
            updates.append("A_point=%s"); params.append(A_point)
        if B_point is not None:
            updates.append("B_point=%s"); params.append(B_point)
        if not updates:
            return True  # nothing to do

        set_clause = ", ".join(updates)
        params.append(note_id)

        conn = connection.connect()
        with conn.cursor() as cur:
            cur.execute(f"UPDATE notes SET {set_clause} WHERE id=%s", tuple(params))
            conn.commit()
            return True
    except Exception as e:
        #print(f"[ERROR][update_note_db] {e}")
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            connection.close(None, conn)

def delete_note_db(note_id: int):
    conn = None
    try:
        conn = connection.connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM notes WHERE id=%s", (note_id,))
            conn.commit()
            return True
    except Exception as e:
        #print(f"[ERROR][delete_note_db] {e}")
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            connection.close(None, conn)

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
    #print(f"[DEBUG] get_user_id_by_username called with: {username}")
    row = fetch_one("SELECT id FROM users WHERE username=%s", (username,))
    #print(f"[DEBUG] fetch_one returned: {row}")
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
    """Get list of users that user_id is following."""
    sql = """
        SELECT u.id, u.username, u.mail
        FROM users u
        JOIN user_follow uf ON u.id = uf.followed_id
        WHERE uf.follower_id = %s
    """
    return fetch_all(sql, (user_id,))

def db_get_followers(user_id: int) -> List[Dict[str, Any]]:
    """Get list of users who are following user_id."""
    sql = """
        SELECT u.id, u.username, u.mail
        FROM users u
        JOIN user_follow uf ON u.id = uf.follower_id
        WHERE uf.followed_id = %s
    """
    return fetch_all(sql, (user_id,))

def db_count_followers(user_id: int) -> int:
    """Count how many users are following this user (followers_count)."""
    row = fetch_one("SELECT COUNT(*) as cnt FROM user_follow WHERE followed_id = %s", (user_id,))
    return row['cnt'] if row else 0

def db_count_following(user_id: int) -> int:
    """Count how many users this user is following (followed_count)."""
    row = fetch_one("SELECT COUNT(*) as cnt FROM user_follow WHERE follower_id = %s", (user_id,))
    return row['cnt'] if row else 0

def db_count_user_publications(user_id: int) -> int:
    """Count how many media (publications) a user has created."""
    row = fetch_one("SELECT COUNT(*) as cnt FROM media WHERE user_id = %s", (user_id,))
    return row['cnt'] if row else 0

# last line