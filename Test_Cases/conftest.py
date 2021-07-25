from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'Chrome':
        driver = webdriver.Chrome()
        print("launching Chrome Browser")
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
        print("launching Chrome Firefox")
    return driver


def pytest_addoption(parser):  # This value get from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()  # This will return the browser value to setup method
def browser(request):
    return request.config.getoption("--browser")


############ To genarate HTML reports ###########

def pytest_configure(config):  # it is a hook for adding environment for HTML report
    config._metadata['Project Name'] = "Odoo_CRM_Automation"
    config._metadata['Module Name'] = "CRM main Page"
    config._metadata['Team Lead'] = "Sathia Jay"
    config._metadata['Tester'] = "Ajith Kumar"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
