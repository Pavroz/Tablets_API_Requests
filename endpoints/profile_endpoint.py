import requests
import random
import string
from data import data_test
from endpoints.auth_endpoint import AuthEndpoint



class ProfileEndpoint(AuthEndpoint):


    def create_new_profile(self):
        name = ''.join(random.choices(string.ascii_lowercase, k=10))
        description = ''.join(random.choices(string.ascii_lowercase, k=10))
        token = self.get_auth_token(data_test.login, data_test.password)
        url = f'{data_test.url}/profiles'
        payload = {'name': name, 'description': description}
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(url, json=payload, headers=headers)
        assert response.status_code == 201
        assert isinstance(response.json(), dict)
        print('\nПрофиль создался успешно')
        return response.json()['id']


    def delete_profile(self, id_for_delete):
        token = self.get_auth_token(data_test.login, data_test.password)
        url = f'{data_test.url}/profiles/{id_for_delete}'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.delete(url, headers=headers)
        assert response.status_code == 204
        print('Профиль удалился успешно')
        return response

    def get_profile_for_id(self, id_for_get):
        token = self.get_auth_token(data_test.login, data_test.password)
        url = f'{data_test.url}/profiles/{id_for_get}'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        print('Профиль получен успешно')
        return None

    def put_profile_for_id(self, id_for_put):
        name = ''.join(random.choices(string.ascii_lowercase, k=10))
        description = ''.join(random.choices(string.ascii_lowercase, k=10))
        token = self.get_auth_token(data_test.login, data_test.password)
        url = f'{data_test.url}/profiles/{id_for_put}'
        payload = {'name': name, 'description': description}
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.put(url, json=payload, headers=headers)
        assert response.status_code == 201
        assert isinstance(response.json(), dict)
        print('Профиль изменен успешно')
        return response.json()['id']

    def get_all_profiles(self):
        token = self.get_auth_token(data_test.login, data_test.password)
        url = f'{data_test.url}/profiles'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        print('\nСписок профилей получен успешно')
        return None

    def copy_profile(self, id_for_copy):
        new_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        token = self.get_auth_token(data_test.login, data_test.password)
        url = f'{data_test.url}/profiles/{id_for_copy}/copy'
        params = {'name': new_name}
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(url, params=params, headers=headers)
        assert response.status_code == 201
        assert isinstance(response.json(), dict)
        print('Профиль скопировался успешно')
        return response.json()['id']
