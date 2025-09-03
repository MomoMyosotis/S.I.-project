# first line
from typing import Optional, Dict, Any, List
from server.db import db_crud

# =====================
# CONFIGURAZIONE TABELLE
# =====================
INTERVENTION_TABLES = {
    "note": "notes",
    "comment": "comments"
}

# =====================
# CREATE INTERVENTION
# =====================
def create_intervention(intervention_type: str,
                        author_id: int,
                        target_id: int,
                        content: str,
                        note_id: Optional[int] = None,
                        extra_fields: Optional[Dict[str, Any]] = None) -> Optional[int]:
    """
    Crea un intervento (note o comment) nel DB.
    - target_id: media_id per commenti o song_id per note
    - note_id: opzionale, solo se il comment è su una nota
    - extra_fields: dizionario per campi opzionali (solo note)
    """
    table = INTERVENTION_TABLES.get(intervention_type)
    if not table:
        db_crud.debug(f"create_intervention: tipo sconosciuto {intervention_type}")
        return None

    extra_fields = extra_fields or {}

    if intervention_type == "note":
        # campi extra supportati per note
        fields = ["x_coord", "y_coord", "start_time", "end_time", "solos", "rhythm", "link"]
        values = [extra_fields.get(f) for f in fields]
        query = f"""
            INSERT INTO notes (song_id, comment, {','.join(fields)})
            VALUES (%s, %s, {','.join(['%s']*len(fields))})
            RETURNING id
        """
        row = db_crud.fetch_one(query, (target_id, content, *values))
    elif intervention_type == "comment":
        # parent_comment_id opzionale
        parent_id = extra_fields.get("parent_comment_id")
        media_id = target_id if note_id is None else None
        query = """
            INSERT INTO comments (user_id, media_id, note_id, parent_comment_id, text)
            VALUES (%s, %s, %s, %s, %s) RETURNING id
        """
        row = db_crud.fetch_one(query, (author_id, media_id, note_id, parent_id, content))
    else:
        return None

    return row.get("id") if row else None

# =====================
# FETCH INTERVENTIONS
# =====================
def fetch_interventions(intervention_type: str,
                        target_id: int,
                        note_id: Optional[int] = None,
                        threaded: bool = False) -> List[Dict[str, Any]]:
    """
    Restituisce lista di interventi (note/commenti).
    - threaded: se True, organizza commenti in annidamento
    """
    table = INTERVENTION_TABLES.get(intervention_type)
    if not table:
        db_crud.debug(f"fetch_interventions: tipo sconosciuto {intervention_type}")
        return []

    if intervention_type == "note":
        return db_crud.fetch_all(f"SELECT * FROM notes WHERE song_id=%s ORDER BY start_time ASC", (target_id,))
    elif intervention_type == "comment":
        rows = db_crud.fetch_all(f"SELECT * FROM comments WHERE note_id=%s ORDER BY id ASC", (note_id,)) if note_id \
            else db_crud.fetch_all(f"SELECT * FROM comments WHERE media_id=%s ORDER BY id ASC", (target_id,))

        if threaded:
            return _build_comment_thread(rows)
        return rows
    return []

# =====================
# THREADING COMMENTI
# =====================
def _build_comment_thread(comments: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Organizza i commenti annidati in struttura ad albero.
    """
    tree = []
    lookup = {c['id']: {**c, "replies": []} for c in comments}

    for c in lookup.values():
        parent_id = c.get("parent_comment_id")
        if parent_id and parent_id in lookup:
            lookup[parent_id]["replies"].append(c)
        else:
            tree.append(c)
    return tree

# =====================
# UPDATE INTERVENTION
# =====================
def update_intervention(intervention_type: str,
                        intervention_id: int,
                        requester_id: int,
                        content: str) -> bool:
    """
    Aggiorna contenuto solo se chi invia è l'autore.
    """
    table = INTERVENTION_TABLES.get(intervention_type)
    if not table:
        db_crud.debug(f"update_intervention: tipo sconosciuto {intervention_type}")
        return False

    row = db_crud.fetch_one(f"SELECT * FROM {table} WHERE id=%s", (intervention_id,))
    if not row:
        return False

    author_id = row.get("user_id") or row.get("author_id")
    if author_id != requester_id:
        db_crud.debug(f"update_intervention: permesso negato per user {requester_id}")
        return False

    column = "text" if intervention_type == "comment" else "comment"
    return db_crud.execute(f"UPDATE {table} SET {column}=%s WHERE id=%s", (content, intervention_id))

# =====================
# CONTROLLI PERMESSI INTERVENTION
# =====================

def can_edit_or_delete_intervention(intervention_type: str,
                                    intervention_id: int,
                                    requester_id: int,
                                    requester_lvl: int) -> bool:
    """
    Controlla se l'utente requester_id può modificare/eliminare l'intervento.
    - Permesso se autore dell'intervento
    - Permesso se autore del media/song collegato
    - Permesso se admin con lvl >= autore
    """
    table = INTERVENTION_TABLES.get(intervention_type)
    if not table:
        return False

    row = db_crud.fetch_one(f"SELECT * FROM {table} WHERE id=%s", (intervention_id,))
    if not row:
        return False

    author_id = row.get("user_id") or row.get("author_id")
    if author_id == requester_id:
        return True  # autore dell'intervento

    # controlla se requester è autore del media/song collegato
    media_author_id = None
    if intervention_type == "comment":
        media_id = row.get("media_id")
        note_id = row.get("note_id")
        if media_id:
            media_row = db_crud.fetch_one("SELECT author_id FROM media WHERE id=%s", (media_id,))
            media_author_id = media_row.get("author_id") if media_row else None
        elif note_id:
            note_row = db_crud.fetch_one("SELECT song_id FROM notes WHERE id=%s", (note_id,))
            song_id = note_row.get("song_id") if note_row else None
            if song_id:
                song_row = db_crud.fetch_one("SELECT user_id FROM songs WHERE id=%s", (song_id,))
                media_author_id = song_row.get("user_id") if song_row else None

    elif intervention_type == "note":
        song_id = row.get("song_id")
        if song_id:
            song_row = db_crud.fetch_one("SELECT user_id FROM songs WHERE id=%s", (song_id,))
            media_author_id = song_row.get("user_id") if song_row else None

    if media_author_id == requester_id:
        return True  # autore del media/songs

    # livello admin
    author_row = db_crud.fetch_one("SELECT lvl FROM users WHERE id=%s", (author_id,))
    author_lvl = author_row.get("lvl") if author_row else -1
    if requester_lvl > author_lvl:
        return True  # admin superiore

    return False

# =====================
# DELETE INTERVENTION CON PERMESSI
# =====================
def delete_intervention(intervention_type: str,
                        intervention_id: int,
                        requester_id: int,
                        requester_lvl: int) -> bool:
    """
    Elimina intervento se:
    - autore
    - autore del media/songs collegato
    - admin con livello >= autore
    """
    if not can_edit_or_delete_intervention(intervention_type, intervention_id, requester_id, requester_lvl):
        db_crud.debug(f"delete_intervention: permesso negato per user {requester_id}")
        return False

    table = INTERVENTION_TABLES.get(intervention_type)
    return db_crud.execute(f"DELETE FROM {table} WHERE id=%s", (intervention_id,))


# last line