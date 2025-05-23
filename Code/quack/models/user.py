# first line

from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, username, email, password=None, birthday=None, password_hash=None):
        self.username = username
        self.birthday = birthday
        self.email = email
        if password_hash:  # Se esiste una password hashata, usa quella
            self.password_hash = password_hash
        elif password:
            self.password_hash = generate_password_hash(password)
        else:
            raise ValueError("Password or Hash needed to create an User")

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "birthday": self.birthday,
            "password_hash": self.password_hash
        }

    def get_username(self):
        return str(self.username)

    def is_authenticated(self):
        return True  # Consideriamo l'utente sempre autenticato per il momento

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

# last line