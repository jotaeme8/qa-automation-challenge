from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

class TestE2ESauceDemo:
    VALID_USER = "standard_user"
    PASSWORD = "secret_sauce"
    PRODUCTS = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    def test_login_invalido_exibe_erro(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("usuario_errado", "senha_errada")
        error = login.get_error_message()
        assert "Username and password do not match" in error

    def test_fluxo_completo_de_compra(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login(self.VALID_USER, self.PASSWORD)

        inventory = InventoryPage(driver)
        assert inventory.is_loaded()

        for product in self.PRODUCTS:
            inventory.add_item_to_cart(product)

        assert inventory.get_cart_count() == len(self.PRODUCTS)

        inventory.go_to_cart()
        checkout = CheckoutPage(driver)
        checkout.proceed_to_checkout()
        checkout.fill_form("QA", "Automation", "64000-000")
        checkout.finish_order()

        confirmation = checkout.get_confirmation_text()
        assert "Thank you for your order" in confirmation
