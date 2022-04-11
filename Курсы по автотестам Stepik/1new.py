import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear")
add_product = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
add_product.click()
alert = browser.switch_to.alert
x = alert.text.split(" ")[2]
answer = str(math.log(abs((12 * math.sin(float(x))))))
alert.send_keys(answer)
alert.accept()
try:
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Your code: {alert_text}")   
    alert.accept()
except NoAlertPresentException:
    print("No second alert presented")
print(answer)