from selene.support.shared.jquery_style import s
from selene import be


def change_city():
    s('.city-select-city').click()
    s('//*[contains(@class,"city-selector-item__btn")]/*[text()="Санкт-Петербург"]').click()
    s('//*[@class="city-select-city"][text()="Санкт-Петербург"]').should(be.visible)