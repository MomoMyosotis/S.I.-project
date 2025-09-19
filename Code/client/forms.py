#first line

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class Login(FlaskForm):
    username = StringField("Username or Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

class Register(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    birthday = DateField("Birthday", validators=[DataRequired()])

class Recover(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])

class Assistance(FlaskForm):
    identifier = StringField("Username/Email", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired(), Length(min=10)])

# last line