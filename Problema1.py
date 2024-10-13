import requests

def obtener_precio_bitcoin():
    """Función que obtiene el precio actual del Bitcoin en USD desde la API de CoinDesk."""
    try:
        # Consulta a la API de CoinDesk para obtener el precio actual de Bitcoin
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Detecta errores HTTP
        
        # Parseo del JSON recibido
        datos = respuesta.json()
        
        # Extraer el precio actual en USD
        precio_usd = datos['bpi']['USD']['rate_float']
        return precio_usd
    except requests.RequestException as e:
        # Manejo de posibles errores de la petición
        print(f"Error al consultar la API: {e}")
        return None

def calcular_valor_bitcoins(n, precio_usd):
    """Función que calcula el valor de 'n' Bitcoins en USD."""
    return n * precio_usd

def main():
    try:
        # Solicitar al usuario la cantidad de bitcoins que posee
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
        
        # Obtener el precio actual del Bitcoin en USD
        precio_bitcoin_usd = obtener_precio_bitcoin()
        
        if precio_bitcoin_usd is not None:
            # Calcular el valor de los bitcoins en USD
            valor_total = calcular_valor_bitcoins(n, precio_bitcoin_usd)
            
            # Mostrar el valor con formato adecuado
            print(f"El valor de {n} Bitcoins es: ${valor_total:,.4f} USD")
        else:
            print("No se pudo obtener el precio de Bitcoin en este momento.")
    
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
