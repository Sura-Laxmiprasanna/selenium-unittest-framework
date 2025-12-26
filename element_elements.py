from webbrowser import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://letcode.in/test")
wait = WebDriverWait(driver, 10)
web_elements=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"a.card-footer-item")
                                                            )
                        )
for ele in web_elements:
    print(type(ele), ele.text.lower())
driver.quit()