#to check the total number of links in the page ,use tag nae <a>
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import requests
driver = webdriver.Chrome()
driver.maximize_window()

#driver.get("https://demo.nopcommerce.com/")
driver.get("http://www.deadlinkcity.com/")

#click on Links.
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# time.sleep(3)

#find total number of links using <a>tagname
tol_links = driver.find_elements(By.TAG_NAME,"a")
print(len(tol_links))
c = 0
for i in tol_links:
    #print(i.text) #theempyt is coming they dont have the name static name 
    link_name = i.get_attribute("href")
    try:
        res = requests.head(link_name)
    except Exception as e:
        print(e)
    if res.status_code>=400:
        print("its broken link")
        c+=1
    else:
        print("its correct link")
    

#how to handle broken link(imp),to verify the broken links we use the request module
