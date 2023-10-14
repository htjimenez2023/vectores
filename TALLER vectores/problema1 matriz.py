# Definir una matriz de 5 filas y 6 columnas inicializada con ceros
matriz = [[0] * 6 for _ in range(5)]

# Pedir al usuario que ingrese los números en la matriz
for fila in range(5):
    for columna in range(6):
        numero = int(input(f"Ingrese el número en la fila {fila + 1}, columna {columna + 1}: "))
        matriz[fila][columna] = numero

# Calcular la suma de los números en la matriz
suma = 0
for fila in range(5):
    for columna in range(6):
        suma += matriz[fila][columna]

# Imprimir la matriz
print("Matriz:")
for fila in matriz:
    print(fila)

# Imprimir la suma de los números en la matriz
print(f"La suma de los números en la matriz es: {suma}")



