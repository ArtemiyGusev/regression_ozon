from selene import Element
from selene import be


class Checkbox:
    def __init__(self, element: Element):
        self.element = element

    def check_checkbox(self):
        if self.element.matching(be.enabled):
            self.element.click()
            self.element.matching(be.disabled)
        elif self.element.matching(be.disabled):
            self.element.click()
            self.element.matching(be.enabled)
