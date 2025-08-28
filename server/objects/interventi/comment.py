# obj comment

class Commento:

    def __init__(self, id, user_id, file_id, text, node, likes, dislikes):
        self.id = id # id del commento UNIVOCO
        self.user_id = user_id # dato un id recuper username
        self.file_id = file_id # dato l'id del file lega il commento al file
        self.text = text
        self.node = node # è l'id del commento a cui si riferisce (può essere NULL)
        self.likes = likes # è semplicemente un int che aumenta ad ogni utente che clicca il pulsante
        self.dislikes = dislikes # davvero? che pensi che sia?

    def __str__(self):
        return f"{self}"

    def comment_dict(self):
        return {
            "id del commento" : self.id,
            "utente che ha pubblicato il commento" : self.user_id,
            "file di riferimento" : self.file_id,
            "testo" : self.text,
            "nodo di riferimento" : self.node,
            "like count" : self.likes,
            "dislike count" : self.dislikes
        }

def pubblish(self):
    return "it's a placeholder server\objects\interventi\comment.\n"
    # pubblish a comment

def delete(self):
    return "it's a placeholder server\objects\interventi\comment.\n"
    # delete a comment

def segment(self):
    segment()
    # delimita istante di inizio
    # delinea istante di fine
    # if delta t < 1 segna il singolo istante
    return "it's a placeholder server\objects\interventi\comment.\n"

def previous_leaf(self):
    return "it's a placeholder server\objects\interventi\comment.\n"
    # punta all'id del nodo precedente da cui dipende

def react(self):
    return "it's a placeholder server\objects\interventi\comment.\n"
    # like or dislike a comment -> just increases or decreases an int
    # also can report comment

def set_font(self):
    return "it's a placeholder server\objects\interventi\comment.\n"

# last line