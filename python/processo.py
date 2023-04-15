import sys
import numpy as np
import multiprocessing as mp
import time

# Define a estratégia de inicialização de processos
mp.set_start_method('fork')

# leitura dos argumentos
if len(sys.argv) != 4:
    print("Use o comando: python processos.py M1.txt M2.txt P")
    sys.exit()


arquivo1 = sys.argv[1]
arquivo2 = sys.argv[2]

# Define a quantidade de processos
p = int(sys.argv[3])

def le_matriz_arquivo(filename):
    with open(filename, "r") as f:
        # pega a primeira linha para leitura do tamanho da matriz
        l, c = map(int, f.readline().split())
        # inicialização da matriz
        M = [[0 for _ in range(c)] for _ in range(l)]
        # leitura dos elementos
        for i in range(l):
            for j in range(c):
                # pega da linha a segunda posição do array ["c12 2"], converte em int e retorna 2
                value = int(f.readline().split()[1])
                # preenchimento da matriz
                M[i][j] = value
    # Transforma as listas em matrizes NumPy
    return np.array(M)

# Define a função que realiza a multiplicação de uma parte da matriz resultante
def multiplicar_parte(start_index, end_index, result, m1, m2, num_processos, proc_id):
    # Calcula o tamanho de cada segmento da matriz resultante
    chunk_size = (end_index - start_index) // m2.shape[1]

    # Cria o arquivo de texto para o processo
    with open(f"processo_{proc_id}.txt", "w") as f:
        f.write(f"{result.shape[0]} {result.shape[1]}\n")
        start_time = time.time()
        for i in range(start_index, end_index):
            row = i // m2.shape[1]
            col = i % m2.shape[1]
            value = sum(m1[row][k] * m2[k][col] for k in range(m1.shape[1]))
            result[row][col] = value
            f.write(f"c{row+1}{col+1} {value}\n")
        end_time = time.time()
        # Escreve o tempo gasto pelo processo no final do arquivo de texto
        f.write(f"{end_time - start_time:.5f}")

# Define as matrizes M1 e M2
m1 = le_matriz_arquivo(arquivo1)
m2 = le_matriz_arquivo(arquivo2)

# Cria a matriz resultante
result = np.zeros((m1.shape[0], m2.shape[1]))

# Define os processos e inicia cada um deles
processos = []
for i in range(p):
    start_index = (i * result.size) // p
    end_index = ((i + 1) * result.size) // p
    processo = mp.Process(target=multiplicar_parte, args=(start_index, end_index, result, m1, m2, p, i))
    processo.start()
    processos.append(processo)

# Aguarda todos os processos terminarem
for processo in processos:
    processo.join()
