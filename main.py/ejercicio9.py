#Clasificación de edades

#Solicitar edad de usuario
edad=int(input("Ingrese su edad:\n "))

#Clasificar edad

if edad <= 12:
    print("Usted es un niño.")
elif edad >= 13 and edad <= 17:
    print("Usted es un adolescente.")
elif edad >= 18 and edad <= 64:
    print("Usted es un adulto.")
else:
    print("Usted es un anciano.")
    