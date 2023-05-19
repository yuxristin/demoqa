import time
from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver import ActionChains
from pages.droppable import droppable
def test_drag_and_drop(browser):
    drag_drop = droppable(browser)
    action_chains = ActionChains(browser)
    drag_drop.visit()

    action_chains.drag_and_drop(
        drag_drop.drag.find_element(), #element
        drag_drop.drop.find_element()
    ).perform() #target

    time.sleep(1)


def test_drag_and_drop1(browser):
    drag_drop2 = droppable(browser)
    action_chains = ActionChains(browser)
    drag_drop2.visit()

    assert action_chains.drag_and_drop.check_css('backgroundColor', 'rgba(0,0,0,0)')
    drag_drop2.drag.find_element(), #element
    drag_drop2.drop.find_element()
    ).perform()
    #target

    time.sleep(1)

    assert drag_drop2.drop.check_css('backgroundColor', 'rgba(70,130,180,1)')
    action_chains.drag_and_drop_by_offset(drop.)
    #не закончено