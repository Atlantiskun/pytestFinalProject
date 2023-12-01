from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > *")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    ALERT_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info strong")