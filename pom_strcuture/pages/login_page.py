from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "q") # Google search for example

    def type_something(self, text):
        self.driver.find_element(*self.username_field).send_keys(text)