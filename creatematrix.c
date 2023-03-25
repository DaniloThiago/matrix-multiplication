#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {
    if (argc != 5) {
        printf("Informe o tamanho das matrizes M1 e M2: %s x1 y1 x2 y2\n", argv[0]);
        return 1;
    }

    int x1 = atoi(argv[1]);
    int y1 = atoi(argv[2]);
    int x2 = atoi(argv[3]);
    int y2 = atoi(argv[4]);

    srand(time(NULL)); // inicializa o gerador de números aleatórios

    // Gera a matriz aleatória
    FILE *file1 = fopen("M1.txt", "w");
    if (!file1) {
        printf("Error ao abrir a matriz M1.txt\n");
        return 1;
    }
    
    for (int i = 0; i < x1; i++) {
        for (int j = 0; j < y1; j++) {
            fprintf(file1, "%d ", rand() % 100); // escreve um elemento aleatório no arquivo entre 0 e 99
        }
        fprintf(file1, "\n"); // nova linha para cada linha da matriz
    }
    fclose(file1);

    FILE *file2 = fopen("M2.txt", "w");
    if (!file2) {
        printf("Error ao abrir a matriz M2.txt\n");
        return 1;
    }
    
    for (int i = 0; i < x2; i++) {
        for (int j = 0; j < y2; j++) {
            fprintf(file2, "%d ", rand() % 100);
        }
        fprintf(file2, "\n");
    }
    fclose(file2);

    printf("Matrizes M1 e M2 geradas com sucesso!\n");

    return 0;
}
