from selenium import webdriver

import time

site = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(site)
    elements = browser.find_elements_by_xpath("//div/input")
    for element in elements:
        element.send_keys("Asd")
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
finally:
    time.sleep(10)
    browser.quit()