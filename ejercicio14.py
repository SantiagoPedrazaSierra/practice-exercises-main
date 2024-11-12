import random

def generar_letra_secreta():
    # Genera una letra aleatoria entre A y Z
    return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Generar la letra secreta
letra_secreta = generar_letra_secreta()

# Bucle para que el usuario siga intentando
while True:
    # Solicitar al usuario que ingrese una letra
    letra_usuario = input("Adivina la letra secreta: ").upper()

    # Comprobar si el usuario ingresó una sola letra válida
    if len(letra_usuario) != 1 or not letra_usuario.isalpha():
        print("Por favor, ingresa solo una letra.")
        continue  # Volver a pedir la letra si no es válida
    
    # Usar la declaración match para comparar la letra
    match letra_usuario:
        case letra_secreta:
            print("¡Felicidades! Adivinaste la letra secreta.")
            break  # Termina el bucle si adivina correctamente
        case _:
            print(f"Lo siento, la letra secreta era '{letra_secreta}'. Intenta nuevamente.")
            # Nota: Aquí se revela la letra secreta si se equivoca, puedes eliminar esta línea si lo prefieres.
