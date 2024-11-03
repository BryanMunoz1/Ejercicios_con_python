# ***
# Centro de biotecnologia agropecuaria
# Ficha: 2877795
# Aprendiz: Juan Camilo Ballesteros y Bryan Muñoz
# Version: Python312
# Fecha: 25/04/2024
# ***

# Este programa tiene la funcion de hacernos operaciones basicas de forma aleatoria

from random import randrange
# importa el modulo de colorama
from colorama import Fore, init, Style

init()

# esta funcion da la bienvenida
def bienvenida():
     print(f"{Fore.GREEN} bienvenidos a adso 2024 {Fore.RESET}")

# esto funciona para la suma de dos numeros
def sumar(dato1, dato2):
    return dato1 + dato2 

# esto funciona para la resta de dos numeros
def restar(dato1, dato2):
    return dato1 - dato2 

# esto funciona para la multiplicacion de dos numeros
def multiplicar(dato1, dato2):
    return dato1 * dato2 

# esta funciona para la divicion de dos numeros
def dividir(dato1, dato2):
    if dato2 == 0:
        return "no se pueden hacer divisiones por 0"
    else:
        return dato1 / dato2 

# esta funcion es para el numero aleatorio del dato1  
def dato1():
    numero1 = randrange(0,100)
    return numero1
# esta funcion es para el numero aleatorio del dato2
def dato2():    
    numero2 = randrange(0,100)
    return numero2

num1 = dato1()
num2 = dato2()


bienvenida()
print(f"{Fore.GREEN}* Inicio *{Fore.RESET}")
print(f"{Fore.GREEN}los numeros son: {Fore.RESET}")
print(Fore.LIGHTYELLOW_EX + str(num1) + "+" + str(num2) + "=" + str(sumar(num1, num2)) + Style.RESET_ALL)
print(Fore.LIGHTYELLOW_EX + str(num1) + "-" + str(num2) + "=" + str(restar(num1, num2)) + Style.RESET_ALL)
print(Fore.LIGHTYELLOW_EX + str(num1) + "*" + str(num2) + "=" + str(multiplicar(num1, num2)) + Style.RESET_ALL)
print(Fore.LIGHTYELLOW_EX + str(num1) + "/" + str(num2) + "=" + str(dividir(num1, num2)) + Style.RESET_ALL)
print(f"{Fore.GREEN}* Fin *{Fore.RESET}")