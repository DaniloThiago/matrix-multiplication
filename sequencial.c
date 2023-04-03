#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]){
	int l1,c1,l2,c2,mult;
	if(argc != 3){
		printf("Informe o tamanho das matrizes M1 e M2: %s x1 y1 x2 y2 \n", argv[0]);
		return 1;
	}

	//abre os arquivos recebidos na linha de comando
	FILE *matriz1 = fopen(argv[1], "r");
	FILE *matriz2 = fopen(argv[1], "r");

	//le o tamanho da matriz
	fscanf(matriz1, "%d %d", &l1, &c1);
	fscanf(matriz2, "%d %d", &l2, &c2);

	// aqui eu usarei um vetor para armazenar os valores da matriz
	mult = l1 * c1;
	int vet1[mult];
	int vet2[mult];
	for(int i = 0; i <= mult; i++){
		fscanf(matriz1, "%d", vet1);
		fscanf(matriz2, "%d", vet2);
	}

	//aqui gravo os valores que etsão armazenados no vetor em uma matriz
	int new_matriz1[l1][c1], new_matriz2[l2][c2], resultado[l1][c1];
	for(int i = 0; i < l1; i++){
		for(int j = 0; j < c1; j++){
			fscanf(matriz1, "%d", new_matriz1[i][j]);
			fscanf(matriz2, "%d", new_matriz2[i][j]);
		}
	}

	//multiplicação
	clock_t inicia = clock();
	for(int i = 0; i < l1; i++){
		for(int j = 0; j < c1; j++){
			resultado[i][j] = 0;
			for(int k = 0; k <= l1; l1++){
				resultado[i][j] += new_matriz1[i][k] * new_matriz2[i][j];
			}
		}
	}
	clock_t fim = clock();
	//calculo de tempo
	double tempo = (double)(fim - inicia)/ CLOCKS_PER_SEC;

	fclose(matriz1);
	fclose(matriz2);

	//gravando o resultado em outro arquivo
	FILE *saida = fopen("saida.txt","w");
	for(int i = 0; i < l1; i++){
		for(int j = 0; j < c1; j++){
			fprintf(saida, "%d", resultado[i][j]);
		}
		fprintf(saida, "\n");
	}
	fprintf(saida, "%f", tempo);
	fclose(saida);

	return 0;
}
