# first line

from flask import Blueprint, render_template
startpage = Blueprint('startpage', __name__)

@startpage.route('/')
def index():
    return render_template('index.html')


# last line