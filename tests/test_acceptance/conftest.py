import os

import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from selene import Browser, Config
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def driver_init(request):
#def driver_init():
    browser_version = request.config.getoption('--browser_version')
    options = Options()
    prefs = {"profile.default_content_setting_values.geolocation": 2}
    options.add_experimental_option("prefs", prefs)
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    browser.config.hold_browser_open = (
            os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
    )
    browser.config.timeout = float(os.getenv('selene.timeout', '10'))
    browser.config.base_url = 'https://www.myglo.ru'

    browser_config = Browser(Config(driver))
    #browser.config.browser_name = 'chrome'
    #browser.config.base_url = 'https://myglo.ru'
    #browser_config = browser.config

    yield browser_config

    attach.add_attachment(browser_config)
    attach.add_logs(browser_config)
    attach.add_html(browser_config)
    attach.add_video(browser_config)

    browser.quit()
