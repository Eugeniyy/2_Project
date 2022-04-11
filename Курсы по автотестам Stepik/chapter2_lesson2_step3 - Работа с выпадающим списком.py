from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

def sum(x, y):
    return str(x + y) 

try:

    browser = webdriver.Chrome()
    browser.get(link)

    button_click = browser.find_element_by_tag_name("button")
    select = Select(browser.find_element_by_id("dropdown"))

    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    value_input = sum(int(x), int(y))

    select.select_by_value(value_input)
    button_click.click()

finally:
    time.sleep(7)
    browser.quit()