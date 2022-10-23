from base_page.helper.acceptance_test_modul import url_open_size, add_file, remove_element, passing_modal, scroll_click
from base_page.controls.application_manager import app
from env import *
import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s, ss
from base_page.pages.pick_point import select_pick_point
from base_page.pages.change_city import change_city


def test_case_practice_form():
    allure.dynamic.tag("Web application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты automation-practice-form")
    allure.dynamic.story("Проверка отправленных данных в таблице через форму")

    with allure.step('Открываем /automation-practice-form'):
        url_open_size('/internet-magazin/devices')
        passing_modal()
        change_city()

    with allure.step('Заполняем поля данными'):
        scroll_click(add_device)

        s(go_to_checkout).click()

        s(delivery_pick_point).click()

        s(select_point).click()

        select_pick_point()
        #s('//*[@id="userEmail"]').type('Jack@mail.ru')
        #s('//*[@id="userNumber"]').type('4815162342')
        #s('//*[@id="currentAddress"]').type('Oceanic')

    #with allure.step('Выбираем элемент в поле Subject'):
        #app.subject(s(subjects_input)).select_element_in_list('g', select_element_in_subject)

    #with allure.step('Выбираем текущую дату'):
    #    app.date_picker(s(date_of_birth_input)).select_date_in_datepicker(date_of_birth)

    #with allure.step('Выбираем пол: male'):
    #    s(gender_select_male).click()

    #with allure.step('Выбираем хобби: Спорт'):
    #    s(hobbies_select_sports).click()

    #with allure.step('Добавляем картинку в поле загрузки файла'):
    #    add_file(send_picture_button, file_name=file_name1)

    #with allure.step('Кликаем по кнопки "Отправить форму"'):
    #    s(send_data).click()
