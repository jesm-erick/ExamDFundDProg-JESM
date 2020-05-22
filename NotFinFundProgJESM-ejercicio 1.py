def NotFinFundProgJESM ():
    #Datos de entrada
    nota1=int(input("ingrese la nota 1: "))
    nota2=int(input("iingrese la nota2: "))
    nota3=int(input("ingrese la nota 3: "))
    trabajo_final=int(input("ingrese el trabajo final: "))
    #Proceso
    nota_final=(nota1*0.10)+(nota2*0.15)+(nota3*0.25)+(trabajo_final*0.50)
    #Datos de salida 
    print (f"la nota final es: {nota_final}")

NotFinFundProgJESM ()