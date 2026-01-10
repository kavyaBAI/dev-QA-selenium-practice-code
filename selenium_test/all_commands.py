from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
###########################1.application_commnads#########################################################3
# driver.get("https://practicetestautomation.com/practice-test-login/")
# print(driver.title)
# print(driver.current_url)
# #print(driver.page_source)
# app_url =driver.current_url
# print("app",app_url)

######################2.conditional_command##################################################################
#is_displayed(),is_enabled(),is_selected()
driver.get("https://demo.nopcommerce.com/")
search_bar = driver.find_element(By.XPATH,'//*[@id="small-searchterms"]')
print(search_bar,"000000")
print("displayed",search_bar.is_displayed())
print("enebaled",search_bar.is_enabled())
#used it radio button and check boxes is_selcted()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
rdm = driver.find_element(By.XPATH,'//*[@id="gender-male"]')
rdf = driver.find_element(By.XPATH,"//*[@id='gender-female']")
print(rdm.is_selected())
print(rdf.is_selected())
rdf.click()
print(rdm.is_selected())
print(rdf.is_selected())
###################################3.brower_commands###################################################
##################################naviagtionl commands#################################
