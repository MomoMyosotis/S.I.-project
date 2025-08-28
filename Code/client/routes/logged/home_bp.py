# first line

from flask import Blueprint, render_template, request

home_bp = Blueprint('home', __name__, url_prefix='/home')

@home_bp.route('/', methods=['GET'])
def homepage():
    # Qui setti il form_type di default come 'homepage'
    form_type = request.args.get('form_type', 'home')
    return render_template('home.html', form_type=form_type)

# Eventuali route secondarie per feed, profile, libraries
@home_bp.route('/feed', methods=['GET'])
def feed():
    return render_template('home.html', form_type='feed')

@home_bp.route('/profile', methods=['GET'])
def profile():
    return render_template('home.html', form_type='profile')

@home_bp.route('/libraries', methods=['GET'])
def libraries():
    return render_template('home.html', form_type='libraries')

# last line