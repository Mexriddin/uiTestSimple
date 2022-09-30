import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# @pytest.fixture
# def driver():
#     driver_service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=driver_service)
#     driver.maximize_window()
#     yield driver
#     driver.quit()


def pytest_addoption(parser):
    parser.addoption('--url', default='https://demoqa.com', help='Base application url')
    parser.addoption('--browser', default='chrome', help='Browser for run tests')


@pytest.fixture(scope='session')
def browser(request):
    base_url = request.config.getoption("--url")
    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.maximize_window()
    elif browser == 'firefox':
        driver_service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=driver_service)
        driver.maximize_window()

    driver.get(base_url)
    driver.base_url = base_url
    yield driver
    driver.quit()
