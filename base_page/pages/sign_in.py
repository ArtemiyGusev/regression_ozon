from selene.support.shared.jquery_style import s
from selene import be


def sign_in(email, password):
    s('[class^="userbar__customer "]').click()
    s('//*[contains(@class,"Root_link")][text()="Войти по паролю"]').click()
    s('[name="login[username]"]').type(email)
    s('[type="password"]').type(password)
    s('[class*="PasswordLogin_btn"]').click()
    s('//*[@class="base"][text()="Моя учётная запись"]').should(be.visible)