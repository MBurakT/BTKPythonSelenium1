import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

file_path = os.path.abspath("kurs.html")

driver = webdriver.Chrome()
driver.get(file_path)

# find_element()
header = driver.find_element(By.ID, "header")
print(header.text)

subtitle = driver.find_element(By.TAG_NAME, "h2")
print(subtitle.text)

input_element = driver.find_element(By.NAME, "username")
print(input_element.get_attribute("placeholder"))

course = driver.find_element(By.CLASS_NAME, "course-card")
course_title = course.find_element(By.TAG_NAME, "h2")
course_description = course.find_element(By.TAG_NAME, "p")
course_price = course.find_element(By.TAG_NAME, "span")
print(course_title.text)
print(course_description.text)
print(course_price.text)
print()

# find_elements()
courses = driver.find_elements(By.CLASS_NAME, "course-card")
print(len(courses))

for c in courses:
    title = c.find_element(By.TAG_NAME, "h2").text
    description = c.find_element(By.TAG_NAME, "p").text
    price = c.find_element(By.TAG_NAME, "span").text
    print(f"{title} {description} {price}\n{"-" * 50}" )

time.sleep(3)

input("Input: ")
driver.quit()