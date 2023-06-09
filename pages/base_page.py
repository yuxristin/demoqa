import time
import logging
from components.components import WebElement
# все методы для страницы! от него наследуется страница и прочее
class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

        self.metaView = WebElement(driver, 'head > meta')

    def visit(self):
        self.driver.get(self.base_url)

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        return self.driver.title()

    def get_url(self):
        time.sleep(3)
        return self.driver.current_url

    def equal_url(self):
        if self.get_url() == self.base_url:
            return False
        return True

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
        return False



