#Números pares en un rango

#Solicitar a usuario dos numeros enteros
num_1=int(input("Ingrese el primer numero entero: "))
num_2=int(input("Ingrese el segundo numero entero: "))

#Mostrar los numeros pares entre los dos numeros ingresados
for i in range(num_1,num_2+1):
    if i % 2 == 0:#Verificar si el numro es par
        print(i)