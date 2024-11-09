#Días de la semana

#Pedir a usuario numeros
number=float(input("Enter number from 1 to 7: "))

#Lista de dias a la semana 
match number:
    case 1:
        print("Monday.")
    case 2:
        print("Tuesday.")
    case 3:
        print("Wednesday.")
    case 4:
        print("Thursday.")
    case 5:
        print("Friday.")
    case 6:
        print("Saturday.")
    case 7:
        print("Sunday.")
    case _:
        print("Enter number from 1 to 7.")
                 