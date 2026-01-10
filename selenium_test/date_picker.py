from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


driver = webdriver.Chrome()
driver.get('https://jqueryui.com/datepicker/')
driver.maximize_window()

data_picker = driver.find_element(By.XPATH,'//*[@id="content"]/iframe')
driver.switch_to.frame(data_picker)

#1.to open the date picker
driver.find_element(By.ID,'datepicker').click()
#select the data mont year
mon= 'August'
year = "2026"
date_= "19"
time.sleep(3)
#now i need to chcke the codition it it matching the month and date i have passed ? use loop idk the exit condition 
while True:
    cuur_mon = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[1]').text
    curr_year = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[2]').text
    # print(curr_year,cuur_mon,type(cuur_mon))
    # print(mon,year)
    if cuur_mon == str(mon) and curr_year== str(year):
        break

    driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[2]/span').click() 
     

#select the date 
date = driver.find_elements(By.XPATH,'//*[@id="ui-datepicker-div"]//tr/td')
#print(date,type(date))
for  i in date:
    #print(i.text,type(i.text))
    #print(str(date_), i.text)
    if str(date_) == i.text:
        print(i.text)
        i.click()
        time.sleep(3)
        break


    




