from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'
def function(x):
    return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button1 = browser.find_element(By.ID, "book")

    button1.click()

    value = int(browser.find_element(By.ID, "input_value").text)
    input_value = function(value)

    field_value = browser.find_element(By.ID, "answer")
    field_value.send_keys(input_value)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    time.sleep(7)
    browser.quit()

#Пустая строка