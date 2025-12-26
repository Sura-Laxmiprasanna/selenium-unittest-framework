from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_basics.pom_project_demo.Locators.locators import Locators


class Loginpage:

    def __init__(self, driver, app=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.username = (By.NAME, Locators.username)
        self.password = (By.NAME, Locators.password)
        self.login_button = (By.CSS_SELECTOR, Locators.login_button)
        self.invalid_username_message=(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p')

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

