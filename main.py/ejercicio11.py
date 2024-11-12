#Conversión de temperaturas

#Funcion para convertir grados Celsius a Fahrenheit
def convertir_temperatura(temperatura,escala):

#Convertir Celsius a Fahrenheit
    match escala:
        case "C" | "c":
        #Conversion de Celsius a Fahrenheit
            resultado = (temperatura * 1.8 ) +32 
            print(f"{round(temperatura)}°C es igual a {resultado:.2f}°F")

        case "F" | "f":
        #Conversion de Fahrenheit a Celsius#    
            resultado = (temperatura - 32) /1.8 
            print(f"{round(temperatura)}°F es igual a {resultado:.2f}°C")
        case _:
            print("Escala de temperatura no válida. Use 'C' para Celsius o 'F' para Fahrenheit.")

#Solicitar temperatura y escala al usuario
temperatura=float(input("Ingrese la temperatura:\n "))
escala=(input("Ingrese la escala de temperatura (C/F):\n "))
convertir_temperatura(temperatura, escala)