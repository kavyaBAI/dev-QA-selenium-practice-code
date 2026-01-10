#employeetable,
#popuppage,registeruser

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get("https://vinothqaacademy.com/iframe/")
driver.maximize_window()

#this doenst work there is no website to check and the innerframe..becoz most application avoid the innerfrmae 
#we use web elment using webelemnt we go outer frame 
outer_frame = driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[1]/div/div/div/div/div/div/iframe[3]')
#//*[@id="header"]/div[2]/div/div/div[1]/div/a
driver.switch_to.frame(outer_frame)

inner_frame = driver.find_element(By.XPATH,'//*[@id="registration-1"]')
driver.switch_to.frame(inner_frame )
val = driver.find_element(By.XPATH,'//*[@id="item-vfb-1"]/div/h3')
print("innferframe 1 text ",val.text)
