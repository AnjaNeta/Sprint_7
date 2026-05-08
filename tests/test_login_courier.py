import allure
import pytest
import requests
from data import CourierData
from helpers import generate_random_string


@allure.feature('Логин курьера')
class TestLoginCourier:

    @allure.title('Авторизация с валидными данными')
    def test_login_courier_success(self, create_and_delete_courier):
        payload = {
            "login": create_and_delete_courier["login"],
            "password": create_and_delete_courier["password"]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Авторизация с неверным логином')
    def test_login_courier_wrong_login_fails(self, create_and_delete_courier):
        payload = {
            "login": generate_random_string(10), 
            "password": create_and_delete_courier["password"]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    @allure.title('Авторизация с неверным паролем')
    def test_login_courier_wrong_password_fails(self, create_and_delete_courier):
        payload = {
            "login": create_and_delete_courier["login"],
            "password": generate_random_string(10)  
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    @allure.title('Авторизация без обязательного поля')
    def test_login_courier_missing_login_fails(self, create_and_delete_courier):
        payload = {
            "password": create_and_delete_courier["password"]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для входа"}

