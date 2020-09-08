from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_stuff_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def stuff_name_check(self):
        name = self.browser.find_element(*ProductPageLocators.STUFF_NAME)
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_STUFF_NAME)
        assert name.text == added_name.text, "Name is not right"

    def stuff_price_check(self):
        price = self.browser.find_element(*ProductPageLocators.STUFF_PRICE)
        added_price = self.browser.find_element(*ProductPageLocators.ADDED_STUFF_PRICE)
        assert price.text == added_price.text, "Price is not right"
