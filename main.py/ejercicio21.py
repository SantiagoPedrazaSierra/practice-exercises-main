# Sistema de estacionamiento con tarifas progresivas

#Solicitar a usuario numero de horas de estacionamiento
horas_estacionado= float(input("Ingrese el numero de horas que duro estacionado:\n"))
costo=0
#Calcular costo de etacionamiento segun las horas 
if horas_estacionado == 1:#Solo una hora
    costo =5
elif  2 <= horas_estacionado <= 4:#Entre 2 y 4 horas
    costo = 5 + (horas_estacionado-1) *4
else:#Mas de 4 horas
    costo+= 5 + 12 + (horas_estacionado-4) * 3

#Mostrar el costo de estacionamiento
print(f"El costo de estacionamiento es: ${costo:.2f}")