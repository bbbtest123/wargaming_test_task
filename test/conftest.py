import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")


def pytest_generate_tests(metafunc):
    browser = metafunc.config.option.browser
    if "browser" in metafunc.fixturenames and browser is not None:
        metafunc.parametrize("browser", [browser])


@pytest.fixture(scope="function")
def before_and_after(browser):
    if browser == "chrome":
        pytest.driver = webdriver.Chrome()
    if browser == "firefox":
        pytest.driver = webdriver.Firefox()
    pytest.driver.implicitly_wait(10)
    pytest.driver.get("https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites")

    yield pytest.driver

    pytest.driver.close()
