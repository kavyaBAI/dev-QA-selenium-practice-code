from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# driver.switch_to.frame("employeetable")

#1.caluclating the number of rows
no_of_rowws = len(driver.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]//tr'))
print(no_of_rowws ,"no_of_rowws ")
# #2caluclating the number of table
# num = len(driver.find_elements(By.XPATH,'//*[@id="myTable"]/tbody'))
# print(num ,"no_of_table")
#3calculating the number of columns
num_of_col = len(driver.find_elements(By.XPATH,'//*[@id="HTML1"]/div[1]//tr[1]/th'))
print("num_of_col",num_of_col)

#4read specific column and row 
data = driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]//tr[2]/td[3]')
print(type(data))
print(data.text,"data text")

#5.read all the columns and rows data
# for row in range(2,no_of_rowws+1):
#     for col in range(1,num_of_col+1):
#         data = driver.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]//tr[{row}]/td[{col}]')
#         print(data.text)
#     print('------------------------------------')

#6.read the data based on the condition eg:author is Amit and price is 300
for row in range(2,no_of_rowws+1):
    authorname =  driver.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]//tr[{row}]/td[2]').text
    price =  driver.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]//tr[{row}]/td[4]').text
    #print(authorname,price,"----------------")
    if authorname == 'Amit' and price=='300':
        data =driver.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]//tr[{row}]/td[1]').text
        data1 = driver.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]//tr[{row}]/td[3]').text
        print(data,data1),"ppppppppppppppppppppppppp")
        


#6.get all the books whos author is mukesh 
for row in range(2,no_of_rowws+1):
    authorname =  driver.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]//tr[{row}]/td[2]').text
    if authorname =='Mukesh':
        book= driver.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]//tr[{row}]/td[1]').text
        print(book)

