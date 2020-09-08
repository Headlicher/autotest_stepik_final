from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    STUFF_NAME = (By.CSS_SELECTOR, "h1")
    STUFF_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADDED_STUFF_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    ADDED_STUFF_PRICE = (By.CSS_SELECTOR, "div.alert-info strong")
