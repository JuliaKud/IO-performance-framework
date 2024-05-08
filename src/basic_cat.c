#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 4096

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: <filePath>\n");
        return 1;
    }
    
    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
        perror("Erorr while opening a file");
        return 1;
    }
    
       char buffer[BUFFER_SIZE];
   
    size_t bytes_read;
    while ((bytes_read = fread(buffer, 1, BUFFER_SIZE, file)) > 0) {
        fwrite(buffer, 1, bytes_read, stdout);
    }
    
        if (ferror(file)) {
        perror("Error while readling a file");
        fclose(file);
        return 1;
    }
    
        fclose(file);
    
    return 0;
}
