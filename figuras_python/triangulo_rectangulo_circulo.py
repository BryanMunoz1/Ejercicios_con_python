# *****
# Centro de biotecnologia agropecuaria
# Ficha: 2877795
# Aprendiz:Bryan Muñoz
# Version: Python312
# Fecha: 20/05/2024
# *****


import math
from colorama import Fore, init
class Circulo:
    """
    Clase para representar un círculo.
    """
    def __init__(self, radio):
        """
        Inicializa un objeto de la clase Circulo con un radio dado.
        """
        self._radio = radio

    def set_radio(self, radio):
        """
        Establece el radio del círculo.
        """
        self._radio = radio

    def get_radio(self):
        """
        Devuelve el radio del círculo.
        """
        return self._radio

    def calcular_area(self):
        """
        Calcula y devuelve el área del círculo.
        """
        return math.pi * (self._radio ** 2)

    def calcular_perimetro(self):
        """
        Calcula y devuelve el perímetro del círculo.
        """
        return 2 * math.pi * self._radio


class Rectangulo:
    """
    Clase para representar un rectángulo.
    """
    def __init__(self, base=0, altura=0):
        """
        Inicializa un objeto de la clase Rectangulo con una base y altura dadas.
        """
        self._base = base
        self._altura = altura

    def set_base(self, base):
        """
        Establece la base del rectángulo.
        """
        self._base = base

    def get_base(self):
        """
        Devuelve la base del rectángulo.
        """
        return self._base

    def set_altura(self, altura):
        """
        Establece la altura del rectángulo.
        """
        self._altura = altura

    def get_altura(self):
        """
        Devuelve la altura del rectángulo.
        """
        return self._altura

    def calcular_area(self):
        """
        Calcula y devuelve el área del rectángulo.
        """
        return self._base * self._altura

    def calcular_perimetro(self):
        """
        Calcula y devuelve el perímetro del rectángulo.
        """
        return 2 * (self._base + self._altura)


class Triangulo:
    """
    Clase para representar un triángulo.
    """
    def __init__(self, lado1=0, lado2=0, lado3=0):
        """
        Inicializa un objeto de la clase Triangulo con los lados dados.
        """
        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3

    def set_lado1(self, lado1):
        """
        Establece el primer lado del triángulo.
        """
        self._lado1 = lado1

    def get_lado1(self):
        """
        Devuelve el primer lado del triángulo.
        """
        return self._lado1

    def set_lado2(self, lado2):
        """
        Establece el segundo lado del triángulo.
        """
        self._lado2 = lado2

    def get_lado2(self):
        """
        Devuelve el segundo lado del triángulo.
        """
        return self._lado2 

    def set_lado3(self, lado3):
        """
        Establece el tercer lado del triángulo.
        """
        self._lado3 = lado3

    def get_lado3(self):
        """
        Devuelve el tercer lado del triángulo.
        """
        return self._lado3 

    def calcular_area(self):
        """
        Calcula y devuelve el área del triángulo.
        """
        try:
            if self._lado1 and self._lado2 and self._lado3:
                # Calcular el área utilizando la fórmula de Herón
                s = (self._lado1 + self._lado2 + self._lado3) / 2
                area = math.sqrt(s * (s - self._lado1) * (s - self._lado2) * (s - self._lado3))
                return area
            else:
                raise ValueError("Faltan uno o más lados para calcular el área.")
        except ValueError as e:
            return str(e)

    def calcular_perimetro(self):
        """
        Calcula y devuelve el perímetro del triángulo.
        """
        try:
            if self._lado1 and self._lado2 and self._lado3:
                return self._lado1 + self._lado2 + self._lado3
            else:
                raise ValueError("Faltan uno o más lados para calcular el perímetro.")
        except ValueError as e:
            return str(e)


while True:
    print(f"{Fore.GREEN}\nMenu:{Fore.RESET}")
    print(f"1. Calcular el área del {Fore.RED}triángulo{Fore.RESET}")
    print(f"2. Calcular el perímetro del {Fore.RED}triángulo{Fore.RESET}")
    print(f"3. Calcular el área del {Fore.MAGENTA}rectángulo{Fore.RESET}")
    print(f"4. Calcular el perímetro del {Fore.MAGENTA}rectángulo{Fore.RESET}")
    print(f"5. Calcular el área del {Fore.YELLOW}círculo{Fore.RESET}")
    print(f"6. Calcular el perímetro del {Fore.YELLOW}círculo{Fore.RESET}")
    print(f"7. SALIR:")

    opcion = input(f"{Fore.GREEN}Seleccione una opción:{Fore.RESET}")

    if opcion == "1":
        lado1 = float(input("Digite el primer lado del triángulo: "))
        lado2 = float(input("Digite el segundo lado del triángulo: "))
        lado3 = float(input("Digite el tercer lado del triángulo: "))
        triangulo = Triangulo(lado1, lado2, lado3)
        print(f"El área del triángulo es: {triangulo.calcular_area()}")
    elif opcion == "2":
        lado1 = float(input("Digite el primer lado del triángulo: "))
        lado2 = float(input("Digite el segundo lado del triángulo: "))
        lado3 = float(input("Digite el tercer lado del triángulo: "))
        triangulo = Triangulo(lado1, lado2, lado3)
        print(f"El perímetro del triángulo es: {triangulo.calcular_perimetro()}")
    elif opcion == "3":
        base = float(input("Digite la base del rectángulo: "))
        altura = float(input("Digite la altura del rectángulo: "))
        rectangulo = Rectangulo(base, altura)
        print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    elif opcion == "4":
        base = float(input("Digite la base del rectángulo: "))
        altura = float(input("Digite la altura del rectángulo: "))
        rectangulo = Rectangulo(base, altura)
        print(f"El perímetro del rectángulo es: {rectangulo.calcular_perimetro()}")
    elif opcion == "5":
        radio = float(input("Digite el radio del círculo: "))
        circulo = Circulo(radio)
        print(f"El área del círculo es: {circulo.calcular_area()}")
    elif opcion == "6":
        radio = float(input("Digite el radio del círculo: "))
        circulo = Circulo(radio)
        print(f"El perímetro del círculo es: {circulo.calcular_perimetro()}")
    elif opcion == "7":
        print("Proceso finalizado...")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
