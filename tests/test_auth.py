import pytest
import allure

@allure.feature('Авторизация')
class TestAuth:

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка авторизации')
    @pytest.mark.auth
    def test_auth(self, auth_endpoint):
        auth_endpoint.get_auth_token()

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с пустыми полями ввода')
    @pytest.mark.auth
    def test_empty_login_and_password(self, auth_endpoint):
        auth_endpoint.auth_empty_login_and_password()

    @allure.story('Негативные сценарии')
    @allure.title('Проерка авторизации с пустым логином')
    @pytest.mark.auth
    def test_auth_empty_login(self, auth_endpoint):
        auth_endpoint.auth_empty_login()

    @allure.story('Негативные сценарии')
    @allure.title('Проерка авторизации с пустым паролем')
    @pytest.mark.auth
    def test_auth_empty_password(self, auth_endpoint):
        auth_endpoint.auth_empty_password()

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с некорректным логином и паролем')
    @pytest.mark.auth
    def test_auth_incorrect_login_and_password(self, auth_endpoint):
        auth_endpoint.auth_incorrect_login_and_password()

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с некорректным логином')
    @pytest.mark.auth
    def test_auth_incorrect_login(self, auth_endpoint):
        auth_endpoint.auth_incorrect_login()

    @allure.story('Негативные сценарии')
    @allure.title('Проверка авторизации с некорректным паролем')
    @pytest.mark.auth
    def test_auth_incorrect_password(self, auth_endpoint):
        auth_endpoint.auth_incorrect_password()