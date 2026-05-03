from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        return True

    def add_item_to_cart(self, item_name):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in items:
            if item_name in item.find_element(By.CLASS_NAME, "inventory_item_name").text:
                btn = item.find_element(By.CSS_SELECTOR, "button[id^=add-to-cart]")
                self.driver.execute_script("arguments[0].click();", btn)
                return
        raise ValueError(f"Produto nao encontrado: {item_name}")

    def get_cart_count(self):
        badge = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return int(badge[0].text) if badge else 0

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
