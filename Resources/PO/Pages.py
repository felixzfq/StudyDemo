import sys,os,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
gradparentdir = os.path.dirname(parentdir)
sys.path.append(gradparentdir)

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from Resources.TestData import TestData
from Resources.Locators import Locators
from time import sleep


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def assert_element_text(self,by_locator,element_text):
        web_element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return web_element == element_text

    def enter_text(self,by_locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_enabled(self,by_locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))

    def is_visible(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def hover_to(self,by_locator):
        elememnt = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(elememnt).perform()


class HomePage(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def search(self):
        self.driver.find_element(*Locators.SEARCH_TEXTBOX).clear()
        self.enter_text(Locators.SEARCH_TEXTBOX,TestData.SEARCH_TERM)
        self.click(Locators.SEARCH_SUBMIT_BUTTON)


class SearchResultPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def click_search_result(self):
        self.click(Locators.SEARCH_RESULT_LINK)


class ProductDetailsPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def click_add_to_cart_button(self):
        self.click(Locators.ADD_TO_CART_BUTTON)


class SubCartPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def click_cart_link(self):
        self.click(Locators.CART_LINK)


class CartPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def delete_item(self):
        cartCount = int(self.driver.find_element(*Locators.CART_COUNT).text)
        if cartCount < 1:
            print("Cart is empty")
            exit()
        if self.driver.title.startswith("Amazon.in Shopping Cart"):
            self.click(Locators.DELETE_ITEM_LINK)
            sleep(3)

    def click_proceed_to_checkout_button(self):
        self.click(Locators.PROCEED_TO_CHECKOUT_BUTTON)


class SignInPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
