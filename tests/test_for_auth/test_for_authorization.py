import pytest

from pages.auth_page.authorization_page import AuthorizationPage
from conftest import driver


class TestAuthorization:
    class TestSuccessfulAuthorization:

        def test_successful_authorization(self, driver):
            authorization_page = AuthorizationPage(driver, 'http://95.182.122.183/login')
            authorization_page.open()
            alert_message = authorization_page.fill_all_fields_for_authorization()
            assert alert_message == 'Вы успешно залогинились', f'Ошибка при логине: {alert_message}'

    class TestUnsuccessfulAuthorization:

        @pytest.mark.parametrize('case_name', [
            'password_too_long',
            'email_without_at'
        ])
        def test_unsuccessful_authorization(self, driver, case_name):
            authorization_page = AuthorizationPage(driver, 'http://95.182.122.183/login')
            authorization_page.open()
            alert_message, expected_message = authorization_page.negative_authorization(case_name)
            assert alert_message == expected_message, \
                f'Ошибка "{alert_message}" не соответствует ожидаемой "{expected_message[case_name]['expected']}"'

        def test_check_auth_button_is_disabled_with_empty_fields(self, driver):
            authorization_page = AuthorizationPage(driver, 'http://95.182.122.183/login')
            authorization_page.open()
            auth_button = authorization_page.check_auth_button_is_disabled_with_empty_fields()
            assert auth_button is False, \
                'При незаполненных полях кнопка авторизации кликабельна'