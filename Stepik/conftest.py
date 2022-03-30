#conftest.py
import pytest
from selenium import webdriver

def pytest_addoption(parser):
	#создаем параметр browser_name
    parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    #получаем значение параметра browser_name из командной строки
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser...")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser...")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser...")
    browser.quit()

#Пустая строка!