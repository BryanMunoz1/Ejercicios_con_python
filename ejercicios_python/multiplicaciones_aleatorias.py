# ***
# Centro de biotecnologia agropecuaria
# Ficha: 2877795
# Aprendiz: Bryan Muñoz
# Version: Python312
# Fecha: 27/04/2024
# **
"""
Este programa tiene la funcion de darnos un numero aleatorio
segun ese numero nos muestra las tablas de multiplicar hasta dicho numero
"""

# importa el modulo de colorama
from colorama import Fore, init


# importa el modulo para utilizar las funciones y poder sacar el numero aleatorio
from random import randrange


# importa da acceso a modulos para implementar algunos servicios de windows
import msvcrt


# Inicializa Colorama
init()

# esta funcion sirve para definir las tablas
def mostrar_tablas(numero):
    
    
    # for i es para mostrar el rango de la tabla del 1 a el numero aleatorio
    for i in range(1, numero + 1):
        
        
        msvcrt.getch()
        
        
        print(f"**{Fore.LIGHTYELLOW_EX}Tabla de multiplicar del {i}:{Fore.RESET}****si")
        
        
        # for j es para mostrar el rango del numero por el que se va a multiplicar
        for j in range(1, 11):
            
            
            resultado = i * j
            print(f"{Fore.LIGHTYELLOW_EX}{i} x {j} = {resultado}{Fore.RESET}")
        
        
        print()  # Línea en blanco para separar las tablas

def main():
    # este while me genera un bucle para continuar con el proseso o finalzarlo
    while True:
        
        
        # aca utilizamos el imput y su funcion es darle entrada al bucle
        respuesta = input(f"{Fore.GREEN}¿Deseas continuar? (si/no):{Fore.RESET}")
        
        # aca utilizamos if y su funcion es que en caso de que la condcion sea verdadera la ejecita y la salta si es falsa
        # utilizamos un .lower el cual no sirve para cambiar o mayusculas a minuscula o al contrario segun lo desee el programador
        if respuesta.lower() == "no":
            print(f"{Fore.GREEN}Proceso finalizado.{Fore.RESET}")
            break
        
        
        # esta funcion es para comprobar si la condicion es falsa
        elif respuesta.lower() == "si":
            print(f"{Fore.GREEN}Continuando con el proceso...{Fore.RESET}")
            
        # estas funciones son las que me dan el numero aleatorio    
            numero_aleatorio = randrange(1, 21)
            print(f"{Fore.LIGHTYELLOW_EX}Número aleatorio: {numero_aleatorio}{Fore.RESET}")
            mostrar_tablas(numero_aleatorio)
        
        
        #  esta funcion se utiliza cuando las condiciones anteriores no son verdaderas o falsas dando otra opcion de respuesta
        else:
            print(f"{Fore.LIGHTYELLOW_EX}Respuesta no válida. Por favor, ingresa 'si' o 'no'.{Fore.RESET}")


if __name__ == "__main__":
    main()