#Número positivo, negativo o cero

numero = float(input("Ingrese un número: "))

if numero > 0:
    print(f"El numero {int(numero)} es positivo.")
elif numero < 0:
    print(f"El numero {int(numero)} es negativo.") 
else:
    print(f"El numero {int(numero)} es cero.")   