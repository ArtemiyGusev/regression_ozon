from selene.support.shared.jquery_style import s


class Subject:
    def __init__(self, element):
        self.element = element

    def select_element_in_list(self, element_text, element_select=None):
        if element_select is None:
            self.element.type(element_text).press_enter()
        else:
            self.element.type(element_text)
            self.element.click()
            s(element_select).click()

