import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def wait_for_loader(driver, timeout=20):
    """Wait until Magento loading overlay disappears."""
    try:
        WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.loading-mask"))
        )
    except:
        pass


@pytest.mark.usefixtures("driver")
def test_magento_checkout(driver):
    driver.get("https://magento2-demo.magebit.com/")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
    )

    # Close popup if it appears
    try:
        driver.find_element(By.CSS_SELECTOR, ".action-close").click()
    except:
        pass

    # Open first product
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.product-item-link"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "option-label-size-157-item-170"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "option-label-color-93-item-57"))
    ).click()

    # Add to cart
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "product-addtocart-button"))
    ).click()

    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".message-success.success.message"),
            "You added"
        )
    )
    # Wait for mini cart update
    wait_for_loader(driver)
    cart_icon = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".minicart-wrapper .showcart"))
    )
    ActionChains(driver).move_to_element(cart_icon).pause(1).click().perform()
    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".counter-number"),
            "1"
        )
    )

    # Proceed to checkout
    wait_for_loader(driver)
    checkout_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "top-cart-btn-checkout"))
    )
    checkout_btn.click()

    # Fill checkout form (guest checkout)
    wait_for_loader(driver)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "firstname"))
    ).send_keys("John")
    driver.find_element(By.NAME, "lastname").send_keys("Doe")
    driver.find_element(By.NAME, "street[0]").send_keys("123 Test St")
    driver.find_element(By.NAME, "city").send_keys("Testville")
    driver.find_element(By.NAME, "postcode").send_keys("12345")
    driver.find_element(By.NAME, "telephone").send_keys("1234567890")

    # Country & State (Magento demo needs dropdowns handled)
    from selenium.webdriver.support.ui import Select
    Select(driver.find_element(By.NAME, "country_id")).select_by_visible_text("United States")
    Select(driver.find_element(By.NAME, "region_id")).select_by_visible_text("California")

    # Continue to shipping
    wait_for_loader(driver)
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='ko_unique_1']"))
    ).click()  # select flat rate shipping
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Next']"))
    ).click()

    actions = ActionChains(driver)
    actions.send_keys(Keys.PAGE_UP).perform()

    email_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "customer-email"))
    )
    email_field.send_keys("roni_cost@example.com")

    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Next']"))
    ).click()

# email_password= WebDriverWait(driver, 20).until(
#    EC.presence_of_element_located((By.ID, "customer-password"))
# )
# email_password.send_keys("roni_cost3@example.com")

# WebDriverWait(driver, 15).until(
#   EC.element_to_be_clickable(By.ID, "//fieldset[@class ='fieldset login'] // span[contains(text(), 'Sign In')]")).click()


