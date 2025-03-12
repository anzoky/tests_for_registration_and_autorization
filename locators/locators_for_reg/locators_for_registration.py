from selenium.webdriver.common.by import By


class RegistrationLocators:

    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[id="email"]')
    EMAIL_ERROR = (By.XPATH,
                           '//input[@id="email"]/following-sibling::div[contains(@class, "mt-2 text-sm text-rose-600 italic")]')

    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[id="pass1"]')
    PASSWORD_ERROR = (By.XPATH,
                           '//input[@id="pass1"]/following-sibling::div[contains(@class, "mt-2 text-sm text-rose-600 italic")]')

    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[id="pass2"]')
    CONFIRM_PASSWORD_ERROR = (By.XPATH,
                                    '//input[@id="pass2"]/following-sibling::div[contains(@class, "mt-2 text-sm text-rose-600 italic")]')

    NAME_FIELD = (By.CSS_SELECTOR, 'input[id="name"]')
    NAME_ERROR = (By.XPATH,
                  '//input[@id="name"]/following-sibling::div[contains(@class, "mt-2 text-sm text-rose-600 italic")]')

    BUTTON_REGISTRATION = (By.CSS_SELECTOR, 'button[class="ui button blue"]')

    LIST_OF_ERROR_MESSAGES = (By.CSS_SELECTOR, 'div[class="mt-2 text-sm text-rose-600 italic"]')

    ALERT_MESSAGE = (By.CSS_SELECTOR, 'div[role="alert"]')