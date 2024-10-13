import requests
import sqlite3
from pymongo import MongoClient

# Función para obtener datos del API de SUNAT
def obtener_tipo_cambio(fecha):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={fecha}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

# Configuración de la base de datos SQLite
def configurar_sqlite():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info
                      (fecha TEXT, compra REAL, venta REAL)''')
    conn.commit()
    return conn

# Configuración de MongoDB
def configurar_mongodb():
    cliente = MongoClient('localhost', 27017)
    db = cliente['tipo_cambio_db']
    return db['sunat_info']

# Guardar en SQLite
def guardar_sqlite(conn, fecha, compra, venta):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)", (fecha, compra, venta))
    conn.commit()

# Guardar en MongoDB
def guardar_mongodb(coleccion, fecha, compra, venta):
    coleccion.insert_one({"fecha": fecha, "compra": compra, "venta": venta})

# Mostrar datos de SQLite
def mostrar_sqlite(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sunat_info")
    filas = cursor.fetchall()
    for fila in filas:
        print(f"Fecha: {fila[0]}, Compra: {fila[1]}, Venta: {fila[2]}")

def main():
    conn_sqlite = configurar_sqlite()
    coleccion_mongodb = configurar_mongodb()

    # Fechas de 2023 (puedes optimizar este paso con un rango de fechas)
    fechas = ["2023-01-01", "2023-02-01", "2023-03-01"]  # Agrega las fechas de todo el 2023

    for fecha in fechas:
        datos = obtener_tipo_cambio(fecha)
        if datos:
            compra = datos['compra']
            venta = datos['venta']
            print(f"Guardando datos del {fecha} - Compra: {compra}, Venta: {venta}")
            guardar_sqlite(conn_sqlite, fecha, compra, venta)
            guardar_mongodb(coleccion_mongodb, fecha, compra, venta)

    print("Mostrando datos almacenados en SQLite:")
    mostrar_sqlite(conn_sqlite)
    conn_sqlite.close()

if __name__ == '__main__':
    main()
