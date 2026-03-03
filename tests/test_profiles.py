import pytest
import allure
import logging

logger = logging.getLogger(__name__)

@allure.feature('Страница профилей')
class TestProfiles:

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка получения профиля')
    @pytest.mark.profiles
    def test_get_profile_by_id(self, profile_endpoint):
        id_profile = profile_endpoint.create_new_profile().json()['id']
        response = profile_endpoint.get_profile_by_id(id_profile)
        logger.info(f'Получен профиль id={response.json()["id"]}')
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        assert id_profile == response.json()['id']
        profile_endpoint.delete_profile(id_profile)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка изменения профиля')
    @pytest.mark.profiles
    def test_put_profile_by_id(self, profile_endpoint):
        id_new_profile = profile_endpoint.create_new_profile().json()['id']
        response = profile_endpoint.put_profile_by_id(id_new_profile)
        logger.info(f'Профиль изменен, новые данные: {response.json()}')
        assert response.status_code == 201
        assert isinstance(response.json(), dict)
        profile_endpoint.delete_profile(id_new_profile)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка удаления профиля')
    @pytest.mark.profiles
    def test_delete_profile(self, profile_endpoint):
        id_profile = profile_endpoint.create_new_profile().json()['id']
        profile_endpoint.delete_profile(id_profile)
        logger.info('Профиль успешно удален')
        response = profile_endpoint.get_profile_by_id(id_profile)
        logger.info(f'Удаленный профиль не найден, ошибка: {response.status_code}')
        assert response.status_code == 404

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
        response = profile_endpoint.create_new_profile()
        logger.info(f'Создан профиль id={response.json()["id"]}, name={response.json()["name"]}')
        assert response.status_code == 201
        assert isinstance(response.json(), dict)
        profile_endpoint.delete_profile(response.json()['id'])

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка копирования профиля')
    @pytest.mark.profiles
    def test_copy_profile(self, profile_endpoint):
        response = profile_endpoint.create_new_profile().json()['id']
        new_response = profile_endpoint.copy_profile(response)
        assert new_response.status_code == 201
        assert isinstance(new_response.json(), dict)
        profile_endpoint.delete_profile(response)
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
        id_profile = profile_endpoint.create_new_profile().json()['id']
        response = profile_endpoint.activate_profile(id_profile)
        assert response.status_code == 204
        active = profile_endpoint.get_active_profile()
        assert active.json() == id_profile
        profile_endpoint.delete_profile(id_profile)

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка деактивации профиля')
    @pytest.mark.profiles
    def test_deactivate_profile(self, profile_endpoint):
        id_new_profile = profile_endpoint.create_new_profile().json()['id']
        response = profile_endpoint.deactivate_profile()
        assert response.status_code == 204
        profile_endpoint.delete_profile(id_new_profile)
