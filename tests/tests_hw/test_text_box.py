import time

from pages.text_box import TextBox
def test_test_box(browser):
    ttbox = TextBox(browser)
    ttbox.visit()
    ttbox.fullname.send_keys('Scott')
    ttbox.currentAddress.send_keys('LosAlamos')
    ttbox.submit.click_force()
    time.sleep(2)
    ttbox.name.exist()
    time.sleep(2)
    ttbox.currentAddress.exist()
    time.sleep(2)
    assert ttbox.name.get_text() == 'Name:Scott'
    assert ttbox.currentAddressCh.get_text() == 'Current Address :LosAlamos'


