El Proyecto EasyBrokerAPI es una biblioteca de Python que proporciona una interfaz para interactuar con la API de EasyBroker y obtener información sobre solicitudes de contacto. Permite realizar operaciones como obtener las solicitudes de contacto, imprimir los títulos de las mismas y realizar pruebas automatizadas para asegurar el correcto funcionamiento del código.

Características
Clase EasyBrokerAPI: Proporciona métodos para interactuar con la API de EasyBroker y obtener información sobre solicitudes de contacto.
Pruebas Unitarias: Se incluyen pruebas automatizadas utilizando pytest para verificar el comportamiento y la funcionalidad de la clase EasyBrokerAPI.

Requisitos
Python 3.x instalado en su sistema.
La biblioteca requests debe estar instalada. Si no está instalada, puede instalarla ejecutando pip install requests.
La biblioteca pytest debe estar instalada para ejecutar las pruebas. Si no está instalada, puede instalarla ejecutando pip install pytest.

Uso del archivo easybroker_api.py
El archivo easybroker_api.py contiene la clase EasyBrokerAPI que proporciona una interfaz para interactuar con la API de EasyBroker.
import requests

class EasyBrokerAPI:
    # Implementación de la clase EasyBrokerAPI
    # ...


Para utilizar la clase EasyBrokerAPI, primero debe instanciarla con su clave de API de EasyBroker:
api_key = "l7u502p8v46ba3ppgvj5y2aad50lb9"
api = EasyBrokerAPI(api_key)

Una vez que haya creado la instancia, puede utilizar los métodos proporcionados por la clase para obtener información sobre las solicitudes de contacto:

# Obtener solicitudes de contacto
contact_requests = api.get_contact_requests()

# Imprimir títulos de las solicitudes de contacto
api.print_contact_request_titles()

Pruebas
El proyecto incluye pruebas unitarias automatizadas utilizando el framework pytest. Estas pruebas verifican el correcto funcionamiento de la clase EasyBrokerAPI y aseguran que los métodos proporcionados se comporten como se espera.

Para ejecutar las pruebas, siga estos pasos:

Descargue o clone el proyecto en su máquina local.

Asegúrese de tener las dependencias necesarias instaladas: requests y pytest.

Ejecute el siguiente comando desde la terminal para ejecutar las pruebas:
pytest test_easybroker_api.py
Si todas las pruebas pasan correctamente, verá una indicación de que todas las pruebas se aprobaron.
