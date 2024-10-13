import os

class TablaMultiplicar:
    # Método para generar y guardar la tabla en un archivo
    def generar_tabla(self, n):
        try:
            # Verificamos que el número esté entre 1 y 10
            if not (1 <= n <= 10):
                raise ValueError("El número debe estar entre 1 y 10.")
            
            nombre_archivo = f"tabla-{n}.txt"
            with open(nombre_archivo, 'w') as archivo:
                for i in range(1, 11):
                    archivo.write(f"{n} x {i} = {n * i}\n")
            print(f"Tabla del {n} guardada en {nombre_archivo}")
        except Exception as e:
            print(f"Error al generar la tabla: {e}")

    # Método para leer la tabla completa desde un archivo
    def leer_tabla(self, n):
        try:
            nombre_archivo = f"tabla-{n}.txt"
            if os.path.exists(nombre_archivo):
                with open(nombre_archivo, 'r') as archivo:
                    contenido = archivo.read()
                    print(f"Tabla del {n}:\n{contenido}")
            else:
                print(f"El archivo {nombre_archivo} no existe.")
        except Exception as e:
            print(f"Error al leer la tabla: {e}")

    # Método para mostrar una línea específica de la tabla
    def mostrar_linea(self, n, m):
        try:
            nombre_archivo = f"tabla-{n}.txt"
            if os.path.exists(nombre_archivo):
                with open(nombre_archivo, 'r') as archivo:
                    lineas = archivo.readlines()
                    if 1 <= m <= 10:
                        print(f"Línea {m} de la tabla del {n}: {lineas[m - 1]}")
                    else:
                        print("El número de línea debe estar entre 1 y 10.")
            else:
                print(f"El archivo {nombre_archivo} no existe.")
        except Exception as e:
            print(f"Error al mostrar la línea: {e}")

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Generar tabla de multiplicar")
    print("2. Leer tabla de multiplicar")
    print("3. Mostrar línea específica de una tabla")
    print("4. Salir")

# Función principal que organiza el flujo del programa
def main():
    tabla = TablaMultiplicar()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n = int(input("Ingrese un número entre 1 y 10 para generar la tabla: "))
            tabla.generar_tabla(n)
        elif opcion == "2":
            n = int(input("Ingrese un número entre 1 y 10 para leer la tabla: "))
            tabla.leer_tabla(n)
        elif opcion == "3":
            n = int(input("Ingrese un número entre 1 y 10 para leer la tabla: "))
            m = int(input("Ingrese el número de línea (1 a 10) que desea ver: "))
            tabla.mostrar_linea(n, m)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

# Llamada a la función principal
if __name__ == "__main__":
    main()
