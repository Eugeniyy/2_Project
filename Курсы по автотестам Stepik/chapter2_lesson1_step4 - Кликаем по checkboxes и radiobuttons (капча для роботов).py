from selenium import webdriver
import time
import math

site = 'http://suninjuly.github.io/math.html'
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(site)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    answer = calc(x)
    answer_input = browser.find_element_by_id("answer")
    answer_input.send_keys(answer)
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox'")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(7)
    browser.quit()

# Пустая строка