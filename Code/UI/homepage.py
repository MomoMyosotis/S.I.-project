# first line

from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)
    user_data = {}

    @app.route('/')
    def home():
        return render_template("login.html")

    @app.route('/submit', methods=['POST'])
    def submit():
        username = request.form['username']
        password = request.form['password']
        user_data['username'] = username
        user_data['password'] = password
        return f"Login successful! Benvenuto {username}"


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


# last line