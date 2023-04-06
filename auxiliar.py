import sys
import numpy as np

if len(sys.argv) != 5:
    print("Use o comando: python auxiliar.py n1 m1 n2 m2")
    sys.exit()

# Recebe os parâmetros
n1 = int(sys.argv[1])
m1 = int(sys.argv[2])
n2 = int(sys.argv[3])
m2 = int(sys.argv[4])

# Cria as matrizes M1 e M2
M1 = np.random.randint(1, 99, size=(n1, m1))
M2 = np.random.randint(1, 99, size=(n2, m2))

# Salva as matrizes em arquivos .txt
np.savetxt('M1.txt', M1, fmt='%d', header=f'{n1} {m1}')
np.savetxt('M2.txt', M2, fmt='%d', header=f'{n2} {m2}')
