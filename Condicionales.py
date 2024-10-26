# Ejemplo de función para determinar si una persona es mayor de edad

def es_mayor_de_edad(edad):
    """
    Función que determina si una persona es mayor de edad.
    
    Parámetros:
    edad (int - integer - entero): La edad de la persona.
    
    Retorna:
    bool: True si es mayor de edad, False si no. True=verdadero, False=falso

    >= es el simbolo que significa mayor o igual
    """
    if edad >= 18:  # Verificar si la edad es mayor o igual a 18
        print("Es mayor de edad")
        return True  # Retorna True si es mayor de edad
    else: # Si no es mayor o igual a 18 else significa "si no"
        print("Es menor de edad")
        return False  # Retorna False si no es mayor de edad

# Ejemplo de uso de la función

edad_usuario = 20  # Cambia este valor para probar con diferentes edades
print("Edad del usuario:", edad_usuario)
resultado = es_mayor_de_edad(edad_usuario)

# Imprimir el resultado
print("¿Es mayor de edad?", resultado)


""" 
Nivel básico:
Verificar si un número es positivo, negativo o cero
Descripción: Crea un programa que pida al usuario un número y verifique si es positivo, negativo o cero.

Determinar si un estudiante aprobó o no
Descripción: Crea un programa que pida la calificación de un estudiante y determine si ha aprobado (60 o más) o no.


Nivel intermedio:
Comprobar si un número es par o impar
Descripción: Crea un programa que pida al usuario un número y determine si es par o impar.

Verificar si un número está dentro de un rango
Descripción: Crea un programa que pida al usuario un número y verifique si está en el rango de 1 a 10 (inclusive). 

Nivel Avanzado:

Clasificación de Números
    Descripción: Crea una función que reciba una lista de números enteros y clasifique cada número como "positivo", "negativo" o "cero". La función debe devolver un diccionario que contenga el conteo de cada categoría.

    Requisitos:

    Utilizar if, elif y else para clasificar los números.
    Deberá considerar si el número es impar o par, y agregar esta información al diccionario.

Cálculo de Tarifas de Envío
    Descripción: Diseña una función que calcule la tarifa de envío basada en el peso del paquete y el destino. La tarifa debe ser calculada usando las siguientes reglas:

    Menos de 1 kg: $5
    De 1 a 5 kg: $10
    Más de 5 kg: $20
    Si el destino es internacional, sumar un recargo del 50% al costo total.
    Requisitos:

Usa if y else para determinar el costo según el peso.
Usa if adicional para comprobar si el envío es internacional y calcular el recargo correspondiente.
"""