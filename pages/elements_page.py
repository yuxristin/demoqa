from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.components import WebElement
# это страница сайта, аналогично demoqa, может использовать base_page и собственные элементы
class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super(). __init__(driver, self.base_url)
        self.cen = WebElement(driver, '#app > div > div > div.pattern-backgound.playgound-header > div')
        self.text_box_icon = WebElement(driver, '#item-0 > svg')
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, '#app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(1) > div > ul > #item-0 > span')
        self.btn_sidebar_first1 = WebElement(driver, 'div:nth-child(1) > div >ul >#item-1 > span')
        self.btn_sidebar_first_menu = WebElement(driver, 'div:nth-child(1) > div > ul > li')
