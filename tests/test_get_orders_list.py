import allure
import requests


@allure.feature('Получение списка заказов')
class TestGetOrdersList:

    @allure.title('В тело ответа возвращается список заказов')
    def test_get_orders_list_returns_list(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        assert response.status_code == 200
        response_body = response.json()
        assert 'orders' in response_body
        assert isinstance(response_body['orders'], list)

    def test_get_orders_list_limited(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/v1/orders?limit=10&page=0')
        assert response.status_code == 200
        

