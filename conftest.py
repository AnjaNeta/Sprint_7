import pytest
import requests
from helpers import register_new_courier_and_return_login_password


@pytest.fixture(scope='function')
def create_and_delete_courier():
    login_pass = register_new_courier_and_return_login_password()
    if not login_pass:
        pytest.skip("Не удалось создать курьера для теста")
    
    courier_data = {
        "login": login_pass[0],
        "password": login_pass[1],
        "first_name": login_pass[2]
    }
    
    yield courier_data
    
    # Удаление курьера после теста
    auth_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', 
                                   data={"login": courier_data["login"], "password": courier_data["password"]})
    courier_id = auth_response.json().get('id')
    if courier_id:
        requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')

        