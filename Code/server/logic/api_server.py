# first line

from flask import Flask, request, jsonify
import json, threading
from server.services.redirect import dispatch_command
from server.logic.admin_console import start_admin_server, macr
from server.logic.config_loader import load_config
from server.services.email_service import init_mail

app = Flask(__name__)
sessions = {}      # token -> user_obj (condiviso)
mode_ref = ["auto"]  # modalità mutabile

# Load configuration and initialize Flask-Mail
try:
    config = load_config()
    
    # Configure Flask app with email settings
    app.config['MAIL_SERVER'] = config.get('MAIL_SERVER', 'smtp.gmail.com')
    app.config['MAIL_PORT'] = config.get('MAIL_PORT', 587)
    app.config['MAIL_USE_TLS'] = config.get('MAIL_USE_TLS', True)
    app.config['MAIL_USERNAME'] = config.get('MAIL_USERNAME', '')
    app.config['MAIL_PASSWORD'] = config.get('MAIL_PASSWORD', '')
    app.config['MAIL_DEFAULT_SENDER'] = config.get('MAIL_DEFAULT_SENDER', 'noreply@app.com')
    
    # Initialize Flask-Mail
    init_mail(app)
    print("[DEBUG][api_server] Flask-Mail configured and initialized")
    
except Exception as e:
    print(f"[WARNING][api_server] Failed to configure email: {str(e)}")
    print("[WARNING][api_server] Email functionality may not work. Check your config file.")

# Admin TCP console (non-blocking). No stop callback here, only approvals/mode.
start_admin_server(mode_ref, host='127.0.0.1', port=60000)

@app.route("/api", methods=["POST"])
def api_entry():
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"status": "ERROR", "error_msg": "Invalid JSON"}), 400

    command = data.get("command")
    args = data.get("args", [])
    token = data.get("token")

    user_obj = sessions.get(token)

    # manual register check
    if command == "register_user" and mode_ref[0] == "manual":
        approved = macr(timeout=30)
        if not approved:
            return jsonify({"status": "ERROR", "error_msg": "Registration denied by admin"})

    # dispatch_command retorna: (serialized_response, new_user_obj, new_token, status)
    serialized_resp, new_user_obj, new_token, status = dispatch_command(command, args, user_obj)

    # se dispatch ha creato una nuova sessione, salvala
    if new_token:
        sessions[new_token] = new_user_obj

    # il serialized_resp è (spesso) una stringa JSON: proviamo a deserializzarla
    try:
        parsed_response = json.loads(serialized_resp)
    except Exception:
        # non JSON, mantienilo come stringa
        parsed_response = serialized_resp


    true_status = parsed_response.get("status") if isinstance(parsed_response, dict) else status

    # Choose an appropriate HTTP status code when errors occur so clients can react
    status_code = 200
    if isinstance(true_status, str) and true_status.lower() in ("error", "err", "failed"):
        status_code = 500

    return jsonify({
        "status": true_status,
        "response": parsed_response,
        "token": new_token
    }), status_code

# last line