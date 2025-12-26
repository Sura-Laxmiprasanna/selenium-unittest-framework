from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homepage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # User dropdown (Admin)
    user_dropdown = (By.CLASS_NAME, "oxd-userdropdown-name")

    # Logout option
    logout_btn = (By.XPATH, "//a[text()='Logout']")

    def click_user_dropdown(self):
        self.wait.until(
            EC.element_to_be_clickable(self.user_dropdown)
        ).click()

    def click_logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.logout_btn)
        ).click()
