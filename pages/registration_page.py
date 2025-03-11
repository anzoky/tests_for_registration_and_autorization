import time

from locators.locators_for_registration import RegistrationLocators
from pages.base_page import BasePage
from data.user_data import DATA_FOR_SUCCESSFUL_REGISTRATION


class RegistrationPage(BasePage):

    locators = RegistrationLocators()

    def fill_all_fields_for_registration(self):
        email = DATA_FOR_SUCCESSFUL_REGISTRATION['email']
        password = DATA_FOR_SUCCESSFUL_REGISTRATION['password']
        name = DATA_FOR_SUCCESSFUL_REGISTRATION['name']
        self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
        self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys(password)
        self.element_is_visible(self.locators.CONFIRM_PASSWORD_FIELD).send_keys(password)
        self.element_is_visible(self.locators.NAME_FIELD).send_keys(name)
        self.element_is_visible(self.locators.BUTTON_REGISTRATION).click()
        alert_message = self.element_is_visible(self.locators.ALERT_MESSAGE).text
        return alert_message
