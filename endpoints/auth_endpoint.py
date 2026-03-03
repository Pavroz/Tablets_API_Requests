import requests
from config import config
from requests import Response
import logging

# Получение логгера для текущего модуля
logger = logging.getLogger(__name__)

class AuthEndpoint:

    def __init__(self, token: str | None = None):
        self.token = token
        self.headers = (
            {'Authorization': f'Bearer {token}'} if token else {}
        )


    def auth_correct(self) -> Response:
        url = f'{config.URL}/common/auth'
        payload = {'login': config.LOGIN, 'password': config.PASSWORD}

        logger.info("Начало запроса авторизации")
        logger.info(f"URL: {url}")
        logger.info(f"Payload: {payload}")

        response = requests.post(url, json=payload)

        logger.info(f"Ответ на авторизацию получен. Статус: {response.status_code}")
        return response


    def auth_empty_login_and_password(self) -> Response:
        """Авторизация с пустыми полями"""
        url = f'{config.URL}/common/auth'
        payload = {'login': ' ', 'password': ' '}
        response = requests.post(url, json=payload)
        return response

    def auth_empty_login(self) -> Response:
        """Авторизация с некорректным логином"""
        url = f'{config.URL}/common/auth'
        payload = {'login': ' ', 'password': config.PASSWORD}
        response = requests.post(url, json=payload)
        return response

    def auth_empty_password(self) -> Response:
        url = f'{config.URL}/common/auth'
        payload = {'login': config.LOGIN, 'password': ' '}
        response = requests.post(url, json=payload)
        return response

    def auth_incorrect_login_and_password(self) -> Response:
        url = f'{config.URL}/common/auth'
        payload = {'login': 'qwe', 'password': 'qwe'}
        response = requests.post(url, json=payload)
        assert response.json()['errorMessage'] == f"Пользователь с логином '{payload["login"]}' не найден"
        return response

    def auth_incorrect_login(self) -> Response:
        url = f'{config.URL}/common/auth'
        payload = {'login': 'qwe', 'password': config.PASSWORD}
        response = requests.post(url, json=payload)
        assert response.json()['errorMessage'] == f"Пользователь с логином '{payload["login"]}' не найден"
        return response

    def auth_incorrect_password(self) -> Response:
        url = f'{config.URL}/common/auth'
        payload = {'login': config.LOGIN, 'password': 'qwe'}
        response = requests.post(url, json=payload)
        if response.status_code != 401:
            logger.error(f'Ожидался статус 401 при некорректном пароле, получили {response.status_code}')
        try:
            assert response.json()['errorMessage'] == "Неверные учетные данные"
        except AssertionError:
            logger.error(f'Сообщение об ошибке некорректное: {response.json()}')
        return response
