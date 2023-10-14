
import random

# Crear una matriz de 20x20 llena de valores aleatorios entre 1 y 100
matriz = [[random.randint(5, 70) for _ in range(20)] for _ in range(20)]

# Inicializar variables para almacenar la suma máxima y la columna correspondiente
max_sum = 0
max_col = 0

# Calcular la suma de cada columna e identificar la columna con la suma máxima
for col in range(20):
    col_sum = sum(matriz[row][col] for row in range(20))
    if col_sum > max_sum:
        max_sum = col_sum
        max_col = col + 1  # Sumar 1 para mostrar la columna comenzando desde 1 en lugar de 0

# Imprimir la columna con la suma máxima y el valor de esa suma
print(f"La columna con la suma máxima es la columna {max_col} con una suma de {max_sum}.")
