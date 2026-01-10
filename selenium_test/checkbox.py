from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
print("hiiiii")

driver.get('https://testautomationpractice.blogspot.com/')
#1.to get the particular element 
#driver.find_element(By.XPATH,'//*[@id="sunday"]').click()

#2.to select the all th elements in the check box
check_val = driver.find_elements(By.XPATH,"//*[@type='checkbox' and contains(@id,'day')]")
#print(len(check_val))
for i in check_val:
    i.click()

#3how to check the specific checkbox,like monday or sunday 
# for i in check_val:
#     week_name = i.get_attribute('value')
#     if week_name in ['wednesday','friday']:
#           i.click()

#4.select last 2 elements :
# for i in range(len(check_val)-2,len(check_val)):
#     check_val[i].click()

#5select first 2 elements:
# for i in range(len(check_val)):
#     if i<2:
#         check_val[i].click()

#6 unselct all the check box which is selected
for i in check_val:
    if i.is_selected():
        i.click()
driver.quit()

