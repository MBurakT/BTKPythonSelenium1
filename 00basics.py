import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.google.com")

print(driver.title)

time.sleep(3)

driver.quit()