# first line

import os, uuid, shutil

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
        shutil.copyfile(temp_path, dest)  # Copia normalmente su Linux
        print(f"File salvato su Linux: {dest}")
    else:
        print("Sistema operativo non supportato")
        return None

    return dest  # salva questo in media.file_path

def delete_file(file_path: str) -> None:
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass

# last line