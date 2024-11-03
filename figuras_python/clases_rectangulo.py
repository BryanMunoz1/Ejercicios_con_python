# *****
# Centro de biotecnologia agropecuaria
# Ficha: 2877795
# Aprendiz: Bryan Muñoz
# Version: Python312
# Fecha: 20/05/2024
# *****

class Rectangulo:
    # Inicializa la clase Rectangulo con base y altura
    def __init__(self, base=0, altura=0):
        self._base = base
        self._altura = altura

    # Establece el valor de la base del rectángulo
    def set_base(self, base):
        self._base = base

    # Obtiene el valor de la base del rectángulo
    def get_base(self):
        return self._base

    # Establece el valor de la altura del rectángulo
    def set_altura(self, altura):
        self._altura = altura

    # Obtiene el valor de la altura del rectángulo
    def get_altura(self):
        return self._altura

    # Calcula el área del rectángulo
    def calcular_area(self):
        return self._base * self._altura

    # Calcula el perímetro del rectángulo
    def calcular_perimetro(self):
        return 2 * (self._base + self._altura)

# Bucle infinito para el menú de opciones
while True:
    print("\nMenu:")
    print("1. Calcular el área del rectángulo")
    print("2. Calcular el perímetro del rectángulo")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")

    # Opción para calcular el área del rectángulo
    if opcion == "1":
        rectangulo = Rectangulo()
        base = float(input("Digite la base del rectángulo: "))
        rectangulo.set_base(base)

        altura = float(input("Digite la altura del rectángulo: "))
        rectangulo.set_altura(altura)

        print("El área del rectángulo es:", rectangulo.calcular_area())

    # Opción para calcular el perímetro del rectángulo
    elif opcion == "2":
        rectangulo = Rectangulo()
        base = float(input("Digite la base del rectángulo: "))
        rectangulo.set_base(base)

        altura = float(input("Digite la altura del rectángulo: "))
        rectangulo.set_altura(altura)

        print("El perímetro del rectángulo es:", rectangulo.calcular_perimetro())

    # Opción para salir del programa
    elif opcion == "3":
        print("Saliendo del programa...")
        break

    # Opción no válida
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
