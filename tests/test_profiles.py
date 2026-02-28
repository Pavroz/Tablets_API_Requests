import pytest
import allure

@allure.feature('Страница профилей')
class TestProfiles:

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка получения профиля')
    @pytest.mark.profiles
    def test_get_profile_by_id(self, profile_endpoint):
        id_new_profile = profile_endpoint.create_new_profile()
        response = profile_endpoint.get_profile_by_id(id_new_profile)
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        profile_endpoint.delete_profile(id_new_profile)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка изменения профиля')
    @pytest.mark.profiles
    def test_put_profile_by_id(self, profile_endpoint):
        id_new_profile = profile_endpoint.create_new_profile()
        response = profile_endpoint.put_profile_by_id(id_new_profile)
        assert response.status_code == 201
        assert isinstance(response.json(), dict)
        profile_endpoint.delete_profile(id_new_profile)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка удаления профиля')
    @pytest.mark.profiles
    def test_delete_profile(self, profile_endpoint):
        id_new_profile = profile_endpoint.create_new_profile()
        profile_endpoint.delete_profile(id_new_profile)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка получения всех профилей')
    @pytest.mark.profiles
    def test_get_all_profiles(self, profile_endpoint):
        response = profile_endpoint.get_all_profiles()
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка создания профиля')
    @pytest.mark.profiles
    def test_create_new_profile(self, profile_endpoint):
        id_new_profile = profile_endpoint.create_new_profile()
        profile_endpoint.delete_profile(id_new_profile)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка копирования профиля')
    @pytest.mark.profiles
    def test_copy_profile(self, profile_endpoint):
        id_new_profile = profile_endpoint.create_new_profile()
        new_response = profile_endpoint.copy_profile(id_new_profile)
        assert new_response.status_code == 201
        assert isinstance(new_response.json(), dict)
        profile_endpoint.delete_profile(id_new_profile)
        profile_endpoint.delete_profile(new_response.json()["id"])

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка получения активного профиля')
    @pytest.mark.profiles
    def test_get_active_profile(self, profile_endpoint):
        response = profile_endpoint.get_active_profile()
        assert response.status_code == 200

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка активации профиля')
    @pytest.mark.profiles
    def test_activate_profile(self, profile_endpoint):
        id_new_profile = profile_endpoint.create_new_profile()
        response = profile_endpoint.activate_profile(id_new_profile)
        assert response.status_code == 204
        profile_endpoint.delete_profile(id_new_profile)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка деактивации профиля')
    @pytest.mark.profiles
    def test_deactivate_profile(self, profile_endpoint):
        id_new_profile = profile_endpoint.create_new_profile()
        response = profile_endpoint.deactivate_profile()
        assert response.status_code == 204
        profile_endpoint.delete_profile(id_new_profile)
