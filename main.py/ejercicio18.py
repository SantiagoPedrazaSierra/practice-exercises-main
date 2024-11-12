#Sistema de evaluación de créditos universitarios

#Solicitar a usuario el numero de materias que ha cursado
num_materias= int(input("Ingrese cuantas materias ha cursado:\n"))

#Inicializar variable para contar los creditos 
creditos_totales = 0

#Procesar cada materia 
for i in range (num_materias):
    #Solicitar el puntaje de cada materia 
    puntaje=float(input(f"Ingrese el puntaje obtenido en la materia {i+1}: \n"))
    #Verificar si la materia fue aprobada
    if puntaje >=60:
        creditos_totales += 3 #Sumar credtos por materia aprobada 
        print(f"La materia {i+1} fue aprobada")
    else:
        print(f"La materia {i+1} fue reprobada")

#Mostrar el numero total de creditos
print(f"El numero de creditos obtenidos es: {creditos_totales}")