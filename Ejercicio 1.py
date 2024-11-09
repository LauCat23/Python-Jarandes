#1. Mayor de Tres Números: Cargar tres números distintos por teclado y mostrar cuál es el mayor.
Numero_1=float(input("Ingresa el primer numero: "))
Numero_2=float(input("Ingresa el Segundo numero: "))
Numero_3=float(input("Ingresa el Tercer numero: "))

if Numero_1>Numero_2 and Numero_1>Numero_3:
    print(Numero_1,"ES EL NUMERO MAYOR")
elif Numero_2>Numero_1 and Numero_2>Numero_3:
    print(Numero_2,"ES EL NUMERO MAYOR")
else:
    print(Numero_1,"ES EL NUMERO MAYOR")



