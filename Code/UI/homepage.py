from flask import Flask, render_template, request, redirect, url_for

fake_users_db = {
    "user@example.com": {"username": "user", "password": "password123"},
    "admin@example.com": {"username": "admin", "password": "admin123"}
}

# Funzione per inviare un link di reset della password (simulato)
def send_reset_link(email):
    # Qui andrebbe la logica per inviare effettivamente un'email
    # In questa simulazione, stampiamo semplicemente l'email.
    print(f"Reset link sent to {email}")

def create_app():
    app = Flask(__name__)
    user_data = {}

    # Route per la home/login
    @app.route('/')
    def home():
        return render_template("login.html")

    # Route per il login
    @app.route('/submit', methods=['POST'])
    def submit():
        username = request.form['username']
        password = request.form['password']
        user_data['username'] = username
        user_data['password'] = password
        return f"Login successful! Welcome ^^ {username}"

    @app.route('/recover_password', methods=['GET', 'POST'])
    def recover_password():
        if request.method == 'POST':
            username_or_email = request.form['username_or_email']
            user = fake_users_db.get(username_or_email)
            if user:
                send_reset_link(username_or_email)
                return render_template('recover pswd.html', success=True)
            else:
                return render_template('recover pswd.html', success=False, error="User not found")
        return render_template('recover pswd.html', success=False)



    # Route per la registrazione
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            mail = request.form['mail']
            username = request.form['username']
            password = request.form['password']
            birthday = request.form['birthday']
            bio = request.form.get('bio', '')

            # profile_pic richiede gestione file, per ora ignoro o la salvi in locale
            profile_pic = request.files.get('profile_pic')

            # Qui potresti fare controllo, salvataggio su DB o file JSON
            # Per esempio solo salva in user_data (non sicuro ma per demo)
            user_data[username] = {
                'mail': mail,
                'password': password,
                'birthday': birthday,
                'bio': bio,
                # profile_pic da gestire meglio, ma per ora ignoriamo
            }

            return f"Registrazione completata per {username}! Torna al <a href='{url_for('home')}'>login</a>"

        return render_template('registration.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
