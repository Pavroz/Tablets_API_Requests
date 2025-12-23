from data import test_data
from endpoints.auth_endpoint import AuthEndpoint
import requests

class MemberEndpoint(AuthEndpoint):

    def put_member(self):
        pass

    def create_member(self, profileid, middlename=None, subject=None, position=None):
        token = self.get_auth_token()
        url = f'{test_data.url}/members'
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
        assert response.status_code == 201
        assert isinstance(response.json(), dict)
        return response.json()['id']








    def delete_member(self):
        pass