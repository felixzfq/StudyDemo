# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url = "https://www.amazon.in/"
search_term="Foundation of Software Testing by Dorothy Graham and Rex Black"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(base_url)
driver.implicitly_wait(10)
assert "Amazon" in driver.title
SearchTestBox = driver.find_element_by_id("twotabsearchtextbox")
SearchTestBox.clear()
SearchTestBox.send_keys(search_term)
SearchTestBox.send_keys(Keys.ENTER)
assert f"Amazon.in: {search_term}" in driver.title
assert "No results found." not in driver.page_source
driver.close()