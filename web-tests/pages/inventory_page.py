from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def is_loaded(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        return True

    def add_item_to_cart(self, item_name):
        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if item_name in name:
                btn = item.find_element(By.TAG_NAME, "button")
                self.wait.until(EC.element_to_be_clickable(btn))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                time.sleep(0.5)
                self.driver.execute_script("arguments[0].click();", btn)
                time.sleep(0.5)
                return
        raise ValueError(f"Produto nao encontrado: {item_name}")

    def get_cart_count(self):
        try:
            badge = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
            return int(badge.text)
        except:
            return 0

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
