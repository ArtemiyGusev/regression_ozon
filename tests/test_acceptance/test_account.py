import time

from base_page.controls.add_device import add_device_api, delete_all_device_api, add_device_click
from base_page.helper.acceptance_test_modul import url_open_size, passing_modal, scroll_click, go_to_page
from env import *
import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s, ss
from base_page.pages.pick_point import select_pick_point
from base_page.pages.change_city import change_city
from base_page.pages.sign_in import sign_in
from selene import be
from base_page.controls.application_manager import app
from base_page.api_controls.am_bearer_authenticated import AmBearerAuthenticated


def test_checkout_not_authorize():
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты myglo.ru")
    allure.dynamic.story("Проверка требования авторизации после выбора Pick point")

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


def test_check_postcode():
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты myglo.ru")
    allure.dynamic.story("Проверка на наличие и корректность посткода после ввода адреса")

    with allure.step('Открываем страницу входа'):
        url_open_size('/customer/account/login')
        passing_modal()
        change_city()

    with allure.step('Вход в аккаунт'):
        sign_in(email='dfgdr33drgdr@test.ru', password='Test20202020]')

    with allure.step('Переход в адресную книгу'):
        s('//*[text()="Адресная книга"]').click()

    with allure.step('Добавляем новый адрес'):
        s('[role="add-address"]').click()
        s('[name="glo_dadata_address"]').type('г Санкт-Петербург, ул Пионерская, д 1')
        s('[class^="AutoSuggestions_suggestionsList"]').s('[class^="AutoSuggestions_suggestion"]').click()
    with allure.step('Проверяем корректный ПостКод'):
        s('//*[contains(@class,"AddressForm_postcodeText")]/strong[text()="197198"]').should(be.visible)


def test_subscription():
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты myglo.ru")
    allure.dynamic.story("Проверка работоспособности настроек в подписке")

    with allure.step('Открываем страницу входа'):
        url_open_size('/customer/account/login')
        passing_modal()
        change_city()

    with allure.step('Вход в аккаунт'):
        sign_in(email='dfgdr33drgdr@test.ru', password='Test20202020]')

    with allure.step('Переход в рассылки'):
        s('//*[text()="Рассылка"]').click()

    with allure.step('Проверяем чекбоксы'):
        app.check_box('(//*[@class="g-checkbox-tick gri gri-tick"])[1]')
        app.check_box('(//*[@class="g-checkbox-tick gri gri-tick"])[2]')
        app.check_box('(//*[@class="g-checkbox-tick gri gri-tick"])[3]')
        s('[type="submit"]').press_enter()

    with allure.step('Проверяем уведомление'):
        s('//*[@class="message-content"]/*[text()="Мы обновили вашу подписку."]').should(be.visible)


def test_checkout_button_enabled():
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты myglo.ru")
    allure.dynamic.story("Проверка что кнопка оформить заказ стала активной после прохождения шагов на чекауте")

    with allure.step('Открываем /customer/account/login'):
        url_open_size('/customer/account/login')
        passing_modal()
        change_city()

    with allure.step('Вход в аккаунт'):
        sign_in(email='dfgdr33drgdr@test.ru', password='Test20202020]')

    with allure.step('Чистим корзину'):
        delete_all_device_api(email='dfgdr33drgdr@test.ru', password='Test20202020]')

    with allure.step('Добавляем девайс в корзину'):
        add_device_api(device='10119143', email='dfgdr33drgdr@test.ru', password='Test20202020]')

    with allure.step('Переходим на чекаут'):
        go_to_page('/checkout')

    with allure.step('Нажимаем на выбрать пункт выдачи'):
        s('//*[contains(@class,"RadioMethods_optionLabel")][text()="Курьерская доставка"]/..').click()

    with allure.step('Выбираем адрес'):
        s('[class^="Radio_labelText"]').click()

    with allure.step('Пишем комментарий к заказу'):
        s('[name="note"]').type('Тестовый заказ!')

    with allure.step('Выбираем метод оплаты Оплата картой при доставке'):
        s('//*[text()="Оплата картой при доставке"]/..').click()

    with allure.step('Проверяем что кнока Оформить заказ стала активной'):
        s('[class^="Button_button"]').should(be.enabled)


def test_add_my_device():
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты myglo.ru")
    allure.dynamic.story("Проверка что кнопка оформить заказ стала активной после прохождения шагов на чекауте")

    with allure.step('Открываем /customer/account/login'):
        url_open_size('/customer/account/login')
        passing_modal()
        change_city()

    with allure.step('Вход в аккаунт'):
        sign_in(email='dfgdr33drgdr@test.ru', password='Test20202020]')

    with allure.step('Переходим в ЛК раздел Мои Девайсы'):
        go_to_page('/glo_device_management/account/mydevices')

    with allure.step('Удаляем девайсы из корзины'):
        a = ss('[class^="DeviceItem_optionsToggle"]').should(s)
        print(a)

    with allure.step('Переходим на чекаут'):
        go_to_page('/checkout')

    with allure.step('Нажимаем на выбрать пункт выдачи'):
        s('//*[contains(@class,"RadioMethods_optionLabel")][text()="Курьерская доставка"]/..').click()

    with allure.step('Выбираем адрес'):
        s('[class^="Radio_labelText"]').click()

    with allure.step('Пишем комментарий к заказу'):
        s('[name="note"]').type('Тестовый заказ!')

    with allure.step('Выбираем метод оплаты Оплата картой при доставке'):
        s('//*[text()="Оплата картой при доставке"]/..').click()

    with allure.step('Проверяем что кнока Оформить заказ стала активной'):
        s('[class^="Button_button"]').should(be.enabled)