
# Crear un vector con 30 numeros
vector_original = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62]


# Crear un vector vacío para almacenar los resultados
vector_resultante = []

# Elevar al cuadrado cada valor en el vector original y almacenar el resultado en el vector resultante
for numero in vector_original:
    resultado = numero ** 2
    vector_resultante.append(resultado)

# Imprimir el vector original y el vector resultante
print("Vector Original:", vector_original)
print("Vector Resultante:", vector_resultante)
