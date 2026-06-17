import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def check_positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201

def check_negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

def test_create_kit_with_one_letter_in_name_get_success_response():
    new_kit_body = get_kit_body("a")
    check_positive_assert(new_kit_body)

def test_create_kit_with_five_hundred_eleven_letters_in_name_get_success_response():
    string_length_511 = "Abcdefghij" * 51 + "a"
    new_kit_body = get_kit_body(string_length_511)
    check_positive_assert(new_kit_body)

def test_create_kit_with_empty_name_get_success_response():
    new_kit_body = get_kit_body("")
    check_positive_assert(new_kit_body)

def test_create_kit_with_five_hundred_twelve_letters_in_name_get_error_response():
    string_length_512 = "Abcdefghij" * 51 + "ab"
    new_kit_body = get_kit_body(string_length_512)
    check_negative_assert(new_kit_body)

def test_create_kit_with_special_characters_in_name_get_success_response():
    new_kit_body = get_kit_body("\"№%@\",")
    check_positive_assert(new_kit_body)

def test_create_kit_with_spaces_in_name_get_success_response():
    new_kit_body = get_kit_body("A B C")
    check_positive_assert(new_kit_body)

def test_create_kit_with_numbers_in_name_get_success_response():
    new_kit_body = get_kit_body("123")
    check_positive_assert(new_kit_body)

def test_create_kit_without_name_parameter_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    check_negative_assert(kit_body)

def test_create_kit_with_integer_type_name_get_error_response():
    new_kit_body = get_kit_body(123)
    check_negative_assert(new_kit_body)