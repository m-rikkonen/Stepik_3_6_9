import time
from selenium.webdriver.common.by import By


def test_contains_add_to_cart_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")


