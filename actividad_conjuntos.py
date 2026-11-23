    # Actividad: Análisis de Matrículas del Centro de Formación

# 1. Definir los conjuntos de aprendices por programa
python_curso = {"Ana", "Luis", "Marta", "Carlos", "Sofía"}
java_curso = {"Luis", "Carlos", "Pedro", "Laura", "Diego"}
bd_curso = {"Marta", "Sofía", "Laura", "Ana", "Miguel"}

print("=== CONJUNTOS DE APRENDICES ===")
print("Python:", python_curso)
print("Java:  ", java_curso)
print("BD:    ", bd_curso)
print()

# 2. Operaciones de conjuntos

# Total de aprendices únicos (unión triple)
todos = python_curso | java_curso | bd_curso
print("Total de aprendices únicos (unión de los 3 programas):", len(todos))
print("Aprendices únicos:", todos)
print()

# Aprendices que cursan Python Y Java simultáneamente
python_y_java = python_curso & java_curso
print("Aprendices en Python Y Java:", python_y_java)
print()

# Aprendices que están solo en Python (no en Java ni en BD)
solo_python = python_curso - java_curso - bd_curso
print("Aprendices solo en Python:", solo_python)
print()

# Aprendices que están en exactamente dos programas
en_dos = (
    (python_curso & java_curso) |
    (python_curso & bd_curso) |
    (java_curso & bd_curso)
) - (python_curso & java_curso & bd_curso)

print("Aprendices en exactamente dos programas:", en_dos)
print()

# 3. Lista con duplicados → conjunto para obtener únicos
inscripciones = ["Ana", "Luis", "Ana", "Marta", "Carlos", "Luis", "Sofía", "Pedro", "Ana"]
inscritos_unicos = set(inscripciones)

print("=== INSCRIPCIONES CON DUPLICADOS ===")
print("Lista original:", inscripciones)
print("Cantidad de aprendices únicos:", len(inscritos_unicos))
print("Aprendices únicos:", inscritos_unicos)
print()

# 4. Diccionario conteo_programas (comprensión de diccionario)
conteo_programas = {
    aprendiz: (
        (aprendiz in python_curso) +
        (aprendiz in java_curso) +
        (aprendiz in bd_curso)
    )
    for aprendiz in todos
}

print("=== CONTEO DE PROGRAMAS POR APRENDIZ ===")
for nombre, cantidad in sorted(conteo_programas.items()):
    print(f"{nombre}: {cantidad} programa(s)")
print()

# 5. Bonus: Quién está matriculado en los tres programas a la vez
en_tres = python_curso & java_curso & bd_curso
print("=== BONUS: APRENDICES EN LOS TRES PROGRAMAS ===")
print("Aprendices en Python + Java + BD:", en_tres if en_tres else "Ninguno")