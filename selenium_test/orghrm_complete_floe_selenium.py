from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
#login
u_name = wait.until(EC.visibility_of_element_located((By.NAME,'username')))
u_name.send_keys("Admin")
passwd = wait.until(EC.visibility_of_element_located((By.NAME,'password')))
passwd.send_keys("admin123")
val = wait.until(EC.visibility_of_element_located((By.TAG_NAME,'button')))
val.click()
time.sleep(3)
#go to admin-->users to usermanagemnt 


driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span').click()


time.sleep(3)
driver.close()
#go to admin-->users to usermanagemnt 
