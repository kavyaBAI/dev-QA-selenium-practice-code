#https://demo.nopcommerce.com/
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.save_screenshot(os.getcwd()+"\\home.png")
#driver.save_screenshot_as_file("hone.png")
driver.close
