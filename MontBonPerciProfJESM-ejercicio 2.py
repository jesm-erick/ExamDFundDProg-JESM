def MontBonPerciProfJESM ():
    #Datos de entrada
    punt=int(input("El punto obtenido es: "))
    salario=int(input("El salario es: "))
    #Proceso
    if punt>=50 and punt<=100:
        bono_recibido=salario*0.10
    elif punt>=101 and punt<=150:
        bono_recibido=salario*0.50
    else:
        punt>=151
        bono_recibido=salario*1
    #Datos de salida
    print (f"el monto que recibira un maestro es: {bono_recibido}")

MontBonPerciProfJESM ()