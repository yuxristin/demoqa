import time
from pages.koup import KoUp
from pages.koup_add import KoUpAdd
def test_add_remove(browser):
    add_remove = KoUp(browser)
    add_element = KoUpAdd(browser)


    add_remove.visit()
    add_remove.koup_add_remove.click()
    time.sleep(2)
    add_element.btn_add_element.click_kcikle()
    time.sleep(2)

    assert add_element.btn_delete.check_count_elements(4)

    for element_del in add_element.btn_delete.find_elements():
        assert element_del.text == 'Delete'

    #for btn_delete_zm in range(4):
    #        add_element.btn_delete.click()

    while add_element.btn_delete.exist():
        add_element.btn_delete.click()

    assert not add_element.btn_delete.exist()






