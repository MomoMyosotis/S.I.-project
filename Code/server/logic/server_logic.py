# first line
import json
import secrets
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from server.services.redirect import dispatch_command
from server.logic.admin_console import manual_cmd, macr

# Sessioni e modalità server
sessions = {}
mode_ref = ["auto"]

def generate_token(length: int = 32) -> str:
    """Genera un token sicuro per sessioni utente."""
    return secrets.token_hex(length // 2)

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_POST(self):
        if self.path != "/command":
            self._set_headers(404)
            self.wfile.write(json.dumps({
                "status": "ERROR",
                "error_msg": "Unknown endpoint"
            }).encode())
            return

        content_length = int(self.headers.get('Content-Length', 0))
        raw_data = self.rfile.read(content_length)

        try:
            data = json.loads(raw_data)
            command = data.get("command")
            args = data.get("args", [])
            token = data.get("token")
        except Exception:
            self._set_headers(400)
            self.wfile.write(json.dumps({
                "status": "ERROR",
                "error_msg": "Invalid JSON"
            }).encode())
            return

        user_obj = sessions.get(token)

        # Intercetta register_user in modalità manuale
        if command == "register_user" and mode_ref[0] == "manual":
            approved = macr(timeout=30)
            if not approved:
                self._set_headers(200)
                self.wfile.write(json.dumps({
                    "status": "ERROR",
                    "error_msg": "Registration denied by admin"
                }).encode())
                return

        # Dispatcher principale
        response, new_user_obj, new_token, status = dispatch_command(command, args, user_obj)
        if new_token:
            sessions[new_token] = new_user_obj

        # Parsing
        try:
            response_dict = json.loads(response) if isinstance(response, str) else response
        except Exception:
            response_dict = {"status": "error", "error_msg": "Malformed response"}

        self._set_headers(200)
        self.wfile.write(json.dumps({
            "status": response_dict.get("status", status),
            "response": response_dict,
            "token": new_token
        }).encode())

def start_server(host: str, port: int):
    """Avvia l'HTTP server e il thread admin console."""
    # Thread per comandi admin (manual mode)
    threading.Thread(target=manual_cmd, args=(None, mode_ref), daemon=True).start()

    server = HTTPServer((host, port), RequestHandler)
    print(f"Server running on {host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received. Shutting down server...")
        server.server_close()

def stop_server(server: HTTPServer):
    """Chiude il server HTTP."""
    server.server_close()
    print("Server stopped.")

# last line