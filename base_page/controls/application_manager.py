from base_page.controls.dropdown import DropDown
from base_page.controls.check_table_text import CheckTableText
from base_page.controls.datepicker import DatePicker
from base_page.controls.subject import Subject


class ApplicationManager:

    def __init__(self):
        self.drop_down = DropDown
        self.check_table_text = CheckTableText
        self.date_picker = DatePicker
        self.subject = Subject


app = ApplicationManager()
