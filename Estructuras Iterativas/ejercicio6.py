#Generar numero aleatorio entre 1 y 100
import random
random_number=random.randint(1, 100)
print("Adivine el numero entre 1 a 100 que estoy pensando...")

#Bucle de juego
while True:
    #Solicitar al usuario que adivine el  numero
    user_number=int(input("Ingrese un numero: "))
    #Comparar el numero ingresado con el generado aleatoriamente
    if user_number == random_number:
        print("Felicidades! has adivinado el numero.")
    elif user_number<random_number:
        print("El numero ingresado es menor.")
    elif user_number>random_number:
        print("El numero ingresado es mayor.")
