#Sistema de calificaciones con bonificaciones

#Solicitar calificacion de estudiante 
calificacion_estudiante=float(input("Ingrese su calificacion:\n"))

#Preguntar a usuario si hizo tareas adicionales
tareas_adicionales=input("¿Hizo tareas adicionales? (Si/No)\n")

#Dependiendo de la respuesta, aumentar la calificacion final en 0.5
if tareas_adicionales.lower() == "si":
    calificacion_estudiante += calificacion_estudiante * 0.05
    #Asegurarse que la calificacion no sea mayor a 100
    if calificacion_estudiante > 100:
        calificacion_estudiante = 100
    
#Mostrar calificacion final
print(f"Su calificacion final es: {calificacion_estudiante:.2f}")
