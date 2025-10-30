import pytest

from endpoints.auth_endpoint import AuthEndpoint
from endpoints.create_url_endpoint import CreateUrlEndpoint
import random
import string # Хранилище стринговых символов

from endpoints.profile_endpoint import ProfileEndpoint


@pytest.fixture()
def create_url_endpoint():
    return CreateUrlEndpoint()

@pytest.fixture()
def auth_endpoint():
    return AuthEndpoint()

@pytest.fixture()
def profile_endpoint():
    return ProfileEndpoint()

@pytest.fixture()
def random_string():
    return ''.join(random.choices(string.ascii_lowercase, k=10))

@pytest.fixture()
def create_and_delete_profile(create_url_endpoint, random_string):
    """Создание и удаление профиля"""
    name = random_string
    description = random_string
    create_url_endpoint.create_new_profile(name, description)
    print('\nПрофиль создан')
    yield
    create_url_endpoint.delete_profile()
    print('\nПрофиль удален')