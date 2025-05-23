# first line

from werkzeug.security import check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from quack.services.auth_service import (
    load_users,
    login_user,
    register_new_user,
    recover_password,
    contact_assistance
)

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# modulo di login
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form.get('identifier')
        password = request.form.get('password')

        user = login_user(identifier, password)
        if user:
            session['user_id'] = user.email
            flash('Login effettuato con successo!', 'success')
            return redirect(url_for('home.home'))
        else:
            flash('Credenziali non valide, riprova.', 'danger')

    return render_template('login.html')

# modulo di registrazione
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
            return render_template('registration.html')

        success, msg = register_new_user(email, username, password, birthday)
        if success:
            flash("Registrazione avvenuta con successo, puoi fare il login!", "success")
            return redirect(url_for('auth.login'))
        else:
            flash(msg or "Errore nella registrazione", "danger")

    return render_template('registration.html')

# modulo di recupero credenziali
@auth_bp.route('/recover', methods=['GET', 'POST'])
def recover():
    if request.method == 'POST':
        identifier = request.form.get('identifier')
        success = recover_password(identifier)
        if success:
            flash("Link per reset password inviato (debug: guarda console)", "info")
        else:
            flash("Utente non trovato", "warning")

    return render_template('recover_pswd.html')

# modulo per contattare l'assistenza
@auth_bp.route('/assistance', methods=['GET', 'POST'])
def assistance():
    if request.method == 'POST':
        user_info = request.form.get('user_info')
        issue = request.form.get('issue')
        success = contact_assistance(user_info, issue)
        if success:
            flash("Assistance has been contacted on your behalf, please be patient", "info")
        else:
            flash("An error has occurred.\nERROR 82", "warning")
    return render_template('assistance.html')

# moduo per il logout
@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Sei stato disconnesso.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/submit', methods=['POST'])
def submit_login():
    data = request.get_json() if request.is_json else request.form
    username = data.get("username")
    password = data.get("password")

    print(url_for('home.home'))  # Verifica che la rotta sia corretta
    print(session)  # Mostra la sessione per il debug
    print(f"Redirecting to: {url_for('home.home')}")

    # Controllo login
    user = login_user(username, password)  # Non passare 'session' qui

    if user:
        print("Login OK")

        # salva utente in sessione
        session['user_id'] = user.email

        if request.is_json:
            return jsonify({"success":True, "Message":"Login Successful"})
        else:
            # Redirezione alla homepage
            return redirect(url_for('home.home'))
    else:
        if request.is_json:
            return jsonify({"Success": False, "message":"Username or password wrong"})
        else:
            print("Login FALLITO")
            return redirect(url_for("auth.login"))


# last line