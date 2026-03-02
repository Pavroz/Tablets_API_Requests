import requests
import random
import string
from endpoints.auth_endpoint import AuthEndpoint
from config import config
from requests import Response



class ProfileEndpoint(AuthEndpoint):

    def __init__(self, token: str):
        super().__init__(token)

    def _generate_profile_name(self, prefix='test_', length=20):
        suffix = ''.join(random.choice(string.ascii_lowercase + string.digits)
                         for _ in range(length - len(prefix)))
        return f'{prefix}{suffix}'

    def _random_string(self):
        return ''.join(random.choices(string.ascii_lowercase, k=10))

    def get_profile_by_id(self, id_for_get: str) -> Response:
        url = f'{config.URL}/profiles/{id_for_get}'
        response = requests.get(url, headers=self.headers)
        # assert response.status_code == 200
        # assert isinstance(response.json(), dict)
        # print('Профиль получен успешно')
        return response

    def put_profile_by_id(self, id_for_put: str) -> Response:
        name = self._generate_profile_name()
        description = self._random_string()
        url = f'{config.URL}/profiles/{id_for_put}'
        payload = {'name': name, 'description': description}
        response = requests.put(url, json=payload, headers=self.headers)
        # assert response.status_code == 201
        # assert isinstance(response.json(), dict)
        # print('Профиль изменен успешно')
        # return response.json()['id']
        return response

    def delete_profile(self, id_for_delete: str) -> Response:
        url = f'{config.URL}/profiles/{id_for_delete}'
        response = requests.delete(url, headers=self.headers)
        assert response.status_code == 204
        # print('Профиль удалился успешно')
        return response

    def get_all_profiles(self) -> Response:
        url = f'{config.URL}/profiles'
        response = requests.get(url, headers=self.headers)
        # assert response.status_code == 200
        # assert isinstance(response.json(), list)
        # print('\nСписок профилей получен успешно')
        return response

    def create_new_profile(self) -> Response:
        name = self._generate_profile_name()
        description = self._random_string()
        url = f'{config.URL}/profiles'
        payload = {'name': name, 'description': description}
        response = requests.post(url, json=payload, headers=self.headers)
        print(response)
        return response

    def copy_profile(self, id_for_copy: str) -> Response:
        new_name = self._generate_profile_name()
        url = f'{config.URL}/profiles/{id_for_copy}/copy'
        params = {'name': new_name}
        response = requests.post(url, params=params, headers=self.headers)
        # assert response.status_code == 201
        # assert isinstance(response.json(), dict)
        # print('Профиль скопировался успешно')
        return response

    def get_active_profile(self) -> Response:
        """Получение активного профиля"""
        url = f'{config.URL}/profiles/active'
        response = requests.get(url, headers=self.headers)
        return response

    def activate_profile(self, id_for_set: str) -> Response:
        """Активация профиля"""
        url = f'{config.URL}/profiles/active'
        params = {'id': id_for_set}
        response = requests.post(url, params=params, headers=self.headers)
        return response

    def deactivate_profile(self) -> Response:
        """Деактивация профиля"""
        url = f'{config.URL}/profiles/active'
        response = requests.delete(url, headers=self.headers)
        return response
