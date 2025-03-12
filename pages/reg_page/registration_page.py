import time

from locators.locators_for_reg.locators_for_registration import RegistrationLocators
from pages.base_page import BasePage
from data.user_data import DATA_FOR_SUCCESSFUL_REG_AND_AUTH, registration_test_data


class RegistrationPage(BasePage):

    locators = RegistrationLocators()

    def fill_registration_form(self, email=None, password=None, confirm_password=None, name=None):
        if email:
            self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
        if password:
            self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys(password)
        if confirm_password:
            self.element_is_visible(self.locators.CONFIRM_PASSWORD_FIELD).send_keys(confirm_password)
        if name:
            self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)

    def positive_registration(self):
        self.fill_registration_form(
            email=DATA_FOR_SUCCESSFUL_REG_AND_AUTH['email'],
            password=DATA_FOR_SUCCESSFUL_REG_AND_AUTH['password'],
            confirm_password=DATA_FOR_SUCCESSFUL_REG_AND_AUTH['password'],
            name=DATA_FOR_SUCCESSFUL_REG_AND_AUTH['name']
        )
        self.element_is_visible(self.locators.BUTTON_REGISTRATION).click()
        alert_message = self.element_is_visible(self.locators.ALERT_MESSAGE).text
        return alert_message

    def positive_registration_without_name(self):
        self.fill_registration_form(
            email=DATA_FOR_SUCCESSFUL_REG_AND_AUTH['email'],
            password=DATA_FOR_SUCCESSFUL_REG_AND_AUTH['password'],
            confirm_password=DATA_FOR_SUCCESSFUL_REG_AND_AUTH['password']
        )
        self.element_is_visible(self.locators.BUTTON_REGISTRATION).click()
        alert_message = self.element_is_visible(self.locators.ALERT_MESSAGE).text
        return alert_message

    def negative_registration_with_incorrect_data(self, case_name, locator=None):
        self.fill_registration_form(
            email=registration_test_data[case_name]['email'],
            password=registration_test_data[case_name]['password'],
            confirm_password=registration_test_data[case_name]['confirm_password'],
            name=registration_test_data[case_name]['name']
        )
        self.element_is_visible(self.locators.BUTTON_REGISTRATION).click()
        error_text = self.element_is_visible(locator).text
        expected_result = registration_test_data[case_name]['expected']
        return error_text, expected_result

    def negative_registration_boundary_test_cases(self, case_name):
        self.fill_registration_form(
            email=registration_test_data[case_name]['email'],
            password=registration_test_data[case_name]['password'],
            confirm_password=registration_test_data[case_name]['confirm_password'],
            name=registration_test_data[case_name]['name']
        )
        self.element_is_visible(self.locators.BUTTON_REGISTRATION).click()
        list_of_error_messages = self.elements_are_visible(self.locators.LIST_OF_ERROR_MESSAGES)
        return [value.text for value in list_of_error_messages]

