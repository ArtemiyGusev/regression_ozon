import datetime
from selene.support.shared.jquery_style import s

now_date = datetime.datetime.now()
str(now_date)


class DatePicker:

    def __init__(self, element):
        self.element = element

    def select_date_in_datepicker(self, elements_in_datepicker=None):
        if elements_in_datepicker is None:
            self.element.set_value("%d %b %Y")
        else:
            self.element.click()
            s(elements_in_datepicker).s('[value="%d' % now_date.year + '"]').click()
            s(elements_in_datepicker).s('[value="%d' % (now_date.month - 1) + '"]').click()
            s(elements_in_datepicker).s('[aria-label*="%s' % now_date.strftime("%B ") + '%d' % now_date.day + '"]').click()
