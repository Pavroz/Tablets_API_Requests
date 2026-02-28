import pytest
import allure
from constants import member_cases


class TestMember:

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка создания участника')
    @pytest.mark.parametrize(
        "middlename, subject, position", member_cases.MEMBER_CASES)
    def test_create_member(
            self, profile_endpoint, member_endpoint,
            middlename, subject, position
    ):
        id_new_profile = profile_endpoint.create_new_profile()
        response = member_endpoint.create_member(
            profileid=id_new_profile,
            middlename=middlename,
            subject=subject,
            position=position)
        assert response.status_code == 201
        assert isinstance(response.json(), dict)
        assert 'id' in response.json()
        profile_endpoint.delete_profile(id_new_profile)

    def test_get_member(self, profile_endpoint, member_endpoint):
        id_new_profile = profile_endpoint.create_new_profile()
        id_member = member_endpoint.create_member(profileid=id_new_profile)
        response = member_endpoint.get_member(id_member.json()['id'])
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        assert 'id' in response.json()
        assert isinstance(response.json()['id'], int)
        assert response.json()['id'] == id_member.json()['id']
        profile_endpoint.delete_profile(id_new_profile)