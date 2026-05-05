from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def proceed_to_checkout(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        self.driver.execute_script("arguments[0].click();", btn)

    def fill_form(self, first_name, last_name, zip_code):
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "continue")))
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_info")))

    def finish_order(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        self.driver.execute_script("arguments[0].click();", btn)

    def get_confirmation_text(self):
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
        return element.text
