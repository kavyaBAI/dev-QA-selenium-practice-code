from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#1.implict 
driver.get("https://www.google.com")
#driver.find_element(By.XPATH,'//*[@id="input"]').send_keys("selenium")
if True:
    search_box=driver.find_element(By.NAME, "q")
    search_box.send_keys("selenium")
    search_box.submit()
    print("Success: Found the element and typed text!")
# except:
#     print("Error: Element not found. Check if Google changed their HTML!")
driver.quit()


