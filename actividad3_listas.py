"""Actividad 3: Gestión de Lista de Reproducción Musical
1. Crea actividad3_listas.py. Declara una lista canciones con 5 nombres de canciones
de tu género favorito.
2. Aplica los siguientes métodos en orden y muestra el estado de la lista después de
cada uno: append() para agregar una canción nueva al final; insert() para agregar
otra canción en la segunda posición; extend() para fusionar con esta lista: ["Bonus
Track 1", "Bonus Track 2"].
3. Usa remove() para eliminar una canción por su nombre y pop() para eliminar la
última canción, guardando el valor eliminado e imprimiéndolo.
4. Usa sort() para ordenar la lista alfabéticamente y muéstrala ordenada.
5. Responde estas preguntas usando métodos: ¿Cuántas canciones tiene la playlist?
¿En qué posición está la primera canción que agregaste? ¿Cuántas veces aparece
el string 'Bonus Track 1'?"""


canciones = [
    "Monaco",
    "Punto_40",
    "Tu_con_el",
    "Loco_paranoico",
    "Bokete"
]

print("=== Lista de reproducción inicial ===")
print(canciones)
print()

canciones.append("EEO")
print(f"se agrega una nueva cancion al final {canciones}")
print()

canciones.insert(0, "Ninio")
print(f"se agrega una cancion en la posicion 0 {canciones}")
print()

canciones_extras = ["cybertruck", "120"]
canciones.extend(canciones_extras)
print(f"se agrega canciones de otra lista {canciones}")
print()

canciones.remove("Monaco")
print(f"elimina una cancion de la lista {canciones}")
print()


cancion_eliminada = canciones.pop()
print(canciones)
print("Canción eliminada con pop():", cancion_eliminada)
print()

canciones.sort()
print(f"ordena alfabeticamente {canciones}")
print()


# 5. Responder las preguntas usando métodos
print("=== Respuestas a las preguntas ===")

# ¿Cuántas canciones tiene la playlist?
print("¿Cuántas canciones tiene la playlist?", len(canciones))

# ¿En qué posición está la primera canción que agregaste?
print("¿En qué posición está la primera canción que agregaste ('EEO')?", canciones.index("EEO"))

# ¿Cuántas veces aparece 'cybertruck'?
print("¿Cuántas veces aparece 'cybertruck'?", canciones.count("cybertruck"))

print(canciones)
