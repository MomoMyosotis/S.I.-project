# first line
from typing import Optional, Dict, Any, List, Type
from datetime import datetime
from server.db import db_crud
from server.objects.media.media import Media
from server.objects.media.song import Song
from server.objects.media.document import Document
from server.objects.media.video import Video

# =====================
# CONFIGURAZIONE TABELLE
# =====================
MEDIA_CHILD_TABLES = {
    "song": {"table": "songs", "fields": ["duration", "location", "additional_info"], "class": Song},
    "document": {"table": "documents", "fields": ["format", "pages", "caption", "song_id"], "class": Document},
    "video": {"table": "videos", "fields": ["duration", "location", "additional_info", "director"], "class": Video}
}

# =====================
# CREATE MEDIA
# =====================
def create_media(obj: Media, requester_id: int, requester_lvl: int) -> Optional[int]:
    # in teoria chi crea è sempre autorizzato a se stesso, ma puoi inserire controlli extra
    if requester_lvl < 0:  # esempio controllo minimale
        db_crud.debug(f"create_media: permesso negato per user {requester_id}")
        return None

    media_type = obj.media_type()
    cfg = MEDIA_CHILD_TABLES.get(media_type)
    if not cfg:
        db_crud.debug(f"create_media: tipo sconosciuto {media_type}")
        return None

    child_table, child_fields = cfg["table"], cfg["fields"]
    data = obj.to_dict()

    # Inserimento nella tabella principale media
    query_main = """
        INSERT INTO media (type, title, author, author_id, year, description, link)
        VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id
    """
    values_main = (
        media_type,
        data.get('title'),
        data.get('author') or data.get('performer'),
        requester_id,
        data.get('year'),
        data.get('description'),
        data.get('link')
    )

    conn = None
    try:
        conn = db_crud.connection.connect()
        with conn.cursor() as cur:
            db_crud.debug(f"create_media: inserimento in media {values_main}")
            cur.execute(query_main, values_main)
            media_id = cur.fetchone()[0]

            if child_fields:
                values_child = [media_id] + [data.get(f) for f in child_fields]
                placeholders = ','.join(['%s'] * len(values_child))
                columns = ','.join(['id'] + child_fields)
                cur.execute(f"INSERT INTO {child_table} ({columns}) VALUES ({placeholders})", values_child)

            conn.commit()
            db_crud.debug(f"create_media: commit avvenuto per media {media_id}")
            return media_id
    except Exception as e:
        if conn:
            conn.rollback()
        db_crud.debug(f"[DB ERROR create_media {media_type}]: {e}")
        return None
    finally:
        if conn:
            db_crud.connection.close(None, conn)

# =====================
# FETCH MEDIA
# =====================
def fetch_media(media_type: str, media_id: int) -> Optional[Media]:
    cfg = MEDIA_CHILD_TABLES.get(media_type)
    if not cfg:
        db_crud.debug(f"fetch_media: tipo sconosciuto {media_type}")
        return None

    child_table, child_fields, cls = cfg["table"], cfg["fields"], cfg["class"]
    child_select = ','.join([f"{child_table}.{f}" for f in child_fields])
    query = f"""
        SELECT m.*, {child_select}
        FROM media m
        JOIN {child_table} ON {child_table}.id = m.id
        WHERE m.id=%s
    """
    row = db_crud.fetch_one(query, (media_id,))
    if row:
        return cls.from_dict(row)
    return None

# =====================
# UPDATE MEDIA CON PERMESSI
# =====================
def update_media(media_type: str, media_id: int, updates: Dict[str, Any], requester_id: int, requester_lvl: int) -> bool:
    if not can_edit_or_delete(media_id, requester_id, requester_lvl):
        db_crud.debug(f"update_media: permesso negato per user {requester_id}")
        return False

    cfg = MEDIA_CHILD_TABLES.get(media_type)
    if not cfg:
        db_crud.debug(f"update_media: tipo sconosciuto {media_type}")
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
        success &= db_crud.execute(f"UPDATE media SET {set_clause} WHERE id=%s", params)

    if child_updates:
        table = cfg["table"]
        set_clause = ", ".join(f"{k}=%s" for k in child_updates.keys())
        params = tuple(child_updates.values()) + (media_id,)
        success &= db_crud.execute(f"UPDATE {table} SET {set_clause} WHERE id=%s", params)

    return success

# =====================
# DELETE MEDIA CON PERMESSI
# =====================
def delete_media(media_type: str, media_id: int, requester_id: int, requester_lvl: int) -> bool:
    if not can_edit_or_delete(media_id, requester_id, requester_lvl):
        db_crud.debug(f"delete_media: permesso negato per user {requester_id}")
        return False

    cfg = MEDIA_CHILD_TABLES.get(media_type)
    if not cfg:
        db_crud.debug(f"delete_media: tipo sconosciuto {media_type}")
        return False

    table = cfg["table"]
    success = db_crud.execute(f"DELETE FROM {table} WHERE id=%s", (media_id,))
    success &= db_crud.execute(f"DELETE FROM media WHERE id=%s", (media_id,))
    return success

# =====================
# LIBRERIA LIFO (storia media)
# =====================

class MediaLibrary:
    """
    Libreria personale dei media per utente, persistente nel DB.
    Ordine LIFO basato sul timestamp di aggiunta.
    """

    def __init__(self, user_id: int):
        self.user_id = user_id

    def add(self, media_id: int) -> bool:
        """
        Aggiunge un media alla libreria dell'utente.
        Se già presente, non lo aggiunge di nuovo.
        """
        existing = db_crud.fetch_one(
            "SELECT 1 FROM UserMediaLibrary WHERE user_id=%s AND media_id=%s",
            (self.user_id, media_id)
        )
        if existing:
            return True  # già presente, non serve reinserire

        query = """
            INSERT INTO UserMediaLibrary (user_id, media_id, added_at)
            VALUES (%s, %s, %s)
        """
        return db_crud.execute(query, (self.user_id, media_id, datetime.now()))

    def pop_last(self) -> Optional[int]:
        """
        Rimuove e ritorna l'ultimo media aggiunto (LIFO).
        """
        row = db_crud.fetch_one(
            "SELECT media_id FROM UserMediaLibrary WHERE user_id=%s ORDER BY added_at DESC LIMIT 1",
            (self.user_id,)
        )
        if not row:
            return None

        media_id = row["media_id"]
        db_crud.execute(
            "DELETE FROM UserMediaLibrary WHERE user_id=%s AND media_id=%s",
            (self.user_id, media_id)
        )
        return media_id

    def all_ids(self) -> List[int]:
        """
        Ritorna tutti gli ID dei media della libreria dell'utente in ordine LIFO.
        """
        rows = db_crud.fetch_all(
            "SELECT media_id FROM UserMediaLibrary WHERE user_id=%s ORDER BY added_at DESC",
            (self.user_id,)
        )
        return [r["media_id"] for r in rows]

# =====================
# PERMESSI
# =====================
def can_edit_or_delete(media_id: int, requester_id: int, requester_lvl: int) -> bool:
    row = db_crud.fetch_one("SELECT author_id FROM media WHERE id=%s", (media_id,))
    if not row:
        return False

    creator_id = row.get("author_id")
    if creator_id == requester_id:
        return True

    creator_row = db_crud.fetch_one("SELECT lvl FROM users WHERE id=%s", (creator_id,))
    creator_lvl = creator_row.get("lvl") if creator_row else -1
    if requester_lvl > creator_lvl:
        return True

    return False

# last  line