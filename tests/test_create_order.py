import allure
import pytest
import requests
from data import OrderData


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с цветом: {color}')
    @pytest.mark.parametrize('order_payload, color', [
        (OrderData.order_payloads[0], "BLACK"),
        (OrderData.order_payloads[1], "GREY"),
        (OrderData.order_payloads[2], "BLACK+GREY"),
        (OrderData.order_payloads[3], "без цвета")
    ])
    def test_create_order_different_colors(self, order_payload, color):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=order_payload)
        assert response.status_code == 201
        assert 'track' in response.json()

        