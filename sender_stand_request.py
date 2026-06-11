import requests
import configuration
import data

# Función para crear el usuario y obtener las respuestas de la API
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Función para crear el kit usando el token de autorización
def post_new_client_kit(kit_body, auth_token):
    current_headers = data.headers.copy()
    current_headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=current_headers)