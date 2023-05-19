from pages.base_page import BasePage
from components.components import WebElement
class droppable(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/droppable'
        super().__init__(driver, self.base_url)
        self.drag = WebElement(driver, '#draggable')
        self.drop = WebElement(driver, '#droppable')

def drag_and_drop_by_offset(self, sourse, xoff) #не закончено