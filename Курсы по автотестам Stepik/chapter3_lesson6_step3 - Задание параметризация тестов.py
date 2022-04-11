import time
import pytest
from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

params = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]
expected_result = "Correct!"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit brower...")
    browser.quit()

@pytest.mark.parametrize("param", params)
def test_step(browser, param):
    print(f"\nrun test for url:{param}")
    link = f"https://stepik.org/lesson/{param}/step/1"
    browser.get(link)
    input_field = WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea")))
    input_field = browser.find_element_by_css_selector("textarea")
    answer = math.log(int(time.time()))
    input_field.send_keys(answer)
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    actual_result = WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    actual_result = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert expected_result == actual_result

#Пустая строка!