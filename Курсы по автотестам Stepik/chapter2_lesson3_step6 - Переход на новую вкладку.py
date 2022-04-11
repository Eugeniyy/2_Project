from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"
def function(x):
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector('button[type="submit"')
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    source_value = browser.find_element_by_id("input_value").text
    input_value = function(int(source_value))

    answer = browser.find_element_by_id("answer")
    answer.send_keys(input_value)

    button2 = browser.find_element_by_css_selector("button")
    button2.click()

finally:
    time.sleep(7)
    browser.quit()

#Пустая строка