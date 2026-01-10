from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ops= webdriver.ChromeOptions()
ops.add_argument('--disable-notification')

driver = webdriver.Chrome(options=ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window()
time.sleep(2)
driver.close()