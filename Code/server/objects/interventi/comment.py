# obj comment

from datetime import datetime
from typing import Optional, Dict, Any, List
from objects.users.root import Root
from db.db_crud import (
                        fetch_relations,
                        create_intervention_db,
                        fetch_interventions_db,
                        update_intervention_db,
                        fetch_media_db,
                        delete_intervention_db
)

class Comment:
    def __init__(self,
                id: Optional[int] = None,
                user_id: Optional[int] = None,
                media_id: Optional[int] = None,
                note_id: Optional[int] = None,
                parent_comment_id: Optional[int] = None,
                text: str = "",
                like_count: int = 0,
                dislike_count: int = 0):
        """
        Inizializza un oggetto Comment con i campi provenienti dalla tabella SQL.
        """
        self.id = id
        self.user_id = user_id
        self.media_id = media_id
        self.note_id = note_id
        self.parent_comment_id = parent_comment_id
        self.text = text
        self.like_count = like_count
        self.dislike_count = dislike_count

    def to_dict(self) -> Dict[str, Any]:
        """
        Serializza l'oggetto Comment in un dizionario (utile per API/JSON).
        """
        return {
            "id": self.id,
            "user_id": self.user_id,
            "media_id": self.media_id,
            "note_id": self.note_id,
            "parent_comment_id": self.parent_comment_id,
            "text": self.text,
            "like_count": self.like_count,
            "dislike_count": self.dislike_count
        }

    @classmethod
    def add_comment(user_id: int, media_id: int, content: str, parent_id: Optional[int] = None) -> Optional[int]:
        """
        Aggiunge un commento e imposta automaticamente i flag:
            - is_author = True se l'utente è autore della canzone
            - is_performer = True se l'utente è tra gli interpreti
            """
        # Controllo autore
        authors = fetch_relations("song_authors", "song_id", media_id)
        is_author = any(a["author_id"] == user_id for a in authors)

        # Controllo performer
        performers = fetch_relations("song_performances", "song_id", media_id)
        is_performer = any(p["performer_id"] == user_id for p in performers)

        now = datetime.now()
        fields = ('user_id', 'media_id', 'parent_id', 'content', 'is_author', 'is_performer', 'created_at')
        values = (user_id, media_id, parent_id, content, is_author, is_performer, now)

        comment_id = create_intervention_db("comments", fields, values)
        return comment_id

    @classmethod
    def fetch_comments(media_id: int) -> List[Dict[str, Any]]:
        # Recupera tutti i commenti su un media, aggiungendo flag autore/interprete
        comments = fetch_interventions_db("comments", "media_id", media_id, order_by="created_at ASC")

        # fetch relazioni per questo media
        authors = {a["author_id"] for a in fetch_relations("song_authors", "song_id", media_id)}
        performers = {p["performer_id"] for p in fetch_relations("song_performances", "song_id", media_id)}

        for c in comments:
            c["is_author"] = c["user_id"] in authors
            c["is_performer"] = c["user_id"] in performers

        return comments

    @classmethod
    def update_comment(user_id: int, comment_id: int, new_content: str) -> bool:
        comment = fetch_interventions_db("comments", "id", comment_id)
        if not comment:
            return False
        owner_id = comment[0]["user_id"]
        if not Root.can_manage_content(user_id, owner_id):
            raise PermissionError("Non hai i permessi per modificare questo commento")
        return update_intervention_db("comments", comment_id, "content", new_content)

    @classmethod
    def delete_comment(user_id: int, comment_id: int) -> bool:
        comment = fetch_interventions_db("comments", "id", comment_id)
        if not comment:
            return False
        owner_id = comment[0]["user_id"]
        media = fetch_media_db(comment[0]["media_id"], "songs", ["user_id"])
        if not media:
            return False
        media_owner_id = media["user_id"]
        if not Root.can_manage_content(user_id, owner_id) and user_id != media_owner_id:
            raise PermissionError("Non hai i permessi per cancellare questo commento")
        return delete_intervention_db("comments", comment_id)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Comment":
        """
        Crea un'istanza di Comment da un dizionario.
        """
        return cls(
            id=data.get("id"),
            user_id=data.get("user_id"),
            media_id=data.get("media_id"),
            note_id=data.get("note_id"),
            parent_comment_id=data.get("parent_comment_id"),
            text=data.get("text"),
            like_count=data.get("like_count", 0),
            dislike_count=data.get("dislike_count", 0)
        )


# last line