from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name=\"registration_submit\"]")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > *")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    ALERT_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info strong")


class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
