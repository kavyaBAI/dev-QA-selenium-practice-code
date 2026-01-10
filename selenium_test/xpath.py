from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
#absolute xpath
driver.get('https://practicetestautomation.com/practice-test-login/')
driver.find_element(By.XPATH,'/html/body/div/div/section/section/div[1]/div[1]/input').send_keys('student')
driver.find_element(By.XPATH,'/html/body/div/div/section/section/div[1]/div[2]/input').send_keys('Password123')
#relative xpath
# driver.file_element(By.XPATH,'//*[@id="username"]').send_keys('student')
# driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('Password123')
# driver.find_element(By.ID,"submit").click()
time.sleep(2)