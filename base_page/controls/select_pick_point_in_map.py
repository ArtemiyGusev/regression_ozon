import datetime
from selene.support.shared.jquery_style import s
from selene.core.entity import Element


class PickPoint:

    def __init__(self, element: Element):
        self.element = element

    def select_pick_point(self, point):
        self.element.element(point).click()
