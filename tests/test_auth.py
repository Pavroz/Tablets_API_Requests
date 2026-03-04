import pytest
import allure
import logging
from utils.validator import Validator

logger = logging.getLogger(__name__)

@allure.feature('Авторизация')
class TestAuth:

    validator = Validator()

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка авторизации с корректными данными')
    @pytest.mark.api
    @pytest.mark.auth
    def test_auth_correct(self, auth_endpoint):
        response = auth_endpoint.auth_correct()
        self.validator.assert_isinstance(response.text, str)
        self.validator.assert_response_not_empty(response)
        self.validator.assert_len(response.text)
        self.validator.assert_status_code(response, 200)


    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с пустыми полями ввода')
    @pytest.mark.auth
    def test_auth_empty_login_and_password(self, auth_endpoint):
        response = auth_endpoint.auth_empty_login_and_password()
        self.validator.assert_status_code(response, 400)
        self.validator.assert_isinstance(response.json(), dict)
        self.validator.assert_violation_message(response, "не должно быть пустым")

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с пустым логином')
    @pytest.mark.auth
    def test_auth_empty_login(self, auth_endpoint):
        response = auth_endpoint.auth_empty_login()
        self.validator.assert_isinstance(response.json(), dict)
        self.validator.assert_status_code(response, 400)
        self.validator.assert_violation_message(response, "не должно быть пустым")

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с пустым паролем')
    @pytest.mark.auth
    def test_auth_empty_password(self, auth_endpoint):
        response = auth_endpoint.auth_empty_password()
        self.validator.assert_isinstance(response.json(), dict)
        self.validator.assert_status_code(response, 400)
        self.validator.assert_violation_message(response, "не должно быть пустым")

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с некорректным логином и паролем')
    @pytest.mark.auth
    def test_auth_incorrect_login_and_password(self, auth_endpoint):
        response = auth_endpoint.auth_incorrect_login_and_password()
        self.validator.assert_isinstance(response.json(), dict)
        self.validator.assert_status_code(response, 401)

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с некорректным логином')
    @pytest.mark.auth
    def test_auth_incorrect_login(self, auth_endpoint):
        response = auth_endpoint.auth_incorrect_login()
        self.validator.assert_isinstance(response.json(), dict)
        self.validator.assert_status_code(response, 401)

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с некорректным паролем')
    @pytest.mark.auth
    def test_auth_incorrect_password(self, auth_endpoint):
        response = auth_endpoint.auth_incorrect_password()
        self.validator.assert_isinstance(response.json(), dict)
        self.validator.assert_status_code(response, 401)