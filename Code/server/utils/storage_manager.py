# first line

import os
import shutil
from typing import Optional

# ==========================
# CONFIG STORAGE
# ==========================
BASE_STORAGE = r"server/storage"
FOLDERS = {
    "document": "documents",
    "note": "notes",
    "song": "songs",
    "video": "videos"
}

# Assicura che tutte le cartelle esistano
for folder in FOLDERS.values():
    os.makedirs(os.path.join(BASE_STORAGE, folder), exist_ok=True)

def get_path(file_type: str, file_name: str) -> str:
    folder = FOLDERS.get(file_type)
    if not folder:
        raise ValueError(f"Unknown file type: {file_type}")
    return os.path.join(BASE_STORAGE, folder, file_name)

# ==========================
# SAVE FILE
# ==========================
def save_file(file_type: str, file_name: str, content: bytes) -> str:
    path = get_path(file_type, file_name)
    with open(path, "wb") as f:
        f.write(content)
    return f"File saved at {path}"

# ==========================
# FETCH FILE
# ==========================
def fetch_file(file_type: str, file_name: str) -> Optional[bytes]:
    path = get_path(file_type, file_name)
    if not os.path.isfile(path):
        return None
    with open(path, "rb") as f:
        return f.read()

# ==========================
# UPDATE FILE
# ==========================
def update_file(file_type: str, file_name: str, content: bytes) -> str:
    path = get_path(file_type, file_name)
    if not os.path.isfile(path):
        return "File does not exist"
    with open(path, "wb") as f:
        f.write(content)
    return f"File updated at {path}"

# ==========================
# DOWNLOAD FILE
# ==========================
def download_file(file_type: str, file_name: str, target_path: str) -> str:
    src = get_path(file_type, file_name)
    if not os.path.isfile(src):
        return "File does not exist"
    shutil.copy(src, target_path)
    return f"File copied to {target_path}"

# ==========================
# DELETE FILE
# ==========================
def delete_file(file_type: str, file_name: str) -> str:
    path = get_path(file_type, file_name)
    if not os.path.isfile(path):
        return "File does not exist"
    os.remove(path)
    return f"File removed from {path}"

# last line