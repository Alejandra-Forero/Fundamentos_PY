
#---------------------FUNCIONES------------------

# las funciones son utilizadas cuando se repiten tareas y asi "reciiclar un bloque de codigo"  de define con def 


#estructura 
#declarar o definir uhna funcion 

def nombre_funcion():
    print("Hola soy una funcion")
    
#llamar o invocar una funcion 

nombre_funcion()

#funciones con parametros de entrada

def saludar(nombre, apellido, ficha=3233140):
    print( f"Hola, {nombre} {apellido} de la ficha {ficha} bienvenido a la programacion con python" )
    
saludar("Alejandra","Forero")
saludar("Valentina","Avellaneda",12130789)
saludar("Kevin","Huertas")
saludar( 12130789,"Perez","Liliana")

#Diligenciar los argumentos en diferente orden
saludar(ficha= 321331258,apellido="Perez",nombre="Liliana")

#funcion con tipo de dato  lista como argumento de entrada

#ver o read aprendices 
def imprimir_aprendiz (lista_aprendices, ficha):
    for aprendiz in lista_aprendices:
        print(f" el aprendiz {aprendiz}, esta en la ficha {ficha}")
        
aprendices_3233140=["Luisa","Angela","Mariana" ]
aprendices_2314564=["cesar","sofia","camila" ]

imprimir_aprendiz(aprendices_3233140,"3233140")
imprimir_aprendiz(aprendices_2314564,"0987655")

#agregar aprendiz nuevo

def agregar_aprendices(ficha,aprendiz):
    ficha.append(aprendiz)
    print(f"el aprendiz {aprendiz} a sido agregado exitosamente a la ficha {ficha}")
    
agregar_aprendices(aprendices_3233140,"juana")
agregar_aprendices(aprendices_2314564,"Cristina")
    
#modificar aprendiz

def modificar_aprendiz(ficha,aprendiz_viejo,aprendiz_nuevo):

    if aprendiz_viejo in ficha:
        indice_aprendiz=ficha.index(aprendiz_viejo)#busca el indice
        ficha[indice_aprendiz]=aprendiz_nuevo  #modifica el aprendiz
        print (f"el aprendiz ha sido moficicado exitosamente, {ficha}")
    else:
        print(f"el aprendiz {aprendiz_viejo}, no se encuetra en la la ficha")

modificar_aprendiz(aprendices_3233140,"Angela","Mauren")
modificar_aprendiz(aprendices_2314564,"sofia", "laura")

#eliminar un aprendiz (delete)

def eliminar_aprendiz(ficha,aprendiz_borrado):
    if aprendiz_borrado in ficha:
        ficha.remove(aprendiz_borrado)#borra al aprendiz
        print(f"el aprendiz {aprendiz_borrado} ha sido eliminado exitosamente de la ficha {ficha}")
        
    else:
        print(f"el aprendiz {aprendiz_borrado} no se encuentra en la ficha")
        
eliminar_aprendiz(aprendices_3233140, "Mauren")


#APLICACION DE CONSOLA PARA GESTIONAR APRENDICES


ficha_nueva=[]
opcion = int(input("Selecciona una Opcion: \n 1. Agregar Aprendiz \n 2. Modificar Aprendiz \n 3. Eliminar Aprendiz \n 4. Imprimir Aprendices \n 5. Salir \n"))
while opcion !=5:
    if opcion == 1:
        nuevo_aprendiz = input("Ingrese el Nombre del Nuevo Aprendiz:  ").capitalize()
        
        agregar_aprendices(ficha_nueva, nuevo_aprendiz)
    elif opcion == 2:
        aprendiz_viejo = input("Ingrese el Nombre el Aprendiz a Modificar:  ").capitalize()
        aprendiz_nuevo = input("Ingrese el Nuevo Nombre del Aprendiz:  ").capitalize()
        
        modificar_aprendiz(ficha_nueva, aprendiz_viejo, aprendiz_nuevo)
    elif opcion == 3:
        aprendiz_eliminado = input("Ingrese el Nombre del Aprendiz a Eliminar:  ").capitalize()
        
        eliminar_aprendiz(ficha_nueva, aprendiz_eliminado)
    elif opcion == 4:
        imprimir_aprendiz(ficha_nueva)
    else:
        print("Opcion invalida")
        
    opcion = int(input("Selecciona una Opcion: \n 1. Agregar Aprendiz \n 2. Modificar Aprendiz \n 3. Eliminar Aprendiz \n 4. Imprimir Aprendices \n 5. Salir \n"))
        