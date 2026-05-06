import os
import sys
from typing import Final

root_path = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, root_path)

from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestE2ESauceDemo:
    VALID_USER: Final[str] = "standard_user"
    PASSWORD: Final[str] = "secret_sauce"

    def test_login_invalido_exibe_erro(self, driver) -> None:
        login = LoginPage(driver)
        login.open()
        login.login("usuario_errado", "senha_errada")

        error = login.get_error_message()
        assert "Username and password do not match" in error

    def test_fluxo_completo_de_compra(self, driver) -> None:
        login = LoginPage(driver)
        login.open()
        login.login(self.VALID_USER, self.PASSWORD)

        inventory = InventoryPage(driver)
        assert inventory.is_loaded()

        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.go_to_cart()

        checkout = CheckoutPage(driver)
        checkout.proceed_to_checkout()
        checkout.fill_form("QA", "Automation", "64000-000")
        checkout.finish_order()

        confirmation = checkout.get_confirmation_text()
        assert "Thank you for your order" in confirmation
