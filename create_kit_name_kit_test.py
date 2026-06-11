import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def check_positive_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == name

def check_negative_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400

def test_create_kit_with_one_letter_in_name_get_success_response():
    check_positive_assert("a")

def test_create_kit_with_five_hundred_eleven_letters_in_name_get_success_response():
    string_length_511 = "Abcdefghij" * 51 + "a"
    check_positive_assert(string_length_511)

def test_create_kit_with_empty_name_get_error_response():
    check_negative_assert("")

def test_create_kit_with_five_hundred_twelve_letters_in_name_get_error_response():
    string_length_512 = "Abcdefghij" * 51 + "ab"
    check_negative_assert(string_length_512)

def test_create_kit_with_special_characters_in_name_get_success_response():
    check_positive_assert("\"№%@\",")

def test_create_kit_with_spaces_in_name_get_success_response():
    check_positive_assert(" A B C ")

def test_create_kit_with_numbers_in_name_get_success_response():
    check_positive_assert("123")

def test_create_kit_without_name_parameter_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    check_negative_assert(kit_body)
def test_create_kit_with_integer_type_name_get_error_response():
    check_negative_assert(123)