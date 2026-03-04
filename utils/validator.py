import allure

class Validator:

    @allure.step('Проверить, что тело ответа не пустое')
    def assert_response_not_empty(self, response):
        assert len(response.text) > 0

    @allure.step('Проверка кода ответа')
    def assert_status_code(self, response, expected_status):
        assert response.status_code == expected_status

    @allure.step('Проверка сообщения об ошибке')
    def assert_violation_message(self, response, expected_message):
        violations = response.json()['violations']
        for v in violations:
            assert v['message'] == expected_message

    @allure.step('Проверка тела ответа')
    def assert_isinstance(self, response, type):
        assert isinstance(response, type)

    @allure.step('Проверка длины ответа')
    def assert_len(self, response):
        assert len(response) > 0

    @allure.step('Проверка равенства')
    def assert_equality(self, one_argument, two_argument):
        assert one_argument == two_argument

    @allure.step('Проверка, что один аргумент входит в другой')
    def assert_in(self, one_argument, two_argument):
        assert one_argument in two_argument

    @allure.step('Проверка является ли один аргумент вторым')
    def assert_is(self, one_argument, two_argument):
        assert one_argument is two_argument