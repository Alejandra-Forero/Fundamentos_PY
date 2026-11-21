#DICCIONARIOS------------------------------------

#ESTRUCTURA DE U DICCIONARIO

diccionario={
    "clave_1" :"valor_1",
    "clave_2" : "valor_2",
    "clave_2" : "valor_3"   
}

#diccionario vacio

diccionario_vacio={}
print(type(diccionario_vacio))

#crear un diccionario con elementos
diccionario_aprendiz={
    "nombre":"Alejandra",
    "apellido":"Forero",
    "Programa":"ADSO",
    "Ficha":"3233140"
}
print(diccionario_aprendiz)

#@obtener el valor de un diccionario

print(diccionario_aprendiz["Programa"]) #entrega el valor 
#print(diccionario_aprendiz["email"])#error

print(diccionario_aprendiz.get("Programa"))

#OBTENER SOLO LAS CLAVES DEL DICCIONARIO

print(diccionario_aprendiz.keys())
#resultado obtenido dict_keys(['nombre', 'apellido', 'Programa', 'Ficha'])

print(diccionario_aprendiz.values())
#resultado obtenido dict_values(['Alejandra', 'Forero', 'ADSO', '3233140'])

#obtener clave y valor
print(diccionario_aprendiz.items())
#RESULTADO OBTENIDO  dict_items([('nombre', 'Alejandra'), ('apellido', 'Forero'), ('Programa', 'ADSO'), ('Ficha', '3233140')])

#COMO AGREGAR O CREAE UN ELEMENTO NUEVO AL DICCIONARIO

diccionario_aprendiz["correo"]="alejandravalentinaforero@gmail.com"
print(diccionario_aprendiz)

#modificar un valor del diccionario
diccionario_aprendiz["Programa"]="MINAS"
print(diccionario_aprendiz)

#METODO UPDATE PARA ACTUALIZAR

diccionario_aprendiz.update({"nombre":"valentina"}) #cambia el valor de nombre
print(diccionario_aprendiz)
diccionario_aprendiz.update({"ciudad":"Duitama"}) #crea el elemento ciudad y lo agrega al diccionario
print(diccionario_aprendiz)



#ELIMINAR ELEMENTOS----------------------------------------
#elimina el ultimo elemento
diccionario_aprendiz.popitem()
print(diccionario_aprendiz)

#elimina un elementos especificos
diccionario_aprendiz.pop("correo")
print(diccionario_aprendiz)

#eliminar todos los elementos del diccionario
#diccionario_aprendiz.clear()
#print(diccionario_aprendiz)

#comprobar pertenecia de un elemento con in
print( "Ficha" in diccionario_aprendiz)#TRUE
print( "Celular" in diccionario_aprendiz)#FALSE

if "FICHA " in diccionario_aprendiz:
    print(f" si se encuentra dentro del dioccionario ")
else:
    print("no se encuentra dentro del diccionario")

#RECORRER UN DICCIONARIO CON EL CICLO FOR 

#RECORRER SOLO LAS CLAVES(KEYS)

for clave in diccionario_aprendiz.keys():
    print(clave)

#RECORRER SOLO LOS VALORES 

for valor in diccionario_aprendiz.values():
    print(valor)
    
#RECORRER lOS VALORES Y LAS CLAVES

for clave,valor in diccionario_aprendiz .items():
    print(f"{clave},{valor}")
    
    
    

#DICCIONARIOS ANIDADOS---------------------------------------

aprendices={
    "aprendiz_1":{
        "nombre":"Sara",
        "apellido":"Quiroz",
        "Programa":"ADSO",
    },
    "aprendiz_2":{
        "nombre":"Alejandra",
        "apellido":"Forero",
        "Programa":"SST",
    },
    "aprendiz_3":{
        "nombre":"Santiago",
        "apellido":"Aguilar",
        "Programa":"Minas",
}
} 
#acceder a un valor de un diccionario anidado
print(aprendices["aprendiz_3"]["Programa"])


#ciclo for para recorrer un diccionario anidado

for aprendiz,datos in aprendices.items():
    print(f"{aprendiz}:")
    for clave,valor in datos.items():
        print(f"{clave}:{valor}")

