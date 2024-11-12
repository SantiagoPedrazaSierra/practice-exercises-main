#Calculadora de IMC (Índice de Masa Corporal)

#Función para calcular el IMC
def calcular_imc(peso,altura):
    return peso/altura**2

#Funcio para clasificar el IMC

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc >= 18.5 and imc < 24.9:
        return "Normal"
    elif imc < 25 and imc < 29.9:
        return "Sobrepeso"
    elif imc >= 30:
        return "Obesidad"

#Solicitar datos a usuario
peso=float(input("Ingrese su peso en kilogramos:\n "))
altura=float(input("Ingrese su altura en metros:\n "))

#Calcular IMC
imc=calcular_imc(peso,altura)

#Clasificar IMC
clasificar_imc(imc)

#Mostrar resultados 

print(f"Su IMC es: {imc:.2f}")
print(f"Usted se encuentra en el grupo: {clasificar_imc(imc)}")