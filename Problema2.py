import random
from pyfiglet import Figlet

def main():
    # Crear una instancia de Figlet
    figlet = Figlet()

    # Obtener la lista de fuentes disponibles
    fuentes_disponibles = figlet.getFonts()

    # Solicitar al usuario una fuente
    fuente_usuario = input("Ingrese el nombre de una fuente (deje en blanco para elegir una aleatoria): ")

    # Si no se ingresa ninguna fuente puede seleccionar una aleatoria
    if fuente_usuario == "":
        fuente_seleccionada = random.choice(fuentes_disponibles)
        print(f"Fuente seleccionada aleatoriamente: {fuente_seleccionada}")
    else:
        if fuente_usuario in fuentes_disponibles:
            fuente_seleccionada = fuente_usuario
        else:
            print("Fuente no válida, se seleccionará una fuente aleatoria.")
            fuente_seleccionada = random.choice(fuentes_disponibles)

    # Establecer la fuente seleccionada
    figlet.setFont(font=fuente_seleccionada)

    # Solicitar al usuario el texto a imprimir
    texto_imprimir = input("Ingrese el texto a convertir en arte ASCII: ")

    # Imprimir el texto en la fuente seleccionada
    print(figlet.renderText(texto_imprimir))

if __name__ == "__main__":
    main()
