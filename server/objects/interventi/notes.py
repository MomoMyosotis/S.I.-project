# obj nota

class Note:
    def __init__(self, id, user_id, file_id, coordinate, istanti, assoli, esecutori, strumenti, ritmo, link, commento):
        self.id = id
        self.user_id = user_id
        self.file_id = file_id
        self.coordinate = coordinate
        self.istanti = istanti
        self.assoli = assoli
        self.esecutori = esecutori
        self.strumenti = strumenti
        self.ritmo = ritmo
        self.link = link
        self.commento = commento

    def __str__(self):
        return f"{self}"

    def note_dict(self):
        return {
            "id della nota" : self.id,
            "username dell'utente che ha pubbblicato la nota" : self.user_id,
            "file di riferimento" : self.file_id,
            "coordinate della nota" : self.coordinate,
            "istanti" : self.istanti,
            "assolo" : self.assoli,
            "esecutore" : self.esecutori,
            "strumenti" : self.strumenti,
            "rythm" : self.ritmo,
            "external link" : self.link,
            "commento" : self.commento

        }