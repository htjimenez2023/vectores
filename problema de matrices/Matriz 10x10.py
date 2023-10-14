
import random

# Definir el tamaño de la matriz
filas = 10
columnas = 10

# Crear una matriz de 10x10 llena de números aleatorios diferentes
matriz = [[0] * columnas for _ in range(filas)]
numeros_utilizados = set()

for i in range(filas):
    for j in range(columnas):
        # Generar un número aleatorio que no se haya utilizado antes
        numero = random.randint(5, 60)  # Cambia el rango según tus necesidades
        while numero in numeros_utilizados:
            numero = random.randint(1, 100)
        matriz[i][j] = numero
        numeros_utilizados.add(numero)

# Encontrar el número mayor y su posición
numero_mayor = matriz[0][0]
posicion_mayor = (0, 0)

for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] > numero_mayor:
            numero_mayor = matriz[i][j]
            posicion_mayor = (i, j)

# Imprimir la matriz y la posición del número mayor
for fila in matriz:
    print(fila)

print(f"El número mayor es {numero_mayor} y se encuentra en la posición {posicion_mayor}")
  



