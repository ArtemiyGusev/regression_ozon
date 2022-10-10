from tests.controls.datepicker import now_date

table_name = 'table td'
send_data = '#submit'
send_picture_button = '#uploadPicture'
file_name1 = 'resources/123.png'
element_in_list_city = '//*[contains(text(),"Delhi")]'
list_city = '#city'
element_in_list_state = '//*[contains(text(),"NCR")]'
list_state = '#state'
hobbies_select_sports = '[for=hobbies-checkbox-1]'
gender_select_male = '[for=gender-radio-1]'
date_of_birth = '#dateOfBirth'
date_of_birth_input = '#dateOfBirthInput'
subjects_input = '#subjectsInput'
select_element_in_subject = '#react-select-2-option-0'

expected_result_in_table = 'Student Name', \
                           'Jack Shepard', \
                           'Student Email', \
                           'Jack@mail.ru', \
                           'Gender', \
                           'Male', \
                           'Mobile', \
                           '4815162342', \
                           'Date of Birth', \
                           now_date.strftime("%d %B,%Y"), \
                           'Subjects', \
                           'English', \
                           'Hobbies', \
                           'Sports', \
                           'Picture', \
                           '123.png', \
                           'Address', \
                           'Oceanic', \
                           'State and City', \
                           'NCR Delhi'
