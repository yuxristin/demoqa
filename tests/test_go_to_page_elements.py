from pages.demoga import DemoQa
from pages.elements_page import ElementsPage


def test_go_to_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()


