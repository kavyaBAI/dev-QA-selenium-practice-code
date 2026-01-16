from selenium import webdriver
import time 

def headless_chrome():
    ops=webdriver.ChromeOptions()
    #ops.headless=True #old synatx
    ops.add_argument("--headless=new")
    driver=webdriver.Chrome(options=ops)
    return driver


def headless_edge():
    ops=webdriver.EdgeOptionsOptions()
    ops.add_argument("--headless=new")
    driver=webdriver.Chrome(options=ops)
    return driver

driver=headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()