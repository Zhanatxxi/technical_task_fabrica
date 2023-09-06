<h4>Документация </h4>

http://164.90.230.152/swagger/ </br>
http://164.90.230.152/redoc/

<h4>Admin panel </h4>
http://164.90.230.152/admin/ </br>
<strong> email: admin@amin.com </br>
password: 1 </stong>

POST http://164.90.230.152/api/v1/account/register/ </br>
регистрация нового пользователя по email
POST http://164.90.230.152/api/v1/account/login/ </br>
авторизция пользователя (email, password)
return: Token, нужно передавать в headers Authorization: Token <obtain_token>

GET http://164.90.230.152/api/v1/account/telegram-token/
получение уникального токена для идентификации в боте
PUT http://164.90.230.152/api/v1/account/telegram-token/
обновление уникального токена

GET http://164.90.230.152/api/v1/telegram/message/
получения списка сообщений
POST http://164.90.230.152/api/v1/telegram/message/
data key 'message': <your_message>

telegram bot: @agent_test_bot

для локального запуска нужен poetry and python > 3.10 </br>
создать файл .env
c данными (TELEGRAM_TOKEN, SECRET_KEY, DEBUG, SENTRY_DSN)
git clone project </br>
poetry install </br>
poetry run python manage.py migrate </br>
poetry run python manage.py runserver </br>
poetry run python manage.py run_bot </br>

