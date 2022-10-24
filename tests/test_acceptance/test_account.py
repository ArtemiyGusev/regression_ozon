from base_page.helper.acceptance_test_modul import url_open_size, passing_modal, scroll_click
from env import *
import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s, ss
from base_page.pages.pick_point import select_pick_point
from base_page.pages.change_city import change_city
from selene import be


def test_case_practice_form():
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты automation-practice-form")
    allure.dynamic.story("Проверка отправленных данных в таблице через форму")

    with allure.step('Открываем /automation-practice-form'):
        url_open_size('/internet-magazin/devices')
        passing_modal()
        change_city()

    with allure.step('Добавляем девайс в корзину'):
        scroll_click(add_device)

    with allure.step('Переходим на чекаут'):
        s(go_to_checkout).click()

    with allure.step('Добавляем еще один девайс в корзину'):
        s('[alt="plus"]').click()

    with allure.step('Нажимаем на выбрать пункт выдачи'):
        s(delivery_pick_point).click()

    with allure.step('Выбираем ПикПоинт'):
        select_pick_point()

    with allure.step('Проверяем что заказ доступен только зарегистрированным пользователям'):
        s('//*[text()="Заказ доступен только зарегистрированным пользователям."]').should(be.visible)