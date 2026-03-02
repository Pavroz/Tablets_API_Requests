from endpoints.auth_endpoint import AuthEndpoint
import requests
from requests import Response
from config import config
import random
import string

class MemberEndpoint(AuthEndpoint):

    def __init__(self, token: str):
        super().__init__(token)

    @staticmethod
    def _random_string():
        return ''.join(random.choices(string.ascii_lowercase, k=10))

    def create_member(self, id_profile: str, middlename: str=None, subject: str=None, position: str=None) -> Response:
        url = f'{config.URL}/members'
        payload = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "middleName": middlename,
            "position": position,
            "county": subject,
            "profileId": id_profile
        }
        response = requests.post(url, json=payload, headers=self.headers)
        return response


    def get_member(self, id_member: str) -> Response:
        url = f'{config.URL}/members/{id_member}'
        response = requests.get(url, headers=self.headers)
        return response


    def put_member(
            self,
            id_profile: str,
            id_member: str,
            firstname: str,
            lastname: str,
            middlename: str=None,
            position: str=None,
            subject: str=None
    ) -> Response:
        url = f'{config.URL}/members'
        payload = {
            'id': id_member,
            'firstName': firstname,
            'lastName': lastname,
            'middleName': middlename,
            'position': position,
            'county': subject,
            'profileId': id_profile
        }
        response = requests.put(url, json=payload, headers=self.headers)
        return response



    def delete_member(self):
        pass