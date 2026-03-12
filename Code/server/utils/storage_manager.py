# first line

import os, shutil, platform
from typing import Optional

# ==========================
# CONFIG STORAGE
# ==========================
BASE_STORAGE = r"server/storage"
FOLDERS = {
    "image": "images",
    "document": "documents",
    "song": "songs",
    "video": "videos",
    "notes": "notes"
}

# Assicura che tutte le cartelle esistano
for folder in FOLDERS.values():
    os.makedirs(os.path.join(BASE_STORAGE, folder), exist_ok=True)

def get_path(file_type: str, file_name: str) -> str:
    # If caller provided a "stored_at"-like path (eg. "song/name.mp3"), prefer it
    if (os.path.sep in file_name) or ('/' in file_name):
        candidate = os.path.join(BASE_STORAGE, file_name)
        # return path
        return candidate

    folder = FOLDERS.get(file_type)
    if folder:
        return os.path.join(BASE_STORAGE, folder, file_name)

    # fallback: try to find the file in any known folder
    for f in FOLDERS.values():
        p = os.path.join(BASE_STORAGE, f, file_name)
        if os.path.isfile(p):
            return p

    # last resort: return a path under BASE_STORAGE
    return os.path.join(BASE_STORAGE, file_name)

# ==========================
# SAVE FILE
# ==========================
def save_file(file_type: str, file_name: str, content: bytes) -> str:
    path = get_path(file_type, file_name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(content)
    return f"File saved at {path}"

# ==========================
# FETCH FILE
# ==========================
def fetch_file(file_type: str, file_name: str) -> Optional[bytes]:
    path = get_path(file_type, file_name)
    if os.path.isfile(path):
        with open(path, "rb") as f:
            return f.read()

    # Try to locate a file matching the given name with any extension inside the designated folder
    folder = FOLDERS.get(file_type)
    if folder:
        folder_path = os.path.join(BASE_STORAGE, folder)
        if os.path.isdir(folder_path):
            for fname in os.listdir(folder_path):
                if fname == file_name or fname.startswith(f"{file_name}.") or fname.startswith(file_name):
                    candidate = os.path.join(folder_path, fname)
                    if os.path.isfile(candidate):
                        with open(candidate, "rb") as f:
                            return f.read()

    # Global fallback: search the entire storage tree for the basename (tolerant matching)
    target_basename = os.path.basename(file_name).lower()

    def normalize(n: str) -> str:
        # strip non-alphanum and lowercase to allow fuzzy matches (e.g. spaces/dashes/upper/lower)
        core = os.path.splitext(n)[0]
        return "".join(ch for ch in core.lower() if ch.isalnum())

    target_norm = normalize(target_basename)
    for root, _, files in os.walk(BASE_STORAGE):
        for fname in files:
            fname_low = fname.lower()
            if fname_low == target_basename or fname_low.startswith(f"{target_basename}."):
                candidate = os.path.join(root, fname)
                try:
                    with open(candidate, "rb") as f:
                        return f.read()
                except Exception:
                    continue
            # tolerant normalized check: allow similar filenames (ignores spaces/dashes/case)
            if target_norm and target_norm == normalize(fname):
                candidate = os.path.join(root, fname)
                try:
                    with open(candidate, "rb") as f:
                        return f.read()
                except Exception:
                    continue
    return None

# ==========================
# UPDATE FILE
# ==========================
def update_file(file_type: str, file_name: str, content: bytes) -> str:
    path = get_path(file_type, file_name)
    if not os.path.isfile(path):
        return "File does not exist"
    os.makedirs(os.path.dirname(path), exist_ok=True)
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

    system_name = platform.system()

    try:
        if system_name == "Windows":
            os.system(f'copy "{src}" "{target_path}"')
        elif system_name in ("Linux", "Darwin"):
            os.system(f'cp "{src}" "{target_path}"')
        else:
            shutil.copy(src, target_path)
    except Exception as e:
        return f"Error copying file: {e}"

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