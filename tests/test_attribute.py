from pages.text_box import TextBox
def test_placeholder(browser):

        pl = TextBox(browser)
        pl.visit()
        assert pl.fullname.get_dom_attribute('placeholder') == 'Full Name' #проверка, используется всегда

""" проверка значения атрибута """