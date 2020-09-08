import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome', help='Choose browser: firefox or chrome')
    parser.addoption("--language", action='store', default ='en', help='Choose language')

@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    return language



@pytest.fixture(scope="function")
def browser(request,language):
    browser_name = request.config.getoption("browser_name")
    browser = None
    print("\nstart browser for test..")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages':language})
        browser = webdriver.Chrome(options = options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages",language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name must be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
