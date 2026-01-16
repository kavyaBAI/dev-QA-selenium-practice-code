import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#connection of database
con = mysql.connector.connect(
    host='127.0.0.1',
    user="root",          
    password='kavya1822', 
    database="seedar_v1" 
)
cursor = con.cursor()
cursor.execute("SELECT username, password, expected FROM login_users")
db_data = cursor.fetchall() 
con.close()
print(f"Fetched {len(db_data)} rows from database.")

#__________________________________________
ops = webdriver.ChromeOptions()
#diabling all the pop msg becoz its not application alert its browser feature
prefs = {
    "credentials_enable_service": False,     
    "profile.password_manager_enabled": False, 
    "profile.password_manager_leak_detection": False, 
    "safebrowsing.enabled": True 
}
ops.add_experimental_option("prefs", prefs)
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=ops)
driver.maximize_window()

for row in db_data:
    username = row[0]
    password = row[1]
    expected_result = row[2]  

    print(f"\nTesting User: {username} | Expecting: {expected_result}")
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    actual_result = ""
    if "inventory.html" in driver.current_url:
        actual_result = "Pass"
    else:
        actual_result = "Fail"

    if actual_result == expected_result:    
        if actual_result == "Pass":
            driver.find_element(By.ID, "react-burger-menu-btn").click()
            time.sleep(1)
            driver.find_element(By.ID, "logout_sidebar_link").click()
            
    else:
        print(f"Expected: {expected_result}, but got: {actual_result}")

driver.quit()
print("All tests completed.")