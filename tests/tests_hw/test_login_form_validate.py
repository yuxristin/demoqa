import time

from selenium.webdriver.common.by import By
from components.components import WebElement
from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys
def test_login_form_validate(browser):
    valid = FormPage(browser)
    valid.visit()
    assert valid.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert valid.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert valid.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert valid.user_email.get_dom_attribute(
        'pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    time.sleep(2)
    browser.set_window_size(width=1400, height=937)
    time.sleep(5)
    valid.btn_submit.click_force()
    time.sleep(2)
    assert valid.validated.get_dom_attribute('class') == 'was-validated'


def test_state_2(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.input_state.send_keys('NCR')
    form_page.input_state.send_keys(Keys.ENTER)
    time.sleep(2)












