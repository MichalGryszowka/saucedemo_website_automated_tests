from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.std_user_inventory_page import StdUserInvPage
from technical.locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver, url=' '):
        super().__init__(driver, url)

    def get_user_form(self):
        return self.driver.find_element(*LoginPageLocators.USER_NAME_LOCATOR)

    def fill_in_user(self, user):
        self.get_user_form().send_keys(user)

    def get_pwd_form(self):
        return self.driver.find_element(*LoginPageLocators.PWD_LOCATOR)

    def fill_in_pwd(self, password):
        self.get_pwd_form().send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON_LOCATOR).click()

    def log_in_user(self, user, pwd):
        self.fill_in_user(user)
        self.fill_in_pwd(pwd)
        self.click_login_button()
        if user == 'locked_out_user':
            return LoginPage(self.driver, self.driver.current_url)
        else:
            return StdUserInvPage(self.driver, self.driver.current_url)

    def find_error_frame(self):
        return self.driver.find_element(*LoginPageLocators.ERROR_CONTAINER_LOCATOR)

    def get_error_message(self):
        return self.find_error_frame().get_attribute('innerText')

    def click_error_cross_button(self):
        self.driver.find_element(*LoginPageLocators.ERROR_CROSS_BUTTON).click()

    def wait_for_error_frame_to_disappear(self):
        return WebDriverWait(self.driver, 2).until_not(EC.presence_of_element_located(self.get_error_message()))

    def wait_for_delay_user_to_log_on(self):
        return WebDriverWait(self.driver, 1).until_not(EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON_LOCATOR))










