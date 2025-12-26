from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")

wait = WebDriverWait(driver, 20)

# FIRST NAME
first_name = wait.until(
    EC.visibility_of_element_located((By.ID, "firstName"))
)
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", first_name)
first_name.click()
first_name.clear()
first_name.send_keys("Sachin")

# LAST NAME
last_name = wait.until(
    EC.visibility_of_element_located((By.ID, "lastName"))
)
last_name.click()
last_name.clear()
last_name.send_keys("Tendulkar")

time.sleep(2)

# Scroll & Submit
submit = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", submit)
submit.click()

time.sleep(2)
driver.quit()



