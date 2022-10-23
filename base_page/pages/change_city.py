from selene.support.shared.jquery_style import s


def change_city():
    s('.city-select-city').click()
    s('//*[contains(@class,"city-selector-item__btn")]/*[text()="Санкт-Петербург"]').click()