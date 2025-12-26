import time

from pyexpat.errors import messages
from selenium.webdriver.chrome.service import service, Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from selenium_basics.page.login_page import Loginpage
from selenium_basics.page.home_page import Homepage
import unittest
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        cls.wait = WebDriverWait(cls.driver, 15)

    def test_login(self):
        login = Loginpage(self.driver)
        login.login("Admin1", "admin123")
        time.sleep(2)

        # Enter username
        """self.wait.until(
            EC.element_to_be_clickable((By.NAME, "username"))
        ).send_keys("Admin")

        # Enter password
        self.wait.until(
            EC.element_to_be_clickable((By.NAME, "password"))
        ).send_keys("admin123")

        # Click login
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.orangehrm-login-button"))
        ).click()

        # Open profile dropdown
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-userdropdown-tab"))
        ).click()

        # Click logout
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
        ).click() """

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Login & Logout successful")

if __name__ == "__main__":
        import os
        import unittest
        import HtmlTestRunner

        report_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(report_dir, exist_ok=True)

        unittest.main(
            testRunner=HtmlTestRunner.HTMLTestRunner(
                output=report_dir,
                report_name="Login_Test_Report",
                combine_reports=True,
                add_timestamp=True
            )
        )

