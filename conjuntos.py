#CONJUNTOS SETS

#ESTRUCTURA DE UN CONJUNTO

conjunto={"elemento_1","elemento_2", "elemento_3"}
print(type(conjunto))

conjunto_2=set()
print(type(conjunto_2))

conjunto_3={}
print(type(conjunto_3))#class dict


#crear conjunto

programas={"ADSO","SST","MINERIA","ADSO","SST"}
print(programas) #no tiene en cuenta datos repetidos



#metodos de los conjuntos

frutas={"mango","guayaba","maracuya","granadilla","toronja","papaya"}

#agregar un nuevo elemento al conjunto
frutas.add("gulupa")
print(frutas)   

#eliminar un elemento del conjunto  si genera errores cuando el elemento no existe
frutas.remove("guayaba")
print(frutas)

#metodo .discard no manda errores si el elemento no existe

frutas.discard("maracuya")
print(frutas)

#metodo pop elimina un elemento aleatorio
elemento=frutas.pop()
print(elemento)
print(frutas)
#clear elimina o limpia todos los elementos
frutas.clear()
print(frutas)
#eliminar todo el conjunto con el metodo del
del frutas
#print(frutas)

#verificar la ppertenencia de un elemento en un conjunto
aprendices={"alejandra","andres","pepe"}
print("andres" in aprendices) #true
print("juanita" in aprendices) #false

#operacoines de la teoria de conjuntos
aprendices_formacion={"alejandra","maria","jennifer","adriana","diana","dayana"}
aprendices_apoyo={"diana","adriana","sebastian", "juan"}

#union exrae todos los elementos de los dos conjuntos
#union
union_aprendices=aprendices_formacion|aprendices_apoyo
print(union_aprendices)

union_aprendices_2=aprendices_apoyo.union(aprendices_formacion)
print(union_aprendices_2)

#interseccion con &

interseccion_aprendices=aprendices_formacion & aprendices_apoyo
print(interseccion_aprendices)

#.intersection
interseccion_aprendices_2=aprendices_formacion.intersection(aprendices_apoyo)
print(interseccion_aprendices_2)

#diferencia "-"
diferencia_aprendices= aprendices_formacion - aprendices_apoyo
print(diferencia_aprendices)
#diferencia .difference(set)
diferencia_aprendices_2= aprendices_formacion.difference(aprendices_apoyo)
print(diferencia_aprendices_2)

#diferencia simetrica
diferencia_simetrica_2=aprendices_formacion.symmetric_difference(aprendices_apoyo)
print(diferencia_simetrica_2)


