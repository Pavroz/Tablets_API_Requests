import requests
from data import data_test



class AuthEndpoint:



    def get_auth_token(self, login, password):
        url = f'{data_test.url}/common/auth'
        payload = {'login': login, 'password': password}
        response = requests.post(url, json=payload)
        response.raise_for_status() # Проверка, что ответ успешен
        assert isinstance(response.text, str) # Проверка, что ответ - строка
        assert len(response.text) > 0 # Проверка, что длина ответа > 0
        assert response.status_code == 200 # Проверка, что код ответа 200
        return response.text
