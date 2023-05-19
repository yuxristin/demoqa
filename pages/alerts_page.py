from pages.base_page import BasePage
from components.components import WebElement
class alerts(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)
        self.alert_btn = WebElement(driver, '#alertButton')
        self.confirm_btn = WebElement(driver,'#confirmButton')
        self.conf_rez = WebElement(driver, '#confirmButton')
        self.prompt_btn = WebElement(driver, '#promtButton')
        self.prompt_form_check = WebElement(driver, '#promptResult')
