import sender_stand_request
import data
import configuration

# Prueba 1
# El parámetro contiene un 1 caracter

def test_create_kit_1_letter_in_first_name_get_success_response():
    sender_stand_request.positive_assert(data.kit_body_1)

# Prueba 2
# El número permitido de caracteres 511

def test_create_kit_511_letter_in_name_get_success_response():
    sender_stand_request.positive_assert(data.kit_body_2)

# Prueba 3 - negativa
# 	El número de caracteres es menor que la cantidad permitida
def test_create_kit_cero_letter_in_name_get_success_response():
    sender_stand_request.negative_assert_code_400(data.kit_body_3)

# Prueba 4 - negativa
# El número de caracteres es mayor que la cantidad permitida 512

def test_create_kit_512_letter_in_name_get_success_response():
    sender_stand_request.negative_assert_code_400(data.kit_body_4)

# Prueba 5 -positive
# Se permiten caracteres especiales

def test_create_kit_caracter_special_in_name_get_success_response():
    sender_stand_request.positive_assert(data.kit_body_5)

# Prueba 6 - positive
# Se permiten espacios

def test_create_kit_caracter_space_in_name_get_success_response():
    sender_stand_request.positive_assert(data.kit_body_6)

# Prueba 7 -positive
# Se permiten numeros
def test_create_kit_caracter_number_in_name_get_success_response():
    sender_stand_request.positive_assert(data.kit_body_7)


# Prueba 8 - negative
# El parámetro no se pasa en la solicitud
def test_create_kit_caracter_x_in_name_get_success_response():
    sender_stand_request.negative_assert_code_400(data.kit_body_8)

# Prueba 9 - negative
# 	Se ha pasado un tipo de parámetro diferente (número):
def test_create_kit_caracter_strangernumber_in_name_get_success_response():
    sender_stand_request.negative_assert_code_400(data.kit_body_9)