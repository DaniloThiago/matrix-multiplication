import sys
import time

# Função para ler uma matriz a partir de um arquivo
def le_matriz_arquivo(filename):
    with open(filename, 'r') as f:
        # Lê o tamanho da matriz
        m, n = map(int, f.readline().split())

        # Inicializa a matriz com zeros
        matriz = [[0 for _ in range(n)] for _ in range(m)]

        # Lê os valores da matriz
        for i in range(m):
            linha = f.readline().split()
            for j in range(n):
                matriz[i][j] = int(linha[j])

    return matriz


# Função para multiplicar duas matrizes
def multiplica_matrizes(matriz1, matriz2):
    # Verifica se as matrizes são compatíveis para a multiplicação
    if len(matriz1[0]) != len(matriz2):
        return None

    # Inicializa a matriz resultante com zeros
    saida = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]

    # Realiza a multiplicação
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                saida[i][j] += matriz1[i][k] * matriz2[k][j]

    return saida

# Lê as matrizes de entrada
m1_filename = sys.argv[1]
m2_filename = sys.argv[2]
m1 = le_matriz_arquivo(m1_filename)
m2 = le_matriz_arquivo(m2_filename)

# Multiplica as matrizes
tempo_inicio = time.time()
resultado = multiplica_matrizes(m1, m2)
tempo_fim = time.time()

# Escreve o resultado no arquivo de saída
output_filename = sys.argv[3]
with open(output_filename, 'w') as f:
    # Escreve o tamanho da matriz
    f.write(f"{len(resultado)} {len(resultado[0])}\n")

    # Escreve os valores da matriz
    for i in range(len(resultado)):
        for j in range(len(resultado[0])):
            if resultado[i][j] != 0:
                f.write(f"c{i+1}{j+1} {resultado[i][j]}\n")

    # Escreve o tempo de execução
    f.write(f"{tempo_fim - tempo_inicio:.2f}")
