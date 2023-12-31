from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_added_to_cart(self, should_solve_captcha=False):
        self.add_to_cart(should_solve_captcha)
        self.should_be_product_name_equal_alert_product_name()
        self.should_be_product_price_equal_alert_basket_total()

    def add_to_cart(self, should_solve_captcha=False):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()
        if should_solve_captcha:
            self.solve_quiz_and_get_code()
        assert (self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_NAME) and
                self.is_element_present(*ProductPageLocators.ALERT_BASKET_TOTAL)), ("Alert should be shown after "
                                                                                    "adding to cart")

    def should_be_product_name_equal_alert_product_name(self):
        alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert alert_product_name.text == product_name.text, ("Product name from product card and from alert should be "
                                                              "the same")

    def should_be_product_price_equal_alert_basket_total(self):
        alert_cart_total = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_TOTAL)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert alert_cart_total.text == product_price.text, "Product price and basket total should be the same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), ("Success message is presented, "
                                                                                   "but should not be")

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should be disappeared"
