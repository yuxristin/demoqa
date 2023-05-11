from pages.base_page import BasePage
from components.components import WebElement
class SauceDemo(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/'
        super().__init__(driver, self.base_url)
        self.username = WebElement(driver, '#user-name')
        self.password = WebElement(driver, '#password')
        self.submit = WebElement(driver, '#login-button')
        self.new_url = 'https://www.saucedemo.com/inventory.html'
        self.tov = WebElement(driver,'#add-to-cart-sauce-labs-backpack ')
        self.tov2 = WebElement(driver,'#add-to-cart-sauce-labs-bolt-t-shirt')
        self.kor = WebElement(driver, '#shopping_cart_container > a')
