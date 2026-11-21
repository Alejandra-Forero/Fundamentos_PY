#deben ir en corteches cuadrados               [dato_1,dato_2,dato_3]
#para modificar se utiliiza el item del dato       0     1       2


#ESTRUCTURA DE UNA LISTA

#PONER NMOMBE DE LA VARABLE
lista=[ "dato_1", "dato_2","dato_3"]
print(type(lista))
print(lista[2]) #imprime el indice que indica

#LISTA MIXTA ---------------------------------------------------------------------

lista_mixta=[" HOLAA", 3233140, 1.65, True, ["ADSO","SST", "SUPERVISION DE MINAS"] ]

#EJERCICIO LISTA DE APRENDICES SENA------------------------------------------------

aprendices=["Miguel","Sebastian","Alejandra","Jenni","Luis","lizeth"]
print(aprendices[1])

#MODIFICAR A UN ELEMENTO DE LA LISTA-----------------------------------------------

aprendices[0]="luismi"
print(aprendices)

#CONSULTAR RANGOS DE ELEMENTOS EN LAS LISTAS---------------------------------------

print(aprendices[0:4]) #toma los primero 3 items el ultimo no lo tiene en cuenta
print(aprendices[1:3])
print(aprendices[0::2])

#CONCATENAR LISTAS con + ----------------------------------------------------------

programas_tecnicos=["sistemas teleinformaticos", "Redes"]
programas_tecnologos=["ADSO","Topografia"]
programas_SENA= programas_tecnicos + programas_tecnologos
print (programas_SENA)

#EXTENDER LISTAS CON EXTEND--------------------------------------------------------

nuevos_programas_tecnicos=["inteligencia artificial","Mineria de datos", "Redes"]
programas_tecnicos.extend(nuevos_programas_tecnicos)
print(programas_tecnicos)

#MEDIR LONGITUD .LEN DE UNA LISTA--------------------------------------------------

print(len(programas_tecnicos))
print(len(aprendices))

#CONTAR ELEMENTOS REPETIDOS DE UNA LISTA--------------------------------------------
print(programas_tecnicos)
print(programas_tecnicos.count("Redes"))

#OBTENER INDICE DE UN ELEMENTO .index()---------------------------------------------

print(aprendices.index("Alejandra"))
print(programas_tecnicos.index("Mineria de datos"))
print(programas_tecnologos.index("ADSO"))

#COPIAR UNA LISTA NUEVA CON LA FUNCION .copy()----------------------------------------

nueva_lista_aprendices= aprendices.copy()
print(nueva_lista_aprendices)

#AGREGAR NUEVOS ELEMENTOS CON LA FUNCION .append(item)------------------------------

nueva_lista_aprendices.append("Adriana")
print(nueva_lista_aprendices)

#AGREGAR NUEVOS ELEMENTOS en la posicion del indice .insert()------------------------------
nueva_lista_aprendices.insert(1,"Andrea")
print(nueva_lista_aprendices)

#ELIMINAR UN ELEMENTO DE LA LISTA---------------------------------------------
    #REMOVE()elimina la primera ocurrecia de la lista
nueva_lista_aprendices.remove("lizeth")
print(nueva_lista_aprendices)
    
#ELIMINAR POR EL INDICE .pop()-------------------------------------------------------

nueva_lista_aprendices.pop(5)
print(nueva_lista_aprendices)

#.clear() limpia todos los elemenos de la lista-----------------------------
#nueva_lista_aprendices.clear()
#print(nueva_lista_aprendices)

#ORDENAR LISTAS -------------------------
#DE MANERA ASCENDENTE A-Z .sort()

nueva_lista_aprendices.sort()
print(nueva_lista_aprendices)

#DE MANERA DESENDENTE A-Z .reverse()

nueva_lista_aprendices.reverse()
print(nueva_lista_aprendices)

#BUSCAR ELEMENTOS CON EL OPERQADOR IN
if "Alejandra" in nueva_lista_aprendices:
    print ("si esta en la lista de aprendices")
else:
    print("no esta")
    
