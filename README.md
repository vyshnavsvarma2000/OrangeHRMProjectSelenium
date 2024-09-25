# OrangeHRM Login Automation

This project automates the login functionality of the OrangeHRM web application. The automation suite is developed using Python, Selenium WebDriver, and pytest with Allure for reporting. It covers both positive and negative test cases for login attempts, ensuring robust validation of the login page.

## Project Overview

The purpose of this project is to automate the login workflow of the OrangeHRM application hosted at [OrangeHRM Demo](https://awesomeqa.com/hr/web/index.php/auth/login). The automation tests are designed to:
- Validate successful login with valid credentials.
- Ensure proper handling of invalid login attempts.
- Capture and log error messages for incorrect credentials.
- Generate detailed test reports using Allure.

## Features

- **Selenium WebDriver** is used to interact with the OrangeHRM web elements for login.
- **Explicit Waits** are implemented to handle dynamic content loading.
- **XPath locators** ensure stable and reliable element identification.
- **Test Automation Framework** is built with `pytest`, supporting modular test scripts.
- **Allure Reporting** provides beautiful, interactive reports for easy analysis of test results.

## Test Scenarios

### Positive Test Case
- **Login with Valid Credentials**: The test ensures that a user can successfully log in when providing correct username and password.

### Negative Test Cases
- **Login with Invalid Credentials**: The test checks that invalid credentials trigger the correct error messages.
- **Login with Empty Fields**: Ensures the appropriate error is displayed when login is attempted without entering credentials.

## Installation & Setup

### Prerequisites
- Python 3.x
- `pip` package manager
- Google Chrome (or any browser)
- ChromeDriver (for Selenium WebDriver)

### Installation Steps

1. Clone the repository:
   ```bash
   https://github.com/vyshnavsvarma2000/OrangeHRMProjectSelenium.git
   
## Install dependencies
   ```bash
   pip install -r requirements.txt 
   ```
 ## Run the tests:
```chatinput
pytest --alluredir=allure-results
```
### To view Allure reports, first ensure Allure is installed:

```chatinput
allure serve allure-results
```

## Project Structure
