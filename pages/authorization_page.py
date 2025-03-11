import time

from locators.locators_for_authorization import AuthorizationLocators
from pages.base_page import BasePage
from data.user_data import DATA_FOR_SUCCESSFUL_AUTHORIZATION


class AuthorizationPage(BasePage):
     locators = AuthorizationLocators()

     def fill_all_fields_for_authorization(self):

          email = DATA_FOR_SUCCESSFUL_AUTHORIZATION['email']
          password = DATA_FOR_SUCCESSFUL_AUTHORIZATION['password']

          self.element_is_visible(self.locators.EMAIL_FIELD).send_keys(email)
          self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys(password)
          self.element_is_visible(self.locators.ENTER_BUTTON).click()

          alert_message = self.element_is_visible(self.locators.ALERT_MESSAGE).text

          return alert_message
