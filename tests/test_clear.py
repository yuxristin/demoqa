
import time

from pages.text_box import TextBox
def test_clear(browser):

    tc = TextBox(browser)
    tc.visit()
    tc.fullname.send_keys('Elevator') #ввести данные
    time.sleep(2)
    tc.fullname.clear() #очистить поле
    time.sleep(2)
    assert tc.fullname.get_text() == '' #проверка пустое поле


