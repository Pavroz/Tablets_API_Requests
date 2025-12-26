import pytest
from constants import member_cases


class TestMember:

    @pytest.mark.parametrize(
        "middlename, subject, position", member_cases.MEMBER_CASES)
    def test_create_member(
            self, profile_endpoint, member_endpoint,
            middlename, subject, position
    ):
        response = profile_endpoint.create_new_profile()
        member_endpoint.create_member(
            profileid=response,
            middlename=middlename,
            subject=subject,
            position=position)
        profile_endpoint.delete_profile(response)