import pytest
from selenium import webdriver

@pytest.fixture()
def oneTimeSetup(request,browser):
    print("Running one time setup")
    if browser=="firefox":
        value=webdriver.Firefox(executable_path="./drivers/geckodriver.exe")
    else:
        value = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
    if request.cls is not None:
        request.cls.value=value

    yield value
    print("Running one time tearDown")
    print("Closing browser......")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

