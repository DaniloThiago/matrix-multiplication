#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {
    int l1, c1, l2, c2;

    // abre os arquivos
    FILE *matriz1 = fopen(argv[1], "r");
    FILE *matriz2 = fopen(argv[2], "r");

    // le o tamanho
    fscanf(matriz1, "%d %d", &l1, &c1);
    fscanf(matriz2, "%d %d", &l2, &c2);

    // aloca matriz
    int **new_matriz1 = (int **) malloc(l1 * sizeof(int *));
    int **new_matriz2 = (int **) malloc(l2 * sizeof(int *));
    int **resultado = (int **) malloc(l1 * sizeof(int *));

    for (int i = 0; i < l1; i++) {
        new_matriz1[i] = (int *) malloc(c1 * sizeof(int));
        resultado[i] = (int *) malloc(c2 * sizeof(int));
    }

    for (int i = 0; i < l2; i++) {
        new_matriz2[i] = (int *) malloc(c2 * sizeof(int));
    }

    // leitura das matrizes
    for (int i = 0; i < l1; i++) {
        for (int j = 0; j < c1; j++) {
            fscanf(matriz1, "%d", &new_matriz1[i][j]);
        }
    }

    for (int i = 0; i < l2; i++) {
        for (int j = 0; j < c2; j++) {
            fscanf(matriz2, "%d", &new_matriz2[i][j]);
        }
    }

    // multiplicação
    clock_t inicia = clock();
    for (int i = 0; i < l1; i++) {
        for (int j = 0; j < c2; j++) {
            resultado[i][j] = 0;
            for (int k = 0; k < c1; k++) {
                resultado[i][j] += new_matriz1[i][k] * new_matriz2[k][j];
            }
        }
    }
    clock_t fim = clock();

    // cálculo de tempo
    double tempo = (double)(fim - inicia) / CLOCKS_PER_SEC;

    // gravação do resultado em outro arquivo
    FILE *saida = fopen("saida.txt", "w");
    fprintf(saida, "%d %d\n", l1, c2);  // tamanho da matriz resultante

    for (int i = 0; i < l1; i++) {
        for (int j = 0; j < c2; j++) {
            fprintf(saida, "%d %d %d\n", i, j, resultado[i][j]);  // posição linha, coluna e valor
        }
    }

    fprintf(saida, "%.6f", tempo);  // tempo de execução
    fclose(saida);
	
return 0;
}
