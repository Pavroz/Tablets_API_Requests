import pytest
from endpoints.auth_endpoint import AuthEndpoint


from endpoints.member_endpoint import MemberEndpoint
from endpoints.profiles_endpoint import ProfileEndpoint

@pytest.fixture()
def auth_endpoint():
    return AuthEndpoint()

@pytest.fixture()
def profile_endpoint():
    return ProfileEndpoint()

@pytest.fixture()
def member_endpoint():
    return MemberEndpoint()


