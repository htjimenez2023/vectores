# Crear un vector con 20 números
vector_original = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 52,55, 58,61]

# Crear un vector vacío para almacenar los números en orden inverso
vector_inverso = []

# Recorrer el vector original en orden inverso y almacenar los números en el vector inverso
for numero in reversed(vector_original):    vector_inverso.append(numero)
# Imprimir el vector inverso
print("Vector Original:", vector_original)
print("Vector Inverso:", vector_inverso)
