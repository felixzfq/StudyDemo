import sys,os,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir+'\\Resources')
sys.path.append(parentdir+'\\Resources\\PO')

from selenium import webdriver
from Pages import HomePage,SearchResultPage,ProductDetailsPage,SubCartPage,CartPage,SignInPage
from Locators import Locators
from TestData import TestData
import unittest
import HtmlTestRunner


class Test_AMZN_Search_Base(unittest.TestCase):

    def setUp(self):
        chrome_option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH,options=chrome_option)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class Test_AMZN_Search(Test_AMZN_Search_Base):

    def setUp(self):
        super().setUp()

    def test_home_page_loaded_successfully(self):
        self.home_page = HomePage(self.driver)
        self.assertIn(TestData.HOME_PAGE_TITLE,self.home_page.driver.title)

    def test_user_should_be_able_to_search(self):
        self.home_page = HomePage(self.driver)
        self.home_page.search()
        self.search_result_page = SearchResultPage(self.home_page.driver)
        self.assertIn(f"Amazon.in: {TestData.SEARCH_TERM}", self.search_result_page.driver.title)
        self.assertNotIn(TestData.NO_RESULTS_TEXT, self.search_result_page.driver.page_source)

    def test_user_should_be_able_to_add_item_to_cart(self):
        self.home_page = HomePage(self.driver)
        self.home_page.search()
        self.search_result_page = SearchResultPage(self.home_page.driver)
        self.search_result_page.click_search_result()
        self.search_result_page.driver.switch_to.window(self.search_result_page.driver.window_handles[1])
        self.product_details_page = ProductDetailsPage(self.search_result_page.driver)
        self.product_details_page.click_add_to_cart_button()
        self.sub_cart_page = SubCartPage(self.product_details_page.driver)
        self.assertTrue(self.sub_cart_page.is_enabled(Locators.SUB_CART_DIV))
        self.assertTrue(self.sub_cart_page.is_visible(Locators.PROCEED_TO_BUY_BUTTON))

    def test_user_should_be_able_to_delete_item_from_cart(self):
        self.home_page = HomePage(self.driver)
        self.home_page.search()
        self.search_result_page = SearchResultPage(self.home_page.driver)
        self.search_result_page.click_search_result()
        self.search_result_page.driver.switch_to.window(self.search_result_page.driver.window_handles[1])
        self.product_details_page = ProductDetailsPage(self.search_result_page.driver)
        self.product_details_page.click_add_to_cart_button()
        self.sub_cart_page = SubCartPage(self.product_details_page.driver)
        self.sub_cart_page.click_cart_link()
        self.cart_page = CartPage(self.sub_cart_page.driver)
        cart_count_before_deletion = int(self.cart_page.driver.find_element(*Locators.CART_COUNT).text)
        self.cart_page.delete_item()
        self.assertTrue(int(self.cart_page.driver.find_element(*Locators.CART_COUNT).text) < cart_count_before_deletion)

    def test_user_must_signin_to_checkout(self):
        self.home_page = HomePage(self.driver)
        self.home_page.search()
        self.search_result_page = SearchResultPage(self.home_page.driver)
        self.search_result_page.click_search_result()
        self.search_result_page.driver.switch_to.window(self.search_result_page.driver.window_handles[1])
        self.product_details_page = ProductDetailsPage(self.search_result_page.driver)
        self.product_details_page.click_add_to_cart_button()
        self.sub_cart_page = SubCartPage(self.product_details_page.driver)
        self.sub_cart_page.click_cart_link()
        self.cart_page = CartPage(self.sub_cart_page.driver)
        self.cart_page.click_proceed_to_checkout_button()
        self.sign_in_page = SignInPage(self.cart_page.driver)
        self.assertTrue(self.sign_in_page.driver.title.startswith(TestData.SIGN_IN_PAGE_TITLE))
        self.assertTrue(self.sign_in_page.is_visible(Locators.USER_EMAIL_OR_MOBIL_NO_TEXTBOX))


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=parentdir + '\Reports'))
