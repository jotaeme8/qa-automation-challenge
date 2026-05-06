from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, timeout=30)

    def is_loaded(self) -> bool:
        self.find_element(By.CLASS_NAME, "inventory_list")
        return True

    def add_item_to_cart(self, item_name: str) -> None:
        button_id = f"add-to-cart-{item_name.lower().replace(' ', '-')}"
        self.click_element(By.ID, button_id)

    def go_to_cart(self) -> None:
        self.click_element(By.CLASS_NAME, "shopping_cart_link")
