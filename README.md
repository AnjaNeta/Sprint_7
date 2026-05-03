# Sprint_7

# Автотесты для сервиса «Яндекс.Самокат»
документация: qa-scooter.praktikum-services.ru/docs/.

## Описание
Проект содержит API-автотесты для учебного сервиса «Яндекс.Самокат».

## Структура проекта

├── .gitignore
├── requirements.txt
├── conftest.py # Фикстуры для тестов
├── helpers.py # Вспомогательные функции
├── data.py #  Тестовые данные
├── tests/
│   ├── test_create_courier.py # 1. Cоздание курьера
│   ├── test_login_courier.py # 2. Логин курьера
│   ├── test_create_order.py # 3. Создание заказа
│   └── test_get_orders_list.py # 4. Список заказов
└── README.md

# добавляем папку с отчётом Allure к файлам. Ключ -f пригодится, если папка target указана в .gitignore
git add -f .\target\allure-results\.
# выполняем коммит
git commit -m "add allure report"
# так отправишь файлы в удалённый репозиторий
git push

