from endpoints.auth_endpoint import AuthEndpoint
import requests
from config import config
import random
import string

class MemberEndpoint(AuthEndpoint):

    def _random_string(self):
        return ''.join(random.choices(string.ascii_lowercase, k=10))

    def create_member(self, id_profile, middlename=None, subject=None, position=None):
        token = self.get_auth_token()
        url = f'{config.URL}/members'
        headers = {'Authorization': f'Bearer {token}'}
        payload = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "middleName": middlename,
            "position": position,
            "county": subject,
            "profileId": id_profile
        }
        response = requests.post(url, json=payload, headers=headers)
        return response


    def get_member(self, id_member):
        token = self.get_auth_token()
        url = f'{config.URL}/members/{id_member}'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        return response


    def put_member(self, id_profile, id_member, firstname, lastname, middlename=None, position=None, subject=None):
        token = self.get_auth_token()
        url = f'{config.URL}/members'
        headers = {'Authorization': f'Bearer {token}'}
        payload = {
            'id': id_member,
            'firstName': firstname,
            'lastName': lastname,
            'middleName': middlename,
            'position': position,
            'county': subject,
            'profileId': id_profile
        }
        response = requests.put(url, json=payload, headers=headers)
        return response



    def delete_member(self):
        pass