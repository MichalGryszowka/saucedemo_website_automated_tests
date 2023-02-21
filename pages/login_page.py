from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

USER_LOCATOR = (By.ID, "user-name")
PWD_LOCATOR = (By.ID, "password")


class BasePage:
    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.base_url = 'https://www.saucedemo.com/'
        self.get()

    def get(self):
        full_url = self.base_url + self.url
        self.driver.get(full_url)

    def get_input_form_text_value(self, locator: tuple[By, str]) -> str | None:
        form_object = self.driver.find_element(*locator)
        return form_object.get_attribute("value")


class LoginPage(BasePage):
    def __init__(self, driver, url=''):
        super().__init__(driver, url)

    def get_text(self, locator: tuple[By, str]) -> str | None:
        form_object = self.driver.find_element(*locator)
        return form_object.get_attribute("value")

    def get_user_form(self):
        return self.driver.find_element(By.ID, "user-name")

    def fill_in_user(self, user):
        self.get_user_form().send_keys(user)

    def get_text_user(self):
        return self.get_text(USER_LOCATOR)

    def get_pwd_form(self):
        return self.driver.find_element(By.ID, "password")

    def fill_in_pwd(self, password):
        self.get_pwd_form().send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.NAME, "login-button").click()

    def get_url(self):
        return self.driver.current_url

    def find_error_frame(self):
        return self.driver.find_element(By. CLASS_NAME, 'error-message-container')

    def get_error_message(self):
        error_msg = self.find_error_frame()
        return error_msg.get_attribute('innerText')

    def click_red_cross_button_error(self):
        self.driver.find_element(By.CLASS_NAME, 'error-button').click()

    # DO PRZEGADANIA NA LEKCJI

    def wait_for_delay_user_to_log_on(self):
        element = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/span')))










