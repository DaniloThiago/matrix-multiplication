import sys
import time

# leitura dos argumentos
if len(sys.argv) != 4:
    print("Use o comando: python sequencial.py M1.txt M2.txt M3.txt")
    sys.exit()

arquivo1 = sys.argv[1]
arquivo2 = sys.argv[2]
arquivo3 = sys.argv[3]

# leitura da matriz 1
with open(arquivo1, "r") as f:
  # leitura do tamanho da matriz
  m, n = map(int, f.readline().split())
  # inicialização da matriz
  M1 = [[0 for j in range(n)] for i in range(m)]
  # leitura dos elementos
  for i in range(m):
    for j in range(n):
      line = f.readline().split()
      # preenchimento da matriz
      M1[i][j] = int(line[1])

# leitura da matriz 2
with open(arquivo2, "r") as f:
  # leitura do tamanho da matriz
  p, q = map(int, f.readline().split())
  # inicialização da matriz
  M2 = [[0 for j in range(q)] for i in range(p)]

  # leitura dos elementos
  for i in range(p):
    for j in range(q):
      line = f.readline().split()
      # preenchimento da matriz
      M2[i][j] = int(line[1])

# cálculo da matriz resultante
t0 = time.time()
M3 = [[0 for j in range(q)] for i in range(m)]
for i in range(m):
    for j in range(q):
        for k in range(n):
            M3[i][j] += M1[i][k] * M2[k][j]

# escrita da matriz resultante
with open(arquivo3, "w") as f:
    f.write(f"{m} {q}\n")
    for i in range(m):
        for j in range(q):
            f.write(f"c{i+1}{j+1} {M3[i][j]}\n")
    t1 = time.time()
    f.write(f'{t1-t0:.3f}')

print(f'{t1-t0:.3f}')
