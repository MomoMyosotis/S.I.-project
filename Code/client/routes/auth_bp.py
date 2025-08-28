# first line

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from client.forms import LoginForm, RegisterForm, RecoverForm, AssistanceForm
from client.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    response = None

    if form.validate_on_submit():
        print("[DEBUG] Login form valido:", form.username.data, form.password.data)
        response = AuthService.login(form.username.data, form.password.data)
        print("[DEBUG] Risposta raw da AuthService:", repr(response))

        if response.startswith("OK") or response.startswith("ACCEPTED") or "Waiting" in response:
            if "|" in response:
                token = response.split("|", 1)[1]
                session["session_token"] = token
            session["login_status"] = "ACCEPTED" if response.startswith("OK") else "PENDING"

            if session["login_status"] == "PENDING":
                session["pending_user"] = form.username.data
                flash("Login pending admin approval =^^=", "info")
                return render_template("auth.html", form_type="login", form=form)
            else:
                flash("Login successful!", "success")
                return redirect(url_for("home.homepage"))

        elif response.upper().startswith("BLACKLISTED"):
            session["login_status"] = "REFUSED"
            flash("Account blocked. Contact support.", "danger")
        else:
            session["login_status"] = "REFUSED"
            flash(f"Error: {response}", "danger")

    else:
        # Se il form non è valido, stampo gli errori
        print("[DEBUG] Login form NON valido:", form.errors, request.form)

    # In ogni altro caso, mostro il form di login
    return render_template("auth.html", form_type="login", form=form)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    response = None

    if form.validate_on_submit():
        birthday_str = form.birthday.data.strftime("%Y-%m-%d")  # oppure "%d/%m/%Y" se vuoi
        print("[DEBUG] Register form valido:", form.email.data, form.username.data, form.password.data, form.birthday.data)
        response = AuthService.register(
            form.email.data,
            form.username.data,
            form.password.data,
            birthday_str
        ).strip()
        print("[DEBUG] Risposta raw da AuthService:", repr(response))

        if response.startswith("ACCEPTED") or "already" in response:
            flash("Account created! Please log in. =^^=", "info")
            return redirect(url_for("auth.login"))
        elif response.upper().startswith("BLACKLISTED"):
            flash("Your account is blocked. Contact support.", "danger")
        else:
            flash(f"Error: {response}", "danger")

    else:
        # Se il form non è valido, stampo gli errori
        print("[DEBUG] Register form NON valido:", form.errors, request.form)

    # In ogni altro caso, mostro il form di registrazione
    return render_template("auth.html", form_type="register", form=form)

@auth_bp.route("/recover", methods=["GET", "POST"])
def recover():
    form = RecoverForm()
    if form.validate_on_submit():
        response = AuthService.recover(form.email.data).strip()
        flash(response, "info")
    return render_template("auth.html", form_type="recover", form=form)

@auth_bp.route("/assistance", methods=["GET", "POST"])
def assistance():
    form = AssistanceForm()
    response = None

    if form.validate_on_submit():
        print("[DEBUG] Assistance form valido:", form.identifier.data, form.message.data)
        response = AuthService.assistance(form.identifier.data, form.message.data).strip()
        print("[DEBUG] Risposta raw da AuthService:", repr(response))
        flash(response, "info")
    else:
        print("[DEBUG] Assistance form NON valido:", form.errors, request.form)

    return render_template("auth.html", form_type="assistance", form=form)


# last line