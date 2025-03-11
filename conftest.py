import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException


@pytest.fixture(scope='function')
def driver():
    driver = None
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        yield driver
    except WebDriverException as e:
        pytest.fail(f'Failed to initialize Webdriver: {e}')
    finally:
        if driver:
            driver.quit()
