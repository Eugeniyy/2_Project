import time
import pytest
from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/lesson/236896/step/1"
expected_result = "Correct!!"

browser = webdriver.Chrome()
browser.get(link)

input_field = WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea")))
input_field = browser.find_element_by_css_selector("textarea")
answer = math.log(int(time.time()))
input_field.send_keys(answer)
button = browser.find_element_by_css_selector(".submit-submission")
button.click()
actual_result = WebDriverWait(browser,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
actual_result = browser.find_element_by_css_selector(".smart-hints__hint").text
assert expected_result == actual_result
browser.quit()