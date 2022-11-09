from base_page.controls.select_pick_point_in_map import PickPoint
from base_page.controls.check_checkbox import Checkbox


class ApplicationManager:

    def __init__(self):
        self.pick_point = PickPoint
        self.check_box = Checkbox


app = ApplicationManager()
