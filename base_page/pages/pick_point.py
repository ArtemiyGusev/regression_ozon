import time
from selene import be, have
from selene.core.wait import Command
from selene.support import webdriver
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selene import query
import re

from base_page.helper.acceptance_test_modul import click_with_offset


def select_pick_point():
    while True:
        time.sleep(1)
        if s('//ymaps[@class="ymaps-2-1-79-svg-icon-content"]/ymaps').matching(be.visible):
            s('[class*="ZoomButtons_plus"]').click()
        else:
            break
    x_y = s('#yandex-map-id > ymaps > ymaps > ymaps > ymaps.ymaps-2-1-79-places-pane > ymaps:last-child').get(
        query.attribute('style'))
    print(x_y)
    regex = r"^.*left\:\s(.\d+).*top\:\s(.\d+).*$"

    matches = re.search(regex, x_y)
    x = int(matches.groups()[0]) + -960
    y = int(matches.groups()[1]) + -403
    s('#yandex-map-id').perform(click_with_offset(x, y))
    s('[class="primary-button js-select-point"]').should(be.visible)