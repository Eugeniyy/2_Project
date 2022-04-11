from msilib.schema import CheckBox
from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/execute_script.html"

def function(x):
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    answer = browser.find_element_by_id("answer")
    checkbox_robot = browser.find_element_by_id("robotCheckbox")
    radiobutton_robot = browser.find_element_by_id("robotsRule")
    button = browser.find_element_by_tag_name("button")
    input_value = browser.find_element_by_id("input_value").text

    input_function = function(int(input_value))
    answer.send_keys(input_function)

    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox_robot)
    checkbox_robot.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton_robot)
    radiobutton_robot.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(7)
    browser.quit()