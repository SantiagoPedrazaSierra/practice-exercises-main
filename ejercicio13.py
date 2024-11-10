#Comparación de tres números

#Solicitar a usuario ingresar tres números
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
num3=int(input("Ingrese el tercer número: "))

#Función para comparar los números
def compare_numeros(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return f"{num1} es el mayor."
    elif num2 > num1 and num2 > num3:
        return f"{num2} es el mayor."
    else:
        return f"{num3} es el mayor."

#Mostrar el resultado
print(compare_numeros(num1, num2, num3))