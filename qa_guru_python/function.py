def func_name(func, locals):
    print(f'{func.__name__} {locals}')


def open_browser(browser_name):
    func_name(open_browser, locals())


def go_to_companyname_homepage(page_url):
    func_name(go_to_companyname_homepage, locals())


def find_registration_button_on_login_page(page_url, button_text):
    func_name(find_registration_button_on_login_page, locals())


open_browser('Chrome')
go_to_companyname_homepage('https://mail.ru/')
find_registration_button_on_login_page('https://mail.ru/', 'Войти')
