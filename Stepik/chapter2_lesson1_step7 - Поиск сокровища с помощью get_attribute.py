from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_id("treasure")
    robot_check = browser.find_element_by_id("robotCheckbox")
    robot_radio_button = browser.find_element_by_id("robotsRule")
    input_answer = browser.find_element_by_id("answer")
    button_submit = browser.find_element_by_tag_name("button")

    value_x = int(chest.get_attribute("valuex"))
    value_input = math.log(abs(12*math.sin(value_x)))

    robot_check.click()
    robot_radio_button.click()
    input_answer.send_keys(value_input)
    button_submit.click()
finally:
    time.sleep(7)
    browser.quit()

#Пустая строка