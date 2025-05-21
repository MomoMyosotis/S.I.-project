# obj song

class Song:

    def __init__(self, id, user_id, media_name, title, durata, authors, id_generi, year, esecutore, strumenti, location, file_id, ulteriori_info):
        self.id = id
        self.user_id = user_id
        self.media_name = media_name
        self.title = title
        self.durata = durata
        self.authors = authors
        self.id_generi = id_generi
        self.year = year
        self.esecutore = esecutore
        self.strumenti = strumenti
        self.location = location
        self.file_id = file_id
        self.ulteriori_info = ulteriori_info

    def __str__(self):
        return f"{self}"

    def song_dict(self):
        return {
            "song id" : self.id,
            "user' username" : self.user_id,
            "media name" : self.media_name,
            "song's title" : self.title,
            "song's lenght" : self.durata,
            "song's authors" : self.authors,
            "genres" : self.id_generi,
            "pubblication year" : self.year,
            "song's executor" : self.esecutore,
            "instruments" : self.strumenti,
            "location" : self.location,
            "file allegato" : self.file_id,
            "extra info" : self.ulteriori_info
        }

# method
def play(self):
    p(self)

def stop(self):
    s(self)

def rewind(self):
    r(self)

def pull_data(self):
    p(self)

def report(self):
    r(self)

def share(self):
    s(self)

def add_to_playlist(self):
    atp(self)

# last line