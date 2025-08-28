# first line

import socket
import threading
from client.services.config import Config


class TCPClient:
    def __init__(self, host=Config.TCP_HOST, port=Config.TCP_PORT, timeout=15):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = None
        self.token = None
        self.lock = threading.Lock()

    def connect(self):
        """Apre la connessione TCP verso il server"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(self.timeout)
            self.sock.connect((self.host, self.port))
            print(f"[DEBUG] Connesso a {self.host}:{self.port}")
        except Exception as e:
            print(f"[ERROR] Connessione TCP fallita: {e}")
            self.sock = None

    def disconnect(self):
        """Chiude la connessione TCP"""
        if self.sock:
            try:
                self.sock.close()
            except:
                pass
            self.sock = None
            print("[DEBUG] Connessione chiusa")

    def send(self, payload: str):
        """
        Bassa astrazione: invia un messaggio raw al server e ritorna la risposta.
        """
        print(f"[DEBUG] Tentativo invio payload: {payload}")
        if not self.sock:
            self.connect()
            if not self.sock:
                return "ERROR: Non connesso"

        try:
            with self.lock:
                message = payload + "\n"
                self.sock.sendall(message.encode("utf-8"))
                print(f"[DEBUG] Dati inviati: {message.strip()}")
                response = self.sock.recv(4096).decode("utf-8").strip()
                print(f"[DEBUG] Risposta ricevuta: {response}")
                return response
        except socket.timeout:
            return "ERROR: Timeout"
        except Exception as e:
            print(f"[ERROR] Errore durante invio/ricezione: {e}")
            self.disconnect()
            return f"ERROR: {str(e)}"

    def send_request(self, command: str, data=None, require_auth=False):
        """
        Invio generico al server.
        - command: stringa del comando (es. LOGIN, REGISTER, COMMENT, ecc.)
        - data: lista di parametri (verrà joinata con '|')
        - require_auth: se True, aggiunge il token all'inizio (fallisce se assente)
        """
        print(f"[DEBUG] send_request chiamato con command={command}, data={data}, require_auth={require_auth}, token={self.token}")

        if require_auth and not self.token:
            print("[DEBUG] Richiesta autenticata ma token mancante → errore")
            return "ERROR: Non autenticato"

        parts = [command]
        if require_auth:
            parts.insert(0, self.token)

        if data:
            parts.extend(str(x) for x in data if x is not None)

        payload = "|".join(parts)
        print(f"[DEBUG] Payload costruito: {payload}")
        return self.send(payload)


# Oggetto client condiviso (singleton) da importare e riutilizzare
tcp_client = TCPClient()


# Wrapper per inviare richieste (più comodo da usare nei service)
def send_request_to_server(command: str, data=None, require_auth=False):
    return tcp_client.send_request(command, data, require_auth)

# last lines