# first line

####################
# gestisce cd.json #
####################

import json, os

FILE = 'services/cd.json'

# carica e valida cd.json
def load_config(file_path=FILE):
    if not os.path.exists(file_path):
        raise FileNotFoundError (f"Server config file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error in file parsing: {e}")

    # basic controls
    required_keys = ["HOST", "PORT", "MODE", "TIMEOUT", "BLACKLIST"]
    for key in required_keys:
        if key not in config:
            raise TypeError("BLACKLIST must be, well... a list")

    return config

# last line