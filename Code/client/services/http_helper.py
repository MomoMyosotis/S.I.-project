# first line

import requests
from typing import Optional, List, Any

class HTTPClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.token: Optional[str] = None

    def send_request(self,
                    command: str,
                    args: Optional[List[Any]] = None,
                    require_auth: bool = False) -> dict:
        print(f"\n_______________________\n[DEBUG][http_helper.HTTPClient.send_request]\nself is: {self}\ncommand is: {command}\nargs are: {args}\n________________\n")
        payload = {"command": command, "args": args or []}
        if require_auth:
            if not self.token:
                return {"status": "ERROR", "error_msg": "Non autenticato"}
            payload["token"] = self.token

        try:
            response = requests.post(f"{self.base_url}/api", json=payload, timeout=15)
            response.raise_for_status()
            data = response.json()
            if "token" in data and data["token"]:
                self.token = data["token"]
            return data
        except requests.exceptions.RequestException as e:
            return {"status": "ERROR", "error_msg": str(e)}

# Singleton condiviso
http_client = HTTPClient("http://127.0.0.1:8000")

# last line