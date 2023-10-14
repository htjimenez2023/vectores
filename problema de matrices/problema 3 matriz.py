
# Definir las dimensiones de la matriz
filas = 7
columnas = 7

# Crear una matriz de 7x7 llena de ceros
matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

# Llenar la matriz con valores (en este ejemplo, llenamos la matriz con números aleatorios)
import random

for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = random.randint(10, 20)  # Cambia estos valores según tus necesidades

# Inicializar vectores para almacenar las sumas de renglones y columnas
suma_renglones = [0] * filas
suma_columnas = [0] * columnas

# Calcular la suma de cada renglón y almacenarla en el vector suma_renglones
for i in range(filas):
    suma_renglones[i] = sum(matriz[i])

# Calcular la suma de cada columna y almacenarla en el vector suma_columnas
for j in range(columnas):
    suma_columnas[j] = sum(matriz[i][j] for i in range(filas))

# Imprimir la matriz
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end='\t')
    print()

# Imprimir las sumas de renglones y columnas
print("Suma de renglones:", suma_renglones)
print("Suma de columnas:", suma_columnas)
