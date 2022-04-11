import unittest
from selenium import webdriver
import time

class Test(unittest.TestCase):
    def test_1(self):
        self.link = 'http://suninjuly.github.io/registration1.html'
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
        self.input1 = self.browser.find_element_by_css_selector('.first_block input.first')
        self.input1.send_keys("a")
        self.input2 = self.browser.find_element_by_css_selector('.first_block input.second')
        self.input2.send_keys("b")
        self.input3 = self.browser.find_element_by_css_selector('.first_block input.third')
        self.input3.send_keys("c")
        self.button = self.browser.find_element_by_css_selector("button.btn")
        self.button.click()
        time.sleep(1)
        self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        self.welcome_text = self.welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text, "Except. Text does not match!")
    def test_2(self):
        self.link = 'http://suninjuly.github.io/registration2.html'
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
        self.input1 = self.browser.find_element_by_css_selector('.first_block input.first')
        self.input1.send_keys("a")
        self.input2 = self.browser.find_element_by_css_selector('.first_block input.second')
        self.input2.send_keys("b")
        self.input3 = self.browser.find_element_by_css_selector('.first_block input.third')
        self.input3.send_keys("c")
        self.button = self.browser.find_element_by_css_selector("button.btn")
        self.button.click()
        time.sleep(1)
        self.welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        self.welcome_text = self.welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text, "Except. Text does not match!")

if __name__ == '__main__':
    unittest.main()