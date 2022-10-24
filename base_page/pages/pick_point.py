from selene import be
from selene.support.shared.jquery_style import s, ss
from selene import query
import re
from selene.support.shared import browser

from base_page.helper.acceptance_test_modul import click_with_offset


def select_pick_point():
    s('[class*="Pickup_selectBtn"]').click()
    browser.execute_script('return document.readyState == "complete"')
    s('[class*="ZoomButtons_plus"]').click()
    i = 0
    while i <= 20:
        i += 1
        x_y = s('#yandex-map-id > ymaps > ymaps > ymaps > ymaps.ymaps-2-1-79-places-pane > ymaps:nth-child(' + str(i) + ')')
        int(i)
        x_y = x_y.get(query.attribute('style'))
        regex = r"^.*left\:\s(.\d+).*top\:\s(.\d+).*$"

        matches = re.search(regex, x_y)
        x = int(matches.groups()[0]) + -960
        y = int(matches.groups()[1]) + -403

        s('#yandex-map-id').perform(click_with_offset(x, y))

        if s('[class="primary-button js-select-point"]').matching(be.visible):
            s('[class="primary-button js-select-point"]').click()
            break
