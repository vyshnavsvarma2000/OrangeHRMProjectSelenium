import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils.common_utilities import webdriver_wait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Updated Page Locators
    username = (By.XPATH, "//input[@name='username']")
    password = (By.XPATH, "//input[@name='password']")
    submit_button = (By.XPATH, "//button[@type='submit']")
    error_message = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    # Page Actions
    def get_username(self):
        webdriver_wait(driver=self.driver, element=LoginPage.username)
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        webdriver_wait(driver=self.driver, element=LoginPage.password)
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def login_to_hrm(self, user, password):
        self.get_username().send_keys(user)
        self.get_password().send_keys(password)
        self.get_submit_button().click()

    def get_error_message(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPage.error_message))
        return self.driver.find_element(*LoginPage.error_message)

    def get_error_message_text(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPage.error_message))
        return self.driver.find_element(*LoginPage.error_message).text
