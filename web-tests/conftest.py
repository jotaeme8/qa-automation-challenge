import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver_path():
    driver_path = ChromeDriverManager().install()
    driver_dir = os.path.dirname(driver_path)
    for f in os.listdir(driver_dir):
        if f == "chromedriver" or f == "chromedriver.exe":
            full_path = os.path.join(driver_dir, f)
            os.chmod(full_path, 0o755)
            return full_path
    raise RuntimeError(f"chromedriver nao encontrado em {driver_dir}")


@pytest.fixture(scope="function")
def driver():
    options = Options()

    if os.getenv("CI", "false").lower() == "true":
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-password-manager-reauthentication")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_settings.popups": 0,
        "safebrowsing.enabled": False,
    })

    service = Service(get_driver_path())
    chrome = webdriver.Chrome(service=service, options=options)
    chrome.set_page_load_timeout(60)
    yield chrome
    chrome.quit()
