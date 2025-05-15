# obj comment

class Commento:

    def __init__(self, id, user_data, comment_data, file_data):
        self.id = id # id del commento UNIVOCO
        self.user_data = user_data # dizionario coi dati dell'utente da qui si prende l'id e l'username
        self.comment_data = comment_data # dizionario coi dati del commento - contiene i dati
        self.file_data = file_data # dizionario coi dati dei file, video, musica o documento - ne recuper l'id

    def __str__(self):
        return f"{self}"

def pubblish(self):
    p()
    # pubblish a comment

def delete(self):
    rm()
    # delete a comment

def segment(self):
    segment()
    # delimita istante di inizio
    # delinea istante di fine
    # if delta t < 1 segna il singolo istante

def previous_leaf(self):
    pl()
    # punta all'id del nodo precedente da cui dipende

def react(self):
    r()
    # like or dislike a comment -> just increases or decreases an int
    # also can report comment

def set_font(self):
    sf()



# last line