import time

from pages.modal_dialogs import ModalDialogs
from pages.demoga import DemoQa
def test_modal_elements(browser):
    demo_qa_page = ModalDialogs(browser)
    demo_qa_page.visit()
    assert demo_qa_page.btn_grey.check_count_elements(5)
def test_navigation_modal(browser):
    modal = ModalDialogs(browser)
    demo_qa_page = DemoQa(browser)
    modal.visit()
    browser.refresh()
    modal.btn_icon.click()
    browser.back()
    browser.set_window_size(width=900, height= 400)
    time.sleep(2)
    browser.forward()
    assert browser.current_url == demo_qa_page.base_url #спросить как подтянуть объект
    assert browser.title == demo_qa_page.PageData['title']
    browser.set_window_size(width=1000, height= 1000)
