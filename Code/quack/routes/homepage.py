# first line

from flask import Blueprint, render_template, request, redirect, url_for, session
from quack.services.user_service import get_logged_in_user  # Importa il servizio

home_bp = Blueprint('home', __name__, url_prefix='/home')

# modulo per la schermata home
@home_bp.route('/', methods=['GET', 'POST'])
def home():
    user = get_logged_in_user(session)
    if not user:
        return redirect(url_for('auth.login'))

    form_type = request.args.get('form_type', '')  # prendi il parametro dalla query string

    return render_template('homepage.html', user=user, form_type=form_type)


# last line