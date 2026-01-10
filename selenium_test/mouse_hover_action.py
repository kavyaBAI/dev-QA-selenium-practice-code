from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://vinothqaacademy.com/mouse-event/')
driver.maximize_window()
#opeartion ->hover on demo site-->practice automation>after that elect any option
#to perform hover we have actionChain class
#why we need it ?some application doesnt allow to perform the click operation

demo_site = driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div/div[3]/div[2]/div[2]/ul/li[7]/a')
pratice_auto =driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div/div[3]/div[2]/div[2]/ul/li[7]/ul/li[1]/a')
registtion_form  = driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div/div[3]/div[2]/div[2]/ul/li[7]/ul/li[1]/ul/li[1]/a')
actions = ActionChains(driver)
actions.move_to_element(demo_site).move_to_element(pratice_auto).move_to_element(registtion_form).click().perform()
time.sleep(3)