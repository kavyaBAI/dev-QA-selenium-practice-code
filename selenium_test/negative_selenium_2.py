# Open page
# Type username student into Username field
# Type password incorrectPassword into Password field
# Push Submit button
# Verify error message is displayed
# Verify error message text is Your password is invalid!
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("incorrectPassword")
    driver.find_element(By.ID, "submit").click()

    time.sleep(1)
    error_element = driver.find_element(By.ID, "error")
    
    if error_element.is_displayed():
        print("VERIFICATION 1 PASSED: Error message is visible on the screen.")
    else:
        print("VERIFICATION 1 FAILED: Error message did not appear.")
    actual_error_text = error_element.text
    expected_error_text = "Your password is invalid!"
    
    if actual_error_text == expected_error_text:
        print(f"VERIFICATION 2 PASSED: Correct error message received: '{actual_error_text}'")
    else:
        print(f"VERIFICATION 2 FAILED: Expected '{expected_error_text}' but got '{actual_error_text}'")

finally:
    time.sleep(2)
    driver.quit()