import pytest
import allure
import logging


logger = logging.getLogger(__name__)

@allure.feature('Авторизация')
class TestAuth:

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка авторизации с корректными данными')
    @pytest.mark.api
    @pytest.mark.auth
    def test_auth_correct(self, auth_endpoint):
        logger.info('Старт теста: проверка корректной авторизации')
        with allure.step('Отправка запроса на авторизацию'):
            response = auth_endpoint.auth_correct()
        with allure.step('Проверка тела ответа'):
            assert isinstance(response.text, str)  # Проверка, что ответ - строка
            assert len(response.text) > 0  # Проверка, что длина ответа > 0
        logger.info(f'Статус ответа: {response.status_code}')
        with allure.step('Проверка, что статус код 200'):
            assert response.status_code == 200  # Проверка, что код ответа 200


    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с пустыми полями ввода')
    @pytest.mark.auth
    def test_auth_empty_login_and_password(self, auth_endpoint):
        with allure.step('Отправка запроса на авторизацию'):
            response = auth_endpoint.auth_empty_login_and_password()
        with allure.step('Проверка, что статус кода 400'):
            assert response.status_code == 400
        with allure.step('Проверка тела ответа'):
            assert isinstance(response.json(), dict)
        with allure.step('Проверка сообщения об ошибке'):
            violations = response.json()['violations']
            for v in violations:
                assert v['message'] == "не должно быть пустым"

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с пустым логином')
    @pytest.mark.auth
    def test_auth_empty_login(self, auth_endpoint):
        with allure.step('Отправка запроса на авторизацию'):
            response = auth_endpoint.auth_empty_login()
        with allure.step('Проверка тела ответа'):
            assert isinstance(response.json(), dict)
        with allure.step('Проверка, что статус кода 400'):
            assert response.status_code == 400
        with allure.step('Проверка сообщения об ошибке'):
            violations = response.json()['violations']
            for v in violations:
                assert v['message'] == "не должно быть пустым"

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с пустым паролем')
    @pytest.mark.auth
    def test_auth_empty_password(self, auth_endpoint):
        response = auth_endpoint.auth_empty_password()
        assert isinstance(response.json(), dict)
        assert response.status_code == 400
        violations = response.json()['violations']
        for v in violations:
            assert v['message'] == "не должно быть пустым"

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с некорректным логином и паролем')
    @pytest.mark.auth
    def test_auth_incorrect_login_and_password(self, auth_endpoint):
        response = auth_endpoint.auth_incorrect_login_and_password()
        assert isinstance(response.json(), dict)
        assert response.status_code == 401

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с некорректным логином')
    @pytest.mark.auth
    def test_auth_incorrect_login(self, auth_endpoint):
        response = auth_endpoint.auth_incorrect_login()
        assert isinstance(response.json(), dict)
        assert response.status_code == 401

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с некорректным паролем')
    @pytest.mark.auth
    def test_auth_incorrect_password(self, auth_endpoint):
        response = auth_endpoint.auth_incorrect_password()
        assert isinstance(response.json(), dict)
        assert response.status_code == 401