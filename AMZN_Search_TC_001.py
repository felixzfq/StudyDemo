# -*- coding: utf-8 -*-

from selenium import webdriver

base_url = "https://www.amazon.in/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(base_url)
driver.implicitly_wait(10)
assert "Amazon" in driver.title
driver.close()