import pytest
from selenium import webdriver

link = link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)

#Пустая строка!