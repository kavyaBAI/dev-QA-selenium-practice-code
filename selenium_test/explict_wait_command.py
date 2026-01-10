import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://www.google.com")
    wait = WebDriverWait(driver, 10) #declartion
    search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q"))) #we wait until the elment is visble an dclickable 
    search_box.send_keys("Selenium Python")
    search_box.submit()
    xpath_expression = "//h3[contains(text(),'Selenium')]"
    #Waits until the element is present in the DOM and visible.
    result_link = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_expression)))
    print(f"Found the result: {result_link.text}")
    result_link.click()
    time.sleep(3)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()