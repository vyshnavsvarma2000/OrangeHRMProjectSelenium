import allure
from allure_commons.types import AttachmentType


class Constants:
    @staticmethod
    def app_url():
        return "https://awesomeqa.com/hr/web/index.php/auth/login"

    @staticmethod
    def dashboard_url():
        return "https://awesomeqa.com/hr/web/index.php/pim/viewEmployeeList"

    @staticmethod
    def take_screenshot(driver, name):
        return allure.attach(driver.get_screenshot_as_png(), name=name,  attachment_type=AttachmentType.PNG)