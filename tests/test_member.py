import pytest
from constants import member_cases


class TestMember:

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
        profile_endpoint.delete_profile(id_new_profile)