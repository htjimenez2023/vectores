def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    total = sum(notas)
    promedio = total / len(notas)
    return promedio

def mostrar_informacion_estudiantes(estudiantes):
    for estudiante in estudiantes:
        nombre = estudiante["nombre"]
        notas = estudiante["notas"]
        promedio = calcular_promedio(notas)
        print("Nombre del estudiante:", nombre)
        print("Notas:", notas)
        print("Promedio:", promedio)
        print("")

# Ejemplo de uso con varios estudiantes
estudiantes = [
    {"nombre": "Miguel Arauz", "notas": [78, 85, 90, 95, 92]},
    {"nombre": "Luiz Saldana", "notas": [85, 79, 95, 90, 88]},
    {"nombre": "Sonia Lezcano", "notas": [95, 88, 80, 95, 90]},
    {"nombre": "Solangel Navarro","notas":[85, 90, 98, 88, 79]},
]

mostrar_informacion_estudiantes(estudiantes)
