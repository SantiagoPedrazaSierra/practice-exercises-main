#Solicitar a usuario calificacion
calificacion_num=float(input("Ingrese su calificacion (0-100):\n"))

#Asignar calificacion segun rango
match calificacion_num:
    case _ if 90 <= calificacion_num <= 100:
        print("Su calificacion es A.")
    case _ if 80 <= calificacion_num <= 89:
        print("Su calificacion es B.")
    case _ if 70 <= calificacion_num <= 79:
        print("Su calificacion es C.")
    case _ if 60 <= calificacion_num <= 69:
        print("Su calificacion es D.")
    case _ if 0 <= calificacion_num <= 59:
        print("Su calificacion es F.")
