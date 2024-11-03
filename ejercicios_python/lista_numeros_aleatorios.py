# *
# Centro de biotecnologia agropecuaria
# Ficha: 2877795
# Aprendiz: Bryan Muñoz
# Version: Python312
# Fecha: 06/05/2024
# **
"""
Este programa tiene la funcion de crear una lista de numeros aleatorios y mostrarnos
la suma total:
la longitud:
numeros pares e impares:
"""

# importa el modulo de colorama
from colorama import Fore, init


from random import randrange

# Esta función genera una lista de números aleatorios entre 0 y 19.
# La generación de números se detiene cuando se genera un 0.
def lista_aleatoria():
    numeros = []
    while True:
        numero_aleatorio = randrange(0, 20)
        numeros.append(numero_aleatorio)
        if numero_aleatorio == 0:
            numeros.pop()  # Elimina el 0 de la lista
            break
    return numeros

resultado = lista_aleatoria()
print(f"Lista de números aleatorios: {resultado}")

# Esta función calcula la suma total de los números en la lista generada.
def suma_total():
    suma = 0
    for numero in resultado:
        suma += numero
    print(f"La suma total de la lista es: {suma}")

# Esta función calcula la longitud de la lista generada.
def longitud():
    longitud = len(resultado)
    print(f"La longitud de la lista es: {longitud}")

# Esta función identifica y separa los números pares e impares en la lista generada.
def numeros_pares_impares():
    numeros_pares = []
    numeros_impares = []
    for numero in resultado:
        if numero % 2 == 0:
            numeros_pares.append(numero)
        else:
            numeros_impares.append(numero)
    print(f"Números pares: {numeros_pares}")
    print(f"Números impares: {numeros_impares}")

def main():
    while True:
        init()
        suma_total()
        longitud()
        numeros_pares_impares()
        respuesta = input(f"{Fore.GREEN}¿Deseas continuar? (si/no):{Fore.RESET}")
        # aca utilizamos el imput y su funcion es darle entrada al bucle
        if respuesta.lower() == "no":
            print(f"{Fore.GREEN}Proceso finalizado.{Fore.RESET}")
            break
            # esta funcion es para comprobar si la condicion es falsa
        elif respuesta.lower() == "si":
            print(f"{Fore.GREEN}Continuando con el proceso...{Fore.RESET}")
            #  esta funcion se utiliza cuando las condiciones anteriores no son verdaderas o falsas dando otra opcion de respuesta
        else:
            print(f"{Fore.LIGHTYELLOW_EX}Respuesta no válida. Por favor, ingresa 'si' o 'no'.{Fore.RESET}")

if __name__ == "__main__":
    main()