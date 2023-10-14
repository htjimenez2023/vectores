
# crear un vector con 35 elementos diferentes
vector = list(range(1, 36))

# Imprimir el vector (0pcional)
print("vector:", vector)

# Encontrar la posicion y el elemento mayor
max_valor = max(vector)
posicion_max_valor = vector.index(max_valor)

print(f"el elemento mayor es {max_valor} y se encuentra en la posicion {posicion_max_valor}.")
