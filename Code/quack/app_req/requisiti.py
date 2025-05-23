# first line
import os
import sys
import subprocess

# Verifica dipendenze prima di avviare l'app
def check_dependencies():
    print("Verifica delle dipendenze in corso...")

    # Scegli l'eseguibile giusto a seconda del sistema
    binary = os.path.join("quack", "app_req", "req_check")
    if sys.platform == "win32":
        binary += ".c"

    # Esegue il binario C
    result = subprocess.run(binary, shell=True)

    if result.returncode != 0:
        print("❌ Dipendenze mancanti. Interrompo l'avvio dell'app.")
        sys.exit(1)
    else:
        print("✅ Ambiente verificato. Avvio dell'app...")