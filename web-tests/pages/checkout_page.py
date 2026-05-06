from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, timeout=30)

    def proceed_to_checkout(self) -> None:
        self.click_element(By.ID, "checkout")

    def fill_form(self, first_name: str, last_name: str, zip_code: str) -> None:
        self.find_element(By.ID, "first-name").send_keys(first_name)
        self.find_element(By.ID, "last-name").send_keys(last_name)
        self.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.click_element(By.ID, "continue")
        self.find_element(By.ID, "checkout_summary_container")

    def finish_order(self) -> None:
        self.click_element(By.ID, "finish")

    def get_confirmation_text(self) -> str:
        return self.get_text(By.CLASS_NAME, "complete-header")
