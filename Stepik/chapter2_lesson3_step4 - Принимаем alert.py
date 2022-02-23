from cmath import sin
from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/alert_accept.html'
def function_input(x):
    return math.log(abs(12*sin(x)))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector('button[type="submit"]')
    button1.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()

    input_value = int(browser.find_element_by_id("input_value").text)
    y = function_input(input_value)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    time.sleep(1)
    button2 = browser.find_element_by_css_selector(".btn.btn-primary")
    button2.click()

finally:
    time.sleep(5)
    browser.quit()

# Пустая строка
