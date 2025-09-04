class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name):
        # locate item by name and click "Add to Cart"
        pass

    def proceed_to_checkout(self):
        # click checkout button
        pass

    def is_checkout_successful(self):
        # verify confirmation message
        return True
