#2.Clasificación de Números: Ingresar un número entero y mostrar si es positivo, negativo o nulo (cero).

numero=int(input("Ingresa un numero: "))

if numero>0:
    print(numero,"Es positivo")
elif numero<0:
    print(numero,"Es Negativo")
else:
    print(numero,"El numero es 0")