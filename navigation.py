import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
wait=WebDriverWait(driver,15)
driver.get("https://letcode.in/")
# wait for element
workspace=wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='Explore Workspace']")))

#scroll to element
driver.execute_script("arguments[0].scrollIntoView(true);",workspace)

#click using action_chains
ActionChains(driver).move_to_element(workspace).click().perform()
text1=workspace.text
print(text1)
driver.back()
wait.until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(@class,'navbar-item')]"))
)
print("back navigation successful")

#forward

driver.forward()

text2=wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='Explore Workspace']"))).text
print(text2)

if text1==text2:
    print("navigation is sucessfull")

driver.quit()
