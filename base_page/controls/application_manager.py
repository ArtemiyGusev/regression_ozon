from base_page.controls.dropdown import DropDown
from base_page.controls.check_table_text import CheckTableText
from base_page.controls.select_pick_point_in_map import PickPoint
from base_page.controls.subject import Subject


class ApplicationManager:

    def __init__(self):
        self.drop_down = DropDown
        self.check_table_text = CheckTableText
        self.pick_point = PickPoint
        self.subject = Subject


app = ApplicationManager()
