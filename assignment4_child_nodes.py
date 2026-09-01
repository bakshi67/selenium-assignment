
from selenium import webdriver
from selenium.webdriver.common.by import By

# Start Chrome
driver = webdriver.Chrome()

# Open the Selenium Assignment Test Page
driver.get("file:///C:/Users/ARGHA/selenium_project/test_page.html")

# Print page title
print("Page Title:", driver.title)

# Locate the button inside its parent div using CSS child selector
button = driver.find_element(
    By.CSS_SELECTOR,
    "#button-container > button"
)

# Print button details
print("Button Text:", button.text)

# Interact with the button
button.click()

print("Button clicked successfully.")

# Close browser
driver.quit()

