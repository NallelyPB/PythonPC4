import requests
import zipfile
import os

# Función para descargar la imagen
def descargar_imagen(url, nombre_archivo):
    try:
        # Solicitar la imagen desde el URL
        respuesta = requests.get(url)
        # Verificar si la descarga fue exitosa
        if respuesta.status_code == 200:
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(respuesta.content)
            print(f"Imagen descargada como {nombre_archivo}")
        else:
            print("Error al descargar la imagen")
    except requests.RequestException as e:
        print(f"Ocurrió un error: {e}")

# Función para comprimir la imagen en un archivo zip
def crear_zip(nombre_archivo, nombre_zip):
    try:
        with zipfile.ZipFile(nombre_zip, 'w') as archivo_zip:
            archivo_zip.write(nombre_archivo)
            print(f"Archivo zip creado como {nombre_zip}")
    except Exception as e:
        print(f"Error al crear el archivo zip: {e}")

# Función para descomprimir archivo zip
def descomprimir_zip(nombre_zip, destino):
    try:
        with zipfile.ZipFile(nombre_zip, 'r') as archivo_zip:
            archivo_zip.extractall(destino)
            print(f"Archivo zip descomprimido en {destino}")
    except Exception as e:
        print(f"Error al descomprimir el archivo zip: {e}")

# URL de la imagen
url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# Nombre del archivo de imagen descargada
nombre_imagen = "perrito.jpg"

# Nombre del archivo zip
nombre_zip = "perrito.zip"

# Nombre del directorio de descompresión
directorio_destino = "descomprimido"

# Descargar la imagen
descargar_imagen(url_imagen, nombre_imagen)

# Comprimir la imagen en un archivo zip
crear_zip(nombre_imagen, nombre_zip)

# Descomprimir el archivo zip
# Primero, asegurarse de que el directorio de destino exista
if not os.path.exists(directorio_destino):
    os.makedirs(directorio_destino)

# Descomprimir el archivo zip
descomprimir_zip(nombre_zip, directorio_destino)
