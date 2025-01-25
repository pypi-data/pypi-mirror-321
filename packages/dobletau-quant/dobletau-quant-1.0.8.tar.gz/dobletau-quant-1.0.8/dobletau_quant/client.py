import requests
import pandas as pd

class BotConnector:
    def __init__(self, token):
        """
        Inicializa el cliente para interactuar con la API.
        :param token: Token único del bot asignado.
        """
        self.base_url = "https://concurso-trading.onrender.com"
        self.token = token

    def send_order(self, activo, cantidad):
        """
        Envia una operación de compra o venta de un activo. El token del bot se incluye automáticamente durante la inicialización del cliente.
        """
        try:
            response = requests.post(
                f"{self.base_url}/send-order/",
                json={"activo": activo, "cantidad": cantidad},
                headers={"token": self.token}
            )
            if response.status_code == 200:
                result = response.json()
                print(result.get("message", "Operación enviada exitosamente."))
            else:
                error_detail = response.json().get("detail", "Error desconocido.")
                print(f"Error al enviar operación: {error_detail}")
        except requests.RequestException as e:
            print(f"Error de conexión: {str(e)}")

    def get_history(self):
        """
        Obtiene el historial de operaciones realizadas por el bot.
        :return: DataFrame con las operaciones realizadas o un mensaje de error.
        """
        try:
            # Realiza la solicitud GET al servidor
            response = requests.get(
                f"{self.base_url}/get-history/",
                headers={"token": self.token}
            )
            # Verificar si el servidor respondió
            if response.status_code == 200:
                try:
                    historial = response.json().get("historial", [])
                    print("Historial obtenido exitosamente.")
                    return pd.DataFrame(historial)
                except ValueError:
                    print("Error: Respuesta del servidor no es JSON válida.")
                    print(f"Cuerpo de la respuesta: {response.text}")
                    return pd.DataFrame()  # Devuelve un DataFrame vacío en caso de error

            # Manejar errores devueltos por el servidor
            error_detail = response.json().get("detail", "Error desconocido.")
            print(f"Error al obtener historial: {error_detail}")
            return pd.DataFrame()  # Devuelve un DataFrame vacío en caso de error

        except requests.RequestException as e:
            # Manejar errores de conexión o solicitud
            print(f"Error de conexión: {str(e)}")
            return pd.DataFrame()  # Devuelve un DataFrame vacío en caso de error

    def get_positions(self):
        """
        Obtiene los activos actuales de un bot.
        :return: DataFrame con los activos actuales o un mensaje de error.
        """
        try:
            # Realiza la solicitud GET al servidor
            response = requests.get(
                f"{self.base_url}/get-positions/",
                headers={"token": self.token}
            )
            # Verificar si el servidor respondió
            if response.status_code == 200:
                try:
                    activos = response.json().get("activos_actuales", [])
                    print("Activos del portafolio obtenidos exitosamente.")
                    return pd.DataFrame(activos)
                except ValueError:
                    print("Error: Respuesta del servidor no es JSON válida.")
                    print(f"Cuerpo de la respuesta: {response.text}")
                    return pd.DataFrame()  # Devuelve un DataFrame vacío en caso de error

            # Manejar errores devueltos por el servidor
            error_detail = response.json().get("detail", "Error desconocido.")
            print(f"Error al obtener activos del portafolio: {error_detail}")
            return pd.DataFrame()  # Devuelve un DataFrame vacío en caso de error

        except requests.RequestException as e:
            # Manejar errores de conexión o solicitud
            print(f"Error de conexión: {str(e)}")
            return pd.DataFrame()  # Devuelve un DataFrame vacío en caso de error

    def get_balance(self):
        """
        Obtiene la información de VistaEquity para el bot correspondiente al token.
        :return: Diccionario con {bot, equity, disponible} o un mensaje de error.
        """
        try:
            response = requests.get(
                f"{self.base_url}/get-balance/",
                headers={"token": self.token}
            )
            if response.status_code == 200:
                info = response.json().get("data", {})
                print("Información de la cuenta obtenida exitosamente.")
                return info
            error_detail = response.json().get("detail", "Error desconocido.")
            print(f"Error al obtener información de la cuenta: {error_detail}")
            return {}
        except requests.RequestException as e:
            print(f"Error de conexión: {str(e)}")
            return {}