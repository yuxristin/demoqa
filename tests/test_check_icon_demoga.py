from pages.demoga import DemoQa

def test_icon_exist(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    demo_qa_page.icon.click()
    # assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.exist_icon()


