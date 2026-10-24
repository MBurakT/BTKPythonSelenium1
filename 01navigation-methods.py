import time
from selenium import webdriver

driver = webdriver.Chrome()

url = "http://www.github.com"

driver.get(url)
# driver.set_window_size(800, 600)
driver.maximize_window()
driver.save_screenshot("githubSS.png")

target_url = "sadikturan"
driver.get(f"{url}/{target_url}")

time.sleep(3)

driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)
driver.refresh()
time.sleep(1)

print(f"Title: {driver.title}\nURL: {driver.current_url}")

driver.quit()