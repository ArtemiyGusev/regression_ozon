import pytest
from base_page.controls.add_device import add_device_api, delete_all_device_api
from base_page.helper.acceptance_test_modul import *
from env import *
import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s, ss
from base_page.pages.pick_point import select_pick_point
from base_page.pages.change_city import change_city
from base_page.pages.sign_in import sign_in
from selene import be
from base_page.controls.application_manager import app


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
        scroll_click('[class^="add-to-cart-btn"]')

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
        s(post_code).should(be.visible)


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
        app.check_box(checkbox_email)
        app.check_box(checkbox_sms)
        app.check_box(checkbox_phone)
        s('[type="submit"]').press_enter()

    with allure.step('Проверяем уведомление'):
        s(refresh_sub).should(be.visible)


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
        s(courier_delivery).click()

    with allure.step('Выбираем адрес'):
        s('[class^="Radio_labelText"]').click()

    with allure.step('Пишем комментарий к заказу'):
        s('[name="note"]').type('Тестовый заказ!')

    with allure.step('Выбираем метод оплаты Оплата картой при доставке'):
        s('//*[text()="Оплата картой при доставке"]/..').click()

    with allure.step('Проверяем что кнока Оформить заказ стала активной'):
        s('[class^="Button_button"]').should(be.enabled)


@pytest.mark.parametrize("name, number, email, comment, error", [
    ("ads", "", "test@test1.ru", "asd", "Это поле обязательно для заполнения."),
    ("ads", "911111111", "test@test1.ru", "asd", "Некорректный номер телефона."),
    ("ads", "9111111111", "test", "asd", "Пожалуйста, введите правильный адрес электронной почты (email). Например, ivanivanov@domain.com."),
    ("ads", "9111111111", "", "asd", "Это поле обязательно для заполнения."),
])
def test_add_my_device(name, number, email, comment, error):
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты myglo.ru")
    allure.dynamic.story("Проверка что кнопка оформить заказ стала активной после прохождения шагов на чекауте")

    with allure.step('Открываем /obratnaya-svyaz'):
        url_open_size('/obratnaya-svyaz')
        passing_modal()

    with allure.step('Заполняем форму обратной связи'):
        s('[name="name"]').type(name)
        s('#tel').type(number)
        s('[name="email"]').type(email)
        s('[name="comment"]').type(comment)
        s('[class^="Button"]').click()
    with allure.step('Проверяем наличие сообщения об ошибке'):
        s(f'//*[contains(@class,"Field_error")][text()="{error}"]').should(be.visible)

