from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Start Chrome
driver = webdriver.Chrome()

# Open our local webpage
file_path = os.path.abspath("test_page.html")
driver.get("file:///" + file_path)

print("Page Title:", driver.title)

# CSS selector to find elements whose ID starts with "user_"
user_elements = driver.find_elements(
    By.CSS_SELECTOR,
    '[id^="user_"]'
)

print("Number of elements found:", len(user_elements))

print("\nElements whose ID starts with 'user_':")

for element in user_elements:
    print(
        "ID:",
        element.get_attribute("id"),
        "| Placeholder:",
        element.get_attribute("placeholder")
    )

time.sleep(3)

driver.quit()