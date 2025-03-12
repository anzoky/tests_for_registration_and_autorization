import allure

from locators.locators_for_auth.locators_for_authorization import AuthorizationLocators
from pages.base_page import BasePage
from data.user_data import DATA_FOR_SUCCESSFUL_REG_AND_AUTH, authorization_test_data


class AuthorizationPage(BasePage):

    locators = AuthorizationLocators()

    def fill_authorization_form(self, email=None, password=None):
        with allure.step('Заполнение полей формы авторизации'):
            if email:
                self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
            if password:
                self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys(password)

    def fill_all_fields_for_authorization(self):
        with allure.step('Заполнение полей авторизации'):
            self.fill_authorization_form(
                  email=DATA_FOR_SUCCESSFUL_REG_AND_AUTH['email'],
                  password=DATA_FOR_SUCCESSFUL_REG_AND_AUTH['password']
            )
        self.element_is_visible(self.locators.ENTER_BUTTON_ENABLED).click()
        with allure.step('Получение сообщения из алерта'):
            alert_message = self.element_is_visible(self.locators.ALERT_MESSAGE).text
        return alert_message

    def negative_authorization(self, case_name):
        with allure.step('Заполнение полей авторизации'):
            self.fill_authorization_form(
                email=authorization_test_data[case_name]['email'],
                password=authorization_test_data[case_name]['password']
            )
        self.element_is_visible(self.locators.ENTER_BUTTON_ENABLED).click()
        with allure.step('Получение сообщения из алерта'):
            alert_message = self.element_is_visible(self.locators.ALERT_MESSAGE).text
        with allure.step('Ожидаемый результат'):
            expect_message = authorization_test_data[case_name]['expected']
        return alert_message, expect_message

    @allure.step('Проверка кликабельности кнопки авторизации с пустыми полями')
    def check_auth_button_is_disabled_with_empty_fields(self):
        auth_button = self.element_is_present(self.locators.ENTER_BUTTON_DISABLED)
        return auth_button.is_enabled()
