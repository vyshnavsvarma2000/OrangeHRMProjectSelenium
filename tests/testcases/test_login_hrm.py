import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from tests.constants.Constants import Constants
from tests.pageObjects.LoginPage import LoginPage
from tests.utils.common_utilities import webdriver_wait_url

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    yield driver
    driver.quit()


@allure.epic("  Orange HRM Login Test")
@allure.feature("Orange HRM Login Negative Test")
@pytest.mark.negative
def test_hrm_login_negative(setup):
    loginpage = LoginPage(driver=setup)
    loginpage.login_to_hrm(user="admisn", password="Hacker4321")
    time.sleep(2)
    error_message_text = loginpage.get_error_message_text()
    assert error_message_text == 'Invalid credentials'
    Constants.take_screenshot(driver=setup, name='Negative Test Case')

@allure.epic("  Orange HRM Login Test")
@allure.feature("Orange HRM Login Positive Test")
@pytest.mark.positive
def test_hrm_login_positive(setup):
    loginpage = LoginPage(driver=setup)
    loginpage.login_to_hrm(user="admin", password="Hacker@4321")
    time.sleep(2)
    Constants.take_screenshot(driver=setup, name='Positive Test Case')
    assert setup.current_url == 'https://awesomeqa.com/hr/web/index.php/pim/viewEmployeeList'




