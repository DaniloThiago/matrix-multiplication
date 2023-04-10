import sys
import time
import math
import queue
import threading

# leitura dos argumentos
if len(sys.argv) != 4:
    print("Use o comando: python threads.py M1.txt M2.txt P")
    sys.exit()

arquivo1 = sys.argv[1]
arquivo2 = sys.argv[2]
P = int(sys.argv[3])

# leitura das matrizes
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
    return M

M1 = le_matriz_arquivo(arquivo1)
M2 = le_matriz_arquivo(arquivo2)

# Verifica se as matrizes são compatíveis para a multiplicação
if len(M1[0]) != len(M2):
    print("Matrizes não são compatíveis para a multiplicação")
    sys.exit()

# Função para realizar a multiplicação de uma parte da matriz resultado
def multiplica_parte(M1, M2, q, inicio, fim, m2):
    M3 = [[0 for _ in range(m2)] for _ in range(len(M1[0]))]
    for i in range(len(M1)):
        for j in range(inicio, fim):
            for k in range(len(M2)):
                M3[i][j-inicio] += M1[i][k] * M2[k][j]
    print(M3)
    q.put(M3)

# Cria uma fila de threads para executar a multiplicação
threads = []
q = queue.Queue()

# Define o tamanho de cada parte da matriz resultado
n1, m2 = len(M1), len(M2[0])
partes = math.ceil(n1 / P)
partes = partes * m2
if partes == 0:
    partes = m2

# Define o número total de partes em que a matriz resultado será dividida
partes = P

# Define o nome dos arquivos que serão gerados
arquivos = [f'threads_parte_{i+1}.txt' for i in range(partes)]

P = partes//P
# Cria as threads para executar a multiplicação
for i in range(0, partes, P):
    t0 = time.time()
    inicio, fim = i, i+P
    if fim > partes:
        fim = partes
    arquivo = arquivos[i//P]
    t = threading.Thread(target=multiplica_parte, args=(M1, M2, q, inicio, fim, P))
    threads.append(t)
    t.start()

# Espera todas as threads terminarem
for t in threads:
    t.join()

# Salva os resultados em arquivos separados
print(arquivos)
for i in range(partes):
    M3 = q.get()
    with open(arquivos[i], "w") as f:
        f.write(f"{n1} {m2}\n")
        for i in range(len(M3)):
            for j in range(len(M3[0])):
                f.write(f"c{i+1}{j+1} {M3[i][j]}\n")
        f.write(f'{time.time()-t0:.3f}')

print("Multiplicação de matrizes concluída") 
