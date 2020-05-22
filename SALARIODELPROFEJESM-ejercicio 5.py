def SALARIODELPROFEJESM ():
    #Datos de entrada
    salario_inicial=int(input("ingrese el dato del salario en soles:   "))
    tiempo=int(input("tiempo en años:    "))
    incremento=int(input("incremento del sueldo por año en porcentaje:   "))
    sueldo=0
    año=1
    #Proceso
    paso=1
    for año in range (1,tiempo+1):
      paso=paso*(1+(incremento/100))  
    print(f"su incremento respecto al primer sueldo es:{paso}")
    salariofinal=paso*salario_inicial
    print(f"su sueldo en 06 años es:{salariofinal}")
    print(f".......................................") 
    if tiempo==1 :
        s1=1.1*salario_inicial
        print(f"su sueldo en el primer año es:{s1}")
    elif tiempo==2 :
        s1=1.1*salario_inicial
        print(f"su sueldo en el primer año es:{s1}")
        s2=1.21*salario_inicial
        print(f"su sueldo en el segundo año es:{s2}")
    elif tiempo==3 :
        s1=1.1*salario_inicial
        print(f"su sueldo el primer año es es:{s1}")
        s2=1.21*salario_inicial
        print(f"su sueldo en el segundo año es:{s2}")   
        s3=1.331*salario_inicial
        print(f"su sueldo en el tercer año es:{s3}")
    elif tiempo==4 :
        s1=1.1*salario_inicial
        print(f"su sueldo en el primer año  es:{s1}")
        s2=1.21*salario_inicial
        print(f"su sueldo el segundo año es:{s2}")   
        s3=1.331*salario_inicial
        print(f"su sueldo en el tercer año es:{s3}") 
        s4=1.4641*salario_inicial
        print(f"su sueldo en el cuarto año es:{s4}") 
    elif tiempo==5 :
        s1=1.1*salario_inicial
        print(f"su sueldo en el primer año  es:{s1}")
        s2=1.21*salario_inicial
        print(f"su sueldo el segundo año es:{s2}")   
        s3=1.331*salario_inicial
        print(f"su sueldo en el tercer año es:{s3}") 
        s4=1.4641*salario_inicial
        print(f"su sueldo en el cuarto año es:{s4}")
        s5=1.61051*salario_inicial
        print(f"su sueldo en el quinto año es:{s5}")  
    elif tiempo==6 :
        s1=1.1*salario_inicial
        print(f"su sueldo en el primer año  es:{s1}")
        s2=1.21*salario_inicial
        print(f"su sueldo el segundo año es:{s2}")   
        s3=1.331*salario_inicial
        print(f"su sueldo en el tercer año es:{s3}") 
        s4=1.4641*salario_inicial
        print(f"su sueldo en el cuarto año es:{s4}")
        s5=1.61051*salario_inicial
        print(f"su sueldo en el quinto año es:{s5}") 
        s6=1.771561*salario_inicial
        print(f"su sueldo en el sexto año es:{s6}")  
    else :
        print(f"")         
SALARIODELPROFEJESM ()