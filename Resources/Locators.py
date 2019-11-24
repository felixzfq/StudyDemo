# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class Locators:
    # Home page Locators
    SEARCH_TEXTBOX = (By.ID,"twotabsearchtextbox")
    SEARCH_SUBMIT_BUTTON = (By.ID, "nav-search-submit-text")

    # Search Results Page Locators
    SEARCH_RESULT_LINK = (By.XPATH, "//div[@class='s-result-list s-search-results sg-row']"
                                    "//div[@data-index='0']//img")

    # Product Details Page Locators
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")

    # Sub Cart Page Locators
    SUB_CART_DIV = (By.ID, "hlb-subcart")
    PROCEED_TO_BUY_BUTTON = (By.ID, "hlb-ptc-btn-native")
    CART_COUNT = (By.ID, "nav-cart-count")
    CART_LINK = (By.ID, "nav-cart")

    # Cart Page Locators
    DELETE_ITEM_LINK = (By.XPATH, "//div[@class='s-result-list s-search-results sg-row']"
                                  "//div[@data-index='0']//img")
    PROCEED_TO_CHECKOUT_BUTTON = (By.NAME, "proceedToCheckout")

    # Sign in Page Locators
    USER_EMAIL_OR_MOBIL_NO_TEXTBOX = (By.ID, "ap_email")
