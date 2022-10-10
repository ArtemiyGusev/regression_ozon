from selene.support.shared.jquery_style import s


class DropDown:
    def __init__(self, element):
        self.element = element

    def select_element_in_dropdown(self, select_element):
        self.element.click()
        s(select_element).click()

    def autocomplete(self, contains_text_element):
        self.element.type(contains_text_element).press_tab()
