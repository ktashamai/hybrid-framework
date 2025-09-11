import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture
def driver():
    options = Options()

    # Run in headless mode if in CI
    if os.getenv("CI"):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    # Common options
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)  # Implicit wait for all elements
    yield driver
    driver.quit()
