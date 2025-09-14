import base64
from services.redirect import dispatch_command
import os

# Dummy user per il test
dummy_user = {"id": 1, "username": "tester"}

# Lista di file da testare: (tipo, nome, contenuto bytes)
test_files = [
    ("document", "test1.pdf", b"PDF content"),
    ("document", "test2.odt", b"ODT content"),
    ("song", "song1.mp3", b"MP3 content"),
    ("song", "song2.midi", b"MIDI content"),
    ("video", "video1.mp4", b"MP4 content"),
    ("video", "video2.youtube", b"YOUTUBE content"),
    ("note", "note1.txt", b"First note"),
    ("note", "note2.txt", b"Second note"),
]

def decode_optional_base64(s):
    """Decodifica una stringa base64, gestendo anche 'null' e None."""
    if s in (None, "null"):
        return None
    return base64.b64decode(s)

def test_storage_dispatcher(user_obj):
    print("=== START STORAGE DISPATCHER TEST ===")

    # Salvataggio file
    for ftype, fname, content in test_files:
        serialized, _, _, status = dispatch_command("save_file", [ftype, fname, content], user_obj)
        print(serialized, status)

    # Fetch e controllo contenuto
    for ftype, fname, content in test_files:
        fetched_base64, _, _, status = dispatch_command("fetch_file", [ftype, fname], user_obj)
        fetched_bytes = decode_optional_base64(fetched_base64)
        assert fetched_bytes == content, f"Fetched content mismatch for {fname}"
        print(f"Fetched {fname} successfully", status)

    # Update file
    for ftype, fname, content in test_files:
        new_content = content + b" updated"
        updated, _, _, status = dispatch_command("update_file", [ftype, fname, new_content], user_obj)
        print(updated, status)
        # Verifica aggiornamento
        fetched_base64, _, _, _ = dispatch_command("fetch_file", [ftype, fname], user_obj)
        fetched_bytes = decode_optional_base64(fetched_base64)
        assert fetched_bytes == new_content, f"Updated content mismatch for {fname}"

    # Download file (copia in folder temporanea)
    tmp_dir = "tmp_download"
    os.makedirs(tmp_dir, exist_ok=True)
    for ftype, fname, _ in test_files:
        target_path = os.path.join(tmp_dir, fname)
        result, _, _, status = dispatch_command("download_file", [ftype, fname, target_path], user_obj)
        print(result, status)
        assert os.path.isfile(target_path), f"Download failed for {fname}"

    # Delete file
    for ftype, fname, _ in test_files:
        deleted, _, _, status = dispatch_command("delete_file", [ftype, fname], user_obj)
        print(deleted, status)
        # Verifica rimozione
        fetched_base64, _, _, _ = dispatch_command("fetch_file", [ftype, fname], user_obj)
        fetched_bytes = decode_optional_base64(fetched_base64)
        assert fetched_bytes is None, f"File {fname} was not deleted!"

    print("=== STORAGE DISPATCHER TEST COMPLETED SUCCESSFULLY ===")

if __name__ == "__main__":
    test_storage_dispatcher(dummy_user)
