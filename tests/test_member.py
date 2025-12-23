import pytest



class TestMember:

    @pytest.mark.parametrize(
        "middlename, subject, position",
        [
            (None, None, None),
            ("middlename", None, None),
            (None, "subject", None),
            (None, None, "position"),
            ("middlename", "subject", None),
            ("middlename", None, "position"),
            (None, "subject", "position"),
            ("middlename", "subject", "position"),
        ]
    )
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