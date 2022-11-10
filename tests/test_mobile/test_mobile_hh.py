import allure
from allure_commons.types import Severity
from selene import be, have
from selene.support.shared import browser
from allure import step as title


def test_login():
    allure.dynamic.tag("Mobile android application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты hh")
    allure.dynamic.story("Проверка сохранения ввода Email, после смены типа логина")

    with title('Кликаем по открытию формы авторизации'):
        browser.element('#fragment_intentions_onboarding_choose_direction_button_new_user').tap()

    with title('Вход по телефону или почте'):
        browser.element('«По телефону или почте»').tap()

    with title('Ввод Email'):
        browser.element('#view_line_input_edit_text').type('email@test.ru')

    with title('Меняем тип входа'):
        browser.element('«Войти по паролю»').tap()

    with title('Проверяем что email сохранился'):
        browser.element('«email@test.ru»').should(be.visible)


def test_check_category():
    allure.dynamic.tag("Mobile android application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты hh")
    allure.dynamic.story("Проверка категорий")

    with title('Закрываем форму авторизации'):
        browser.element('#fragment_intentions_onboarding_choose_direction_image_close').tap()

    with title('Клик и проверка открытия страницы Избранное'):
        browser.element('«Избранное»').tap()
        browser.element('//android.widget.FrameLayout[@content-desc="Избранное"]').should(be.visible)

    with title('Клик и проверка открытия страницы Избранное'):
        browser.element('«Отклики»').tap()
        browser.element('//android.widget.FrameLayout[@content-desc="Отклики"]').should(be.visible)

    with title('Клик и проверка открытия страницы Сообщения'):
        browser.element('«Сообщения»').tap()
        browser.element('//android.widget.FrameLayout[@content-desc="Сообщения"]').should(be.visible)

    with title('Клик и проверка открытия страницы Профиля'):
        browser.element('«Профиль»').tap()
        browser.element('//android.widget.FrameLayout[@content-desc="Профиль"]').should(be.visible)


def test_check_notifications():
    allure.dynamic.tag("Mobile android application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты hh")
    allure.dynamic.story("Проверка блока уведомлений")

    with title('Закрываем форму авторизации'):
        browser.element('#fragment_intentions_onboarding_choose_direction_image_close').tap()

    with title('Открываем страницу профиля - уведомления'):
        browser.element('«Профиль»').tap()
        browser.element('//android.widget.ImageView').tap()
        browser.element('«Уведомления»').tap()

    with title('Проверка открытия блока уведомления'):
        browser.element('«Нет уведомлений»').should(be.visible)


def test_check_page_filters():
    allure.dynamic.tag("Mobile android application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты hh")
    allure.dynamic.story("Проверка страницы фильтров")

    with title('Закрываем форму авторизации'):
        browser.element('#fragment_intentions_onboarding_choose_direction_image_close').tap()

    with title('Кликаем на иконку фильтров'):
        browser.element('#view_main_search_image_button_filters').tap()
    with title('Проверяем открытие страницы фильтров'):
        browser.element('«Фильтры»').should(be.visible)


def test_check_change_language():
    allure.dynamic.tag("Mobile android application")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Тесты hh")
    allure.dynamic.story("Проверка страницы фильтров")

    with title('Закрываем форму авторизации'):
        browser.element('#fragment_intentions_onboarding_choose_direction_image_close').tap()
    with title('Клик по профилю'):
        browser.element('«Профиль»').tap()
    with title('Открываем меню ЛК'):
        browser.element('#fragment_resume_list_container_burger_button').tap()
    with title('Открываем страницу выбора языка'):
        browser.element('#cell_advanced_menu_choose_country_image_chevron').tap()
    with title('Меняем язык на Грузию'):
        browser.element('«Грузия»').tap()
    with title('Пришло уведомление о смене языка'):
        browser.element('#snackbar_text').should(have.text('Выбранная страна успешно сохранена'))
    with title('Открываем меню ЛК'):
        browser.element('#fragment_resume_list_container_burger_button').tap()
    with title('Проверяем что язык действительно сменился'):
        browser.element('#cell_advanced_menu_choose_country_text_name').should(have.text('Грузия'))