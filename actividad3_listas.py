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


# 1. Lista inicial
canciones = [
    "Mi Gente", "Safaera", "Ginza", "Dákiti",  "Ay Vamos"         
]
print(f"La lista inicial contiene las canciones: {canciones}")

# 2. Agregar canciones
canciones.append("Me Porto Bonito")
canciones.insert(1, "Qué Pretendes")
canciones.extend(["Bonus Track 1", "Bonus Track 2"])

print(f"se agregan 3 canciones:  {canciones}")

# 3. Eliminar canciones con remove y pop
canciones.remove("Ginza")
eliminada = canciones.pop()
print(f"Lista tras eliminar 2 canciones: {canciones}")

# 4. Ordenar alfabéticamente
canciones.sort()
print(f"Lista ordenada: {canciones}")

# 5. Preguntas
print("¿Cuántas canciones tiene la playlist?", len(canciones))
print("Posición de la primera cancion que agregaste:",canciones.index("Me Porto Bonito"))
print("Veces que aparece 'Bonus Track 1':", canciones.count("Bonus Track 1"))
