# test_E2E UI

1) Установка Python
https://www.python.org/downloads/

2) Устоновка удобной IDE
в моем случае среда разработки VS code

3) Установка Pytest через терминал в IDE
pip install pytest

4) Установка Selene через терминал в IDE  
pip install selene --pre

5) Клонирование / скачивание репозитория:
https://github.com/as-usual-all-the-names-are-busy/test_E2E-UI.git

6) Запустить тест и радоваться жизни)

Сценарий теста:
Тест должен выполнять следующие действия на сайте saucedemo.com:
Авторизация: Использовать тестовый аккаунт:
Логин: standard_user
Пароль: secret_sauce
Выбор товара: "Sauce Labs Backpack" и добавить его в корзину.
Оформление покупки:
Перейти в корзину и убедиться, что товар добавлен.
Оформить покупку, заполнив поля
Завершить покупку.
Проверка: Убедиться, что покупка завершена успешно.
