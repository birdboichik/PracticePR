# Работу выполнил Сашников Данил Евгеньевич МО-221

# Инструкция по запуску:
* Вводим следующие команды в терминал:
* pip install pytest
* pip install playwright
* pip install pytest-html
* pytest tests/
* Отчет находится в файле "report.html"
# Тесты:
* "test_correct_login_and_empty_password.py" - Авторизация с правильным логином, но пустым паролем
* "test_correct_login_and_password.py" - Верная авторизация, бронирование 2-х товаров в корзине, переход в корзину, checkout, полное заполнение полей firstName lastName postalCode.
* "test_empty_login_and_correct_password.py" - Авторизация только с пустым паролем
* "test_empty_login_and_password.py" - Авторизация с неверным паролем 