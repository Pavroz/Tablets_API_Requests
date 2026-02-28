import requests
import random
import string
from endpoints.auth_endpoint import AuthEndpoint
from config import config



class ProfileEndpoint(AuthEndpoint):

    def _generate_profile_name(self, prefix='test_', length=20):
        suffix = ''.join(random.choice(string.ascii_lowercase + string.digits)
                         for _ in range(length - len(prefix)))
        return f'{prefix}{suffix}'

    def _random_string(self):
        return ''.join(random.choices(string.ascii_lowercase, k=10))

    def get_profile_by_id(self, id_for_get):
        token = self.get_auth_token()
        url = f'{config.URL}/profiles/{id_for_get}'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        # assert response.status_code == 200
        # assert isinstance(response.json(), dict)
        # print('Профиль получен успешно')
        return response

    def put_profile_by_id(self, id_for_put):
        name = self._generate_profile_name()
        description = self._random_string()
        token = self.get_auth_token()
        url = f'{config.URL}/profiles/{id_for_put}'
        payload = {'name': name, 'description': description}
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.put(url, json=payload, headers=headers)
        # assert response.status_code == 201
        # assert isinstance(response.json(), dict)
        # print('Профиль изменен успешно')
        # return response.json()['id']
        return response

    def delete_profile(self, id_for_delete):
        token = self.get_auth_token()
        url = f'{config.URL}/profiles/{id_for_delete}'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.delete(url, headers=headers)
        assert response.status_code == 204
        # print('Профиль удалился успешно')
        return response

    def get_all_profiles(self):
        token = self.get_auth_token()
        url = f'{config.URL}/profiles'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        # assert response.status_code == 200
        # assert isinstance(response.json(), list)
        # print('\nСписок профилей получен успешно')
        return response

    def create_new_profile(self):
        name = self._generate_profile_name()
        description = self._random_string()
        token = self.get_auth_token()
        url = f'{config.URL}/profiles'
        payload = {'name': name, 'description': description}
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(url, json=payload, headers=headers)
        assert response.status_code == 201
        assert isinstance(response.json(), dict)
        # print('\nПрофиль создался успешно')
        return response.json()['id']

    def copy_profile(self, id_for_copy):
        new_name = self._generate_profile_name()
        token = self.get_auth_token()
        url = f'{config.URL}/profiles/{id_for_copy}/copy'
        params = {'name': new_name}
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(url, params=params, headers=headers)
        # assert response.status_code == 201
        # assert isinstance(response.json(), dict)
        # print('Профиль скопировался успешно')
        return response

    def get_active_profile(self):
        """Получение активного профиля"""
        token = self.get_auth_token()
        url = f'{config.URL}/profiles/active'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        return response

    def activate_profile(self, id_for_set):
        """Активация профиля"""
        token = self.get_auth_token()
        url = f'{config.URL}/profiles/active'
        params = {'id': id_for_set}
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(url, params=params, headers=headers)
        return response

    def deactivate_profile(self):
        """Деактивация профиля"""
        token = self.get_auth_token()
        url = f'{config.URL}/profiles/active'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.delete(url, headers=headers)
        return response
