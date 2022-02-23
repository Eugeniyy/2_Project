from selenium import webdriver

import time

site = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(site)
    elements = browser.find_elements_by_css_selector("input")
    for element in elements:
        element.send_keys("Ответ")
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()
finally:
    time.sleep(10)
    browser.quit()

# Пустоя строка