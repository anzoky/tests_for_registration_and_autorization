import allure
import pytest
from data.user_data import *
from pages.reg_page.registration_page import RegistrationPage
from locators.locators_for_reg.locators_for_registration import RegistrationLocators
from conftest import driver


@allure.suite('Форма регистрации')
class TestRegistration:
    @allure.feature('Позитивные тесты формы регистрации')
    class TestSuccessfulRegistration:

        @allure.title('Успешная регистрация с заполненными полями')
        def test_positive_registration(self, driver):

            registration_page = RegistrationPage(driver, 'http://95.182.122.183:3000/sign_up')
            registration_page.open()
            alert_text = registration_page.positive_registration()
            assert alert_text == 'Вы успешно зарегистрировались', f'Ошибка при регистрации пользователя: {alert_text}'

    @allure.feature('Негативные тесты формы регистрации')
    class TestUnsuccessfulRegistration:

        @allure.title('Негативные тесты для поля email')
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
            registration_page = RegistrationPage(driver, 'http://95.182.122.183:3000/sign_up')
            registration_page.open()
            error_message, expected_result = registration_page.negative_registration_with_incorrect_data(case_name, locator=error_locator)
            assert error_message == expected_result, \
                f'Ошибка "{error_message}" не соответствует ожидаемой "{expected_result}"'

        @allure.title('Негативные тесты для поля пароль')
        @pytest.mark.parametrize('case_name, error_locator', [
            ('password_too_short', RegistrationLocators.PASSWORD_ERROR),
            ('confirm_password_too_short', RegistrationLocators.CONFIRM_PASSWORD_ERROR),
            ('password_too_long', RegistrationLocators.PASSWORD_ERROR),
            ('confirm_password_too_long', RegistrationLocators.CONFIRM_PASSWORD_ERROR),
            ('password_mismatch', RegistrationLocators.CONFIRM_PASSWORD_ERROR),
            ('password_empty', RegistrationLocators.PASSWORD_ERROR),
            ('confirm_password_empty', RegistrationLocators.CONFIRM_PASSWORD_ERROR)
        ])
        def test_registration_with_incorrect_password(self, driver, case_name, error_locator):
            registration_page = RegistrationPage(driver, 'http://95.182.122.183:3000/sign_up')
            registration_page.open()
            error_message, expected_result = registration_page.negative_registration_with_incorrect_data(case_name, locator=error_locator)
            assert error_message == expected_result, \
                f'Ошибка "{error_message}" не соответствует ожидаемой "{expected_result}"'

        @allure.title('Негативные тесты для поля имя')
        @pytest.mark.parametrize('case_name, error_locator', [
            ('name_too_long', RegistrationLocators.NAME_ERROR),
            ('name_empty', RegistrationLocators.NAME_ERROR)
        ])
        def test_registration_with_incorrect_name(self, driver, case_name, error_locator):
            registration_page = RegistrationPage(driver, 'http://95.182.122.183:3000/sign_up')
            registration_page.open()
            error_message, expected_result = registration_page.negative_registration_with_incorrect_data(case_name, locator=error_locator)
            assert error_message == expected_result, \
                f'Ошибка "{error_message}" не соответствует ожидаемой "{expected_result}"'

        @allure.title('Негативные тесты с пустыми значениями')
        @pytest.mark.parametrize('case_name', [
            'all_fields_empty',
            'email_empty',
            'passwords_is_empty',
            'confirm_password_is_empty'
        ])
        def test_registration_boundary_test_cases(self, driver, case_name):
            registration_page = RegistrationPage(driver, 'http://95.182.122.183:3000/sign_up')
            registration_page.open()
            list_of_errors = registration_page.negative_registration_boundary_test_cases(case_name)
            assert list_of_errors == registration_test_data[case_name]['expected'], \
                f'Ошибка "{list_of_errors}" не соответствует ожидаемой "{registration_test_data[case_name]['expected']}"'
