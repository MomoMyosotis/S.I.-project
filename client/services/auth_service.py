# first line

from client.services.tcp_helper import tcp_client

class AuthService:

    @staticmethod
    def login(username, password):
        print("[DEBUG] AuthService.login chiamato con:", username, password)
        result = tcp_client.send_request("LOGIN", [username, password])
        print("[DEBUG] Risultato da tcp_client.send_request:", repr(result))
        return result

    @staticmethod
    def register(email, username, password, birthday):
        print ("[DEBUG] AuthSerivice.register chiamato con: ", email, username, password, birthday)
        result = tcp_client.send_request("register", [email, username, password, birthday])
        print("[DEUG] Risultato da tcp_client.send_request", repr(result))
        return result

    @staticmethod
    def recover(email):
        print("[DEBUG] AuthService.recover chiamato con: ", email)
        # manda l'email dentro una lista, così il server la riceve come singolo parametro
        result = tcp_client.send_request("recover", [email])
        print("[DEBUG] Risultato da tcp_client.send_request", repr(result))
        return result

    @staticmethod
    def assistance(identifier, message):
        print("[DEBUG] AuthService.assistance chiamato con: ", identifier, message)
        # manda entrambi i parametri dentro una lista
        result = tcp_client.send_request("assistance", [identifier, message])
        print("[DEBUG] Risultato da tcp_client.send_request", repr(result))
        return result

# last line