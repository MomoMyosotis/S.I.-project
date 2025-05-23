#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef _WIN32
    #define OS_WINDOWS
#elif __APPLE__
    #define OS_MAC
#else
    #define OS_LINUX
#endif

int check_command(const char* cmd) {
    char full_cmd[256];
    snprintf(full_cmd, sizeof(full_cmd), "%s >nul 2>&1", cmd);
    return system(full_cmd) == 0;
}

int install_python() {
    #ifdef OS_WINDOWS
        return system("winget install -e --id Python.Python.3") == 0;
    #elif defined(OS_MAC)
        return system("brew install python3") == 0;
    #elif defined(OS_LINUX)
        return system("sudo apt update && sudo apt install -y python3 python3-pip") == 0;
    #endif
    return 1;
}

int ensure_pip() {
    return system("python3 -m ensurepip") == 0;
}

int pip_install(const char* package) {
    char cmd[256];
    snprintf(cmd, sizeof(cmd), "python3 -m pip install %s", package);
    return system(cmd) == 0;
}

int main() {
    printf("🛠️  Verifica ambiente Python...\n");

    // Verifica python
    if (system("python3 --version > /dev/null 2>&1") != 0) {
        printf("❌ Python3 non trovato. Installazione in corso...\n");
        if (!install_python()) {
            fprintf(stderr, "Errore installazione Python.\n");
            return 1;
        }
    } else {
        printf("✅ Python3 trovato.\n");
    }

    // Verifica pip
    if (system("python3 -m pip --version > /dev/null 2>&1") != 0) {
        printf("❌ pip non trovato. Provo a installarlo...\n");
        if (!ensure_pip()) {
            fprintf(stderr, "Errore installazione pip.\n");
            return 1;
        }
    } else {
        printf("✅ pip trovato.\n");
    }

    // Legge moduli da file
    FILE* f = fopen("modules_required.dat", "r");
    if (!f) {
        perror("Errore apertura file modules_required.dat");
        return 1;
    }

    char line[128];
    while (fgets(line, sizeof(line), f)) {
        line[strcspn(line, "\n")] = 0; // Rimuove newline
        if (strlen(line) == 0 || line[0] == '#') continue;
        printf("🔄 Controllo modulo: %s\n", line);
        char test_cmd[256];
        snprintf(test_cmd, sizeof(test_cmd), "python3 -c \"import %s\" > /dev/null 2>&1", line);
        if (system(test_cmd) != 0) {
            printf("📦 Modulo mancante: %s. Installazione...\n", line);
            if (!pip_install(line)) {
                fprintf(stderr, "Errore durante pip install %s\n", line);
            }
        } else {
            printf("✅ %s già presente.\n", line);
        }
    }
    fclose(f);

    printf("✅ Ambiente pronto. Avvia l'app Python.\n");
    return 0;
}
