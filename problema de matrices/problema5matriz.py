
import random

# Definir las dimensiones de la matriz
filas = 5
columnas = 6

# Inicializar las contadores
ceros = 0
positivos = 0
negativos = 0

# Crear la matriz y llenarla con números aleatorios
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        numero = random.randint(-5, 15)  # Rango de números aleatorios (-5 a 15)
        fila.append(numero)
        if numero == 0:
            ceros += 1
        elif numero > 0:
            positivos += 1
        else:
            negativos += 1
    matriz.append(fila)

# Imprimir la matriz
print("Matriz:")
for fila in matriz:
    print(fila)

# Imprimir el recuento de ceros, positivos y negativos
print(f"Ceros: {ceros}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
