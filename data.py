class CourierData:
    # Данные для успешного создания
    valid_payload = {
        "login": "valid_login",
        "password": "valid_pass",
        "firstName": "valid_name"
    }
    # Ожидаемые ответы
    CREATE_COURIER_SUCCESS_RESPONSE = {"ok": True}
    CREATE_COURIER_MISSING_FIELD_ERROR = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    CREATE_COURIER_DUPLICATE_ERROR = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
    
class OrderData:
    # Данные для создания заказа (с цветами и без)
    order_payloads = [
        {"firstName": "Анна", "lastName": "Добрянская", "address": "ул. Пушкина, 10", "metroStation": 1, "phone": "+79991234567", "rentTime": 5, "deliveryDate": "2025-05-15", "comment": "Позвоните за час", "color": ["BLACK"]},
        {"firstName": "Петр", "lastName": "Иванов", "address": "ул. Ленина, 5", "metroStation": 2, "phone": "+79997654321", "rentTime": 3, "deliveryDate": "2025-05-16", "comment": "Домофон 123", "color": ["GREY"]},
        {"firstName": "Елена", "lastName": "Сидорова", "address": "пр. Мира, 15", "metroStation": 3, "phone": "+79991112233", "rentTime": 4, "deliveryDate": "2025-05-17", "comment": "Код домофона 456", "color": ["BLACK", "GREY"]},
        {"firstName": "Иван", "lastName": "Петров", "address": "ул. Садовая, 7", "metroStation": 4, "phone": "+79994445566", "rentTime": 2, "deliveryDate": "2025-05-18", "comment": "Вход со двора", "color": []}
    ]
    # Ожидаемый код ответа и структура
    CREATE_ORDER_EXPECTED_KEYS = ["track"]
    

