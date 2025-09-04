import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures('setup')
class TestLogin:
    def test_valid_login(self):
        self.driver.get('https://example.com/login')
        login_page = LoginPage(self.driver)
        login_page.login('admin', 'admin123')
        assert 'Dashboard' in self.driver.title
