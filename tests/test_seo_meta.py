import time

import pytest

from pages.demoga import DemoQa
from pages.accordion import Accordion
from pages.alerts_page import alerts
from pages.browser_tab import browser_tab
@pytest.mark.parametrize('pages', [Accordion, alerts, DemoQa, browser_tab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.metaView.exist()
    assert page.metaView.get_dom_attribute('name') == "viewport"
    assert page.metaView.get_dom_attribute('content') =='width=device-width,initial-scale=1'