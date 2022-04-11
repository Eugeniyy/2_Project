from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    current_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_path, "file_chapter2_lesson2_step8.txt")

    first_name = browser.find_element_by_css_selector('input[name="firstname"]')
    last_name = browser.find_element_by_css_selector('input[name="lastname"]')
    Email = browser.find_element_by_css_selector('input[name="email"]')
    file_input = browser.find_element_by_css_selector('input[type="file"]')
    submit = browser.find_element_by_css_selector('button[type="submit"]')

    first_name.send_keys("Evgeniy")
    last_name.send_keys("Pol'kin")
    Email.send_keys("explprobe@mail.ru")
    file_input.send_keys(file_path)
    submit.click()

finally:
    time.sleep(7)
    browser.quit()

#Пустая строка
