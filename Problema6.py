def contar_lineas_codigo(ruta_archivo):
    # Verificamos que el archivo tenga extensión .py
    if not ruta_archivo.endswith('.py'):
        print("El archivo debe ser un archivo .py.")
        return
    
    try:
        # Abrimos el archivo en modo lectura
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        # Contador de líneas de código
        lineas_codigo = 0

        for linea in lineas:
            # Eliminamos espacios en blanco al inicio y final
            linea_limpia = linea.strip()
            
            # Verificamos si la línea no está vacía y no es un comentario
            if linea_limpia and not linea_limpia.startswith('#'):
                lineas_codigo += 1
        
        print(f"El archivo {ruta_archivo} tiene {lineas_codigo} líneas de código.")
    
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no fue encontrado.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

# Función principal que solicita la ruta del archivo
def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)

# Ejecutar el programa
if __name__ == "__main__":
    main()
