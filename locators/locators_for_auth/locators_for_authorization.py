from selenium.webdriver.common.by import By


class AuthorizationLocators:

    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[id="email"]')

    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[id="pass"]')

    ENTER_BUTTON_ENABLED = (By.CSS_SELECTOR, 'button[class="ui button blue"]')

    ENTER_BUTTON_DISABLED = (By.CSS_SELECTOR, 'button[class="ui disabled button blue"]')

    ALERT_MESSAGE = (By.CSS_SELECTOR, 'div[role="alert"]')