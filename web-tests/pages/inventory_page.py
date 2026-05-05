from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def is_loaded(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        return True

    def add_item_to_cart(self, item_name):
        btn_id = "add-to-cart-" + item_name.lower().replace(" ", "-")
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, btn_id)))
        self.driver.execute_script("arguments[0].click();", btn)

    def go_to_cart(self):
        link = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        self.driver.execute_script("arguments[0].click();", link)
