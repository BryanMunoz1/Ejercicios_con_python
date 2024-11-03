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
        
        
        print(f"**{Fore.LIGHTYELLOW_EX}Tabla de multiplicar del {i}:{Fore.RESET}****")
        
        
        # for j es para mostrar el rango del numero por el que se va a multiplicar
        for j in range(1, 11):
            
            
            resultado = i * j
            print(f"{Fore.LIGHTYELLOW_EX}{i} x {j} = {resultado}{Fore.RESET}")
        
        
        print()  # Línea en blanco para separar las tablas