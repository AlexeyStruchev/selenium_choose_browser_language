from selenium.webdriver.common.by import By


link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_exists(browser):
    """
    If the button is not found code execution is stopped and assert is not checked.
    To prevent this behavior Find_elements method is used.
    The method allows not to stop code execution and pass empty list in assert statement
    in case the element is not found.
    """
    browser.get(link)
    button_selector = "btn-add-to-basket"
    list_with_basket_button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert list_with_basket_button, f'The item with selector "{button_selector}" is not found'