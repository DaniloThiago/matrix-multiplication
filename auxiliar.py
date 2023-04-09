import sys
import time
import numpy as np

if len(sys.argv) != 5:
    print("Use o comando: python auxiliar.py n1 m1 n2 m2")
    sys.exit()

# Tempo inicial total
t0 = time.time()

# Recebe os parâmetros
n1 = int(sys.argv[1])
m1 = int(sys.argv[2])
n2 = int(sys.argv[3])
m2 = int(sys.argv[4])
# Cria as matrizes M1 e M2
M1 = np.round(np.random.uniform(low=1.0, high=99.0, size=(n1, m1)), decimals=2)
M2 = np.round(np.random.uniform(low=1.0, high=99.0, size=(n2, m2)), decimals=2)

# Salva as matrizes em arquivos .txt
with open('M1.txt', 'w') as f:
    # Tempo inicial
    t1 = time.time()
    f.write(f'{n1} {m1}\n')
    for i in range(n1):
        for j in range(m1):
            f.write(f'c{i+1}{j+1} {M1[i,j]:.2f}\n')
            t2 = time.time()
    f.write(f'{t2-t1:.3f}')

with open('M2.txt', 'w') as f:
    t3 = time.time()
    f.write(f'{n2} {m2}\n')
    for i in range(n2):
        for j in range(m2):
            f.write(f'c{i+1}{j+1} {M2[i,j]:.2f}\n')
            t4 = time.time()
    f.write(f'{t4-t3:.3f}')


# Tempo final total
t5 = time.time()

# Resultado do tempo gasto
print(f'{t5-t0:.3f}')