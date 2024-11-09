#3.Verificar Navidad: Crear un programa que pida una fecha y verifique si corresponde a Navidad (25 de diciembre).
from datetime import datetime
fecha = input("Ingresa una fecha (dd/mm/aaaa): ")
try:
    fecha = datetime.strptime(fecha, "%d/%m/%Y")
    print(f"La fecha ingresada es: {fecha}")
except ValueError:
    print("Formato de fecha incorrecto. Asegúrate de usar dd/mm/aaaa.")

if fecha.day != 25 and fecha.month != 12:
    print(fecha,"La fecha no es navidad")  
else:
    print(fecha,"!Es Navidad!!!")