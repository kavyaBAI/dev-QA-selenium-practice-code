from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    
    driver.get("https://www.saucedemo.com/")
    print("Step: Site Opened")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("Step: Login button clicked")

    expected_title = "Swag Labs"
    actual_title = driver.title 
    
    if actual_title == expected_title:
        print("RESULT: PASSED - Title is correct!")
    else:
        print("RESULT: FAILED - Title is not macthing")
    time.sleep(2)

finally:
    driver.quit()
    print("Step: Browser Closed")