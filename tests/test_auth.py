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
        response = auth_endpoint.auth_empty_login_and_password()
        assert response.status_code == 400
        assert isinstance(response.json(), dict)
        violations = response.json()['violations']
        for v in violations:
            assert v['message'] == "не должно быть пустым"

    @allure.story('Негативные сценарии')
    @allure.title('Проерка авторизации с пустым логином')
    @pytest.mark.auth
    def test_auth_empty_login(self, auth_endpoint):
        response = auth_endpoint.auth_empty_login()
        assert isinstance(response.json(), dict)
        assert response.status_code == 400
        violations = response.json()['violations']
        for v in violations:
            assert v['message'] == "не должно быть пустым"

    @allure.story('Негативные сценарии')
    @allure.title('Проерка авторизации с пустым паролем')
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