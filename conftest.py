import allure
import pytest
import requests
from config import config
from endpoints.auth_endpoint import AuthEndpoint
from endpoints.member_endpoint import MemberEndpoint
from endpoints.profiles_endpoint import ProfileEndpoint
from utils.logger import setup_logger
import logging


# Поднимаем логгер для всего проекта
setup_logger()
logger = logging.getLogger(__name__)

@pytest.fixture()
def auth_endpoint():
    return AuthEndpoint()

@pytest.fixture()
def profile_endpoint(get_auth_token):
    return ProfileEndpoint(token=get_auth_token)

@pytest.fixture()
def member_endpoint(get_auth_token):
    return MemberEndpoint(token=get_auth_token)

@pytest.fixture(scope='session')
def get_auth_token():
    url = f'{config.URL}/common/auth'
    payload = {'login': f'{config.LOGIN}', 'password': f'{config.PASSWORD}'}
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        logger.critical(f'Не удалось получить токен авторизации! Статус: {response.status_code}')
        raise SystemExit('Тесты не могут выполняться без токена')

    response.raise_for_status() # Проверка, что ответ успешен
    assert isinstance(response.text, str) # Проверка, что ответ - строка
    assert len(response.text) > 0 # Проверка, что длина ответа > 0
    assert response.status_code == 200 # Проверка, что код ответа 200
    token = response.text
    logger.info('Токен авторизации получен успешно')
    allure.attach(token, name="Auth Token", attachment_type=allure.attachment_type.TEXT)
    return token

@pytest.fixture(autouse=True)
def log_test_start_end(request):
    """Фикстуру не нужно передавать в тесты, она работает автоматом"""
    test_name = request.node.name

    logger.info(f"===== STARTED TEST: {test_name} =====")

    yield

    # определяем результат
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        logger.error(f"===== FINISHED TEST: {test_name} — FAILED =====")
    else:
        logger.info(f"===== FINISHED TEST: {test_name} — PASSED =====")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        setattr(item, "rep_call", rep)