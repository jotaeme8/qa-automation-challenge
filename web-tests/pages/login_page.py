from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, timeout=10)

    def open(self) -> None:
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        self.find_element(By.ID, "user-name").send_keys(username)
        self.find_element(By.ID, "password").send_keys(password)
        self.click_element(By.ID, "login-button")

    def get_error_message(self) -> str:
        return self.get_text(By.CLASS_NAME, "error-message-container")
