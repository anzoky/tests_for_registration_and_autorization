from pages.registration_page import RegistrationPage
from conftest import driver


class TestRegistration:
    class TestSuccessfulRegistration:

        def test_successful_registration(self, driver):

            registration_page = RegistrationPage(driver, 'http://95.182.122.183/sign_up')
            registration_page.open()
            alert_text = registration_page.fill_all_fields_for_registration()
            assert alert_text == 'Вы успешно зарегистрировались', f'Ошибка при регистрации пользователя: {alert_text}'