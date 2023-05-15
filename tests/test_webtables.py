import time
from components.components import WebElement
from pages.webtales import WebTales
def test_webtales(browser):
    wbtales = WebTales(browser)
    wbtales.visit()

    assert not wbtales.nrf.exist()
    while wbtales.btn_clr.exist():
        wbtales.btn_clr.click()

    assert not wbtales.btn_clr.exist()
    time.sleep(5)

    assert wbtales.nrf.exist()

