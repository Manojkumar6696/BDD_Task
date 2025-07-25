#importing Dependencies
from behave import given, when, then
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#writing function to login page
@given("I am on the Guvi Zen portal login page")
def step_open_login_page(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://v2.zenclass.in/login")
    context.page = LoginPage(context.driver)

#writing function to enter valid credentials
@when("I enter valid credentials")
def step_enter_valid_credentials(context):
    context.page.enter_credentials("manojsekar.6696@gmail.com", "Lucky@96")

#writing function to enter invalid credentials
@when("I enter invalid credentials")
def step_enter_invalid_credentials(context):
    context.page.enter_credentials("manojsekar.896@gmail.com", "Lu0ky@96")

#writing function to click button
@when("I click on the login button")
def step_click_login(context):
    context.page.click_login()

#writing function to validate a login successful
@then("I should login successful")
def step_login_succesfull(context):
    context.page.login_succesfull()

#writing function to validate Dashboard page
@then("I should be redirected to the Dashboard page")
def step_verify_dashboard(context):
    assert "dashboard" in context.driver.current_url.lower(), "Dashboard redirection failed"
    context.driver.quit()

#writing function to validate a error message
@then("I should see an error message")
def step_verify_error_message(context):
    assert context.page.is_error_displayed(), "Invalid email!"
    context.driver.quit()

#writing function to validate a error message
@then("Update the test results in json")
def step_write_result(context):
    write_test_result(filpa)
    context.driver.quit()