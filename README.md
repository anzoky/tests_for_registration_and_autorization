## Описание
Авто-тесты для веб-формы регистрации и авторизации 

## Технологии
- **Selenium WebDriver** – взаимодействие с браузером
- **Pytest** – тестовый фреймворк
- **Allure** – генерация отчётов
- **pytest-xdist** – параллельный запуск тестов


- ## Как запустить проект?
1. **Установите зависимости:**  
   ```bash
   pip install -r requirements.txt

2. **Запустите тесты:**
    ```bash
    pytest --alluredir=allure-results

3. **Сгенерируйте и откройте Allure-отчёт:**
    ```bash
   allure serve allure-results

**Аллюр отчет**
![Allure Report]()
