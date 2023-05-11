from pages.demoga import DemoQa

def test_title(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert browser.title() == demo_qa_page.PageData['title']
