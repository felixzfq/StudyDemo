# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AddItemToCart(unittest.TestCase):
    base_url = "https://www.amazon.in/"
    search_term = "WD My Passport 4TB"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_add_item_to_cart(self):
        driver = self.driver
        driver.get(self.base_url)
        SearchTestBox = driver.find_element_by_id("twotabsearchtextbox")
        SearchTestBox.clear()
        SearchTestBox.send_keys(self.search_term)
        SearchTestBox.send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//div[@class='s-result-list s-search-results sg-row']" 
                                     "//div[@data-index='0']//img").click()
        driver.switch_to.window(self.driver.window_handles[1])
        driver.find_element_by_id("add-to-cart-button").click()
        self.assertTrue(driver.find_element_by_id("hlb-subcart").is_enabled())
        self.assertTrue(driver.find_element_by_id("hlb-ptc-btn-native").is_displayed())

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
