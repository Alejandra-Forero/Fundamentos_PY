#SENTENCIA MATCH--------------------
#MATCH DIAS DE LA SEMANA 

"""dia=int(input("ingrese el numero del dia de la semana:  "))

match dia:
    case 1:
        print("lunes")
    case 2:
        print("martes")
    case 3:
        print("lunes")
    case 4:
        print("jueves")    
    case 5:
        print("viernes")
    case 6:
        print("sabado")
    case 7:
        print("Domingo")
    case _:
        print("el id no es valido")"""
        
        
#EJERCICIO FALTAS APRENDICES SENA

falta_aprendiz=input("ingrese la falta del aprendiz:   ").lower()

match falta_aprendiz:
    case "comer":
        print("llamado de atencion por comer en formacion")
    
    case "inpuntualidad":
        print("llamado de atencion por llegar tarde")
    
    case "uniforme":
        print("llamado de atencion por no portar el uniforme")
        
    case "jugar":
        print("llamado dew atencion por jugar durante la formacion")
        
    case _:
        print("aprendiz sin faltas")