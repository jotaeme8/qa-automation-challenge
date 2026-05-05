import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_chromedriver_path() -> str:
    driver_path = ChromeDriverManager().install()
    if os.path.isfile(driver_path) and driver_path.lower().endswith("chromedriver.exe"):
        return driver_path

    search_dir = os.path.dirname(driver_path)
    for root, _, files in os.walk(search_dir):
        for file_name in files:
            if file_name.lower() == "chromedriver.exe":
                return os.path.join(root, file_name)

    raise RuntimeError(
        f"Could not locate chromedriver executable in {search_dir}."
    )


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--password-store=basic")
    options.add_argument("--use-mock-keychain")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    })
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(get_chromedriver_path())
    chrome = webdriver.Chrome(service=service, options=options)
    chrome.set_page_load_timeout(60)
    yield chrome
    chrome.quit()
