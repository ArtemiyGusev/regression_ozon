import os
from selene import be
from selene.core.wait import Command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium.webdriver import ActionChains


def add_file(element, file_name):
    s(element).type(os.path.abspath(file_name))


def url_open_size(url, width=1920, height=1080):
    browser.config.browser_name = 'chrome'
    browser.open(url).wait_until(5)
    browser.config.driver.add_cookie({'name': 'bat_ageverified_2', 'value': 'true', 'path': '/'})
    browser.driver.refresh()
    browser.config.driver.set_window_size(width, height)


def remove_element(element):
    try:
        browser.execute_script(
            f"var el = document.querySelectorAll('{element}'); if (el.length > 0) {{ el[0].remove(); }}")
    except:
        pass


def passing_modal():
    if s("#age-verification").matching(be.visible):
        s("#age-verification").type('11111990')
        s("[class='age-verification-form__btn g-btn']").click()


def scroll_click(element):
    browser.execute_script(
        f"document.querySelector('{element}').scrollIntoView({{block: 'center', inline: 'nearest'}})")
    s(element).click()


def click_with_offset(x: int, y: int) -> Command:
    action = ActionChains(browser.driver)

    return Command(
        f'click with offset x {x}, y {y}',
        lambda element: action.move_to_element_with_offset(element(), x, y).click().perform()

    )


def go_to_page(url):
    browser.open(url).wait_until(5)
