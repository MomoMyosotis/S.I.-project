# first line

from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from client.forms import Login, Register, Recover, Assistance
from client.services.http_helper import http_client
from client.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# =====================
# LOGIN
# =====================
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        response = AuthService.login(form.username.data, form.password.data)
        # print("[DEBUG][login] Response:", repr(response))

        if isinstance(response, dict):
            status = response.get("status", "").lower()

            if status in ["ok", "accepted", "OK", "ACCEPTED"]:
                token = response.get("token")
                if token:
                    # qui salvi il token nella sessione
                    session["session_token"] = token

                    # e lo passi anche all'http_client
                    http_client.token = token

                session["login_status"] = "ACCEPTED"
                flash("Login successful!", "success")
                # print("[DEBUG][login] http_client id:", id(http_client), "token:", http_client.token)
                return redirect(url_for("home.homepage"))

            elif status == "pending":
                session["login_status"] = "PENDING"
                session["pending_user"] = form.username.data
                flash("Login pending admin approval =^^=", "info")
                return render_template("auth.html", form_type="login", form=form)

            elif status == "error":
                session["login_status"] = "REFUSED"
                flash(f"Error: {response.get('error_msg','Unknown error')}", "danger")
                return render_template("auth.html", form_type="login", form=form)

        # caso fallback per dict sconosciuti
        return render_template("auth.html", form_type="login", form=form)

    # caso GET o form non valido
    return render_template("auth.html", form_type="login", form=form)

# =====================
# LOGOUT
# =====================
@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

# =====================
# REGISTER
# =====================
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = Register()
    if form.validate_on_submit():
        birthday_str = form.birthday.data.strftime("%Y-%m-%d") if form.birthday.data else None

        response = AuthService.register(
            form.email.data,
            form.username.data,
            form.password.data,
            birthday_str
        )

        print("[DEBUG][register] Response:", repr(response))

        if isinstance(response, dict) and response.get("status") == "OK":
            flash("Registration successful! Pending approval.", "success")
            return redirect(url_for("auth.login"))
        elif isinstance(response, dict) and response.get("status") == "ERROR":
            flash(f"Error: {response.get('error_msg','Unknown error')}", "danger")
        elif isinstance(response, str) and "OK" in response:
            flash("Registration successful! Pending approval.", "success")
            return redirect(url_for("auth.login"))
        else:
            flash(f"Error: {response}", "danger")

    return render_template("auth.html", form_type="register", form=form)

# =====================
# RECOVER
# =====================
@auth_bp.route("/recover", methods=["GET", "POST"])
def recover():
    form = Recover()
    if form.validate_on_submit():
        response = AuthService.recover(form.identifier.data)
        print("[DEBUG][recover] Response:", repr(response))

        if isinstance(response, dict):
            status = response.get("status", "").lower()
            if status in ["ok", "accepted"]:
                flash("Recovery successful!\nCheck your email in a few minutes.", "success")
                return redirect(url_for("auth.login"))
            else:
                flash(f"Error: {response.get('error_msg','Unknown error')}", "danger")
        elif isinstance(response, str) and "OK" in response:
            flash("Recovery successful! Check your email.", "success")
            return redirect(url_for("auth.login"))
        else:
            flash(f"Error: {response}", "danger")

    return render_template("auth.html", form_type="recover", form=form)

# =====================
# ASSISTANCE
# =====================
@auth_bp.route("/assistance", methods=["GET", "POST"])
def assistance():
    form = Assistance()
    if form.validate_on_submit():
        response = AuthService.assistance(form.identifier.data, form.message.data)
        print("[DEBUG][assistance] Response:", repr(response))

        if isinstance(response, dict):
            status = response.get("status", "").lower()
            if status in ["ok", "accepted"]:
                flash("Assistance request sent successfully!", "success")
                return redirect(url_for("auth.login"))
            else:
                flash(f"Error: {response.get('error_msg','Unknown error')}", "danger")
        elif isinstance(response, str) and "OK" in response:
            flash("Assistance request sent successfully!", "success")
            return redirect(url_for("auth.login"))
        else:
            flash(f"Error: {response}", "danger")

    return render_template("auth.html", form_type="assistance", form=form)

@auth_bp.route("/index", methods=["GET"])
def index():
    return render_template("unified.html")  # No content_template, shows login

# last line
# =====================
# PASSWORD RESET
# =====================
@auth_bp.route("/reset", methods=["GET"])
def reset_password():
    """Handle password reset via token from email link."""
    # User clicked link from email
    reset_token = request.args.get("token")
    if not reset_token:
        flash("Invalid password reset link.", "danger")
        return redirect(url_for("auth.login"))
    
    # Call server to validate and reset password
    response = http_client.send_request("RESET_PASSWORD", [reset_token])
    print(f"[DEBUG][reset_password] Response: {repr(response)}")
    
    if isinstance(response, dict):
        status = response.get("status", "").lower()
        if status == "ok":
            new_password = response.get("new_password", "Check your email")
            flash(f"Password reset successful! Your new password is: {new_password}", "success")
            return redirect(url_for("auth.login"))
        else:
            flash(f"Error: {response.get('error_msg', 'Password reset failed')}", "danger")
            return redirect(url_for("auth.login"))
    else:
        flash(f"Error: {response}", "danger")
        return redirect(url_for("auth.login"))
