import os
from typing import Any

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 30) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, by: By, locator: str) -> WebElement:
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click_element(self, by: By, locator: str) -> None:
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, by: By, locator: str) -> str:
        return self.find_element(by, locator).text

    def save_screenshot(self, name: str) -> str:
        path = os.path.abspath(name)
        self.driver.save_screenshot(path)
        return path
