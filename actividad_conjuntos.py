# ANALISIS DE MATRICULAS DEL CENTRO DE FORMACION

# CREAR LOS CONJUNTOS DE APRENDICES POR PROGRAMA

curso_python_={"Ana","Luis","Marta","Carlos","Sofia","Pedro"}
curso_java={"Luis","Carlos","Pedro","Laura","Diego"}
curso_bd={"Marta","Sofia","Laura","Ana","Miguel"}



# union: total de aprendices unicos en los tres programas

union_programas=curso_java | curso_java | curso_bd
print("Aprendices unicos en los tres programas:")
print(union_programas)
print("Total de aprendices:",len(union_programas))


# interseccion: aprendices que estudian Python y Java
# pero no estan en BD

python_java=curso_python_ & curso_java
python_java_sin_bd=python_java - curso_bd

print("Aprendices en Python y Java pero no en BD:")
print(python_java_sin_bd)


# APRENDICES MATRICULADOS EN EXACTAMENTE DOS PROGRAMAS

python_java_sin_bd= (curso_python_ & curso_java) - curso_bd
python_bd_sin_java= (curso_python_ & curso_bd) - curso_java
java_bd_sin_python= (curso_java & curso_bd) - curso_python_
exactamente_dos=python_java_sin_bd | python_bd_sin_java | java_bd_sin_python

print("Aprendices matriculados en exactamente dos programas:")
print(exactamente_dos)


# LISTA DE INSCRIPCIONES CON DUPLICADOS

inscripciones=["Ana","Luis","Ana","Marta","Carlos","Luis","Sofia","Pedro","Ana"]

# CONVERTIR LA LISTA EN CONJUNTO PARA ELIMINAR DUPLICADOS

inscripciones_unicas=set(inscripciones)

print("Inscripciones sin duplicados:")
print(inscripciones_unicas)


# DICCIONARIO PARA CONTAR LOS PROGRAMAS DE CADA APRENDIZ

conteo_programas={}

# RECORRER LA UNION DE TODOS LOS APRENDICES

for aprendiz in union_programas:

    cantidad=0

    if aprendiz in curso_python_:
        cantidad=cantidad+1

    if aprendiz in curso_java:
        cantidad=cantidad+1

    if aprendiz in curso_bd:
        cantidad=cantidad+1

    conteo_programas[aprendiz]=cantidad

print("Cantidad de programas por aprendiz:")
print(conteo_programas)


# BONUS: APRENDICES MATRICULADOS EN LOS TRES PROGRAMAS

tres_programas=curso_python_ & curso_java & curso_bd

print("Aprendices matriculados en los tres programas:")
print(tres_programas)