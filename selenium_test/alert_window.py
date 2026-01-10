from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/alerts.html#")
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="prompt"]').click()
time.sleep(2)

#alert is not webelemt ,so webdriver give us command to uset alert/pop msg 
alert_win  = driver.switch_to.alert #alert_win is the object is created my alert command 

#to see the text in the alert msg 
print("msgggggggggggggggggggggggg",alert_win.text)

#now to see ok clciking ok, there is command to clcik okay we have to send some text using alert object 

alert_win.send_keys("hi,what is this pop msg ")
#now the alert winsow has to close right,that will happen using the accept method
#alert_win.accept()
#without giveing any msg,juts to close it using canel button 
alert_win.dismiss()
time.sleep(5)



