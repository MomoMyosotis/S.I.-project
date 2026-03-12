# first line

from flask import Flask, request, jsonify, send_from_directory
import os
import json, threading
from server.services.redirect import dispatch_command
from server.logic.admin_console import start_admin_server, macr, register_stop_callback
from server.logic.admin_ui import bp as admin_bp
from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
from socketserver import ThreadingMixIn

# WSGI server control
_wsgi_server = None
_wsgi_thread = None
_wsgi_lock = threading.Lock()

# Logical enabled/disabled state (pause accepting client API requests)
server_enabled = True

def enable_server():
    global server_enabled
    server_enabled = True
    return True

def disable_server():
    global server_enabled
    server_enabled = False
    return True

def is_server_enabled():
    return server_enabled

def start_wsgi_server(host='127.0.0.1', port=8000):
    global _wsgi_server, _wsgi_thread
    with _wsgi_lock:
        if _wsgi_server is not None:
            return False
        class LoggingWSGIRequestHandler(WSGIRequestHandler):
            """Ensure access lines are always printed to the console (fallback to parent on error)."""
            def log_message(self, format, *args):
                try:
                    # format like: 127.0.0.1 - - [18/Feb/2026 21:11:16] "GET /admin/pending HTTP/1.1" 200 3
                    msg = "%s - - [%s] %s" % (self.client_address[0], self.log_date_time_string(), format % args)
                    print(msg, flush=True)
                except Exception:
                    try:
                        super().log_message(format, *args)
                    except Exception:
                        pass

        class ThreadingWSGIServer(ThreadingMixIn, WSGIServer):
            daemon_threads = True

        _wsgi_server = ThreadingWSGIServer((host, port), LoggingWSGIRequestHandler)
        _wsgi_server.set_app(app)
        _wsgi_thread = threading.Thread(target=_wsgi_server.serve_forever, daemon=True)
        _wsgi_thread.start()
        return True

def stop_wsgi_server():
    global _wsgi_server, _wsgi_thread
    with _wsgi_lock:
        if _wsgi_server is None:
            return False
        try:
            _wsgi_server.shutdown()
            try:
                _wsgi_server.server_close()
            except Exception:
                pass
        except Exception:
            pass
        _wsgi_server = None
        _wsgi_thread = None
        return True

def is_wsgi_running():
    return _wsgi_server is not None
from server.logic.config_loader import load_config
from server.services.email_service import init_mail

app = Flask(__name__)
# Ensure a secret key for session cookies (use env var when available)
app.secret_key = os.environ.get('ADMIN_UI_SECRET') or os.environ.get('SECRET_KEY') or os.urandom(24)
# Ensure werkzeug access logs are visible when Flask/dev server is used
import logging
logging.getLogger('werkzeug').setLevel(logging.INFO)

sessions = {}      # token -> user_obj (condiviso)
mode_ref = ["auto"]  # modalità mutabile

# Allow simple CORS for browser clients (used when client app served on different origin)
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    return response

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
    #print("[DEBUG][api_server] Flask-Mail configured and initialized")
    
except Exception as e:
    print(f"[WARNING][api_server] Failed to configure email: {str(e)}")
    print("[WARNING][api_server] Email functionality may not work. Check your config file.")

# Admin TCP console (non-blocking). No stop callback here, only approvals/mode.
start_admin_server(mode_ref, host='127.0.0.1', port=60000)


# Serve storage images (favicon and other runtime images)
@app.route('/storage/images/<path:filename>', methods=['GET'])
def storage_images(filename):
    # server/logic is current dir for this module; images live in server/storage/images
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'storage', 'images'))
    return send_from_directory(base, filename)


@app.route('/storage/images/admin_logo', methods=['GET'])
def storage_admin_logo():
    """Serve an admin logo image if present; fallback to favicon.ico."""
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'storage', 'images'))
    try:
        for fname in os.listdir(base):
            if fname.lower().startswith('admin_logo'):
                return send_from_directory(base, fname)
    except Exception:
        pass
    # fallback to favicon if available
    fav = os.path.join(base, 'favicon.ico')
    if os.path.exists(fav):
        return send_from_directory(base, 'favicon.ico')
    return jsonify({"error": "admin logo not found"}), 404


@app.route('/favicon.ico')
def favicon():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'storage', 'images'))
    try:
        return send_from_directory(base, 'favicon.ico')
    except Exception:
        return jsonify({"error": "favicon not found"}), 404

# Register admin web UI blueprint
try:
    app.register_blueprint(admin_bp)
except Exception as e:
    print(f"[WARNING][api_server] Failed to register admin blueprint: {e}")

# Register a stop callback to stop the WSGI server when admin requests shutdown
try:
    register_stop_callback(stop_wsgi_server)
except Exception as e:
    print(f"[WARNING][api_server] Could not register stop callback: {e}")

@app.route("/api", methods=["POST"])
def api_entry():
    # If admin has paused the server, reject client API calls
    if not server_enabled:
        return jsonify({"status": "ERROR", "error_msg": "Server paused by admin"}), 503

    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"status": "ERROR", "error_msg": "Invalid JSON"}), 400

    command = (data.get("command") or "").lower()
    args = data.get("args", [])
    token = data.get("token")

    user_obj = sessions.get(token)

    # manual approval check for sensitive actions (register / login)
    if command in ("register", "register_user", "login") and mode_ref[0] == "manual":
        meta = {"command": command, "args": args, "token": token, "remote": request.remote_addr}
        approved = macr(timeout=30, meta=meta)
        if not approved:
            return jsonify({"status": "ERROR", "error_msg": "Registration denied by admin"})

    # dispatch_command retorna: (serialized_response, new_user_obj, new_token, status)
    # dispatch_command lowercases internally, pass the normalized command
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