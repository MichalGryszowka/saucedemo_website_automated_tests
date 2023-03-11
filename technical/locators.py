from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_NAME_LOCATOR = (By.ID, "user-name")
    PWD_LOCATOR = (By.ID, "password")
    LOGIN_BUTTON_LOCATOR = (By.NAME, "login-button")
    ERROR_CONTAINER_LOCATOR = (By.CLASS_NAME, 'error-message-container')
    ERROR_CROSS_BUTTON = (By.CLASS_NAME, 'error-button')
    LOGIN_BUTTON_FRAME_LOCATOR = (By.ID, 'login_button_container')


class StdUserInventoryPageLocators:
    BACKPACK_ADD_TO_CART_LOCATOR = (By.ID, 'add-to-cart-sauce-labs-backpack')
    TSHIRT_ADD_TO_CART_LOCATOR = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    SHOPPING_CART_LOCATOR = (By.CLASS_NAME, 'shopping_cart_link')
    SHOPPING_CART_BADGE_LOCATOR = (By.CLASS_NAME, 'shopping_cart_badge')
    INVENTORY_CONTAINER_LOCATOR = (By.CLASS_NAME, 'inventory_container')
    SORT_CONTAINER_LOCATOR = (By.CLASS_NAME, 'product_sort_container')


class StdUserCartPageLocators:
    CHECKOUT_LOCATOR = (By.ID, 'checkout')


class CheckoutStep1PageLocators:
    FIRST_NAME_LOCATOR = (By.ID, 'first-name')
    LAST_NAME_LOCATOR = (By.ID, 'last-name')
    ZIP_CODE_LOCATOR = (By.ID, 'postal-code')
    CONTINUE_LOCATOR = (By.ID, 'continue')


class CheckoutStep2PageLocators:
    FINISH_LOCATOR = (By.ID, 'finish')


class CompletePageLocators:
    FIRST_NAME_LOCATOR = (By.ID, 'back-to-products')