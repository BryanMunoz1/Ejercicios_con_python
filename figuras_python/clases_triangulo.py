# *****
# Centro de biotecnologia agropecuaria
# Ficha: 2877795
# Aprendiz: Bryan Muñoz
# Version: Python312
# Fecha: 20/05/2024
# *****

class Triangulo:
    # Constructor de la clase Triangulo
    def __init__(self, lado1=0, lado2=0, lado3=0, base=0, altura=0):
        # Inicializa los atributos de la clase
        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3
        self._base = base
        self._altura = altura

    # Métodos setter y getter para el lado1
    def set_lado1(self, lado1):
        self._lado1 = lado1
    def get_lado1(self):
        return self._lado1

    # Métodos setter y getter para el lado2
    def set_lado2(self, lado2):
        self._lado2 = lado2
    def get_lado2(self):
        return self._lado2 

    # Métodos setter y getter para el lado3
    def set_lado3(self, lados3):
        self._lado2 = lados3
    def get_lado3(self):
        return self._lado3 

    # Métodos setter y getter para la base
    def set_base(self, base):
        self._base = base
    def get_base(self):
        return self._base

    # Métodos setter y getter para la altura
    def set_altura(self, altura):
        self._altura = altura
    def get_altura(self):
        return self._altura

    # Método para calcular el área del triángulo
    def calcular_area(self):
        if self._base and self._altura:
            return self._base * self._altura / 2
        else:
            return "Faltan la base y/o la altura para calcular el área."

    # Método para calcular el perímetro del triángulo
    def calcular_perimetro(self):
        if self._lado1 and self._lado2 and self._lado3:
            return self._lado1 + self._lado2 + self._lado3
        else:
            return "Faltan uno o más lados para calcular el perímetro."

# Bucle principal del programa
while True:
    print("\nMenu:")
    print("1. Calcular el área del triángulo")
    print("2. Calcular el perímetro del triángulo")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        base = float(input("Digite la base del triangulo: "))
        altura = float(input("Digite la altura del triangulo: "))
        triangulo = Triangulo(base=base, altura=altura)
        print("El área del triangulo es:", triangulo.calcular_area())
    elif opcion == "2":
        lado1 = float(input("Digite el primer lado del triangulo: "))
        lado2 = float(input("Digite el segundo lado del triangulo: "))
        lado3 = float(input("Digite el tercer lado del triangulo: "))
        triangulo = Triangulo(lado1=lado1, lado2=lado2, lado3=lado3)
        print("El perimetro del triangulo es:", triangulo.calcular_perimetro())
    elif opcion == "3":
        print("proseso finalizado...")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
