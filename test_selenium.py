from selenium import webdriver

driver = None

try:
    driver = webdriver.Chrome()

    driver.get("https://example.com")

    print("Page Title:", driver.title)
    print("Current URL:", driver.current_url)

finally:
    if driver:
        driver.quit()