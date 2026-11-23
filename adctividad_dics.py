# Actividad: Sistema de Registro de Aprendices

# 1. Diccionario 'grupo' con al menos 4 aprendices
# Clave = número de ficha (int)
# Valor = diccionario con: nombre, edad, notas (lista de 4 floats), ciudad

grupo = {
    101: {
        "nombre": "Ana Torres",
        "edad": 19,
        "notas": [4.5, 3.8, 4.2, 4.0],
        "ciudad": "Bogotá"
    },
    102: {
        "nombre": "Carlos Méndez",
        "edad": 21,
        "notas": [2.5, 3.0, 2.8, 3.2],
        "ciudad": "Medellín"
    },
    103: {
        "nombre": "Laura Gómez",
        "edad": 18,
        "notas": [4.8, 4.5, 4.9, 4.7],
        "ciudad": "Cali"
    },
    104: {
        "nombre": "Andrés Ruiz",
        "edad": 20,
        "notas": [3.2, 2.9, 3.5, 3.0],
        "ciudad": "Barranquilla"
    }
}

# 2. Función que recibe la lista de notas y retorna el promedio
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# 3. Reporte usando .items() y un ciclo
print("=== REPORTE DE APRENDICES ===")
print()

for ficha, datos in grupo.items():
    promedio = calcular_promedio(datos["notas"])
    estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"
    
    print(f"Ficha: {ficha}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print(f"Promedio de notas: {promedio:.2f}")
    print(f"Estado: {estado}")
    print("-" * 30)

# 4. Agregar un nuevo aprendiz y actualizar la ciudad de uno existente
print()
print("=== AGREGANDO NUEVO APRENDIZ Y ACTUALIZANDO CIUDAD ===")

# Agregar nuevo aprendiz con una nueva clave de ficha
grupo[105] = {
    "nombre": "Sofía Ramírez",
    "edad": 22,
    "notas": [3.8, 4.1, 3.5, 4.0],
    "ciudad": "Pereira"
}

# Actualizar la ciudad de un aprendiz existente
grupo[102]["ciudad"] = "Cartagena"

print("Nuevo aprendiz agregado (ficha 105):", grupo[105]["nombre"])
print("Ciudad actualizada de Carlos Méndez:", grupo[102]["ciudad"])
print()

# Mostrar de nuevo el reporte incluyendo al nuevo aprendiz
print("=== REPORTE ACTUALIZADO ===")
print()

for ficha, datos in grupo.items():
    promedio = calcular_promedio(datos["notas"])
    estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"
    
    print(f"Ficha: {ficha} | Nombre: {datos['nombre']} | Edad: {datos['edad']} | "
          f"Promedio: {promedio:.2f} | Estado: {estado} | Ciudad: {datos['ciudad']}")

# 5. Bonus: Imprimir la lista de aprendices ordenada de mayor a menor promedio
print()
print("=== APRENDICES ORDENADOS POR PROMEDIO (MAYOR A MENOR) ===")
print()

# sorted() con key= para ordenar por promedio (de mayor a menor)
aprendices_ordenados = sorted(
    grupo.items(),
    key=lambda item: calcular_promedio(item[1]["notas"]),
    reverse=True
)

for ficha, datos in aprendices_ordenados:
    promedio = calcular_promedio(datos["notas"])
    print(f"Ficha: {ficha} | {datos['nombre']} | Promedio: {promedio:.2f}")