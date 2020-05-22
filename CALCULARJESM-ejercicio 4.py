def CALCULARJESM ():
    #Datos de entrada
    numero1=float(input("ingrese el 1er numero"))
    numero2=float(input("ingrese el 2do numero"))
    operacion=str(input( "Ingrese que operacion quiere hacer: suma/resta/multiplicacion/division/potencia:"))
    #Proceso
    if operacion=="suma":
        total=numero1+numero2
    if operacion=="resta":
        total=numero1-numero2
    if operacion=="multiplicacion":
        total=numero1*numero2
    if operacion=="division":
        total=numero1/numero2
    if operacion=="potencia":
        total=numero1**numero2
    #Datos de salida
    print (f" LA RESPUESTA ES DE:: {total}")


CALCULARJESM ()








