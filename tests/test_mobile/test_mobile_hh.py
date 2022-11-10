import allure
from allure_commons.types import Severity
from selene import be
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


def test_check_vacancies():
    with title('Type search'):
        browser.element('#fragment_intentions_onboarding_choose_direction_image_close').tap()
        browser.element('«Вакансии рядом с вами»').tap()
        browser.element('#permission_deny_and_dont_ask_again_button').tap()
        browser.element('#custom_text_layout_container_item').type('QA')
        browser.element('«QA engineer»').should(be.visible)
