import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")
class TestLogin:

    def test_valid_login(self, driver):
        driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Verify login successful by checking URL contains /inventory.html
        assert "inventory.html" in driver.current_url
