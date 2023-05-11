import time

from pages.elements_page import ElementsPage
from pages.saucedemo import SauceDemo
def test_saucedemo(browser):
        sauce_page = SauceDemo(browser)
        sauce_page.visit()
        sauce_page.username.send_keys('USSR')
        time.sleep(2)
        sauce_page.password.send_keys('RUSSIA')
        sauce_page.submit.click()
        assert not browser.current_url == sauce_page.new_url

def test_saucedemo2(browser):
        sauce_page = SauceDemo(browser)
        sauce_page.visit()
        sauce_page.username.send_keys('problem_user')
        time.sleep(2)
        sauce_page.password.send_keys('secret_sauce')
        sauce_page.submit.click()
        time.sleep(2)
        sauce_page.tov.click()
        time.sleep(2)
        sauce_page.tov2.click()
        time.sleep(2)
        sauce_page.kor.click()
        time.sleep(5)
        assert sauce_page.form.check_count_elements(count =2)



