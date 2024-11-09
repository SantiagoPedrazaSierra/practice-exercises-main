#Verificación de números pares e impares

#Solicitar a usuario numero
print("Ingrese un numero:")
numero=int(input())

#Determinar si el numero ingresado es par o impar
if numero % 2 == 0:
    print(f"{numero} es un numero par.")
else:
    print(f"{numero} es impar.")

