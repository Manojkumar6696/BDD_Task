from locators.web_locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
#creating function to enter credentials
    def enter_credentials(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.username_field)
        )
        self.driver.find_element(*Locators.username_field).send_keys(username)
        self.driver.find_element(*Locators.password_field).send_keys(password)

    # creating function to click login
    def click_login(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(Locators.login_button)).click()

    # creating function to check error displayed
    def is_error_displayed(self, timeout=10):
        error=WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(Locators.error_message))
        return error.text

    # creating function to check login successful
    def login_succesfull(self,timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(Locators.name))
