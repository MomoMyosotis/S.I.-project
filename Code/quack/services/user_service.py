# first line

# routes/homepage.py

from flask import Blueprint, render_template, redirect, url_for, flash, session
from quack.services.auth_service import get_logged_in_user  # Importa il servizio

home_bp = Blueprint('home', __name__, url_prefix='/home')

# modulo per la schermata home
@home_bp.route('/', methods=['GET', 'POST'])
def home():
    user = get_logged_in_user(session)  # Usa il servizio per ottenere l'utente loggato
    if not user:
        return redirect(url_for('auth.login'))  # Se l'utente non è loggato, fai il redirect al login

    # La pagina della home che mostra feed, profilo, ecc.
    return render_template('homepage.html', user=user)  # Passa l'utente alla template

# last line