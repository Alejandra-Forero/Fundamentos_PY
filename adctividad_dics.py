#1. Crea actividad2_diccionarios.py. Construye un diccionario grupo donde cada clave sea el número de ficha (int) y el valor sea otro diccionario con los campos: nombre, edad, notas (lista de 4 floats) y ciudad. Registra al menos 4 aprendices.
#2. Escribe una formula calcular_promedio que reciba la lista de notas y retorne el promedio. Úsala al mostrar el reporte.
#3. Usando .items() y un ciclo for, imprime un reporte con: ficha, nombre, edad, promedio de notas y estado (APROBADO/REPROBADO según si el promedio >= 3.0).
#4. Agrega un nuevo aprendiz al diccionario después de crearlo, usando una nueva clave de ficha. Luego actualiza la ciudad de uno de los aprendices existentes con dicc[ficha]['ciudad'] = 'Nueva Ciudad'.
#5. Bonus: Usa sorted() con key= para imprimir la lista de aprendices ordenada de mayor a menor promedio.


# SISTEMA DE REGISTRO DE APRENDICES ----------------------------

# 1. CREAR DICCIONARIO CON 4 APRENDICES

grupo = {
    3233140: {
        "nombre": "Alejandra",
        "edad": 18,
        "notas": [4.0, 3.5, 4.2, 4.5],
        "ciudad": "Duitama"
    },
    3233141: {
        "nombre": "Sara",
        "edad": 19,
        "notas": [3.0, 3.5, 4.0, 3.8],
        "ciudad": "Tunja"
    },
    3233142: {
        "nombre": "Santiago",
        "edad": 20,
        "notas": [2.5, 3.0, 2.8, 3.2],
        "ciudad": "Paipa"
    },
    3233143: {
        "nombre": "Camila",
        "edad": 18,
        "notas": [4.5, 4.8, 4.2, 5.0],
        "ciudad": "Sogamoso"
    }
}


# 2 y 3. MOSTRAR REPORTE Y CALCULAR PROMEDIO

for ficha, datos in grupo.items():

    promedio = sum(datos["notas"]) / 4

    if promedio >= 3.0:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    print(f"Ficha: {ficha}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {estado}")


# 4. AGREGAR UN NUEVO APRENDIZ

grupo[3233144] = {
    "nombre": "Valentina",
    "edad": 19,
    "notas": [4.0, 4.2, 3.8, 4.5],
    "ciudad": "Bogota"
}

# ACTUALIZAR LA CIUDAD DE UN APRENDIZ

grupo[3233141]["ciudad"] = "Nueva Ciudad"


print("Aprendiz agregado y ciudad actualizada")


# 5. BONUS: ORDENAR DE MAYOR A MENOR PROMEDIO

promedios = []

for ficha, datos in grupo.items():
    promedio = sum(datos["notas"]) / 4
    promedios.append((promedio, ficha))

promedios.sort(reverse=True)

print("\n--- APRENDICES ORDENADOS POR PROMEDIO ---")

for promedio, ficha in promedios:

    datos = grupo[ficha]

    if promedio >= 3.0:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"


    print(f"Ficha: {ficha}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print(f"Promedio: round({promedio:.2})")
    print(f"Estado: {estado}")