from components.components import WebElement
from pages.base_page import BasePage
class WebTales(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.nrf = WebElement(driver, 'div.rt-noData')
        self.btn_clr = WebElement(driver, "span[title='Delete']")
