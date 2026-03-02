import pytest
import requests

from config import config
from endpoints.auth_endpoint import AuthEndpoint


from endpoints.member_endpoint import MemberEndpoint
from endpoints.profiles_endpoint import ProfileEndpoint

@pytest.fixture()
def auth_endpoint():
    return AuthEndpoint()

@pytest.fixture()
def profile_endpoint():
    return ProfileEndpoint()

@pytest.fixture()
def member_endpoint():
    return MemberEndpoint()

@pytest.fixture()
def get_auth_token():
    url = f'{config.URL}/common/auth'
    payload = {'login': f'{config.LOGIN}', 'password': f'{config.PASSWORD}'}
    response = requests.post(url, json=payload)
    response.raise_for_status() # Проверка, что ответ успешен
    assert isinstance(response.text, str) # Проверка, что ответ - строка
    assert len(response.text) > 0 # Проверка, что длина ответа > 0
    assert response.status_code == 200 # Проверка, что код ответа 200
    return response.text
