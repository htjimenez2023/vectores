# crear vectores A y B con 36 elementos cada uno
A = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72]
B = [72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

# crear el vector C para almacenar los resultados
C = []

# sumar los elementos de A y B y almacenar el resultado en C
for i in range(36):
    suma = A[i] + B[i]
    C.append(suma)

# Imprimir el vector resultante C
print(C)
    
    
