import time

from components.components import Keys
from pages.webtales import WebTales

def test_wabtales_add(browser):
    testadd = WebTales(browser)
    testadd.visit()

    testadd.btn_add.click()
    testadd.first_name.send_keys('TestUser')
    testadd.last_name.send_keys('TestUserFamily')
    testadd.e_mail.send_keys('TestUser@Family.com')
    testadd.age.send_keys('34')
    testadd.salary.send_keys('1989')
    testadd.department.send_keys('OSZPO')
    time.sleep(2)
    testadd.submit.click()
    time.sleep(2)
    testadd.edit.click()
    time.sleep(2)
    testadd.first_name.clear()
    time.sleep(2)
    testadd.last_name.clear()
    time.sleep(2)
    testadd.first_name.send_keys('TestUserFamily')
    time.sleep(2)
    testadd.last_name.send_keys('TestUser')
    testadd.submit.click()
    time.sleep(2)
    testadd.btn_delete_4.click()
    time.sleep(1)

def test_wabtales_next(browser):
    testnext = WebTales(browser)
    testnext.visit()

    testnext.previous.get_dom_attribute('disabled')  # проверка атрибута disabled
    testnext.next.get_dom_attribute('disabled') #проверка атрибута disabled

    testnext.num_str.send_keys(Keys.ENTER)
    time.sleep(2)
    testnext.str_five.click()
    time.sleep(1)

    testnext.btn_add.click()
    testnext.first_name.send_keys('TestUser')
    testnext.last_name.send_keys('TestUserFamily')
    testnext.e_mail.send_keys('TestUser@Family.com')
    testnext.age.send_keys('34')
    testnext.salary.send_keys('1989')
    testnext.department.send_keys('OSZPO')
    time.sleep(2)
    testnext.submit.click()
    time.sleep(2)

    testnext.btn_add.click()
    testnext.first_name.send_keys('TestUser')
    testnext.last_name.send_keys('TestUserFamily')
    testnext.e_mail.send_keys('TestUser@Family.com')
    testnext.age.send_keys('34')
    testnext.salary.send_keys('1989')
    testnext.department.send_keys('OSZPO')
    time.sleep(2)
    testnext.submit.click()
    time.sleep(2)

    testnext.btn_add.click()
    testnext.first_name.send_keys('TestUser3')
    testnext.last_name.send_keys('TestUserFamily3')
    testnext.e_mail.send_keys('TestUser@Family3.com')
    testnext.age.send_keys('343')
    testnext.salary.send_keys('1989')
    testnext.department.send_keys('OSZPO3')
    time.sleep(2)
    testnext.submit.click()

    testnext.next.click()
    time.sleep(3)
    testnext.previous.click()
    time.sleep(2)



