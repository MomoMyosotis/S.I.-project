# first line

# models/user.py

class User:
    def __init__(self, id, username, email, password, birthday, password_hash=None):
        self.id = id
        self.username = username
        self.birthday = birthday
        self.email = email
        if password_hash:  # Se esiste una password hashata, usa quella
            self.password_hash = password_hash
        else:
            self.password = password  # Altrimenti, usa la password in chiaro

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True  # Consideriamo l'utente sempre autenticato per il momento

    def is_active(self):
        return True

    def is_anonymous(self):
        return False



# last line