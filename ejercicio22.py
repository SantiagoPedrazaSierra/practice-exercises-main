
#Solicitar a usuario ingresear tres angulos

angulo1 = float(input("Ingrese el primer ángulo: "))
angulo2 = float(input("Ingrese el segundo ángulo: "))
angulo3 = float(input("Ingrese el tercer ángulo: "))

#Clasificar los angulos
if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
    print ("Agudo: Todos los angulos son menores a 90°.")
elif angulo1 == 90 or  angulo2 == 90 or angulo3 == 90:
    print("Rectangulo: Un angulo es exactamente 90°.")
elif angulo1 > 90 or  angulo2 > 90 or angulo3 > 90:
    print("Obtuso: Un angulos es mayor a 90°.")