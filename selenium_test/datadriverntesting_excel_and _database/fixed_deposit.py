from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import utility_file


#excel reading excel setting 
file = r"/home/kavr/Desktop/QA-AUTOMATION/DEV_test/selenium_test/datadriverntesting_excel/fixed_deposit.xlsx"
sheetName = "fixed_deposit"
row_num = utility_file.getRowCount(file, sheetName)
print(row_num)


driver = webdriver.Chrome()
driver.maximize_window()


for rownum in range(2,row_num+1):
    #read the data from teh excel 
    pren=utility_file.readData(file, sheetName, rownum, 1)
    RI=utility_file.readData(file, sheetName, rownum, 2)
    PV=utility_file.readData(file, sheetName, rownum, 3)
    pu=utility_file.readData(file, sheetName, rownum, 4)
    freq=utility_file.readData(file, sheetName, rownum, 5)
    excepted_data = utility_file.readData(file, sheetName, rownum, 6)
    print(type(pren),RI,PV,pu,freq,excepted_data)
    #send this data to browser using the driver object 
    driver.get('https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true')
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="principal"]').send_keys(str(pren))
    driver.find_element(By.XPATH,'//*[@id="interest"]').send_keys(RI)
    driver.find_element(By.XPATH,'//*[@id="tenure"]').send_keys(PV)
    driver.find_element(By.XPATH,'//*[@id="frequency"]//option').select_by_visible_text(pu)
    driver.find_element(By.XPATH,'//*[@id="frequency"]//option').sselect_by_visible_text(freq)
    driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[1]/img').click()
    actual_data = driver.find_element(By.XPATH,'/*[@id="response_div"]/div/div[2]').text
    print(actual_data,"actual_data")
    #validate the data excepted_data and actual data 
    if excepted_data==actual_data:
        utility_file.writeData(file, sheetName, rownum, 8, "Passed")
        utility_file.fillGreenColor(file, sheetName, rownum, 8)
    else:
        utility_file.writeData(file, sheetName, rownum, 8, "faied")
        utility_file.fillRedColor(file, sheetName, rownum, 8)

    driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[2]/img').click()