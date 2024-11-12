#Contador de vocales en una cadena

#Solicitar a usuario una cadena de texto 
cadena_texto=str(input("Ingrese una cadena de texto: "))

#Contar numero de vocales que hay en la cadena
numero_vocales=0
for vocales in cadena_texto:
    if vocales.lower() in ['a','e','i','o','u']:
        numero_vocales+=1

#Mostrar numero de vocales en la cadena ingresada
print(f"La cadena de texto {cadena_texto} tiene {numero_vocales} vocales.")
