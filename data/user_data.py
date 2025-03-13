from faker import Faker


fake = Faker()
valid_password = fake.password(
    length=12,
    special_chars=True,
    digits=True,
    upper_case=True,
    lower_case=True
)
valid_email = fake.email()
valid_name = fake.first_name() + " " + fake.last_name()


DATA_FOR_SUCCESSFUL_REG_AND_AUTH = {
    'email': valid_email,
    'password': valid_password,
    'name': fake.first_name()
}


# Словарь тестовых данных
registration_test_data = {

    # Невалидные email
    'email_without_at': {
        'email': 'invalidemail.com',
        'password': valid_password,
        'confirm_password': valid_password,
        'name': valid_name,
        'expected': 'Укажите корректный mail'
    },
    'email_without_domain': {
        'email': 'missing@domain',
        'password': valid_password,
        'confirm_password': valid_password,
        'name': valid_name,
        'expected': 'Укажите корректный mail'
    },
    'email_too_long': {
        'email': 'a' * 320 + '@test.com',
        'password': valid_password,
        'confirm_password': valid_password,
        'name': valid_name,
        'expected': 'Не более 50 символов'
    },
    'email_with_two_point': {
      'email': 'user@domain..com',
      'password': valid_password,
      'confirm_password': valid_password,
      'name': valid_name,
      'expected': 'Укажите корректный mail'
    },
    'email_with_space': {
        'email': 'user@domain .com',
        'password': valid_password,
        'confirm_password': valid_password,
        'name': valid_name,
        'expected': 'Укажите корректный mail'
    },
    'email_with_comma': {
        'email': 'user@domain,com',
        'password': valid_password,
        'confirm_password': valid_password,
        'name': valid_name,
        'expected': 'Укажите корректный mail'
    },
    'email_with_ip': {
        'email': 'user@127.0.0.1',
        'password': valid_password,
        'confirm_password': valid_password,
        'name': valid_name,
        'expected': 'Укажите корректный mail'
    },

    # Проблемы с паролем
    'password_too_short': {
        'email': valid_email,
        'password': 'Short1',
        'confirm_password': valid_password,
        'name': valid_name,
        'expected': 'Не менее 8 символов'
    },
    'confirm_password_too_short': {
        'email': valid_email,
        'password': valid_password,
        'confirm_password': 'Short1',
        'name': valid_name,
        'expected': 'Не менее 8 символов'
    },
    'password_too_long': {
        'email': valid_email,
        'password': 'Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!',
        'confirm_password': valid_password,
        'name': valid_name,
        'expected': 'Не более 50 символов'
    },
    'confirm_password_too_long': {
        'email': valid_email,
        'password': valid_password,
        'confirm_password':  'Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!Aa1!',
        'name': valid_name,
        'expected': 'Не более 50 символов'
    },
    'password_no_digits': {
        'email': valid_email,
        'password': 'Password!',
        'confirm_password': 'Password!',
        'name': valid_name,
        'expected': 'Пароль должен содержать цифры'
    },
    'password_mismatch': {
        'email': valid_email,
        'password': valid_password,
        'confirm_password': 'DifferentPass123!1234',
        'name': valid_name,
        'expected': 'Пароли не совпадают'
    },
    'password_empty': {
        'email': valid_email,
        'password': '',
        'confirm_password': valid_password,
        'name': valid_name,
        'expected': 'Это поле обязательно'
    },
    'confirm_password_empty': {
        'email': valid_email,
        'password': valid_password,
        'confirm_password': '',
        'name': valid_name,
        'expected': 'Это поле обязательно'
    },

    # Проблемы с именем
    'name_with_numbers': {
        'email': valid_email,
        'password': valid_password,
        'confirm_password': valid_password,
        'name': 'John123 Doe',
        'expected': 'Имя может содержать только буквы'
    },
    'name_too_long': {
        'email': valid_email,
        'password': valid_password,
        'confirm_password': valid_password,
        'name': 'A' * 101,
        'expected': 'Не более 50 символов'
    },
    'name_empty': {
        'email': valid_email,
        'password': valid_password,
        'confirm_password': valid_password,
        'name': '',
        'expected': 'Имя обязательно для заполнения'
    },

    # Граничные кейсы
    'all_fields_empty': {
        'email': '',
        'password': '',
        'confirm_password': '',
        'name': '',
        'expected': ['Это поле обязательно', 'Это поле обязательно', 'Это поле обязательно']
    },
    'email_empty': {
        'email': '',
        'password': valid_password,
        'confirm_password': valid_password,
        'name': 'User',
        'expected': ['Это поле обязательно']
    },
    'passwords_is_empty': {
        'email': 'user@example.com',
        'password': '',
        'confirm_password': '',
        'name': 'User',
        'expected': ['Это поле обязательно', 'Это поле обязательно']
    },
    'confirm_password_is_empty': {
        'email': 'user@example.com',
        'password': valid_password,
        'confirm_password': '',
        'name': 'User',
        'expected': ['Это поле обязательно', 'Пароли не совпадают']
    }
}

authorization_test_data = {
    'password_too_long': {
        'email': valid_email,
        'password': 'asd' * 20,
        'expected': 'Неверный логин или пароль'
    },
    'email_without_at': {
        'email': 'invalidemail.com',
        'password': valid_password,
        'expected': 'Неверный логин или пароль'
    },
    'invalid_email_format': {
        'email': 'user@.com',
        'password': valid_password,
        'expected': 'Неверный логин или пароль'
    },
    'password_too_short': {
        'email': valid_email,
        'password': 'a',
        'expected': 'Неверный логин или пароль'
    },
    'sql_injection_email': {
        'email': "admin' OR '1'='1'--",
        'password': valid_password,
        'expected': 'Неверный логин или пароль'
    },
    'sql_injection_password': {
        'email': valid_email,
        'password': "' OR '1'='1'--",
        'expected': 'Неверный логин или пароль'
    },
    'unicode_email': {
        'email': 'юзер@example.com',
        'password': valid_password,
        'expected': 'Неверный логин или пароль'
    },
    'unicode_password': {
        'email': valid_email,
        'password': 'пароль',
        'expected': 'Неверный логин или пароль'
    }
}

auth_test_data_empty_fields_test_cases = {
    'empty_fields': {
        'email': '',
        'password': ''
    },
    'empty_email': {
        'email': '',
        'password': valid_password
    },
    'empty_password': {
        'email': valid_email,
        'password': ''
    }
}