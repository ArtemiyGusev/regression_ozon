import allure_commons
import pytest
from selene.support.shared import browser
from selene import support
from appium import webdriver

import config
from mobile_utils.assist import attach


@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import mobile_utils.assist.selene.patch_selector_strategy  # noqa
    import mobile_utils.assist.selene.patch_element_mobile_commands  # noqa


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )
    browser.config.timeout = config.settings.timeout

    yield

    session_id = browser.config.driver.session_id

    # attach.screenshot_as("Last screenshot");
    # attach.page_source();

    browser.quit()
    '''
    # was:
    step("Close driver", Selenide::closeWebDriver);
    '''

    attach.add_video(session_id, 'Video test')
