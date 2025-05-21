# user obj

from werkzeug.security import generate_password_hash, check_password_hash

class User:

    def __init__(self, id, mail, username, password, birthday, bio, profile_pic, hashed=False):
        self.id = id
        self.mail = mail
        self.username = username
        # se la password non è hashata la hasha - thummbs up emoji
        self.password_hash = password if hashed else generate_password_hash(password)
        self.birthday = birthday
        self.bio = bio
        self.profile_pic = profile_pic

    # serve a stampare bene gli obj (in questo caso lo username)
    def __str__(self):
        return f"User({self.username})"

    # serve per verificare che \la pswd coicnida con quella hashata
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # per la stampa o l'ottenimento di qualunque dato
    def user_dict(self):
        return {
            "id": self.id,
            "mail": self.mail,
            "username": self.username,
            "password": self.password_hash,
            "birthday": self.birthday,
            "bio": self.bio,
            "profile_pic": self.profile_pic
        }

    # Metodi azione
    # per ora sono solo placeholders
    def pubblish_file(self):
        pf()

    def comment(self):
        c()

    def note(self):
        n()

    def register(self):
        r()

    def logout(self):
        lout()

    def login(self):
        lin()

    def report(self):
        repo()

    def remove(self):
        rm()

    def edit_profile(self):
        epo()

# last line