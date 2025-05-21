# first line

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash
from quack.services.db import authenticate_user, register_user, send_password_reset

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form.get('identifier')  # email o username
        password = request.form.get('password')

        user = authenticate_user(identifier, password)
        if user:
            session['user_id'] = user.email  # o un altro ID univoco
            flash('Login effettuato con successo!', 'success')
            return redirect(url_for('homepage.index'))
        else:
            flash('Credenziali non valide, riprova.', 'danger')

    return render_template('auth_login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        birthday = request.form.get("birthday")

        if password != password_confirm:
            flash("Le password non coincidono", "warning")
            return render_template('auth_register.html')

        success, msg = register_user(email, username, password, birthday)
        if success:
            flash("Registrazione avvenuta con successo, puoi fare il login!", "success")
            return redirect(url_for('auth.login'))
        else:
            flash(msg or "Errore nella registrazione", "danger")

    return render_template('auth_register.html')

@auth_bp.route('/recover', methods=['GET', 'POST'])
def recover():
    if request.method == 'POST':
        identifier = request.form.get('identifier')  # email o username
        success = send_password_reset(identifier)
        if success:
            flash("Link per reset password inviato (debug: guarda console)", "info")
        else:
            flash("Utente non trovato", "warning")

    return render_template('auth_recover.html')

def contact_assistance(identifier, problem):
    """
    Funzione che simula l'invio di una richiesta di assistenza.
    Puoi qui implementare la logica per salvare la richiesta su DB,
    inviare un'email o qualsiasi altra cosa serva.
    """
    if not identifier or not problem:
        return False

    # Per ora solo stampa di debug
    print(f"[ASSISTANCE REQUEST] From: {identifier} - Problem: {problem}")

    # Simula successo sempre
    return True

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Sei stato disconnesso.', 'info')
    return redirect(url_for('auth.login'))

# last line