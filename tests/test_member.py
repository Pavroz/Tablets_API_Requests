import pytest
import allure
from constants import member_cases
from tools.validator import Validator

@allure.feature('Страница участников')
class TestMember:

    validator = Validator()

    @allure.story('Позитивные сценарии')
    @allure.title('Проверка создания участника')
    @pytest.mark.parametrize(
        "middlename, subject, position", member_cases.MEMBER_CREATE_CASES)
    def test_create_member(
            self, profile_endpoint, member_endpoint,
            middlename, subject, position
    ):
        id_new_profile = profile_endpoint.create_new_profile().json()['id']
        try:
            response = member_endpoint.create_member(
                id_profile=id_new_profile,
                middlename=middlename,
                subject=subject,
                position=position)
            self.validator.assert_status_code(response, 201)
            self.validator.assert_isinstance(response.json(), dict)
            self.validator.assert_in('id',response.json())
        finally:
            profile_endpoint.delete_profile(id_new_profile)

    def test_get_member(self, profile_endpoint, member_endpoint):
        id_new_profile = profile_endpoint.create_new_profile().json()['id']
        id_member = member_endpoint.create_member(id_new_profile)
        try:
            response = member_endpoint.get_member(id_member.json()['id'])
            self.validator.assert_status_code(response, 200)
            self.validator.assert_isinstance(response.json(), dict)
            self.validator.assert_in('id',response.json())
            self.validator.assert_isinstance(response.json()['id'], int)
            self.validator.assert_equality(response.json()['id'], id_member.json()['id'])
        finally:
            profile_endpoint.delete_profile(id_new_profile)

    @pytest.mark.parametrize('firstname, lastname, middlename, position, subject', member_cases.MEMBER_PUT_CASES)
    def test_put_member(
            self, profile_endpoint, member_endpoint, firstname,
            lastname, middlename, position, subject):
        id_new_profile = profile_endpoint.create_new_profile().json()['id']
        id_member = member_endpoint.create_member(id_profile=id_new_profile)
        try:
            response = member_endpoint.put_member(
                id_member=id_member.json()['id'],
                id_profile=id_new_profile,
                firstname=firstname,
                lastname=lastname,
                middlename=middlename,
                position=position,
                subject=subject
            )
            self.validator.assert_status_code(response, 204)
        finally:
            profile_endpoint.delete_profile(id_new_profile)
