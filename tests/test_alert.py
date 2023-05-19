import time

from pages.alerts_page import alerts
from pages.base_page import BasePage
from components.components import WebElement

def test_login_form(browser):
    alertA = alerts(browser)
    alertA.visit()

    assert not alertA.alert() # подтвердили, что элемента нет

    alertA.alert_btn.click()
    time.sleep(2)
    assert alertA.alert()  #подтвердили, что есть
    alertA.alert().accept()

def test_alert_text(browser):
    alertAT = alerts(browser)
    alertAT.visit()
    alertAT.alert_btn.click()
    assert alertAT.alert().text == ('You clicked a button')
    time.sleep(2)
    alertAT.alert().accept() #accept метод из коробки
    assert not alertAT.alert() # подтвердили, что элемента нет

def test_alert_cancel(browser):
    alertATC = alerts(browser)
    alertATC.visit()

    alertATC.confirm_btn.click()
    time.sleep(2)
    alertATC.alert().dismiss() #accept метод из коробки cancel
    assert alertATC.conf_rez.get_text == 'You selected Cancel'

def test_prompt(browser):
    prompt = alerts(browser)
    prompt.visit()

    prompt.prompt_btn.click()
    p = 'Namer'
    prompt.alert().send_keys(p)
    prompt.alert().accept()
    assert prompt.prompt_form_check.get_text() == f'You entered {p}'







