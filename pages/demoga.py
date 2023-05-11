from components.components import WebElement
from pages.base_page import BasePage

class DemoQa(BasePage):

    def __init__(self, driver):
        # драйвер для открытия страницы
        self.driver = driver
        # прописываем элементы страницы
        self.PageData = {
        'title': 'DEMOQA'
        }
        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.base_url = 'https://demoqa.com/'
        self.toolsqa = WebElement(driver, '#app > footer > span')
        self.cent = WebElement(driver, '//*[@id="app"]/div/div/div[2]/div[2]/text()')
        super(). __init__(driver, self.base_url)
