import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

class TestE2ESauceDemo:
    VALID_USER = "standard_user"
    PASSWORD = "secret_sauce"

    def test_login_invalido_exibe_erro(self, driver):
        login = LoginPage(driver)
        login.open()
        time.sleep(2)
        login.login("usuario_errado", "senha_errada")
        time.sleep(2)
        error = login.get_error_message()
        assert "Username and password do not match" in error
        time.sleep(2)

    def test_fluxo_completo_de_compra(self, driver):
        login = LoginPage(driver)
        login.open()
        time.sleep(2)
        login.login(self.VALID_USER, self.PASSWORD)
        time.sleep(2)

        inventory = InventoryPage(driver)
        assert inventory.is_loaded()
        time.sleep(2)

        inventory.add_item_to_cart("Sauce Labs Backpack")
        time.sleep(2)

        inventory.go_to_cart()
        time.sleep(2)

        checkout = CheckoutPage(driver)
        checkout.proceed_to_checkout()
        time.sleep(2)

        checkout.fill_form("QA", "Automation", "64000-000")
        time.sleep(2)

        checkout.finish_order()
        time.sleep(2)

        confirmation = checkout.get_confirmation_text()
        assert "Thank you for your order" in confirmation
        time.sleep(2)