# first line

from flask import Flask, request, jsonify
import json
import threading
from server.services.redirect import dispatch_command
from server.logic.admin_console import manual_cmd, macr

app = Flask(__name__)
sessions = {}      # token -> user_obj (condiviso)
mode_ref = ["auto"]  # modalità mutabile

# Admin console thread (manual mode)
threading.Thread(target=manual_cmd, args=(None, mode_ref), daemon=True).start()

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

    return jsonify({
        "status": true_status,
        "response": parsed_response,
        "token": new_token
    }), 200

# last line