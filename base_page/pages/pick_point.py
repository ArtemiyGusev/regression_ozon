import time
from selene import be
from selene.support.shared.jquery_style import s, ss
from selene import query
import re
from selene.support.shared import browser

from base_page.helper.acceptance_test_modul import click_with_offset


def select_pick_point():
    # i = 0
    # while i <= 5:
    #     i += 1
    #     time.sleep(1)
    #     if s('//ymaps[@class="ymaps-2-1-79-svg-icon-content"]/ymaps').matching(be.visible):
    #         s('[class*="ZoomButtons_plus"]').click()
    #     else:
    #         break

    #x_y = ss('#yandex-map-id > ymaps > ymaps > ymaps > ymaps.ymaps-2-1-79-places-pane > ymaps')
    x_y = browser.executeScript("document.querySelectorAll('#yandex-map-id > ymaps > ymaps > ymaps > ymaps.ymaps-2-1-79-places-pane > ymaps').length")
    while x_y == 1:
        x_y -= 1
        x_y = s('#yandex-map-id > ymaps > ymaps > ymaps > ymaps.ymaps-2-1-79-places-pane > ymaps:nth-child(' + x_y + ')')

        x_y = x_y.get(query.attribute('style'))
        regex = r"^.*left\:\s(.\d+).*top\:\s(.\d+).*$"

        matches = re.search(regex, x_y)
        x = int(matches.groups()[0]) + -960
        y = int(matches.groups()[1]) + -403

    # while i <= 10:
    #     i += 1
    #    if s('[class="primary-button js-select-point"]').matching(be.not_.visible):
        s('#yandex-map-id').perform(click_with_offset(x, y))
        if s('[class="primary-button js-select-point"]').should(be.visible):
            break
        # else:
        #     break
    #s('[class="primary-button js-select-point"]').click()
    #s('#__next__checkout > div > div > div.Checkout_cols__xDKnD > div.Checkout_stepWrapper__9rLsG > div.ShippingInfo_root__WvOS5 > form > div:nth-child(4) > div.BlockTitle_root__yWK3w').should(be.visible)
    #time.sleep(10)