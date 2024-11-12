#Clasificación de notas

#Solicitar nota de usuario
nota=float(input("Ingrese su nota:\n "))

#Clasificar la nota

if nota >= 90:
    print("Su calificacion es A.")
elif nota >= 80:
    print("Su calificacion es B.")
elif nota >=70:
    print("Su calificacion es C.")
elif nota >= 60:
    print("Su calificacion es D.")
else:
    print("Su calificacion es F.")
    