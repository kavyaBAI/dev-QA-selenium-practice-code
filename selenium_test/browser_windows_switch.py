from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

window1_id = driver.current_window_handle
print("window1",window1_id)
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a').click()
windowsID = driver.window_handles #to get id of that particular browers window id 
time.sleep(4)
#  # the id genrated ghere is dyamic one 
# parent_window = windowsID[0]
# child_window = windowsID[1]
# print(parent_window,child_window)

# driver.switch_to.window(child_window)
# print(driver.title)

# driver.switch_to.window(parent_window)
# print(driver.title)

#apprach 2 using for loop 
for id in windowsID:
    print(id)
    driver.switch_to.window(id)
    print(driver.title)
    #if i want to close the particular window we can use condition
    if driver.title =='OrangeHRM':
        driver.close()
    time.sleep(3)





#if we have multiple browers window to open we can for loop 


