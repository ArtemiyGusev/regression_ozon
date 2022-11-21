from selene.support.shared.jquery_style import s
from selene import be


def passing_modal():
    if s("#age-verification").matching(be.visible):
        s("#age-verification").type('11111990')
        s("[class='age-verification-form__btn g-btn']").click()
