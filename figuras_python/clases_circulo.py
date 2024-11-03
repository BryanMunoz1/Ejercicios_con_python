# *****
# Centro de biotecnologia agropecuaria
# Ficha: 2877795
# Aprendiz:Bryan Muñoz
# Version: Python312
# Fecha: 20/05/2024
# *****

import math

class Circulo:
    # La clase Circulo define un círculo con un radio dado.
    def __init__(self, radio):  # Inicializa el objeto Circulo con un radio.
        self._radio = radio

    def set_radio(self, radio):
        # Establece el radio del círculo.
        self._radio = radio

    def get_radio(self):
        # Devuelve el radio del círculo.
        return self._radio

    def calcular_area(self):
        # Calcula y devuelve el área del círculo.
        return math.pi * (self._radio ** 2)

    def calcular_perimetro(self):
        # Calcula y devuelve el perímetro del círculo.
        return 2 * math.pi * self._radio

# Bucle principal del programa.
while True:
    print("\nMenu:")
    print("1. Área del círculo")
    print("2. Perímetro del círculo")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        radio = float(input("Digite el radio del círculo: "))
        circulo1 = Circulo(radio)  # Crea un objeto Circulo con el radio dado.
        print("El área del círculo es:", circulo1.calcular_area())  # Imprime el área del círculo.

    elif opcion == "2":
        radio = float(input("Digite el radio del círculo: "))
        circulo2 = Circulo(radio)  # Crea un objeto Circulo con el radio dado.
        print("El perímetro del círculo es:", circulo2.calcular_perimetro())  # Imprime el perímetro del círculo.
    
    elif opcion == "3":
        print("Saliendo del programa...")  # Imprime un mensaje de salida y termina el programa.
        break

    else:
        print("Opción no válida. Por favor, intente de nuevo.")  # Imprime un mensaje de error si la opción no es válida.
