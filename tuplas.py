# ----------------------------TUPLAS ----------------------------

#ESTRUCTURA DE UNA TUPLA
#INDICE:


tupla=("elemento_1","elemento_2","elemento_3")
print(type(tupla))

tupla_2="a", "b", "c"
print(type(tupla_2))

tupla_3=("Hola",)
print(type(tupla_3))

tupla_4=tuple ("Holis")
print(type(tupla_4))

tupla_mixta=("hola", 123, True, [1,2,3])
print(tupla_mixta)

#TUPLAS APRENDICES ADSO

aprendices=("Dayana","jhon" ,"oscar", "luismi", "pepito", "pepito")
print(aprendices)

#acceder a un elemento de la tupla
print(aprendices[2])

#modificar un elemento de la tupla
"""no es posible cambiar valores e la tupla son inmutbles
aprendices[0]="Alejaa:)"
print(aprendices)"""


#Consultar rangos de elementos en las tuplas

print(aprendices[0:3])


#concatenar tuplas
tupla_uno=("1,2,3,")
tupla_dos=("4,5,6")
 
tupla_suma=tupla_uno + tupla_dos
print(tupla_suma)

#multiplicaion de tubla
tupla_multiplicar=tupla_uno*4 
print(tupla_multiplicar)

#metodos de las tuplas

#medir longitud de una tupla .len()
print(len(aprendices)) 

#CONTAR ELEMENTOS REPETIDOS
print(aprendices.count("pepito"))


#obtener el indice de un elemento

print(aprendices.index("luismi"))

#modificar una tupla convirtiendola en lista

lenguajes=("JavaScript","html","css")
print(type(lenguajes))

lista_lenguajes=list(lenguajes)
print(type(lista_lenguajes))

lista_lenguajes.append("python")
print(lista_lenguajes)

lenguajes=tuple(lista_lenguajes)
print(type(lenguajes))
#BUSQUEDA DE ELEMENTOS CON IN
print("python" in lenguajes)


if "c++" in lenguajes:
    print("si fue encontrado htmnl")
else:
    print("no fue encontrado")
    
    #empaquetar tuplas
    
programa_1="adso"
programa_2="SST"
programa_3="topograffia"

tupla_programas=(programa_1 , programa_2, programa_3)
print(type(tupla_programas),(tupla_programas))

#DESEMPAQUETAR TUPLAS

tupla_ciudades=("Duitama", "Sogamoso", "Medellin")
ciudad_1,ciudad_2,ciudad_3=tupla_ciudades
print(ciudad_1) #duitama
print(ciudad_2) #Sogamoso
print(ciudad_3) #medellin


#iterrar o recorrer una tupla con for

for ciudad in tupla_ciudades:
    print(ciudad)
