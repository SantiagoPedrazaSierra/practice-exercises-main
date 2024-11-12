#Calculadora básica
import math

#Definir cada operacion
"""
(+) suma 
(-) resta
(*) multiplicacion
(/) division
"""

#Definir operando y operador
numero_1=float(input("Operando: "))
operador=(input("Operador: "))
numero_2=float(input("Operando: "))

#Determinar que operacion se hace segun el operador dado 
def calculadora (numero_1,operador,numero_2):
    if operador == "+":
        print(f"{int(numero_1)} + {int(numero_2)} = {int(numero_1 + numero_2)} ")
    elif operador == "-":
        print(f"{int(numero_1)} - {int(numero_2)} = {int(numero_1 - numero_2)} ")
    elif operador == "*": 
        print(f"{int(numero_1)} * {int(numero_2)} = {int(numero_1 * numero_2)} ")
    elif operador == "/":
        if numero_2 != 0:
            print(f"{int(numero_1)} / {int(numero_2)} = {int(numero_1 / numero_2)} ")
        else:
            print("Error:Division por cero.")

#Mostrar resultado operacion 
calculadora(numero_1,operador,numero_2)


 