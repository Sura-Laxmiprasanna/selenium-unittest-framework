import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import service, Service

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://google.com")
driver.maximize_window()
time.sleep(10)
driver.minimize_window()
time.sleep(10)
print("current url: {}",format(driver.current_url))
print("\n*********************************************\n")
print("page source:{}",format(driver.page_source))
print("\n*********************************************\n")
print("tile",format(driver.title))
driver.quit()
