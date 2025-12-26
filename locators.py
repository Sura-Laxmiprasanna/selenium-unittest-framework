import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file:///C:/Users/User/OneDrive/Desktop/basic.html")  # Must open the test page
driver.maximize_window()
time.sleep(2)

# CLICK USING XPATH + TEXT()
driver.find_element(By.XPATH, "//*[contains(text(),'cricket score')]")


time.sleep(3)
driver.quit()
