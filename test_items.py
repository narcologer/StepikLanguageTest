link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_product_should_be_added_in_cart(browser):
    browser.get(link)
    if browser.find_element_by_css_selector("#add_to_basket_form > button"):
        found = True
    else:
        found = False
    assert found
