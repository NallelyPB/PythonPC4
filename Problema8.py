import sqlite3
import csv
from collections import defaultdict

# Conectar a la base de datos SQLite
conexion = sqlite3.connect('tipo_cambio.db')
cursor = conexion.cursor()

# Crear la tabla tipo_cambio si no existe 
cursor.execute('''
CREATE TABLE IF NOT EXISTS tipo_cambio (
    fecha TEXT PRIMARY KEY,
    tipo_cambio REAL
)
''')

# Insertar tipos de cambio (opcional, para pruebas)
cursor.execute("INSERT OR IGNORE INTO tipo_cambio (fecha, tipo_cambio) VALUES ('2024-07-01', 3.80)")
cursor.execute("INSERT OR IGNORE INTO tipo_cambio (fecha, tipo_cambio) VALUES ('2024-07-02', 3.85)")
conexion.commit()

# Leer el tipo de cambio de la base de datos
tipo_cambio_dict = {}
cursor.execute("SELECT fecha, tipo_cambio FROM tipo_cambio")
for fila in cursor.fetchall():
    fecha, tipo_cambio = fila
    tipo_cambio_dict[fecha] = tipo_cambio

# Cerrar la conexión con la base de datos
conexion.close()

# Leer el archivo CSV
ventas = defaultdict(lambda: {'cantidad': 0, 'precio_usd': 0.0})

with open('ventas.csv', mode='r') as file:
    lector = csv.reader(file)
    next(lector)  # Saltar la cabecera
    for fila in lector:
        fecha, producto, cantidad, precio = fila
        cantidad = int(cantidad)  # Convertir a entero
        precio = float(precio)     # Convertir a float
        
        # Acumular datos
        ventas[producto]['cantidad'] += cantidad
        ventas[producto]['precio_usd'] += cantidad * precio

# Mostrar resultados
print(f"{'Producto':<15} {'Cantidad':<10} {'Total en USD':<15} {'Total en Soles':<15}")
print("-" * 55)
for producto, datos in ventas.items():
    total_usd = datos['precio_usd']
    # Calcular el total en soles usando el tipo de cambio del último registro de la fecha
    # Aquí se usa la fecha del último producto que se procesó
    last_fecha = fecha  # Asumimos que la última fecha es la última procesada
    total_soles = total_usd * tipo_cambio_dict[last_fecha] if last_fecha in tipo_cambio_dict else 0
    print(f"{producto:<15} {datos['cantidad']:<10} {total_usd:<15.2f} {total_soles:<15.2f}")
