from endpoints.auth_endpoint import AuthEndpoint
import requests
from config import config

class MemberEndpoint(AuthEndpoint):

    def put_member(self):
        pass

    def create_member(self, profileid, middlename=None, subject=None, position=None):
        token = self.get_auth_token()
        url = f'{config.URL}/members'
        headers = {'Authorization': f'Bearer {token}'}
        payload = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "middleName": middlename,
            "position": position,
            "county": subject,
            "profileId": profileid
        }
        response = requests.post(url, json=payload, headers=headers)
        return response


    def get_member(self, id_member):
        token = self.get_auth_token()
        url = f'{config.URL}/members/{id_member}'
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        return response






    def delete_member(self):
        pass