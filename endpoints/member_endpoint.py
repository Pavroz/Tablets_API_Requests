from endpoints.auth_endpoint import AuthEndpoint
import requests
from requests import Response
from config import config
import random
import string
import allure
import logging
from tools.logger import logger

class MemberEndpoint(AuthEndpoint):

    def __init__(self, token: str):
        super().__init__(token)

    @staticmethod
    def _random_string():
        return ''.join(random.choices(string.ascii_lowercase, k=10))

    @allure.step('Создание участника')
    def create_member(
            self,
            id_profile: str,
            middlename: str=None,
            subject: str=None,
            position: str=None
    ) -> Response:
        url = f'{config.URL}/members'
        payload = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "middleName": middlename,
            "position": position,
            "county": subject,
            "profileId": id_profile
        }

        logger.info('Создание участника')
        logger.info(f'payload: {payload}')
        response = requests.post(url, json=payload, headers=self.headers)

        logger.info(f'Создание участника завершено. Статус: {response.status_code}')
        return response

    @allure.step('Получение участника')
    def get_member(self, id_member: str) -> Response:
        url = f'{config.URL}/members/{id_member}'

        logger.info(f'Получение участника по id: {id_member}')
        response = requests.get(url, headers=self.headers)

        logger.info(f'Получение участника завершено. Статус: {response.status_code}')
        return response

    @allure.step('Изменение участника')
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

        logger.info(f'Изменение участника по id: {id_member}')
        logger.info(f'payload: {payload}')
        response = requests.put(url, json=payload, headers=self.headers)

        logger.info(f'Изменение участника завершено. Статус: {response.status_code}')
        return response



    def delete_member(self):
        pass