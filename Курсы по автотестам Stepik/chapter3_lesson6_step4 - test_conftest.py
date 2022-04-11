link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    print("\nrun test function...")
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")