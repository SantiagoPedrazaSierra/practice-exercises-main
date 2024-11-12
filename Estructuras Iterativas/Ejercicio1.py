# Solicitar al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Comprobar que el número es positivo
if n <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    # Inicializar la variable para la suma
    suma = 0

    # Usar un ciclo 'for' para calcular la suma de los primeros n números
    for i in range(1, n+1):
        suma += i

    # Mostrar el resultado
    print(f"La suma de los primeros {n} números enteros es: {suma}")
