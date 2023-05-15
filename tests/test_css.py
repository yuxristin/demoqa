import time
from components.components import WebElement
from pages.text_box import TextBox
def test_test_box(browser):
    ttboxcss = TextBox(browser)
    ttboxcss.visit()

    assert ttboxcss.submit.check_css('color', 'rgba(255, 255, 255, 1)')
    assert ttboxcss.submit.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert ttboxcss.submit.check_css('borderColor', 'rgb(0, 123, 255)')


