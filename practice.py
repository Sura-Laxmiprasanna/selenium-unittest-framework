import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)
username=driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")
Password=driver.find_element(By.ID, "password")
Password.send_keys("secret_sauce")
Login_button=driver.find_element(By.ID, "login-button")
Login_button.click()
time.sleep(2)

expected_url="https://www.saucedemo.com/inventory.html"
if driver.current_url == expected_url:
    print("Login Successful")
else:
    print("Login Failed")
driver.close()


