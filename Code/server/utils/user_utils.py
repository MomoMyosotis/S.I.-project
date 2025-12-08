# first line

from typing import Dict, Any, List, Optional
from server.objects.users.root import Root
from server.objects.media.media import Media
from server.db.db_crud import (
    create_relation,
    delete_relation,
    fetch_relations,
    create_dict_entry,
    delete_dict_entry,
    fetch_all_dict_entries,
    db_get_following,
    db_get_followers,
)

# =====================
# FOLLOWERS / FOLLOWED
# =====================

def get_followers(user_id: int) -> list[dict]:
    print(f"[DEBUG] get_followers called with user_id={user_id} (type={type(user_id)})")
    followers = db_get_followers(user_id)
    print(f"[DEBUG] raw followers: {followers}")
    return followers

def get_followed(user_id: int) -> list[dict]:
    print(f"[DEBUG] get_followed called with user_id={user_id} (type={type(user_id)})")
    followed = db_get_following(user_id)
    print(f"[DEBUG] raw followed: {followed}")
    return followed

# =====================
# MEDIA
# =====================

def get_media(media_id: int) -> Optional[Media]:
    return Media.fetch(media_id)

def search_media(filters: Dict[str, Any]) -> List[Media]:
    return Media.advanced_media_search(filters)

# =====================
# RELAZIONI M:N GENERICHE
# =====================
def add_relation(table: str, key_names: tuple[str, str], values: tuple[int, int]) -> bool:
    return create_relation(table, key_names, values)

def remove_relation(table: str, conditions: Dict[str, Any]) -> bool:
    return delete_relation(table, conditions)

def get_relations(table: str, key: str, value: int) -> List[Dict[str, Any]]:
    return fetch_relations(table, key, value)

# =================
# HELPERS
# =================
def add_genre(media_id: int, genre_id: int) -> bool:
    return add_relation("media_genres", ("media_id", "genre_id"), (media_id, genre_id))

def remove_genre(media_id: int, genre_id: int) -> bool:
    return remove_relation("media_genres", {"media_id": media_id, "genre_id": genre_id})

def get_genres(media_id: int) -> List[Dict[str, Any]]:
    return get_relations("media_genres", "media_id", media_id)

def add_author(media_id: int, author_id: int) -> bool:
    return add_relation("media_authors", ("media_id", "author_id"), (media_id, author_id))

def remove_author(media_id: int, author_id: int) -> bool:
    return remove_relation("media_authors", {"media_id": media_id, "author_id": author_id})

def get_authors(media_id: int) -> List[Dict[str, Any]]:
    return get_relations("media_authors", "media_id", media_id)

def add_performer(media_id: int, performer_id: int) -> bool:
    return add_relation("media_performances", ("media_id", "performer_id"), (media_id, performer_id))

def remove_performer(media_id: int, performer_id: int) -> bool:
    return remove_relation("media_performances", {"media_id": media_id, "performer_id": performer_id})

def get_performers(media_id: int) -> List[Dict[str, Any]]:
    return get_relations("media_performances", "media_id", media_id)

# =====================
# INTERVENTI
# =====================
def get_commented_media(user_id: int) -> List[Media]:
    """Restituisce tutti i media su cui l'utente ha lasciato commenti o note (senza duplicati)."""
    all_media_ids = set()
    for table in ["comments", "notes"]:
        records = Media.fetch_interventions(table, "user_id", user_id)
        all_media_ids.update(r["media_id"] for r in records)

    return [Media.fetch(mid) for mid in all_media_ids if Media.fetch(mid)]

def search_user_comments(user_id: int, keyword: str) -> List[Dict[str, Any]]:
    """Cerca nei commenti di un utente."""
    all_comments = Media.fetch_interventions("comments", "user_id", user_id)
    return [c for c in all_comments if keyword.lower() in c["content"].lower()]

# =====================
# DIZIONARI / ENTRIES
# =====================
def add_dict_entry(table: str, name: str) -> Optional[int]:
    return create_dict_entry(table, name)

def add_entry(user_obj: Any, table: str, name: str) -> str:
    entry_id = create_dict_entry(table, name)
    return str(entry_id) if entry_id else "ERROR"

def remove_entry(user_obj: Any, table: str, entry_id: int) -> str:
    success = delete_dict_entry(table, entry_id)
    return "OK" if success else "ERROR"

def get_entries(user_obj: Any, table: str) -> List[Dict[str, Any]]:
    return fetch_all_dict_entries(table)

# =====================
# RICERCHE AVANZATE
# =====================
def search_song(user_obj: Any, **filters) -> List[Media]:
    return Root.advanced_song_search(filters)

def search_document(user_obj: Any, **filters) -> List[Media]:
    return Root.advanced_document_search(filters)

def search_video(user_obj: Any, **filters) -> List[Media]:
    return Root.advanced_video_search(filters)

# last line