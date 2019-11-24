# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest


class AmazonHomePage(unittest.TestCase):
    base_url = "https://www.amazon.in/"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_load_home_page(self):
        driver = self.driver
        driver.get(self.base_url)
        self.assertIn("Amazon", driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()