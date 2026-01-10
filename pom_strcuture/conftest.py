import pytest
from selenium import webdriver

@pytest.fixture() # This marks the function as a 'Setup' tool
def setup(request):
    # --- BEFORE THE TEST ---
    print("\nLaunching Browser...")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
    request.cls.driver = driver
    
    yield  
    
    # --- AFTER THE TEST ---
    print("\nClosing Browser...")
    driver.quit()