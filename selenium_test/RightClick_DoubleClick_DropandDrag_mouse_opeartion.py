from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
############################1RIght click#######################################
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html") # A good practice site
# driver.maximize_window()
# actions = ActionChains(driver)
# btn = driver.find_element(By.XPATH, "//span[text()='right click me']")
# actions.context_click(btn).perform()
# time.sleep(1) # Wait for menu to appear
# driver.find_element(By.XPATH, "//li[contains(@class,'context-menu-icon-copy')]").click()
# time.sleep(3)
# driver.quit()

####################2.Double click######################################
# driver.get("https://demo.guru99.com/test/simple_context_menu.html") 
# driver.maximize_window()
# actions = ActionChains(driver)
# button = driver.find_element(By.XPATH, '//*[@id="authentication"]/button')
# actions.double_click(button).perform()
# val = driver.switch_to.alert
# time.sleep(2)
# print(val.text)
# val.accept()
##################3.Drag and DROP#############################################
# driver.maximize_window()
# driver.get("https://www.w3schools.com/html/html5_draganddrop.asp")
# act = ActionChains(driver)
# source_el = driver.find_element(By.XPATH,'//*[@id="div1"]')
# target_el = driver.find_element(By.XPATH,'//*[@id="div2"]')
# act.drag_and_drop(source_el,target_el).perform()
# time.sleep(3)
# driver.close()

#---------------------4.slide bar range -------------------------------------------------------#
#we will find the element location ,using .location all elemnts will have x ais and y axis 
driver.maximize_window()
driver.get("https://jqueryui.com/slider/")
driver.switch_to.frame(0) 
actions = ActionChains(driver)
slider_handle = driver.find_element(By.XPATH, "//div[@id='slider']/span")
print(slider_handle.location,"-----------location of element------------")
print("moving from L->R")
actions.drag_and_drop_by_offset(slider_handle, 70, 0).perform()
time.sleep(2)
print("Moving  R-->L")
actions.drag_and_drop_by_offset(slider_handle, -30, 0).perform()
time.sleep(3)
driver.quit()





