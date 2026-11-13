print("hola mundo")
#tipo de escritura de las variables-----------------------------------------------------------------------------------------------
#camelCase
aprendizSena="SENA"

#pascal Case
AprendizSena="SENA"

#snake_case
aprendiz_sena="SENA"

#reglas de variables 
#no se puede iniciar con numero una variable,Nombre es diferente a nombre, no se puede usar palabras reservadas, no se puede usar caracteres especiales,
# no se puede usar espacios, no se puede usar tildes, no se puede usar ñ,no se puede usar mayusculas en el medio de la variable, no se puede usar guion 
# bajo al inicio de la variable, no se puede usar guion bajo al final de la variable


#tipos de datos --------------------------------------------------------------------------------------------------------------------
# estructuras-----------------------------------------------------------------------------------------------------------------------
nombre="Aleja" #string
print(type(nombre))

edad=19
print(type(edad)) #int

altura=1.68
print(type(altura)) #float

activo=True
print(type(activo)) #bool

lista=["python","javasacript","java"] 
print(type(lista)) #list

conjunto={"Html","Css","java"}
print(type(conjunto)) #set

tupla =("python","javasacript")
print(type(tupla)) #tuple

diccionario={"nombre":"Aleja","edad":19,"altura":1.68}
print(type(diccionario)) #dict

rango=range(5)
print(type(rango)) #range


#castear o conversion de tipo de datos (cambiar el tipo de tipo de dato)--------------------------------------------------------------------------------------------------------------------
#castear de int a string

telefono= 3213782511
print(type(telefono),telefono)
telefono_str=str(telefono)
print(type(telefono_str),telefono_str)

#casteo de string a int
cedula="1052411118" #string
print(type(cedula),cedula)

cedula_int=int(cedula) #int
print(type(cedula_int),cedula_int)

#casteo de bool a int (0 falso, 1 verdadero)
matriculado= True
print(type(matriculado))

matriculado_int=int(matriculado)
print(type(matriculado_int),matriculado_int)


#casteo de int a bool (0 falso, 1 verdadero)
activo=0
print(type(activo),activo)
activo_bool=bool(activo)
print(type(activo_bool),activo_bool)


# casteo de un bool afloat (0.0 falso, 1.0 verdadero)
beneficiaario= False
print(type(beneficiaario),beneficiaario)
beneficiaario_float=float(beneficiaario)
print(type(beneficiaario_float),beneficiaario_float)   

# casteo de float (decimal) a int (entero)
promedio=4.13
print(type(promedio),promedio)
promedio_int=int(promedio)
print(type(promedio_int),promedio_int)  

#casteo de int a float(decimal)
edad=19
print(type(edad),edad)
edad_float=float(edad)
print(type(edad_float),edad_float)

#comentarios de solo una linea(#)

#identacion
#con un condicional if

if 5>2:
    print("5 es mayor que 2") 
else:
    print("5 no es mayor que 2")
    
# entrada de datos con input
#concatenar es unir dos o mas cadenas de texto
nombre_completo=input("Ingrese su nombre completo: ");
programa=input("cual es tu  programa de formacion: ");

#salida de datos output
print("Hola ", nombre_completo)
print("Tu programa de formacion es: ", programa)
print ("Hola  mi nombre es: "+ nombre_completo + " y pertenezco al programa: "+ programa)

#impresion con formato f-string

print(f"Hola, mi nombre es {nombre_completo} y estoy en el programa  {programa}")