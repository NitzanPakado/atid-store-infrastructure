import pytest
import allure
from workflows.web.atid_flows import AtidFlows
from data.web.atid_store_data import *

class TestAtidCart:
    @pytest.fixture(autouse=True)
    def setup(self, atid_flows: AtidFlows):
        self.flows = atid_flows
        self.flows.go_to_home()
        self.flows.go_to_men_page()
        self.flows.add_product_to_cart()

    @allure.title("Test - Empty Cart")
    @allure.description("Verifies that an empty cart displays the appropriate message and no checkout button.")
    def test_atid_empty_cart(self):
        self.flows.go_to_home()
        self.flows.go_to_cart_page()
        # Since setup adds a product, we need to clear it or just test a fresh flow.
        # However, for 'Entering cart without products', it's better to avoid the setup's add product.
        self.flows.remove_item() 
        self.flows.verify_empty_cart()
        self.flows.verify_checkout_button_visible(False)

    @allure.title("Test - Update Quantity")
    @allure.description("Verifies that the quantity of a product in the cart can be updated successfully using the UI controls.")
    def test_atid_update_quantity(self):
        self.flows.go_to_cart_page()
        self.flows.update_cart_quantity(DEFAULT_QUANTITY)
        self.flows.verify_quantity_value(DEFAULT_QUANTITY)

    @allure.title("Test - Remove Product")
    @allure.description("Verifies that a product can be removed from the cart and that the 'Empty Cart' message is displayed.")
    def test_atid_remove_product(self):
        self.flows.go_to_cart_page()
        self.flows.remove_item()
        self.flows.verify_empty_cart()

    @allure.title("Test - Invalid Coupon")
    @allure.description("Verifies that applying an invalid coupon code results in an appropriate error message.")
    def test_atid_invalid_coupon(self):
        self.flows.go_to_cart_page()
        self.flows.apply_coupon(INVALID_COUPON_CODE)
        self.flows.verify_error(INVALID_COUPON_MSG)

    @allure.title("Test - Empty Coupon")
    @allure.description("Verifies that clicking 'APPLY COUPON' without a code displays an appropriate error message.")
    def test_atid_empty_coupon(self):
        self.flows.go_to_cart_page()
        self.flows.apply_empty_coupon()
        self.flows.verify_error(EMPTY_COUPON_MSG)

    @allure.title("Test - Cart Persistence")
    @allure.description("Verifies that the cart contents persist after a page reload.")
    def test_atid_cart_persistence(self):
        self.flows.go_to_cart_page()
        self.flows.page.reload()
        self.flows.verify_checkout_button_visible(True)

    @allure.title("Test - Update Button State")
    @allure.description("Verifies that the 'Update Cart' button is disabled when the cart is empty.")
    def test_atid_update_button_disabled(self):
        self.flows.go_to_cart_page()
        self.flows.remove_item()
        self.flows.verify_update_button_enabled(False)

    @allure.title("Test - Negative Quantity")
    @allure.description("Verifies that the system rejects negative quantity. Test fails if negative value is accepted (Bug).")
    def test_atid_negative_quantity(self):
        self.flows.go_to_cart_page()
        self.flows.set_quantity(QTY_NEGATIVE)
        # BUG CHECK: If system accepts -1, this assertion should fail (e.g., by checking if it reset or showed a browser error)
        # Note: Playwright can't easily read browser tooltip errors, so we check if value remains -1 after update
        self.flows.verify_quantity_input_value(RESET_QTY_VALUE) # Should reset to 1 or fail

    @allure.title("Test - Large Quantity")
    @allure.description("Verifies that the system has a maximum quantity limit. Test fails if 9999 is accepted (Bug).")
    def test_atid_large_quantity(self):
        self.flows.go_to_cart_page()
        self.flows.set_quantity(QTY_LARGE)
        # BUG CHECK: Site currently accepts 9999. This test WILL FAIL to report the bug.
        self.flows.verify_error(MAX_QTY_ERROR_MSG) 

    @allure.title("Test - Non-Numeric Quantity")
    @allure.description("Verifies that non-numeric input does not remove the product. Test fails if product is removed (Bug).")
    def test_atid_non_numeric_quantity(self):
        self.flows.go_to_cart_page()
        self.flows.set_quantity(QTY_NON_NUMERIC)
        # BUG CHECK: Site currently treats 'abc' as 0 and removes item. This test WILL FAIL to report the bug.
        self.flows.verify_product_in_cart(True)

    @allure.title("Test - Quantity Zero")
    @allure.description("Verifies that setting the quantity to 0 removes the item from the cart.")
    def test_atid_quantity_zero(self):
        self.flows.go_to_cart_page()
        self.flows.set_quantity(QTY_ZERO)
        self.flows.verify_success_message(CART_UPDATED_MSG)
        self.flows.verify_empty_cart()

    @allure.title("Test - Return to Shop Navigation")
    @allure.description("Verifies that clicking 'Return to Shop' from an empty cart navigates to the store page.")
    def test_atid_return_to_shop_navigation(self):
        self.flows.go_to_cart_page()
        self.flows.remove_item()
        self.flows.click_return_to_shop()
        self.flows.verify_store_page()





