from components.components import WebElement
from pages.base_page import BasePage
class KoUp(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/'
        super().__init__(driver, self.base_url)
        self.koup_add_remove = WebElement(driver, '#content > ul > li:nth-child(2) > a')
