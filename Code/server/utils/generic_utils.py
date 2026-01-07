# first line

import os, uuid, shutil
from server.db.db_crud import get_commented_medias_db
from typing import List, Dict, Any

STORAGE = "server/storage"

def save_uploaded_file(temp_path: str, original_name: str) -> str:
    os.makedirs(STORAGE, exist_ok=True)
    ext = os.path.splitext(original_name)[1]
    fname = f"{uuid.uuid4().hex}{ext}"
    dest = os.path.join(STORAGE, fname)

    # Verifica il sistema operativo e copia il file in modo appropriato
    if os.name == 'nt':  # Windows
        shutil.copyfile(temp_path, dest)  # Copia normalmente su Windows
        print(f"File salvato su Windows: {dest}")
    elif os.name == 'posix':  # Linux
        shutil.copyfile(temp_path, dest)
        print(f"File salvato su Linux: {dest}")
    else:
        print("Sistema operativo non supportato")
        return None

    return dest

def delete_file(file_path: str) -> None:
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass

def get_commented_medias(user_id: int):
    print(f"[DEBUG][generic_utils.get_commented_medias] user_id is: {user_id}")
    try:
        medias = get_commented_medias_db(user_id)
        print(f"[DEBUG][generic_utils.get_commented_medias] medias fetched successfully.\nmedias id: {[media['id'] for media in medias]}")
        return medias
    except Exception as e:
        print(f"[ERROR][generic_utils.get_commented_medias] Exception: {e}")
        return []

# last line