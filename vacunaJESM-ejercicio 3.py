def vacunaJESM ():
    #Datos de entrada
    edad=int(input("Ingrese la edad de la persona: "))
    sexo=str(input( "Ingrese su sexo M / F: " ))
    #proceso y Datos de salida
    if edad>=70:
        print(f"A usted se le aplicara el tipo C por tener { edad } años de edad ")
    if edad>=16 and edad<=69 and sexo== "M" :
        print(f"A usted se le aplicara el tipo A por tener { edad } años de edad, por ser varon" )
    if edad>=16 and edad<=69 and sexo== "F" :
        print(f"A usted se le aplicara el tipo B por tener { edad } años de edad, por ser mujer" )
    if edad<=16:
        print(f"A usted se le aplicara el tipo A por tener { edad } años de edad" )
        
vacunaJESM ()


       