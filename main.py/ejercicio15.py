# Cálculo del salario neto

#Solicitar a usuario salario bruto y su pais de residencia
salario_bruto = float(input("Ingrese su salario bruto:\n $"))
pais_residencia = input("Ingrese su pais de residencia:\n ")

#Funcion para calcular salario neto
def calcular_salario_neto(salario_bruto, pais_residencia):

    if pais_residencia == "Argentina":
        porcentaje_impuesto = 0.20
    elif pais_residencia == "Bolivia":
        porcentaje_impuesto = 0.15
    elif pais_residencia == "Colombia":
        porcentaje_impuesto = 0.10
    else:
        porcentaje_impuesto = 0.25

#Calcular impuesto
    impuesto = salario_bruto * porcentaje_impuesto

#Calcular salario neto
    salario_neto= salario_bruto - impuesto
    return salario_neto

#llamar la funcion y calcular salario neto
salario_neto=round(calcular_salario_neto(salario_bruto, pais_residencia))

#Mostrar el salario neto
print(f"Su salario neto es ${salario_neto} en {pais_residencia}.")

