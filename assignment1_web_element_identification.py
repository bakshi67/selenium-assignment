from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Start Chrome
driver = webdriver.Chrome()

# Open our local test webpage
file_path = os.path.abspath("test_page.html")
driver.get("file:///" + file_path)

print("Page Title:", driver.title)

# 1. Locate Username using ID
username = driver.find_element(By.ID, "username")
print("By ID:", username.get_attribute("placeholder"))

# 2. Locate Password using NAME
password = driver.find_element(By.NAME, "password")
print("By NAME:", password.get_attribute("placeholder"))

# 3. Locate Heading using TAG_NAME
heading = driver.find_element(By.TAG_NAME, "h1")
print("By TAG_NAME:", heading.text)

# 4. Locate Google link using LINK_TEXT
google_link = driver.find_element(By.LINK_TEXT, "Google")
print("By LINK_TEXT:", google_link.text)

# 5. Locate Login button using CLASS_NAME
login_button = driver.find_element(By.CLASS_NAME, "login-button")
print("By CLASS_NAME:", login_button.text)

# Keep browser open for 3 seconds
time.sleep(3)

# Close browser
driver.quit()