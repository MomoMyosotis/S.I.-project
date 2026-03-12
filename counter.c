#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>

unsigned long long total_files = 0;
unsigned long long total_lines = 0;
unsigned long long total_chars = 0;

void process_file(const char *path) {
    FILE *f = fopen(path, "rb");
    if (!f) return;

    int c;
    unsigned long long lines = 0;
    unsigned long long chars = 0;

    while ((c = fgetc(f)) != EOF) {
        chars++;
        if (c == '\n') lines++;
    }

    fclose(f);

    total_files++;
    total_lines += lines;
    total_chars += chars;
}

void walk_directory(const char *path) {
    DIR *dir = opendir(path);
    if (!dir) return;

    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        if (!strcmp(entry->d_name, ".") ||
            !strcmp(entry->d_name, ".."))
            continue;

        char full_path[4096];
        snprintf(full_path, sizeof(full_path), "%s/%s", path, entry->d_name);

        struct stat st;
        if (stat(full_path, &st) == -1)
            continue;

        if (S_ISDIR(st.st_mode)) {
            walk_directory(full_path);
        } else if (S_ISREG(st.st_mode)) {
            process_file(full_path);
        }
    }

    closedir(dir);
}

int main(void) {
    walk_directory(".");

    printf("\n=== RISULTATO ===\n");
    printf("File totali     : %llu\n", total_files);
    printf("Righe totali    : %llu\n", total_lines);
    printf("Caratteri totali: %llu\n", total_chars);

    return 0;
}
