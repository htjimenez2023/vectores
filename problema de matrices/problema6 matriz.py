

# Definimos una matriz de 5x5 como una lista de listas
matriz = [[0 for _ in range(5)] for _ in range(5)]

# Llenamos la matriz con valores ingresados por el usuario
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f"Ingresa el valor en la posición ({i+1},{j+1}): "))

# Inicializamos un vector para almacenar la diagonal principal
diagonal_principal = []

# Llenamos el vector con los elementos de la diagonal principal
for i in range(5):
    diagonal_principal.append(matriz[i][i])

# Imprimimos la matriz y el vector resultante
print("Matriz:")
for row in matriz:
    print(row)
print("Diagonal Principal:")
print(diagonal_principal)
