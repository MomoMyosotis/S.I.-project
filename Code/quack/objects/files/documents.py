# obj document

class Document:

    def __init__(self, doc_name, author, year, link, media_id, didascalia, user_id):
        self.doc_name = doc_name
        self.author = author
        self.year = year
        self.link = link
        self.media_id = media_id
        self.didascalia = didascalia
        self.user_id = user_id

    def __str__(self):
        return f"{self}"

    def doc_dict(self):
        return {
            "document's name" : self.doc_name,
            "pubblished by" : self.user_id,
            "document's author" : self.author,
            "pubblication year" : self.year,
            "external link" : self.link,
            "related media" : self.media_id,
            "additional data" : self.didascalia
            }

# method

def view(self):
    v(self)

def share(self):
    s(self)

def add_note(self):
    # calls the function of he note obj
    d(self)

def change_data(self):
    # tipo titolo didascalia o il file stesso
    c(self)

def report(self):
    r(self)

def delete(self):
    d(self)

# last line