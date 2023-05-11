from pages.elements_page import BasePage
from components.components import WebElement
class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordion'
        self.text_element = WebElement(driver, 'section1Content > p')
        super().__init__(driver, self.base_url)
        self.head = WebElement(driver, '#section1Heading')
