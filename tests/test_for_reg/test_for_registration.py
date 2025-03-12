import pytest
from data.user_data import *
from pages.reg_page.registration_page import RegistrationPage
from locators.locators_for_reg.locators_for_registration import RegistrationLocators
from conftest import driver


class TestRegistration:
    class TestSuccessfulRegistration:

        def test_positive_registration(self, driver):

            registration_page = RegistrationPage(driver, 'http://95.182.122.183/sign_up')
            registration_page.open()
            alert_text = registration_page.positive_registration()
            assert alert_text == 'Вы успешно зарегистрировались', f'Ошибка при регистрации пользователя: {alert_text}'

        def test_positive_registration_without_name(self, driver):

            registration_page = RegistrationPage(driver, 'http://95.182.122.183/sign_up')
            registration_page.open()
            alert_text = registration_page.positive_registration_without_name()
            assert alert_text == 'Вы успешно зарегистрировались', f'Ошибка при регистрации пользователя: {alert_text}'

    class TestUnsuccessfulRegistration:
        @pytest.mark.parametrize('case_name, error_locator', [
            ('email_without_at', RegistrationLocators.EMAIL_ERROR),
            ('email_without_domain', RegistrationLocators.EMAIL_ERROR),
            ('email_too_long', RegistrationLocators.EMAIL_ERROR),
            ('email_with_two_point', RegistrationLocators.EMAIL_ERROR),
            ('email_with_space', RegistrationLocators.EMAIL_ERROR),
            ('email_with_comma', RegistrationLocators.EMAIL_ERROR),
            ('email_with_ip', RegistrationLocators.EMAIL_ERROR),
        ])
        def test_registration_with_incorrect_email(self, driver, case_name, error_locator):
            registration_page = RegistrationPage(driver, 'http://95.182.122.183/sign_up')
            registration_page.open()
            error_message, expected_result = registration_page.negative_registration_with_incorrect_data(case_name, locator=error_locator)
            assert error_message == expected_result, \
                f'Ошибка "{error_message}" не соответствует ожидаемой "{expected_result}"'

        @pytest.mark.parametrize('case_name, error_locator', [
            ('password_too_short', RegistrationLocators.PASSWORD_ERROR),
            ('confirm_password_too_short', RegistrationLocators.CONFIRM_PASSWORD_ERROR),
            ('password_too_long', RegistrationLocators.PASSWORD_ERROR),
            ('confirm_password_too_long', RegistrationLocators.CONFIRM_PASSWORD_ERROR),
            ('password_mismatch', RegistrationLocators.CONFIRM_PASSWORD_ERROR),
            ('password_empty', RegistrationLocators.PASSWORD_ERROR),
            ('confirm_password_empty', RegistrationLocators.CONFIRM_PASSWORD_ERROR)
        ])
        def test_registration_with_incorrect_email(self, driver, case_name, error_locator):
            registration_page = RegistrationPage(driver, 'http://95.182.122.183/sign_up')
            registration_page.open()
            error_message, expected_result = registration_page.negative_registration_with_incorrect_data(case_name, locator=error_locator)
            assert error_message == expected_result, \
                f'Ошибка "{error_message}" не соответствует ожидаемой "{expected_result}"'

        @pytest.mark.parametrize('case_name, error_locator', [
            ('name_too_long', RegistrationLocators.NAME_ERROR)
        ])
        def test_registration_with_incorrect_email(self, driver, case_name, error_locator):
            registration_page = RegistrationPage(driver, 'http://95.182.122.183/sign_up')
            registration_page.open()
            error_message, expected_result = registration_page.negative_registration_with_incorrect_data(case_name, locator=error_locator)
            assert error_message == expected_result, \
                f'Ошибка "{error_message}" не соответствует ожидаемой "{expected_result}"'