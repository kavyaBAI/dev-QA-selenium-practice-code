#first download with chrome browser 
# we can download for the differnt  broweser,firefox,edge,chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location=os.getcwd()


# def edge_setup():
#     from selenium.webdriver.edge.service import Service
#   
#     #download files in desired location
#     preferences={"download.default_directory":location}
#     ops=webdriver.EdgeOptions()
#     ops.add_experimental_option("prefs",preferences)
#     driver = webdriver.Edge(options=ops)
#     return driver


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    #to downloa din the desired location 
    preferences={"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    
    driver = webdriver.Chrome(options=ops)
    return driver

chrome_setup()


#Automation code
driver=chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()


