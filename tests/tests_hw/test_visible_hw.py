import time

from pages.accordion import Accordion

def test_visible_accordion(browser):
    demo_qa_page = Accordion(browser)
    demo_qa_page.visit()
    assert demo_qa_page.text_element.visible()
    demo_qa_page.head.click()
    time.sleep(2)
    assert not demo_qa_page.text_element.visible()


def 