from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time



driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
regilink=Keys.CONTROL+Keys.RETURN  #manual keys we enter 
driver.find_element(By.LINK_TEXT,"Register").send_keys(Keys.CONTROL+Keys.RETURN)
time.sleep(3)

#selenium 4  switching to new tab 
driver.get("https://jqueryui.com/slider/")
driver.switch_to.new_window('tab') #will help to open in new tab 
driver.get("https://demo.nopcommerce.com/")

#selenium 4  switching to new window 
driver.get("https://jqueryui.com/slider/")
driver.switch_to.new_window('window')
driver.get("https://demo.nopcommerce.com/")