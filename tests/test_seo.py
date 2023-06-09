import time

import pytest

from pages.demoga import DemoQa
from pages.accordion import Accordion
from pages.alerts_page import alerts
from pages.browser_tab import browser_tab
def test_title(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert browser.title() == demo_qa_page.PageData['title']

@pytest.mark.parametrize('pages', [Accordion, alerts, DemoQa, browser_tab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert browser.title == 'title'
