#Inicializar la suma 
suma=0

#Ciclo while que continuara pidiendo numeros hasta que se ingrese un impar
while True:
    #Solicitar al usuario que ingrese un numero 
    numero=int(input("Ingrese un numero: \n"))

    #Verificar si el numero es impar
    if numero %2!=0:
        print("Su numero es impar")
        print("CERRANDO PROGRAMA.")
        break

#Si el numero es par, sumarlo 
suma += numero

#Mostrar la suma de los numeros pares 
print("La suma de los numeros pares ingresados es:",suma)