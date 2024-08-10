import requests
import configuration
import data


# Creacion de un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def authtoken_new_kit():
    response = post_new_user(data.user_body)
    return response.json()["authToken"]

# Creacion de un nuevo kit
def post_new_client_kit(kit_user_body):
   token = authtoken_new_kit()
   headers = data.headers.copy()
   headers["Authorization"] = f"Bearer {token}"

   return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                       json=kit_user_body,
                       headers=headers)

# Función de prueba positiva
def positive_assert(kit_body):
    response = post_new_client_kit(kit_body)
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    assert response.json()["name"] == kit_body["name"]

# Función de prueba negativa
def negative_assert_code_400(kit_body):
    response = post_new_client_kit(kit_body)

    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"