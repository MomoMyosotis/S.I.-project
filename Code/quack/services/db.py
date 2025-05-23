# first line

from werkzeug.security import generate_password_hash, check_password_hash
from quack.models.user import User
import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'users.json')

# Caricamento utenti da file
def load_users():
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        raw = json.load(f)
        return {email: User(**data) for email, data in raw.items()}

def save_users(users):
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        serializable = {email: user.to_dict() for email, user in users.items()}
        json.dump(serializable, f, indent=2)

# Dizionario utenti in memoria
fake_users_db = load_users()

def authenticate_user(username_or_email, password):
    user = get_user_by_email_or_username(username_or_email)
    if user and check_password_hash(user.password_hash, password):
        return user, None
    return None, "Username o password errati"

def register_user(email, username, password):
    if email in fake_users_db or any(u.username == username for u in fake_users_db.values()):
        return False, "Email o username già in uso"
    hashed = generate_password_hash(password)
    new_user = User(email=email, username=username, password_hash=hashed)
    fake_users_db[email] = new_user
    save_users(fake_users_db)
    return True, None

def send_password_reset(identifier):
    user = get_user_by_email_or_username(identifier)
    if user:
        return True
    return False

def get_user_by_email_or_username(identifier):
    for user in fake_users_db.values():
        if user.email == identifier or user.username == identifier:
            return user
    return None

# last line