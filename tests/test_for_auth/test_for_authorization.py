from pages.auth_page.authorization_page import AuthorizationPage
from conftest import driver


class TestAuthorization:
    class TestSuccessfulAuthorization:

        def test_successful_authorization(self, driver):
            authorization_page = AuthorizationPage(driver, 'http://95.182.122.183/login')
            authorization_page.open()
            alert_message = authorization_page.fill_all_fields_for_authorization()
            assert alert_message == 'Вы успешно залогинились', f'Ошибка при логине: {alert_message}'