from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


driver=webdriver.Chrome()

driver.get("https://www.monsterindia.com/")
driver.maximize_window()

#capture the cookies 
len_cookies = driver.get_cookies()
print(len(len_cookies))

#to ge the attribute values 
for i  in len_cookies:
    #print(i)
    print(i.get("name"),i.get("secure"))


#to add the new cookies and again count the number of cookies 
driver.add_cookie({'name':'newCookie1','secure':True,'value':'123456789'})
new_len_cookie = driver.get_cookies()
time.sleep(2)
print(len(new_len_cookie))

#delete specfic cookie 
driver.delete_cookie("newCookie1")
new_len_cookie1 = driver.get_cookies()
print(len(new_len_cookie1),"after deleteing one cookie ")


#delete all the cookies 
driver.delete_all_cookies()
new_len_cookie1 = driver.get_cookies()
print(len(new_len_cookie1),"after deleteing all cookie ")