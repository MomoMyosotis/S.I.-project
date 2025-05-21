# first line


from flask import Blueprint, render_template, request, redirect, url_for, flash
# DECOMMENTARE riga sotto
# from flask_login import login_user, logout_user, login_required

# servizi per autenticazione, registrazione e pswd reset
from quack.services.auth_service import authenticate_user, register_user, send_password_reset, contact_assistance
# Importiamo il modello User, anche se non viene usato per ora
# from quack.models.user import User

# Creiamo un Blueprint per gestire le route relative all'autenticazione
auth_bp = Blueprint('auth', __name__)

# Route per la pagina di login
# Se la richiesta è GET, renderizziamo il modulo di login
# Se la richiesta è POST, verifichiamo se l'utente esiste e la password è corretta
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # Se è una richiesta POST, cioè l'utente ha inviato il form
        username = request.form.get('username')  # ottiene username
        password = request.form.get('password')  # ottiene password
        user = authenticate_user(username, password)  # Verifica credenziali usate
        if user:
            # = credentials corrette -> home page
            return redirect(url_for('startpage.index'))
        else:
            # = credentials wrong -> send error
            error = "Username o password errati"
            return render_template('login.html', error=error)  # Renderizziamo la pagina di login con l'errore
    return render_template('login.html')  # Se è una richiesta GET, renderizziamo il modulo di login

# Route per la registrazione
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':  # se POST, l'user sending modulo di registrazione
        email = request.form.get('email')  # get email
        username = request.form.get('username')  # get username
        password = request.form.get('password')  # get pswd
        birthday = request.form.get("birthday") # get birthdya

        # registration attempt
        success, error = register_user(email, username, password, birthday)
        if success:
            # Se la registrazione è riuscita, mostriamo un messaggio di successo
            flash("Registrazione riuscita! Effettua il login.")
            return redirect(url_for('auth.login'))  # Reindirizziamo alla pagina di login
        return render_template('registration.html', error=error)  # Se c'è un errore, lo mostriamo
    return render_template('registration.html')  # Se è una richiesta GET, mostriamo il modulo di registrazione

# Route per il recupero della password
# Se la richiesta è GET, renderizziamo il modulo di recupero
# Se la richiesta è POST, inviamo un link di reset password all'utente
@auth_bp.route('/recover', methods=['GET', 'POST'])
def recover():
    if request.method == 'POST':  # Se è una richiesta POST, l'utente sta inviando il modulo di recupero
        identifier = request.form.get('username_or_email')  # Otteniamo il nome utente o l'email
        success = send_password_reset(identifier)  # Proviamo a inviare il link di reset
        if success:
            # Se l'operazione ha avuto successo, informiamo l'utente che il link è stato inviato
            success ="New credentials sent to your mail!"
            return render_template("auth.login")
        else:
            # Se l'utente non è stato trovato, mostriamo un errore
            return render_template('recover_pswd.html', error="Utente non trovato")
    return render_template('recover_pswd.html')  # Se è una richiesta GET, renderizziamo il modulo di recupero

@auth_bp.route('/assistance', methods=['GET', 'POST'])
def assistance():
    if request.method == 'POST':
        identifier = request.form.get('username_or_email')
        problem = request.form.get('problem')
        success = contact_assistance(identifier, problem)
        if success:
            msg="Assistance has been contacted!"
            return render_template("auth.login",  form_type='assistance', success=msg)
        else:
            error = "an error occurred. please retry."
            return render_template("assistance.html", form_type='assistance', error=error)
    return render_template("assistance.html")

# Route per il logout
# Se l'utente è loggato, lo logout (ma non utilizziamo Flask-Login, quindi questa parte è semplificata)
@auth_bp.route('/logout')
# Commentiamo o rimuoviamo il decoratore @login_required perché non lo stiamo usando
# @login_required
def logout():
    # Commentiamo o rimuoviamo il logout_user() perché non stiamo usando Flask-Login
    # logout_user()
    return redirect(url_for('auth.login'))  # Reindirizziamo l'utente alla pagina di login dopo il logout

@auth_bp.route ('/')
def home():
    return render_template('home.html')


# last line