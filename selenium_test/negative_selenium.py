# Open page
# Type username incorrectUser into Username field
# Type password Password123 into Password field
# Push Submit button
# Verify error message is displayed
# Verify error message text is Your username is invalid!
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("incorrectUser")
    driver.find_element(By.ID, "password").send_keys("Password123")

    driver.find_element(By.ID, "submit").click()
    time.sleep(1)
    error_element = driver.find_element(By.ID, "error")
    
    if error_element.is_displayed():
        print("VERIFICATION 1 PASSED: Error message is visible.")
    else:
        print("VERIFICATION 1 FAILED: Error message is NOT visible.")
    actual_error_text = error_element.text
    expected_error_text = "Your username is invalid!"
    
    if actual_error_text == expected_error_text:
        print(f"VERIFICATION 2 PASSED: Error text is correct: '{actual_error_text}'")
    else:
        print(f"VERIFICATION 2 FAILED: Expected '{expected_error_text}' but got '{actual_error_text}'")

finally:
    time.sleep(2)
    driver.quit()