#employeetable,
#popuppage,registeruser

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get("https://vinothqaacademy.com/iframe/")
driver.maximize_window()


driver.switch_to.frame("employeetable")
# check_box = driver.find_element(By.XPATH,'//*[@id="myTable"]/tbody/tr[1]/td[1]/input]').click()
# time.sleep(3)
# driver.find_element(By.XPATH,'//*[@id="deleteBtn"]').click()
# time.sleep(3)

data_val = driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[1]/div/section/div/div/div/div/div/center/h2')
print("first iframe--------------------------",data_val.text)
driver.switch_to.default_content()

driver.switch_to.frame("popuppage")
cont_1 = driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[1]/div/section[1]/div[3]/div/div/div/div/h2')
print('content 2 msges',cont_1.text)
driver.switch_to.default_content()

