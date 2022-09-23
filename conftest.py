import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None)


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': "es"})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()