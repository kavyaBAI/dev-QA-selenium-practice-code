# Test case 1: Positive LogIn test
# Open page
# Type username student into Username field
# Type password Password123 into Password field
# Push Submit button
# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
# Verify button Log out is displayed on the new page

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/")
driver.maximize_window()
try:
    driver.find_element(By.ID,"username").send_keys("student")
    driver.find_element(By.ID,"password").send_keys("Password123")
    driver.find_element(By.ID,"submit").click()
    time.sleep(3)
    excepted_url = "practicetestautomation.com/logged-in-successfully/"
    actual_url = driver.current_url
    if excepted_url==actual_url:
        print("excepted and actual url are same")
    else:
        print("excepted and actual url is not same")

    sucess_msg = driver.find_element(By.CLASS_NAME,"post-title").text
    if sucess_msg in ['Congratulations','successfully logged in']:
        print("verification 2 is passed")
    else:
        print("verification 2 is failed")

    log_out = driver.find_element(By.LINK_TEXT,"log out")
    if log_out.is_displayed :
        print("verfication 3 is passed")
    else:
        print("verfication 3 is not passed")
finally:
    driver.close()
    