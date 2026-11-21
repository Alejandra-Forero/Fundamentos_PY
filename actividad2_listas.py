"""1. Crea actividad2_listas.py con la siguiente lista de temperaturas registradas durante
dos semanas (14 días): temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18,
20, 22, 19].
2. U  sa indexación para imprimir la temperatura del primer día, el último día, el día 7
(mitad) y el penúltimo día, usando tanto índices positivos como negativos.
3. Usa slicing para extraer e imprimir: la primera semana (días 1–7), la segunda
semana (días 8–14), solo los días pares de toda la quincena y la lista de
temperaturas en orden invertido.
4. Calcula e imprime la temperatura promedio de cada semana por separado usando
sum() y len() aplicados a los slices."""


temperaturas=[18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]
print(f"la temperatura del primer dia es, {temperaturas[0]}") #imprime la temperatura del dia 1,indice 0 
print(f"la temperatura del dia 7 es, {temperaturas[6]}" ) #imprime la temperatura del dia 7. indice 6
print(f"la temperatura del dia 14 es, {temperaturas[13]}" ) #imprime la temperatura del dia 14,indice 13


print(f" las temperaturas de la primera semana corresponden a: {temperaturas[0:7]}") #imprime la primera semana
print(f" las temperaturas de la segunda semana corresponden a: {temperaturas[7:14]}") #imprime la segunda semana
print(f" las temperaturas de los dias pares corresponden a: {temperaturas[0::2]}") #imprime los dias pares

promedio_1 = round(sum(temperaturas[0:7]) / 7,2)#promedio semana 1
promedio_2 = sum((temperaturas[7:14]) / 7,2 )#promedio semana 1
print(promedio_1)  
print(promedio_2)


semana_1 = temperaturas[0:7]
print(semana_1)


#5. Bonus: Determina cuál de las dos semanas tuvo mayor temperatura promedio y muestra el resultado con un mensaje descriptivo.
if promedio_1 > promedio_2:
    print(f"la semana con mayor promedio es la semana1 1 con un promedio, {promedio_1}")
else:
    print(f"la semana con mayor opromedio es la semana 2 con un promedio de, {promedio_2}")
    
    
