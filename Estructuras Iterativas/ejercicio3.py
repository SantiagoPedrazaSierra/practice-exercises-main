#Solicitar a usuario que ingrese un numero entero positivo
numero=int(input("Ingrese un numero entero: "))

#Verificar si el numero es negativo
if numero < 0:
    print("El numero ingresado es negativo")

#Calcular factorial de numero ingresado por usuaurio 
else:
    factorial=1    
    for i in range(1,numero+1):
        factorial *= i  #Calcula el factorial de numero

#Mostrar el resultado de el factorialsegun el numero
print(f"El factorial de {numero} es {factorial}.") 