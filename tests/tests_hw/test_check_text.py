from pages.demoga import DemoQa
from components.components import WebElement
from pages.elements_page import ElementsPage

def test_toolsqa(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    #assert(
    if WebElement.get_text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.':
        return True
    else:
        return False


def test_text_po_centru(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    if WebElement.get_text == 'Please select an item from left to start practice.':
        return True
    else:
        return False


def test_page_elements(browser):
    demo_qa_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.cen.get_text() == 'Elements'


def test_text_box_icon(browser):
    demo_qa_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.text_box_icon.exist_icon()


def test_bth_sidebar_first(browser):
    demo_qa_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.btn_sidebar_first.exist_icon()

def test_bth_sidebar_first(browser):
    demo_qa_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.btn_sidebar_first_textbox.exist_icon()
