import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup") # This tells the test: "Go get the waiter first!"
class TestSearch:
    
    def test_google_search(self):
        # 1. Open the site
        self.driver.get("https://www.google.com")
        
        # 2. Use the Page Object
        login = LoginPage(self.driver)
        login.type_something("Selenium Fixtures")
        
        # 3. Validation
        assert "Google" in self.driver.title