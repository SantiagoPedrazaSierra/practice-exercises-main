#Cálculo del tiempo de viaje

#Solicitar a usuario distancia y velocidad
distancia = float(input("Ingrese la distancia en kilómetros de su destino:\n "))
velocidad = float(input("Ingrese su velocidad promedio en km/h:\n "))

#Tiempo de viaje 
tiempo_horas=distancia/velocidad#Calcular tiempo de viaje en horas 
#Convertir tiempo a horas y minutos 
horas=int(tiempo_horas)
minutos=int((tiempo_horas-horas)*60)

#Mostrar resultado
print(f"El tiempo de viaje es {horas} horas y {minutos} minutos para llegar a su destino.")

#Mensaje advertencia en caso de exceso de velocidad
if velocidad > 120:
    print("Advertencia: exceso de velocidad")