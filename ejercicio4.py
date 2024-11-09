#Tipo de triangulo
#Solicitar a usuario datos de lados 
lado1=(input("Primer lado: "))
lado2=(input("Segundo lado: "))
lado3=(input("Tercer lado: "))
print()
#Determinación del tipo de triángulo
def calcular_tipo_triangulo(lado1, lado2, lado3):
    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        return "No es un triángulo"
    elif lado1 == lado2 and lado2 == lado3:
        return "Su triangulo es:Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Su triangulo es:Isósceles"
    else:
        return "Su triangulo es:Escaleno"

#Mostrar tipo de triangulo segun sus lados 
print (calcular_tipo_triangulo(lado1, lado2, lado3))