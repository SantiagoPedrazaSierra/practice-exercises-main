#Juego de adivinanza de números

import random
# Genera un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)
print("\tAdivina el numero del 1 al 10:")
intentos = 0

#Bucle de juego
while True:
    intento = int(input("Ingrese un numero: "))
    intentos +=1
    if numero_aleatorio == intento:
        print(f"Felicidades has acertado el número en {intentos} intentos.")
    elif numero_aleatorio > intento:
        print("El numero aleatorio es mayor.")
    elif numero_aleatorio < intento:
        print("El numero aleatorio es menor.")

