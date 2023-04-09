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
def le_matriz_arquivo(filename):
  with open(filename, "r") as f:
    # leitura do tamanho da matriz
    l, c = map(int, f.readline().split())
    # inicialização da matriz
    M = [[0 for j in range(c)] for i in range(l)]
    # leitura dos elementos
    for i in range(l):
      for j in range(c):
        line = f.readline().split()
        # preenchimento da matriz
        M[i][j] = int(line[1])
  return M

M1 = le_matriz_arquivo(arquivo1)
M2 = le_matriz_arquivo(arquivo2)

# Verifica se as matrizes são compatíveis para a multiplicação
if len(M1) != len(M2):
  print("Matrizes não são compatíveis para a multiplicação")
  sys.exit()
  
# cálculo da matriz resultante
t0 = time.time()
M3 = [[0 for j in range(len(M2[0]))] for i in range(len(M1))]
for i in range(len(M1)):
    for j in range(len(M2[0])):
        for k in range(len(M2)):
            M3[i][j] += M1[i][k] * M2[k][j]

# escrita da matriz resultante
with open(arquivo3, "w") as f:
    f.write(f"{len(M3)} {len(M3[0])}\n")
    for i in range(len(M3)):
        for j in range(len(M3[0])):
            f.write(f"c{i+1}{j+1} {M3[i][j]}\n")
    t1 = time.time()
    f.write(f'{t1-t0:.3f}')
print(f'{t1-t0:.3f}')
