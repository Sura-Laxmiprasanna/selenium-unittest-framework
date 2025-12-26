from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep


service = Service("C:\\Users\\User\\Downloads\\edgedriver_win64\\msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://www.saucedemo.com/")
sleep(2)
username=driver.find_element_by_id('user-name')
username.send_keys("standard_user")
sleep(2)
password=driver.find_element_by_id('password')
password.send_keys("secret_sauce")
sleep(2)
loginbutton=driver.find_element_by_name('login-button')
loginbutton.click()
sleep(3)

driver.close()







