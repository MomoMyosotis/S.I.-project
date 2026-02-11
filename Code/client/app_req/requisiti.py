# first line
import os
import sys
import subprocess

# Verifica dipendenze prima di avviare l'app
def check_dependencies():
    ##print("Verifica delle dipendenze in corso...")

    binary = os.path.join("quack", "app_req", "req_check")
    if sys.platform == "win32":
        binary += ".c"

    # Esegue il binario C
    result = subprocess.run(binary, shell=True)

    if result.returncode != 0:
        #print("Dipendenze mancanti. Interrompo l'avvio dell'app.")
        sys.exit(1)
    else:
        print("Ambiente verificato. Avvio dell'app...")

def check_version():
    #print("Verifica della versione in uso...")

    binary = os.path.join("quack", "app_req", "v_check")
    if sys.platform == "win32":
        binary += ".c"