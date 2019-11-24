# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import HtmlTestRunner

class ViewProductDetails(unittest.TestCase):
    base_url = "https://www.amazon.in/"
    search_term = "WD My Passport 4TB"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_AMZN_Search_TC_001_test_load_home_page(self):
        """User should be able to load Amazon's Home Page"""
        driver = self.driver
        driver.get(self.base_url)
        self.assertIn("Amazon", driver.title)

    def test_AMZN_Search_TC_002_test_search_for_a_term(self):
        """User should be able to Search Products"""
        driver = self.driver
        driver.get(self.base_url)
        SearchTestBox = driver.find_element_by_id("twotabsearchtextbox")
        SearchTestBox.clear()
        SearchTestBox.send_keys(self.search_term)
        SearchTestBox.send_keys(Keys.ENTER)
        self.assertIn(f"Amazon.in: {self.search_term}",driver.title)
        self.assertNotIn("No results found.",driver.page_source)

    def test_AMZN_Search_TC_003_test_add_item_to_cart(self):
        """User should be able to add product to cart"""
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

    def test_AMZN_Search_TC_004_delete_item_from_cart(self):
        """User should be able to delete an item from cart"""
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
        cartCount = int(driver.find_element_by_id("nav-cart-count").text)
        if cartCount < 1:
            print("Cart is empty")
            exit()
        driver.find_element_by_id("nav-cart-count").click()
        if self.driver.title.startswith("Amazon.in Shopping Cart"):
            driver.find_element_by_xpath("//span[@class='a-size-small sc-action-delete']//input").click()
            time.sleep(3)
        self.assertTrue(int(driver.find_element_by_id("nav-cart-count").text) < cartCount)

    def test_AMZN_Search_TC_005_test_sign_in_to_checkout(self):
        """User must sign in to checkout"""
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
        driver.find_element_by_id("hlb-ptc-btn-native").click()
        self.assertTrue(self.driver.title.startswith("Amazon Sign In"))
        self.assertTrue(self.driver.find_element_by_id('ap_email').is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner('./Reports'))