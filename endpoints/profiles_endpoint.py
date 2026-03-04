import requests
import random
import string
from endpoints.auth_endpoint import AuthEndpoint
from config import config
from requests import Response
import logging
import allure
from utils.validator import Validator

logger = logging.getLogger(__name__)

class ProfileEndpoint(AuthEndpoint):

    validator = Validator()

    def __init__(self, token: str):
        super().__init__(token)

    def _generate_profile_name(self, prefix='test_', length=20):
        suffix = ''.join(random.choice(string.ascii_lowercase + string.digits)
                         for _ in range(length - len(prefix)))
        return f'{prefix}{suffix}'

    def _random_string(self):
        return ''.join(random.choices(string.ascii_lowercase, k=10))

    @allure.step('Получение профиля')
    def get_profile_by_id(self, id_for_get: str) -> Response:
        url = f'{config.URL}/profiles/{id_for_get}'

        logger.info(f'Получение профиля по id: {id_for_get}')
        logger.info(f'url: {url}')
        response = requests.get(url, headers=self.headers)

        logger.info(f'Получение профиля завершено. Статус: {response.status_code}')
        return response

    @allure.step('Изменение профиля')
    def put_profile_by_id(self, id_for_put: str) -> Response:
        name = self._generate_profile_name()
        description = self._random_string()
        url = f'{config.URL}/profiles/{id_for_put}'
        payload = {'name': name, 'description': description}

        logger.info(f'Изменение профиля по id: {id_for_put}')
        logger.info(f'url: {url}, payload: {payload}')
        response = requests.put(url, json=payload, headers=self.headers)

        logger.info(f'Изменение профиля завершено. Статус: {response.status_code}')
        return response

    @allure.step('Удаление профиля')
    def delete_profile(self, id_for_delete: str) -> Response:
        url = f'{config.URL}/profiles/{id_for_delete}'

        logger.info(f'Удаление профиля по id: {id_for_delete}')
        response = requests.delete(url, headers=self.headers)
        self.validator.assert_status_code(response, 204)

        logger.info(f'Удаление профиля завершено. Статус: {response.status_code}')
        return response

    @allure.step('Получение всех профилей')
    def get_all_profiles(self) -> Response:
        url = f'{config.URL}/profiles'

        logger.info('Получение всех профилей')
        response = requests.get(url, headers=self.headers)

        logger.info(f'Получение всех профилей завершено. Статус: {response.status_code}')
        return response

    @allure.step('Создание нового профиля')
    def create_new_profile(self) -> Response:
        name = self._generate_profile_name()
        description = self._random_string()
        url = f'{config.URL}/profiles'
        payload = {'name': name, 'description': description}

        logger.info(f'Создание нового профиля: {name}')
        logger.info(f'url: {url}, payload: {payload}')
        response = requests.post(url, json=payload, headers=self.headers)

        logger.info(f'Создание профиля завершено. Статус: {response.status_code}')
        return response

    @allure.step('Копирование профиля')
    def copy_profile(self, id_for_copy: str) -> Response:
        new_name = self._generate_profile_name()
        url = f'{config.URL}/profiles/{id_for_copy}/copy'
        params = {'name': new_name}

        logger.info(f'Копирование профиля по id: {id_for_copy}')
        logger.info(f'url: {url}, params: {params}')
        response = requests.post(url, params=params, headers=self.headers)

        logger.info(f'Копирование профиля завершено. Статус: {response.status_code}')
        return response

    @allure.step('Получение активного профиля')
    def get_active_profile(self) -> Response:
        """Получение активного профиля"""
        url = f'{config.URL}/profiles/active'

        logger.info('Получение активного профиля')
        response = requests.get(url, headers=self.headers)

        logger.info(f'Получение активного профиля завершено. Статус: {response.status_code}')
        return response

    @allure.step('Активация профиля')
    def activate_profile(self, id_for_set: str) -> Response:
        """Активация профиля"""
        url = f'{config.URL}/profiles/active'
        params = {'id': id_for_set}

        logger.info(f'Активация профиля по id: {id_for_set}')
        logger.info(f'url: {url}, params: {params}')
        response = requests.post(url, params=params, headers=self.headers)

        logger.info(f'Активация профиля завершена. Статус: {response.status_code}')
        return response

    @allure.step('Деактивация активного профиля')
    def deactivate_profile(self) -> Response:
        """Деактивация активного профиля"""
        url = f'{config.URL}/profiles/active'

        logger.info('Деактивация активного профиля')
        response = requests.delete(url, headers=self.headers)

        logger.info(f'Деактивация активного профиля завершена. Статус: {response.status_code}')
        return response
