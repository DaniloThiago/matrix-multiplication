import sys
import numpy as np
import threading
import time

# leitura dos argumentos
if len(sys.argv) != 4:
    print("Use o comando: python threads.py M1.txt M2.txt P")
    sys.exit()

arquivo1 = sys.argv[1]
arquivo2 = sys.argv[2]

# Define a quantidade de threads
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

# Define a classe MultiplicationThread
class MultiplicationThread(threading.Thread):
    def __init__(self, thread_id, m1, m2, result, num_threads, start_index, end_index):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.m1 = m1
        self.m2 = m2
        self.result = result
        self.num_threads = num_threads
        self.start_index = start_index
        self.end_index = end_index

    def run(self):
        # Calcula o intervalo de elementos da matriz resultante que a thread é responsável por calcular
        chunk_size = (self.end_index - self.start_index) // self.m2.shape[1]

        # Cria o arquivo de texto para a thread
        with open(f"thread_{self.thread_id+1}.txt", "w") as f:
            f.write(f"{self.result.shape[0]} {self.result.shape[1]}\n")
            start_time = time.time()
            for i in range(self.start_index, self.end_index):
                row = i // self.m2.shape[1]
                col = i % self.m2.shape[1]
                value = sum(self.m1[row][k] * self.m2[k][col] for k in range(self.m1.shape[1]))
                self.result[row][col] = value
                f.write(f"c{row+1}{col+1} {value}\n")
            end_time = time.time()
            # Escreve o tempo gasto pela thread no final do arquivo de texto
            f.write(f"{end_time - start_time:.5f}")

# Define as matrizes M1 e M2
m1 = le_matriz_arquivo(arquivo1)
m2 = le_matriz_arquivo(arquivo2)

# Cria a matriz resultante
result = np.zeros((m1.shape[0], m2.shape[1]))

# Divide a tarefa entre as threads
chunk_size = result.size // p
start_index = 0
threads = []

# Calcula o tempo de início da execução
start_time = time.time()

for i in range(p):
    end_index = start_index + chunk_size if i < p - 1 else result.size
    t = MultiplicationThread(i, m1, m2, result, p, start_index, end_index)
    threads.append(t)
    start_index = end_index

# Calcula o tempo de término da execução
end_time = time.time()

# Inicia as threads
for t in threads:
    t.start()

# Espera as threads terminarem
for t in threads:
    t.join()

# Salva a matriz resultante em um arquivo de texto
# Cria o arquivo de texto para a matriz resultante
with open("threads_M3.txt", "w") as f:
    f.write(f"{result.shape[0]} {result.shape[1]}\n")
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            # f.write(f"c{i+1}{j+1} {result[i][j]}\n")
            f.write(f"c{i+1}{j+1} {result[i][j].astype(int)}\n")
    # Escreve o tempo total gasto no final do arquivo de texto
    f.write(f"{end_time - start_time:.5f}")

# Imprime a matriz resultante
print(result)