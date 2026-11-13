#OPERADORES ARITMETICOS--------------------------------------------------------------------------------------------------

a=10
b=3

#SUMA
suma=a+b
print(f"La suma de {a} y {b} es: {suma}")

#RESTA
resta=a-b
print(f"La resta de {a} y {b} es: {resta}")

#MULTIPLICACION
multiplicacion=a*b
print(f"La multiplicacion de {a} y {b} es: {multiplicacion}")

#DIVISION CON UN SLASH
division=a/b
print(f"La division de {a} y {b} es: {division}")

#DIVISION ENTERA CON DOBLE SLASH
division=a//b 
print(f"La division de {a} y {b} es: {division}")

#MODULO O RESIDUO DE UNA DIVISION
modulo=a%b
print(f"El modulo de {a} y {b} es: {modulo}")

#EXPONENCIACION
exponenciacion=a**b
print(f"La exponenciacion de {a} y {b} es: {exponenciacion}")   


#PRECEDENCIA DE OPERADORES (QUE SE PRIORIZA EN UNA OPERACION )-----------------------------------------------------------------

 #se prioriza primero la multiplicacion y division, luego suma y resta
resultado=a+b*3
print(f"El resultado de {a}+{b}*3 es: {resultado}")

#al poner parentesis se prioriza primero la operacion que esta dentro de los parentesis
resultado_2=(a+b)*3
print(f"El resultado de ({a}+{b})*3 es: {resultado_2}")

#se priorizo la multiplicacion
resultado_3=10*6//3
print(f"El resultado de 10*6//3 es: {resultado_3}")



ejercicio=((a+b)*(a-b)/(a*b))-((a**b)%3)
print(f"El resultado ) es: {ejercicio}")

#LIBRERIAS EN PYTHON

import math
print(math.pi) #imprime el valor de pi
print(math.e) #imprime el valor de euler
print(math.sqrt(16)) #imprime la raiz cuadrada 

import random
print(random.random()) 
