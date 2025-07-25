#importing dependencies
from selenium.webdriver.common.by import By

class Locators:
    username_field = (By.XPATH, '//*[@id=":r0:"]')
    password_field = (By.XPATH, '//*[@id=":r1:"]')
    login_button = (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[2]/div/div/div[3]/div/div/form/div[4]/button')
    error_message = (By.XPATH, '//p[contains(text(),"Invalid email!")]')
    name=(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/p[1]')