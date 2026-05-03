import allure
import requests
from data import CourierData
from helpers import generate_random_string


@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.title('Создание курьера с валидными данными')
    def test_create_courier_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        firstName = generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": firstName
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 201
        assert response.json() == CourierData.CREATE_COURIER_SUCCESS_RESPONSE

        # удаляем созданного курьера
        auth_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', 
                                       data={"login": login, "password": password})
        courier_id = auth_response.json().get('id')
        if courier_id:
            requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')

    @allure.title('Попытка создать двух одинаковых курьеров')
    def test_create_duplicate_courier_fails(self, create_and_delete_courier):
        payload = {
            "login": create_and_delete_courier["login"],
            "password": create_and_delete_courier["password"],
            "firstName": create_and_delete_courier["first_name"]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 409
        assert response.json() == CourierData.CREATE_COURIER_DUPLICATE_ERROR

    @allure.title('Ошибка при отсутствии обязательного поля при создании курьера')
    def test_create_courier_missing_login_field_fails(self):
        password = generate_random_string(10)
        firstName = generate_random_string(10)
        payload = {
            "password": password,
            "firstName": firstName
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 400
        assert response.json() == CourierData.CREATE_COURIER_MISSING_FIELD_ERROR

    @allure.title('Ошибка при создании курьера с существующим логином')
    def test_create_courier_existing_login_fails(self, create_and_delete_courier):
        # Берём существующий логин из словаря, а остальные поля генерируем новые
        existing_login = create_and_delete_courier["login"]
        new_password = generate_random_string(10)
        new_firstName = generate_random_string(10)
        payload = {
            "login": existing_login,
            "password": new_password,
            "firstName": new_firstName
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 409
        assert response.json() == CourierData.CREATE_COURIER_DUPLICATE_ERROR

