import csv

# Función para leer el archivo temperaturas.txt y obtener los datos de temperatura
def leer_temperaturas(nombre_archivo):
    temperaturas = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            for linea in lector_csv:
                # Suponemos que la estructura es fecha, temperatura
                fecha, temperatura = linea
                temperaturas.append(float(temperatura))
        return temperaturas
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

# Función para calcular las estadísticas de las temperaturas
def calcular_estadisticas(temperaturas):
    if not temperaturas:
        return None, None, None
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)
    temperatura_promedio = sum(temperaturas) / len(temperaturas)
    return temperatura_maxima, temperatura_minima, temperatura_promedio

# Función para escribir las estadísticas en un nuevo archivo resumen_temperaturas.txt
def escribir_resumen(nombre_archivo, temperatura_maxima, temperatura_minima, temperatura_promedio):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(f"Temperatura máxima: {temperatura_maxima:.2f}\n")
            archivo.write(f"Temperatura mínima: {temperatura_minima:.2f}\n")
            archivo.write(f"Temperatura promedio: {temperatura_promedio:.2f}\n")
        print(f"Resumen escrito correctamente en {nombre_archivo}")
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo: {e}")

# Nombre del archivo de entrada y salida
archivo_entrada = "temperaturas.txt"  # Aquí deberías descargar el archivo y colocarlo en el mismo directorio
archivo_salida = "resumen_temperaturas.txt"

# Leer el archivo de temperaturas
temperaturas = leer_temperaturas(archivo_entrada)

# Calcular las estadísticas
if temperaturas:
    temp_max, temp_min, temp_promedio = calcular_estadisticas(temperaturas)

    # Escribir el resumen en el archivo de salida
    escribir_resumen(archivo_salida, temp_max, temp_min, temp_promedio)
