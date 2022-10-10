from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture()
def open_browser():
    browser.config.window_width = 1200
    browser.config.window_height = 800


def test_positiv_find(open_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene python').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_negativ(open_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene python').press_enter()
    browser.element('[id="search"]').should(have.no.text('yashaka/selene: питон жив'))