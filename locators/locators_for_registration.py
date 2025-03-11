from selenium.webdriver.common.by import By


class RegistrationLocators:

    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[id="email"]')
    MESSAGE_UNDER_EMAIL = (By.XPATH,
                           '//input[@id="email"]/following-sibling::div[contains(@class, "mt-2 text-sm text-rose-600 italic")]')

    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[id="pass1"]')
    MESSAGE_UNDER_PASSWORD_FIELD = (By.XPATH,
                           '//input[@id="pass1"]/following-sibling::div[contains(@class, "mt-2 text-sm text-rose-600 italic")]')

    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[id="pass2"]')
    MESSAGE_UNDER_CONFIRM_PASSWORD_FIELD = (By.XPATH,
                                    '//input[@id="pass2"]/following-sibling::div[contains(@class, "mt-2 text-sm text-rose-600 italic")]')

    NAME_FIELD = (By.CSS_SELECTOR, 'input[id="name"]')

    BUTTON_REGISTRATION = (By.CSS_SELECTOR, 'button[class="ui button blue"]')

    ALERT_MESSAGE = (By.CSS_SELECTOR, 'div[role="alert"]')