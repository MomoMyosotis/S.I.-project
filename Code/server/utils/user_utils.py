# first line

from typing import Dict, Any, List, Optional
from db.db_crud import (
                        fetch_media_db,
                        create_relation,
                        delete_relation,
                        fetch_relations,
                        create_dict_entry,
                        db_get_following,
                        db_get_followers
)
from objects.media.song import Song
from objects.media.media import Media
from objects.users.root import Root


def get_followers(user_id: int) -> list[dict]:

    print(f"[DEBUG] user_id is: {user_id} (type={type(user_id)})")
    followers = db_get_followers(user_id)
    print(f"[DEBUG] raw followers: {followers}")
    return followers

def get_followed(user_id: int) -> list[dict]:
    print(f"[DEBUG] user_id is: {user_id} (type={type(user_id)})")
    followed = db_get_following(user_id)
    print(f"[DEBUG] raw followed: {followed}")
    return followed

def get_media(media_id: int) -> Optional[Dict[str, Any]]:
    """Recupera media con eventuali dettagli."""
    return fetch_media_db(media_id)

def search_media(filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Ricerche avanzate sui media (autore, titolo, performer, genere)."""
    return Song.advanced_song_search(filters)

def add_genre_to_song(song_id: int, genre_id: int) -> bool:
    return create_relation("song_genres", ("song_id","genre_id"), (song_id, genre_id))

def remove_genre_from_song(song_id: int, genre_id: int) -> bool:
    return delete_relation("song_genres", {"song_id": song_id, "genre_id": genre_id})

def get_song_genres(song_id: int) -> List[Dict[str, Any]]:
    return fetch_relations("song_genres", "song_id", song_id)

def add_author_to_song(song_id: int, author_id: int) -> bool:
    return create_relation("song_authors", ("song_id","author_id"), (song_id, author_id))

def remove_author_from_song(song_id: int, author_id: int) -> bool:
    return delete_relation("song_authors", {"song_id": song_id, "author_id": author_id})

def get_song_authors(song_id: int) -> List[Dict[str, Any]]:
    return fetch_relations("song_authors", "song_id", song_id)

def add_performer_to_song(song_id: int, performer_id: int) -> bool:
    return create_relation("song_performances", ("song_id","performer_id"), (song_id, performer_id))

def remove_performer_from_song(song_id: int, performer_id: int) -> bool:
    return delete_relation("song_performances", {"song_id": song_id, "performer_id": performer_id})

def get_song_performers(song_id: int) -> List[Dict[str, Any]]:
    return fetch_relations("song_performances", "song_id", song_id)

def get_commented_media(user_id: int) -> List[Dict[str, Any]]:
    """Restituisce tutti i media su cui l'utente ha lasciato commenti o note (senza duplicati)."""
    all_media_ids = set()
    for table in ["comments", "notes"]:
        records = Media.fetch_interventions(table, "user_id", user_id)
        all_media_ids.update(r["media_id"] for r in records)

    return [m for m in (Media.fetch_media(mid) for mid in all_media_ids) if m]


def search_user_comments(user_id: int, keyword: str) -> List[Dict[str, Any]]:
    """Cerca nei commenti di un utente."""
    all_comments = Media.fetch_interventions("comments", "user_id", user_id)
    return [c for c in all_comments if keyword.lower() in c["content"].lower()]

def add_dict_entry(table: str, name: str) -> Optional[int]:
    return create_dict_entry(table, name)

# last line