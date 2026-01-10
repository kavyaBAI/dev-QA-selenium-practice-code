
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
time.sleep(3)
drop_down_country = driver.find_element(By.XPATH,'//*[@id="post-2646"]/div[2]/div/div/div/p/select')
county_drop = Select(drop_down_country)
time.sleep(2)
#we have predefined calss SELECT
#option1 :by prefined value
#county_drop.select_by_value("AFG")
#county_drop.select_by_visible_text("Afghanistan")
county_drop.select_by_index(7)
