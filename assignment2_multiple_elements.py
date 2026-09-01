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

# Find ALL links on the webpage
links = driver.find_elements(By.TAG_NAME, "a")

print("Total number of links:", len(links))

print("\nLinks found on the webpage:")

# Loop through all links
for index, link in enumerate(links, start=1):
    print(index, "-", link.text)

time.sleep(3)

driver.quit()