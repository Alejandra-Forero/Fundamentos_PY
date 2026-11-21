#Inventario de la Tienda Escolar
#1. Crea actividad1_listas.py. Declara una lista llamada productos con al menos 6 artículos de una tienda escolar (cuadernos, lapiceros, etc.), usando strings.

#2. Declara una segunda lista precios con los precios correspondientes a cada producto (usa floats). Asegúrate de que ambas listas tengan el mismo número de elementos.
#3. Declara una tercera lista cantidades con la cantidad disponible de cada artículo (enteros).
#4. Imprime las tres listas completas y luego usa len() para mostrar cuántos productos tiene el inventario.
#5. Muestra el tipo de dato de la lista usando type() y el tipo del primer elemento usando type(productos[0]). Explica la diferencia en los comentarios de tu código.

productos=["lapiz","caja de colores","marcadores","temperas","cuadernos","reglas"]
precio=[1.500,12.000,15.000, 8.000, 3.000, 3.500]
cantidades=[12,10,15,8,20,34]

print(productos)
print(precio)
print(cantidades)


print(len(productos))
print(len(precio))
print(len(cantidades))

print(type(productos[0])) #STR el tipo de dato de productos es string
print(type(precio[0]))  #STR el tipo de dato de precio es float
print(type(cantidades[0])) #STR el tipo de dato de cantidad es entero





