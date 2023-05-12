import time
from selenium.webdriver.common.keys import Keys

from pages.form_page import FormPage
from components.components import WebElement
def test_login_form(browser):
    form = FormPage(browser)
    form.visit()
    assert not form.modal_dialog.exist()
    time.sleep(1)
    form.first_name.send_keys('tester')
    form.last_name.send_keys('tester')
    form.user_email.send_keys('test@ttt.tt')
    form.gender_radio_1.click_force()
    form.user_number.send_keys('89600130992')
    time.sleep(1)
    form.hobbies.click_force()
    form.CurrentAddress.send_keys('SPB')
    form.StateAndCity.scroll_to_element()
    form.StateAndCity.send_keys('NCR')
    time.sleep(1)
    form.StateAndCity.send_keys(Keys.ENTER)
    form.btn_submit.click_force()
    time.sleep(1)
    assert form.modal_dialog.exist()
    time.sleep(1)
    form.btn_close_modal.click_force()

