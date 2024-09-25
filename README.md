# OrangeHRM Automation
## Author - VYSHNAV S VARMA

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

  ## Project Structure

```bash
.
├── .idea/                        # IDE settings
├── allure-results/               # Allure report results directory
├── tests/                        # Main test directory
│   ├── __pycache__/              # Compiled Python files
│   ├── constants/                # Constants used across tests
│   ├── pageObjects/              # Page Object Model for different pages
│   ├── testcases/                # Test case implementations
│   └── utils/                    # Utility files for setup, configurations
├── __init__.py                   # Init file for Python package structure
├── pytest.ini                    # pytest configuration file
├── README.md                     # Project documentation
└── requirements.txt              # Python dependencies
```

### CI/CD Run

<img width="1199" alt="Screenshot 2023-08-28 at 5 28 46 PM" src="https://github.com/PramodDutta/PyWebAutomation0x/assets/1409610/b339baf7-ae46-4188-b285-bfb88862f752">

#### How to run Testcase parallel ?

``` pytest -n auto tests/testcases/test_login_hrm.py```

### Running the Tests
### You can run the tests using the following command:
``` pytest --alluredir=allure-results ```
## Reporting
### The project uses Allure for generating test reports. After running the tests, you can generate and serve the report locally using:

```chatinput
allure serve allure-results
```

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!
  
## License
This project is licensed under the MIT License - see the LICENSE file for details.

