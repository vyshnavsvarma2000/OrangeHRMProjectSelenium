from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.constants.Constants import Constants
def webdriver_wait_url(driver):
    WebDriverWait(driver=driver, timeout=2).until(
        EC.url_changes(Constants.dashboard_url()))

def webdriver_wait(driver,  element):
    WebDriverWait(driver=driver, timeout=10).until(
        EC.presence_of_element_located(element)
    )
