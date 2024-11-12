#Determinación de año bisiesto

#Solicitar a usuario el año
año=int(input("Ingrese un año:\n "))

#Determinar si el año es bisiesto
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
                print(f"{año} es un año bisiesto.")
        else:
            print(f"{año} no es un año bisiesto.")
    else:
        print(f"{año} es un año bisiesto.")
else:   
        print(f"{año} no es un año bisiesto.")