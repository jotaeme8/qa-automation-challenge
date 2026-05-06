import os
from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

CHROMEDRIVER_FILENAMES = ("chromedriver.exe", "chromedriver")


def get_chromedriver_path() -> str:
    driver_path = ChromeDriverManager().install()
    if os.path.isfile(driver_path) and os.path.basename(driver_path) in CHROMEDRIVER_FILENAMES:
        return driver_path

    search_dir = os.path.dirname(driver_path)
    for root, _, files in os.walk(search_dir):
        for file_name in files:
            if file_name in CHROMEDRIVER_FILENAMES:
                return os.path.join(root, file_name)

    raise RuntimeError(f"Could not locate chromedriver executable in {search_dir}.")


@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, None, None]:
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-default-apps")
    options.add_argument("--no-first-run")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--password-store=basic")
    options.add_argument("--use-mock-keychain")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values": {"notifications": 2}
    })
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(get_chromedriver_path())
    browser = webdriver.Chrome(service=service, options=options)
    browser.set_page_load_timeout(60)

    try:
        yield browser
    finally:
        browser.quit()
        service.stop()
