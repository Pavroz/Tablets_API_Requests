import requests
from config import config



class AuthEndpoint:

    def get_auth_token(self):
        url = f'{config.URL}/common/auth'
        payload = {'login': f'{config.LOGIN}', 'password': f'{config.PASSWORD}'}
        response = requests.post(url, json=payload)
        response.raise_for_status() # Проверка, что ответ успешен
        assert isinstance(response.text, str) # Проверка, что ответ - строка
        assert len(response.text) > 0 # Проверка, что длина ответа > 0
        assert response.status_code == 200 # Проверка, что код ответа 200
        return response.text

    def auth_empty_login_and_password(self):
        """Авторизация с пустыми полями"""
        url = f'{config.URL}/common/auth'
        payload = {'login': ' ', 'password': ' '}
        response = requests.post(url, json=payload)
        return response

    def auth_empty_login(self):
        """Авторизация с некорректным логином"""
        url = f'{config.URL}/common/auth'
        payload = {'login': ' ', 'password': config.PASSWORD}
        response = requests.post(url, json=payload)
        return response

    def auth_empty_password(self):
        url = f'{config.URL}/common/auth'
        payload = {'login': f'{config.LOGIN}', 'password': ' '}
        response = requests.post(url, json=payload)
        return response

    def auth_incorrect_login_and_password(self):
        url = f'{config.URL}/common/auth'
        payload = {'login': 'qwe', 'password': 'qwe'}
        response = requests.post(url, json=payload)
        assert response.json()['errorMessage'] == f"Пользователь с логином '{payload["login"]}' не найден"
        return response

    def auth_incorrect_login(self):
        url = f'{config.URL}/common/auth'
        payload = {'login': 'qwe', 'password': config.PASSWORD}
        response = requests.post(url, json=payload)
        assert response.json()['errorMessage'] == f"Пользователь с логином '{payload["login"]}' не найден"
        return response

    def auth_incorrect_password(self):
        url = f'{config.URL}/common/auth'
        payload = {'login': config.LOGIN, 'password': 'qwe'}
        response = requests.post(url, json=payload)
        assert response.json()['errorMessage'] == "Неверные учетные данные"
        return response
