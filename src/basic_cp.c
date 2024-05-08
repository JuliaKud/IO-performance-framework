#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 10240

int main(int argc, char *argv[]) {
    FILE *source_file, *destination_file;
    char buffer[BUFFER_SIZE];
    size_t bytes_read;

    if (argc != 3) {
        fprintf(stderr, "Usage: ./basic_cp <sourceFile> <destFile>\n");
        return EXIT_FAILURE;
    }

    source_file = fopen(argv[1], "rb");
    if (source_file == NULL) {
        perror("Can't open source file");
        return EXIT_FAILURE;
    }

    destination_file = fopen(argv[2], "wb");
    if (destination_file == NULL) {
        perror("Can't open destination file");
        fclose(source_file);
        return EXIT_FAILURE;
    }

    while ((bytes_read = fread(buffer, 1, BUFFER_SIZE, source_file)) > 0) {
        fwrite(buffer, 1, bytes_read, destination_file);
    }

    fclose(source_file);
    fclose(destination_file);

    return EXIT_SUCCESS;
}
