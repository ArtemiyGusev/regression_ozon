import os

from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def add_file(element, file_name):
    s(element).type(os.path.abspath(file_name))


def url_open_size(url, width=1920, height=1080):
    browser.config.browser_name = 'chrome'
    browser.open(url)
    browser.config.driver.set_window_size(width, height)


def remove_element(element):
    try:
        browser.execute_script(
            f"var el = document.querySelectorAll('{element}'); if (el.length > 0) {{ el[0].remove(); }}")
    except:
        pass
