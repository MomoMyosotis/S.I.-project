# first line

# fornisce interfaccia semplificata al resto dell'app

import json as J
import os
from flask import session
from quack.services.db import (
                                authenticate_user,
                                register_user,
                                send_password_reset,
                                load_users
                                )

FAKE_USER_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'users.json')

def load_users():
    # Carica utenti dal file JSON (debug o fallback)
    with open(FAKE_USER_PATH, 'r') as file:
        return J.load(file)

def login_user(identifier, password):
    user, err = authenticate_user(identifier, password)
    if user:
        session['user_id'] = user.email  # Salva l'ID dell'utente nella sessione
        print(f"User logged in: {user.email}")  # Log per verificare che l'ID venga impostato
    return user


def register_new_user(email, username, password, birthday):
    # Registra nuovo utente nel DB
    return register_user(email, username, password, birthday)

def recover_password(identifier):
    # Invia link di recupero password
    return send_password_reset(identifier)

def contact_assistance(identifier, problem):
    # Simula invio richiesta assistenza
    if not identifier or not problem:
        return False
    print(f"[ASSISTANCE REQUEST] From: {identifier} - Problem: {problem}")
    return True

def get_logged_in_user(session):

    # if logged -> return obj user
    # else -> return none

    user_id = session.get('user_id')  # get l'ID utente dalla sessione
    print(f"User ID in session: {user_id}")  # Aggiungi un log per vedere l'ID utente
    if user_id:
        users = load_users()  # Ottieni la lista degli utenti dal file JSON
        # Itera attraverso gli utenti per trovare quello con 'user_id'
        user = users.get(user_id)
        if user:
            print(f"User found: {user}")  # Log per vedere l'utente trovato
            return user  # Restituisci l'utente se trovato
    print("User not found or not logged in")  # Log quando l'utente non viene trovato
    return None

# last line