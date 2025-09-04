import pytest
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("setup")
class TestCheckout:

    def test_user_can_checkout(self, driver):
        # Step 1: Login
        login_page = LoginPage(driver)
        login_page.login("testuser", "password123")

        # Step 2: Add item to cart & proceed to checkout
        checkout_page = CheckoutPage(driver)
        checkout_page.add_item_to_cart("Laptop")
        checkout_page.proceed_to_checkout()

        # Step 3: Assert checkout page is displayed
        assert checkout_page.is_checkout_successful() is True
