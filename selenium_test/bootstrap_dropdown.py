#https://www.dummyticket.com/dummy-ticket-for-visa-application/

from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH,'//*[@id="billing_country_field"]/span/span/span[1]/span/span[2]/b').click()
time.sleep(2)
country_list = driver.find_elements(By.XPATH,'//*[@id="select2-billing_country-results"]//li')
for i in country_list:
    if i == 'India':
        i.click()
        time.slee(2)
        break

