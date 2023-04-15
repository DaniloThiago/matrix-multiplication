import sys
import numpy as np
import multiprocessing as mp
import time

# leitura dos argumentos
if len(sys.argv) != 4:
    print("Use o comando: python processos.py M1.txt M2.txt P")
    sys.exit()

arquivo1 = sys.argv[1]
arquivo2 = sys.argv[2]

# Define a quantidade de processos
p = int(sys.argv[3])

def ler_matriz_arquivo(filename):
    with open(filename, "r") as f:
        # Pega as duas primeiras posições do arquivo para ler o tamanho da matriz
        linhas, colunas = map(int, f.readline().split())
        # Inicialização da matriz
        matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]
        # Leitura dos elementos
        for i in range(linhas):
            # Lê uma linha do arquivo com os valores da linha i da matriz
            linha = list(map(int, f.readline().split()))
            # Preenchimento da matriz
            for j in range(colunas):
                matriz[i][j] = linha[j]
    # Transforma as listas em matrizes NumPy
    return np.array(matriz)


# Define a função que realiza a multiplicação de uma parte da matriz resultante
def multiplicar_parte(inicio, fim, resultado, matriz1, matriz2, num_processos, proc_id):
    # Calcula o tamanho de cada segmento da matriz resultante
    tamanho_segmento = (fim - inicio) // matriz2.shape[1]

    # Cria o arquivo de texto para o processo
    with open(f"processo_{proc_id}.txt", "w") as f:
        f.write(f"{resultado.shape[0]} {resultado.shape[1]}\n")
        start_time = time.time()
        for i in range(inicio, fim):
            linha = i // matriz2.shape[1]
            coluna = i % matriz2.shape[1]
            valor = sum(matriz1[linha][k] * matriz2[k][coluna] for k in range(matriz1.shape[1]))
            resultado[linha][coluna] = valor
            f.write(f"c{linha+1}{coluna+1} {valor}\n")
        end_time = time.time()
        # Escreve o tempo gasto pelo processo no final do arquivo de texto
        f.write(f"{end_time - start_time:.5f}")

# Define as matrizes M1 e M2
matriz1 = ler_matriz_arquivo(arquivo1)
matriz2 = ler_matriz_arquivo(arquivo2)

# Cria a matriz resultante
resultado = np.zeros((matriz1.shape[0], matriz2.shape[1]))

if __name__ == '__main__':
    # Divide a matriz resultante em p partes iguais
    tamanho_segmento = resultado.size // p
    processos = []
    for i in range(p):
        inicio = i * tamanho_segmento
        fim = (i + 1) * tamanho_segmento if i < p - 1 else resultado.size
        processos.append(mp.Process(target=multiplicar_parte, args=(inicio, fim, resultado, matriz1, matriz2, p, i)))
    
    # Inicia todos os processos
    for processo in processos:
        processo.start()
    
    # Espera que todos os processos terminem
    for processo in processos:
        processo.join()
